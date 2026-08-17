<!-- source: https://yorkspace.library.yorku.ca/bitstreams/16835387-54b0-439b-8b87-55a295bb75bc/download | converted from PDF -->

THEORY AND APPLICATIONS OF HIGH CODIMENSION BIFURCATIONS

CHUNHUASHAN

A DISSERTATION SUBMITTED TO THE FACULTY OF GRADUATE STUDIES
IN PARTIAL FULFILMENT OF THE REQUIREMENTS
FOR THE DEGREE OF

DOCTOR OF PHILOSOPHY

GRADUATE PROGRAM IN MATHEMATICS AND STATISTICS
YORK UNIVERSITY
TORONTO, ONTARIO
AUGUST2013

THEORY AND APPLICATIONS OF HIGH
CODIMENSION BIFURCATIONS

by Chunhua Shan

a  dissertation  submitted to  the  Faculty of Graduate  Studies
of York  University in  partial  fulfilment  of the  requirements
for the degree of

DOCTOR OF PHILOSOPHY
@2013

Permission  has  been  granted  to:  a)  YORK  UNIVERSITY
LIBRARIES  to  lend  or  sell  copies  of this  dissertation  in
paper,  micro form  or electronic  formats,  and  b)  LIBRARY
AND ARCHIVES CANADA to reproduce,  lend,  distribute,
or sell  copies of this dissertation  anywhere  in  the  world  in
microform,  paper or electronic  formats  and to  authorise  or
procure the reproduction,  loan, distribution or sale of copies
of this dissertation anywhere in the world in micro form,  pa-
per or electronic formats.

The author reserves other publication rights, and neither the
dissertation  nor  extensive  extracts  for  it  may  be  printed  or
otherwise  reproduced  without  the  author's  written  permis-
sion.

THEORY AND APPLICATIONS OF HIGH CODIMENSION BIFURCATIONS

by Chunhua Shan

By virtue of submitting this document electronically, the author certifies that this is a true
electronic equivalent of the copy of the dissertation approved by York University for the
award of the degree. No alteration of the content has occurred and ifthere are any minor
variations  in  formatting,  they  are  as  a result of the coversion to  Adobe Acrobat format
(or similar software application).

Examination Committee Members:

1.  Huaiping Zhu (Supervisor)

2.  Zijiang Yang (Chair/Dean's Representative)

3.  Asia Ivie Weiss (Supervisory Committee Member)

4.  Jianhong Wu (Supervisory Committee Member)

5.  Richard Bello (Internal Examiner)

6.  Xinfu Zou (External Examiner)

Abstract

The  study  of bifurcation of high codimension  singularities and cyclicity  of related

limit  periodic sets  has a long  history and  is  essential in  the  theory  and applications of

differential equations and dynamical systems.  It is also closely related to the second part

of Hilbert's 16th problem.

In  1994, Dumortier, Roussarie and Rousseau launched a program aiming at proving

the finiteness  part of Hilbert's 16th problem for the quadratic vector fields.  For the pro-

gram,  125  graphics need  to  be  proved to  have finite  cyclicity.  Since  the  launch of the

program, most graphics have been proved to have finite  cyclicity,  and there are 40 chal-

lenging cases left.  Among  the rest of the graphics, there are 4 families  of HR-graphics

with a triple nilpotent singularity of saddle or elliptic type.

Based on the work of Zhu  and Rousseau,  by  using techniques including the normal

form  theory,  global blow-up techniques, calculations and analytical properties of Dulac

maps  near the  singular point  of the  blown-up  sphere,  properties of quadratic systems

and the generalized derivation-division methods,  we  prove that these 4 families  of HH-

iv

graphics  (Ji
2 ),  (![
3 ),  (!Jb)  and  (!fib)  have  finite  cyclicity.  Finishing  the  proof of the

cyclicity of these  4  families  of RH-graphics  represents one  important step towards the

proof of the finiteness part of Hilbert's 16th problem for quadratic vector fields.

v

Acknowledgements

First of all, I would  like  to express my  sincere gratitude to my  supervisor Professor

Huaiping Zhu for his patient guidance, constructive advices, consecutive encouragement

and generous support throughout my  PhD study.  He brings me  into the field  of nonlinear

dynamics and bifurcation theory.  From him  I have  learned not only the mathematics but

also how to do researches as a mathematician.

I  would  like  to  thank  Professor Christiane Rousseau  for  her valuable  suggestions

and comments.  I want to thank the committee  members,  Professor Asia Ivie  Weiss  and

Professor Jianhong Wu  for their suggestions, advices and the time of reviewing my thesis.

I am very grateful for the help and support from  Laboratory of Mathematical Parallel

System,  Centre for Disease Modelling and Department of Mathematics and Statistics.

I would  like to thank my  wife  and my  parents for their love,  understanding and sup-

port.

Lastly,  I would  like  to  acknowledge  York  University  for  the  financial  support from

Sept.  2009 to Aug.  2013.
 vi

Table  of Contents

Abstract

Acknowledgements

Table of Contents

List of Tables

List of Figures

1  Introduction

2  Preliminaries

2.1  General finite  cyclicity theorems

2.2  Transition maps  .  .  .  .  .  .  .  .  .  .

2.2.1  Derivative of a regular transition map

2.2.2  Dulac map near a hyperbolic saddle in the plane

vii
 iv

vi

vii

xi

xii

1

11

11

12

12

12

2.2.3  Transition map near a semi-hyperbolic singularity ..

2.3  Normal forms near nilpotent singularities of multiplicity 3

2.4  Blow-up of the family ...... .

2.5  Dulac maps near Pi  (i = 1, 2, 3, 4)

3  Finite cyclicity of (Ji2 )

3 .1  Main theorem

3 .2  Preliminaries

3 .3  Proof of the main theorem

3.3.1  The lower boundary graphic Sxhhlc  .

3 .3 .2  The intermediate graphics Sxhh 1 b

3.4  Finite cyclicity of (Ji2 )  •.••.•.••••

4  Finite cyclicity of (Ji3 )

4.1  Main theorem  ..

4.2  The upper boundary graphic

4.3  The intermediate and lower boundary graphics .

4.3.1  Family Sxhhl  ...... .

4.3.2  Families Sxhh4 and Sxhh6

4.3.3  Family Sxhh5  .

4.3.4  Family Sxhh7  ..
 viii
 15

18

20

24

31

32

32

37

37

44

48

50

51

51

55

59

68

72

76

4.3.5  Family Sxhh8  .

5  Finite cyclicity of ( !Jb)

5.1  Lemmas  ....

5 .2  Main theorem

5 .3  Proof of the main theorem  .

6  Finite cyclicity of (J{1b)

6.1  Main Theorem  ..  . . .  . .

6.2  The upper boundary graphic

6.3  The lower boundary graphic

6.3.1  Ehh 1 c, Ehh2e and Ehh3e  .

6.3.2  Ehh4c  ..

6.3.3  Ehh5c  .

6.3.4  Ehh6c  .

6.3.5  Ehh7c  .

6.3.6  Ehh8c  .

6.4  The intermediate boundary graphic  .  .

6.4.1  Family Ehhl  ......

6.4.2  Families Ehh2 and Ehh3  .....

6.4.3  Family Ehh4  .......

ix
 83

89

90

93

93

110

111

111

112

112

121

121

125

127

133

137

138

138

141

6.4.4  Families Ehh5-Ehh8  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  141

Bibliography  144

x

List of Tables

1.1  The progress of the DRR program  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .

2.1  Convex  limit periodic sets ofHH-type  for the saddle case [53]

2.2  Limit periodic sets ofHH-type  for the elliptic case [53]  ....

xi
 4

23

24

List of Figures

1.1  Graphics through a nilpotent saddle  ...  6

1.2  Nilpotent graphics with an elliptic point  7

1.3  Graphics for which we prove finite  cyclicity  8

2.1  Dulac map near a hyperbolic saddle in the plane  ...  14

2.2  Two  types of transitions near a semi-hyperbolic point  16

2.3  The different topological types  .  .  .  .  .  .  .  19

2.4  The stratified set {rp = O}  in the blown-up  21

2.5  Common  blow-up of the nilpotent singularity  22

2.6  Two  types of Dulac maps  ...........  28

3.1  The graphic (!{2 ) ••••••••••••  •  •  •  •  •  •  •  •  31

3.2  Transition maps for the HR-graphics of saddle type  33

3.3  Transition maps for the lower boundary graphic Sxhh 1 c  .  35

3.4  Transition maps for Sxhh 1 c in the chart F.R. on r = 0  .  .  .  40

xii

3.5  Transition maps for the family Sxhh 1 b in the chart F.R.  on r  = 0  46

4.1  The graphic (!{3) . ........  ·  ·  ·  ·  ·  ·  50

4.2  Upper boundary graphics of saddle type  52

4.3  Transition maps for the RH-graphics of saddle type  56

4.4  Transition maps for the family Sxhh 1  59

4.5  Transition maps for the family Sxhh4  69

4.6  Transition maps for the family Sxhh5  73

4.7  Transition maps for the family Sxhh7  77

4.8  Transition maps for the family Sxhh8  83

5.1  The graphic ( !Jb).  .  .  .  .  .  .  . . .  ·  ·  ·  ·  ·  ·  ·  ·  89

5.2  Transition maps for the graphic Ehhlc of (!Jb)  ..  94

6.1  The graphic (J[1b).  ..........................  110

6.2  Transition maps for the graphics Ehhlc, Ehh2e and Ehh3e of (I[1b)  .  113

6.3  Transition maps for the graphic Ehh5c  122

6.4  Transition maps for the graphic Ehh6c  126

6.5  Transition maps for the graphic Ehh7c  128

6.6  Transition maps for the graphic Ehh8c  133

6.7  Transition maps for the intermediate graphics of Ehh 1 .  139

6.8  Transition maps for the intermediate graphics of Ehh2 and Ehh3  140

xiii

6.9  Transition maps for the intermediate graphics of Ehh5 and Ehh6  .  .  .  .  142

XIV

1  Introduction

The study of the bifurcation of singularities and cyclicity of limit periodic sets is essential

in the theory and applications of differential equations and dynamical systems,  and it is

also closely related to the second part of Hilbert's 16th problem.

The second  part of Hilbert's 16th problem.  [25] For  any n  E  N,  find a  uniform

upper bound H ( n)  < oo  and relative positions of limit cycles for the planar polynomial
.  .

vector fields

where Pn(x, y)  and Qn(x, y) are polynomials of degree n.

The  second  part of Hilbert's  16th  problem  is  still  open  even  for  n  =  2  and till

now  we  only  know  that H(2)  ~ 4  [3, 47].  However,  this  problem  has  inspired  sig-

nificant  progress in  the  geometric  theory  of planar differential  equations,  bifurcation

theory,  normal forms,  foliations  and some topics  in  algebraic geometry.  For the  intro-

duction and recent progress of Hilbert's 16th problem, one may  look at the surveys and

books [28, 30, 35, 43].
 1

For the quadratic vector fields

where  P2 (x,  y)  and Q2 (x,  y)  are  quadratic polynomials,  in  1994, Dumortier,  Roussarie

and Rousseau launched a program [DRR program] aiming at proving the finiteness part

of Hilbert's  16th  problem  for  the  quadratic  vector fields.  The  DRR  program  aims  to

prove that H(2) is finite.

In [15], Dumortier, Roussarie and Rousseau proved the following theorem using the

compactness arguments based on the ideas ofRoussarie [39].

Theorem  1.0.1.  There exists a uniform bound/or the number of limit cycles of quadratic

vector fields if and only if all limit periodic sets surrounding the origin inside the family

{
 .  \  2  2 x  =  AX  - µy + aix  + a2xy + a3y  ,

iJ  = µx + AY + bix2  + b2xy + b3y2  (1.0.1)

The above theorem  is  important and significant.  It transfers the global problem into

a local problem of proving the finite cyclicity of all limit periodic sets in family (1.0.1 ).

Definition  1.0.2.  [22] Let X,x  be any family of vector fields.  A  limit periodic set r  is a

nonempty compact set invariant by X,x0 ,  such that there  exists a sequence  { An}nEN  and

for each An,  X.xn  has a limit cycle /-Xn  with the property:  An  ---+  Ao and distH(r, /.xn)  ---+  0

for n  ---+  oo.
 2

Definition  1.0.3.  [2] A  limit periodic set r of a vector field X,x0  inside a family  X,x  has

finite cyclicity in X,x  if there exist N  E  N and c > 0,  8 > 0 such that X,x  with I A - Ao I < 8

has at most N  limit cycles {i with distH(r, Ii)  < c.  The  minimum of such N  when c and

8 tend to zero is called the cyclicity of r  in  X,x  which we denote by Cy cl (r).

A limit periodic set surrounding the origin inside the family (1.0.1) can be a periodic

orbit, a graphic or the origin itself [ 15].  It was shown that the center-type singularity

and the periodic orbit have finite  cyclicity  in  [2]  and [22],  respectively. Therefore, in

order to prove the finiteness part of Hilbert's 16th problem for the quadratic vector fields,

according to Theorem 1.0.1, one needs to

•  list all the graphics surrounding the origin inside the family (1.0.1 );

•  show that each graphic has finite cyclicity.

In  [15],  all  the possible graphics inside the family  (1.0.1) were listed and named,

and there are a total of 125 graphics. For the DRR program, these 125 graphics are

needed to be proved to have finite cyclicity. The program is progressing well since 1994

when the program was launched, and lots of works have been done towards the program

[10-12, 14, 18, 19, 21, 26, 36-38, 40, 41, 44, 46, 53]. We summarize the DRR progress in

Table  1.1.

A graphic of planar quadratic vector fields can be an elementary graphic, a nilpotent

graphic or a degenerate graphic.  A  graphic is elementary if all  singular points of the

graphic are elementary, i.e., hyperbolic saddle or semi-hyperbolic point (one nonzero

3

eigenvalue).  A  graphic  is  nilpotent if there  is  a nilpotent singularity  in the  graphic.  A

graphic is degenerate if it contains a line or circle of singular points.

Table  1.1: The progress of the DRR program

Class of graphics  Done  Open  My work

Hyperbolic graphics  10

Elementary non-hyperbolic graphics  47  1

Nilpotent graphics of saddle type  2  1 * +1

Nilpotent graphics of elliptic PP-type  20

Nilpotent graphics of elliptic HP-type  6  4

Nilpotent graphics of elliptic HH-tyI?e  10  1 *+1

The four additional cases  4

Nilpotent graphics of saddle-node type  4

Degenerate graphics  2  11

Total=125  85  36  4

For the elementary graphics,  some essential progresses have been made towards the

understanding of the bifurcation and cyclicity of elementary graphics through the works

ofRoussarie [40,41], Mourtada [37,38], Morsalani and Mourtada [36], Il'yashenko [26],

Dumortier, Roussarie and Rousseau [14], Il'yashenko and Yakovenko [29], Kotova and

*Finite cyclicity was proved when the nilpotent singularity is of codimension 3 [53].

4

Stanzo  [33],  Dumortier,  El  Morsalani  and  Rousseau  [12],  El  Morsalani  [21]  and  Du-

mortier, Guzman and Rousseau [1 O].  For the DRR program, nearly all elementary graph-

ics have been proved to have finite  by these works, and only the cyclicity of the graphic

( fi6a)  is still open.

For the graphics with nilpotent singularity, it presents analytic difficulties for the tran-

sition maps near the nilpotent singularity compared to the elementary graphics.  In  [18],

Dumortier, Roussarie and  Sotomayor studied the cuspidal loop by an analytic and geo-

metric method based on the global blow-up techniques for the unfolding [ 4, 7, 42], which

desingularizes the nilpotent graphic of families of vector fields  into elementary graphics

of foliated  local vector fields.  Their work was the first  study of a graphic with a nilpo-

tent point,  and  made the  study of finite  cyclicity of nilpotent graphics  possible.  Later,

Zhu  and Rousseau  refined  and  developed the  ideas  in  [18]  to  study the  finite  cyclicity

of several graphics  passing through a nilpotent point of saddle or elliptic type of codi-

mension  3  [46, 52, 53].  They  proved that  more  than  20  nilpotent graphics  have  finite

cyclicity. Recently, Roussarie and Rousseau studied and proved finite cyclicity of 4 fam-

ilies of nilpotent graphics  of elliptic PP-type  surrounding a center by  using the  Bautin

Ideal [44].

For the  degenerate  graphics,  only the  graphics  (DF1a)  and  (DF2a)  were  proved to

have  finite  cyclicity  by  Dumortier and  Rousseau  [ 19],  and  the  cyclicity of the  rest  11

degenerate graphics are still open.
 5

The study of the finite cyclicity of graphics can not only give a deep understanding of

the existence of limit cycles of planar polynomial vector fields,  but also promote inven-

tions of new mathematical tools and development of nonlocal bifurcations for dynamical

systems.

For the graphics with a nilpotent singular point of multiplicity 3, they can be one of

the following types:

•  graphic through a nilpotent saddle: Fig.  1.1;

•  graphic through a nilpotent elliptic point:  Fig 1.2.

(a)  Convex  (b)  Concave

Figure  1.1:  Graphics through a nilpotent saddle

A  graphic through a nilpotent saddle can  happen in two cases:  convex RH-graphic

and  concave  RH-graphic.  For  the  quadratic  vector  fields,  since  any  non-degenerate

graphic  is  convex,  so  only the  convex RH-graphic  through  a  nilpotent saddle  appears

in the quadratic vector fields.

A  graphic through a nilpotent elliptic point can happen in  three cases:  PP-graphic,

6

(a)  PP-graphic  (b)  HP-graphic  ( c)  HH-graphic

Figure 1.2: Nilpotent graphics with an elliptic point

HP-graphic and RH-graphic.  Following the convention in [33, 53], we use PP to denote

a  graphic  going out of a  parabolic sector to  a  parabolic sector,  HP to denote a  graphic

going out of a hyperbolic sector to a parabolic sector, and HH to denote the graphic going

. out of a hyperbolic sect~r to a hyperbolic sector ..

Among these  125  graphics, there are 4 families of RH-graphic with a nilpotent sad-

dle.  They are  (1{2 ),  (1{3 ),  (FJ)  and (1{4 ),  where the graphics (Ji2 )  and (Jh) surround a

focus,  and the graphics ( FJ)  and ( fi4 )  surround a center.

There  are  12  families  of RH-graphics with a  nilpotent elliptic point.  Among these

12  families  of RH-graphics,  there  are  4  families  of graphics  (Hl),  (H~), (Hf2 )  and

(Hf
5)  which are hemicycles, there are  6  families of graphics  (HJ),  (Fib),  (H{3 ),  (!Jb),

(Hf
3 )  and  (Hf
4 )  which  surround  a  center,  and  the  rest  2  graphics  are  (!Jb)  and  (J{1b)

surrounding a focus.

In the thesis, we will prove that 2 families of convex HR-graphics of saddle type (1{2 ),

7

Uta)  and  2  families  of RH-graphics of elliptic  type  (IJb),  (I{ib)  have  finite  cyclicity.

For these  4  families  of HR-graphics, each family  of RH-graphics surrounding a focus

has an invariant parabola and a triple nilpotent singularity at infinity  which  could be of

codimension  3 or 4 as shown  in  Fig.  1.3.  There  is  an additional attracting saddle-node

on the invariant parabola for the graphic Ula) and (I{1b),  respectively.

For the  graphics (J[2 )  and (!Jb),  if the nilpotent singularity is  of codimension  3,  it

has been done by  Zhu  and Rousseau  [53].  Therefore,  we  only  need to  study  these two

graphics when the nilpotent singularity is of codimension 4.

(d)  (1~3)

Figure 1.3: Graphics for which.we  prove finite  cyclicity

8

To prove the finite cyclicity of graphics (1{2),  (1{3),  (!Jb)  and (I{1b), one basic ingre-

dient is the blow-up of families  developed in  [18].  Some mathematical tools have been

introduced and developed for the study of the cuspidal loop [18] and nilpotent singularity

of saddle or elliptic type [52, 53].  These tools include:

1.  a special normal form  for a family with a nilpotent singularity;

2.  blow-up  of the  family  to  allow  the  calculations  of the  transition  maps  near  the

nilpotent singularity;

3.  the list of limit periodic sets in the blown-up family of vector fields;

4.  calculations of different types of Dulac maps in  the neighborhood of the singular

points of the blown-up sphere;

5.  Poincare maps and displacement functions;

6.  generalized derivation-division methods.

Since the nilpotent singularity can be of codimension 4 in these 4 families of graphics,

some  generic  properties  of the  related  maps  fail  which  brings  more  difficulties  in  our

study.  Therefore, besides the above tools, we also need to make use of some techniques

and special properties of the specific graphics for the proof which include:

1.  first integral of Hamiltonian systems;

9

2.  calculation of Poincare first return map and the second derivative of the transition

map along the invariant parabola;

3.  fixed  connection along the equator.

With the above tools, techniques and  special properties of the specific graphics,  we

prove that the 4 families of HR-graphics (Ji2),  (Ji3),  (!Jb)  and (I{ib) with a triple nilpo-

tent singularity of saddle or elliptic type have finite cyclicity.

The thesis is organized as follows.  In Chapter 2,  we introduce some basic concepts,

theorems and  mathematical tools which  are  fundamental  and  required  for  the  proof of

the finite  cyclicity of graphics.  In Chapter 3,  we prove the finite cyclicity of (Ji2 ).  The

finite  cyclicity of (Jf3 )  is  proved  in  Chapter 4.  We  prove the finite  cyclicity of (!Jb)  in

Chapter 5.  In  Chapter 6,  we  prove  the finite  cyclicity of (Jiib)  except the  cyclicity of

Ehh3e  in which the nilpotent elliptic point is  of codimension 4.  Finishing the  proof of

the  cyclicity of these  4  families  of HR-graphics represents  one  important step towards

the proof of the finiteness part of Hilbert's 16th problem for quadratic systems.

10

2  Preliminaries

In  this  chapter,  we  introduce  some  basic  concepts,  theorems  and  mathematical tools

which are fundamental and required for the proof of the finite  cyclicity  of graphics.

2.1  General  finite  cyclicity theorems

For the  graphics with  a  nilpotent  singular point  of an  analytic  vector  field,  Zhu  and

Rousseau [53] proved the following  theorems.

Theorem  2.1.1.  A convex RH-graphic through a triple nilpotent saddle of codimension

3  has finite  cyclicity if the  graphic  is generic,  i.e.,  the  associated Poincare first return

map P  satisfies P' ( 0)  #  1.

Theorem  2.1.2.  An HR-graphic through a triple nilpotent elliptic point of codimension

3  has finite  cyclicity if the graphic  is  generic,  i.e.,  the  associated Poincare first return

map satisfies P' ( 0)  #  1.
 11

2.2  Transition  maps

2.2.1  Derivative  of a  regular  transition  map

Theorem  2.2.1.  [1] Consider the vector field

a  a
X  = P( x, y) ax + Q( x, y) By  .

Let  E  =  {(x, y)  =  (/1(s), gi(s))}  and E =  {(x, y)  =  (h(s), g2(s))}  be  two  arcs

transverse to  the same orbit r( t).  Let R( s) be the transition map from  E to E.  Then

R'(s) =  exp  divX(r(t))dt  ,
~(s)  (1T(s)  )

~(R(s))  o  (2.2.1)

where T(s)  is the time to go from  (!1(s), gi(s)) to  (h(R(s)),  h(R(s)))  along the orbit

r(t) starting at (fi(s),g1(s))fort =  0,  and

P(f1(s),g1(s))  fHs)

~(s) =

2.2.2  Dulac  map  near  a hyperbolic  saddle  in  the  plane

Definition  2.2.2.  For a planar vector field,  a singular point is elementary if it has at least

one nonzero eigenvalue.  It is hyperbolic (resp.  semi-hyperbolic) if the  two  eigenvalues

are not on the imaginary axis (resp.  exactly one eigenvalue is zero).

Definition  2.2.3.  The  hyperbolicity  ratio  at a  hyperbolic  saddle  is  r

A1  < 0 < A2  are the two eigenvalues.
 12
 _..\i  where
..\2'

Let  X,x,  ,,\  E  A,  be  a  C 00  family  of planar  vector field  defined  in  a  neighborhood

of a  hyperbolic  saddle at the origin,  where  A is  the  parameter space.  Assume that the

coordinate axes are the invariant manifolds of the saddle point.  Let r,x  be the hyperbol-

icity  ratio  of X,x  at  the  origin.  By normal  form  theory,  for  any fixed  k  E  N,  up  to  a

Ck-equivalence, the vector field  X,x  can be written into some explicit expressions of the

normal form  [27, 48].

•  If r 0  is irrational, \:/k  E  N, the vector field  X,x  is Ck-equivalent to

{
 X  =X

ii  =  ~r(A)y,

for ,,\  in a neighborhood W  of the origin in parameter space.

•  If r0  E  Q, let r0  =  E,  (p, q)  =  1.  Then \:/k  E  N,  X,x  is Ck-equivalent to
q
 x  =x,  N(k)
y  = y [ - ro + L ai+1(--\)(xPyq)i],

i=O

for,,\ in a neighborhood W  of the origin in parameter space, and a 1 (--\)  = r(--\)-r0 •

Let E1  =  {y  =  y0 }  and E2  =  { x  =  x0 }  be two  sections transverse to  the  vector

field  X,x  as shown in Fig. 2.1, where x 0 , y0  > 0 are constants.  The flow of X,x  induces a

transition map D ,x ( ·), also called a Dulac map:

13

y

0  x

Figure 2.1: Dulac map near a hyperbolic saddle in the plane

for all A E  W.

The Dulac map is C 00  for x  > 0.  The  following  theorem describes its behavior near

x  =  0.

Proposition  2.2.4.  [37]  The Dulac map D>.  can be written as
 (2.2.2)

where c(.X)  = :¥fu, 'ljJ(x,  .X)  is C 00 for (x,  .X)  E  (0, x 0]  x W. Furthermore, 'ljJ satisfies the
XO

following properties (IQ°):

(IQ°)  :  Vn EN,  an'lj;
lim xn-
8  (x, .X)  =  0  uniformly for A E  W
x-+O  xn  (2.2.3)

Furthermore,

(1) if ro  fl.  Q, then 'ljJ  = 0;

(2) if r 0  = 1,  the expression (2.2.2) is in general not.fine enough/or proving the cyclicity.

14

Definition  2.2.5.  [34, 40] The Leontovich-Andronova-Ecalle-Roussarie compensator of

the vector fields x,\ is defined as
 (2.2.4)
if a1  = 0.

The Dulac map in Proposition  2.2.4 is not fine  enough to prove the cyclicity  for the

case r0  =  1.  In [40], using the compensator, Roussarie has an additional refinement:

Proposition  2.2.6.  [40] If r0  =  1,  the  Dulac map  D,\  has a well-ordered asymptotic

expansion:

D,\(x)  = a1(--\)[xw  + · · ·] + f31(--\)x  (2.2.5)
+a2(--\)[x2w + · · ·] + · · · + ak(--\)[xkw  + · · ·] + 'l/Jk(x,  --\),

where a 1(.A)  =  r(.A)  - 1,  ai(.A)  and {3(--\)  are smooth functions of the parameters--\.  'l/Jk

is a Ck function,  k-.ftat with respect to x  =  0.

2.2.3  Transition  map  near  a semi-hyperbolic  singularity

Let  X,\  be  a  family  of planar vector  fields  sufficiently  differentiable  with  respect  to

( ( x, y),  ,,\)  E  JR2  x  A.  Suppose  that the  vector field  X 0  has a  semi-hyperbolic  singu-

lar point at the origin of codimension  m  and the  coordinate axes  are its  local invariant

manifolds.  In  [27], it was proved that for any k  ~ 2m, the family  X,\  can be written up

15

to a Ck  equivalence form
 {  x  =  F(x,,.\),
(X,\)
 iJ  = -y,

for ,.\  in a neighborhood W  of the origin in parameter space, where

m-1
F(x, ,.\)  = c(,.\)xm+l(l + c(,.\)Q2m+i(,.\)xm) + L Qi(,.\)xi.

i=O

The Qi ( ,.\)  are  smooth functions of the parameters ,.\  with Qi ( 0)  =  0 for 0  ~ i  ~ m  - 1

and  c(O)  #  0.  The quantity  Q 2m+i (0)  is  the  formal  invariant of the  germ  of X0  at the

origin.
 y  y

x

(a)  Central transition  (b)  Stable-centre transition

Figure 2.2:  Two types of transitions near a semi-hyperbolic point

•  Central transition

For some values of the parameters, the vector field  X 0  may have no  singular points.

This  yields  possible  transitions  along  the  center  manifold  {y  =  0}  from  a  =  { x  =

16

-x0 , -yo :::;  y:::;  Yo}  to T  = {x = xo, -y1  :::;  y  :::; Y1}  where xo, Yo, Y1  > 0 are chosen

such thatthe transition D,\(y) is defined from a to T,  and ,XE  Op:=  {.XE  WI  F(x, .X)  #-

0,  \:/x  E  [-xo, xo]}.

Proposition 2.2.7.  [14]  The transition  map D,\(y) is linear  and

D>.(Y)  = m(.X)y  with  ( l
 xo  dx  )
m(.X)  =exp  - -xo  F(x, .X)  .  (2.2.6)

The function m( A)  is  continuous and non-zero on 0  p  and has  a  continuous extension

m(.X)  = Ofor A E  80p.

•  Stable-centre  transition

Take  sections a  =  {y =  Yo, -xo  :::;  x  :::;  xo}  and T  =  { x  =  xo, -y0  :::;  y  :::;  y 0 }

where x0  > 0 and y0  > 0.  For A = 0 and x0 ,  y0  sufficiently  small, we have a transition

D0 ( x) from  a+  =  { ( x, y)  E  a Ix  > 0}  to T  along the trajectories of X0 .  This transition

can  be  extended  for  any  value  of ,X  for  some  subinterval a,\  c  a  to  T  in  a  transition

D(x, .X)  which is also denoted by D,\(x). The subinterval a,\  is defined as follows.

(i) If A E  Op, then a,\  = [-x 0 , x0 ].

(ii) If A tf- Op and z(-X) is the largest root of F(x, .X)  = 0 with -x0  :::; z(-X) :::; x0  and

z(O)  = 0, then a,\= [z(-X),  x0 ].  We  extend D,\(·) continuously at z(.X) by D,\(z(-X)) = 0.

The domain of D,\(x) is C = U,\{a,\, .X}  C  [-x 0 , x0 ]  x  W.

The stable-centre transition map D(x, .X)  satisfies the following  flatness property.

17

Proposition  2.2.8.  [14]  For  the  stable-centre  transition  map  D(x, >-.)  de.fined  above,

V p, n  EN andV (io, ii,···  , iN) with io +ii+···+ iN  = n,  we  have

an D(x, >-.)  = O(I  'IP)  w(  ')  C .  .  x, A  ,  v  x, A  E  .

8xio8)..~
1  ••• x;  (2.2.7)

2.3  Normal  forms  near  nilpotent  singularities  of multiplicity  3

A  family  containing a triple nilpotent singularity of elliptic or saddle type can be written

as [17]
{:

=y,  (2.3.8)

where for the saddle case c 1  =  1 (Fig. 2.3(a)); for the elliptic case ci  =  -1, b >  2)2

(Fig. 2.3(b)),  )..  = (>-.1 ,  )..2 ,  )..3 )  are the parameters, h(x,  )..)  is  C 00  in  (x,  >-.), Q(x,  y,  >-.)  is

C 00  in  (x,  y,  >-.)  and of arbitrarily high order in  (x,  y,  >-.).  For any value of c2,  they  have

the same topological type.

For the purpose of studying the passages in the neighborhood of the nilpotent singu-

larity, a new normal form  to unfold the nilpotent singularity of saddle or elliptic type was

developed in [53].
 18

(a)  Saddle case  (b)  Elliptic case

Figure 2.3:  The different topological types

Theorem  2.3.1.  [53] The family (2.3.8) is C 00 -equivalent to

{;
 = Y  + µ2  + a(µ)X 2,

=  µi + Y(µ3  + X  + €2X2 + X 3h1(X,µ)) + X 4h2(X,µ) + Y 2Q(X, Y,µ),

(2.3.9)

•for the saddle case:  a(O)  E  (-~, 0),

if a(O)  =  -~, the  unfolding is of codimension  4 which corresponds to  the  case

b = 0 in (2.3.8);

•  for the elliptic case:  a(O)  E  (0,  ~ ),

if a(O)  =  ~' the  unfolding is of codimension 4,  type  2,  which corresponds to  the

case £ 2  = 0 in (2.3.8).
 19

µ  =  (µ 1 , µ 2, µ 3)  is  the  parameter,  h1(X,  µ),  h2(X,  µ)  =  €2a  + 0(µ)  + O(X)  and

Q(X, Y,  µ)are  C00  and Q(X, Y,  µ)is of arbitrary  high order in  (X, Y,  µ).

We  denote A= [-~, 0)  for the saddle case, and A= (0, ~)for the elliptic case.

2.4  Blow-up of the family

We  are interested in  the  family  for  a  E  A  and  ( x, y, µ)  in  a  neighborhood U  x  A  of

((0, 0), (0, 0, 0)). Taking A as a sphere, we make the change of parameters
 (2.4.10)

whereµ  =  (p, 1 , p, 2 , p, 3 )  E  § 2  and v  E  (0, v0 ).  Adding  the  equation v = 0  to  system

(2.3.9), we have

x:  y  = v3
P,1 + y [vp,3 + x + €2x
2 + x3
h1(x, vµ) J

+x4h2(x, vp,) + y2Q(x, y, vp,),

ZJ  = o.

We  then make the weighted blow-up

x = rx,  y = r 2fj,  ZJ  = rp,

where r  > 0 and (x,  fj, p)  E  § 2 •
 (2.4.11)

(2.4.12)

By  the blow-up  (2.4.12), we have a C 00  family  X  = ~X. Note that for each (a,µ),

the foliation given by { v = r p = const} is preserved by X (a,µ):

20

(a)  The saddle case  (b)  The elliptic case

Figure 2.4:  The stratified set {rp = O}  in the blown-up

•  For { r p = v} with v  > 0, the leaf is a regular manifold of dimension 2.

•  For {rp  =  O},  we get a  stratified  set  in the critical  locus.  As shown  in  Fig.  2.4,

there are two strata of 2-dimensional manifolds:

the blow-up of the fiber µ  = 0,

- Dµ  = { x
2 + fj2  + p2  = 1,  p  2::  0}.

On Fµ  = {p = 0}, (2.4.12) is just the common blow-up of the nilpotent point:

x  = rx,  y = r
2y.  (2.4.13)

By the blow-up (2.4.13), we get a vector field with four singular points Pi (i = 1, 2, 3, 4).

P3  and P4  are hyperbolic saddles, Pi and P2  are saddles (resp.  nodes) in the saddle (resp.

elliptic) case as shown in Fig. 2.5.

The four points ~ on the circle x 2  + y2  = 1, r  = p = 0 are studied in the charts

P.R.l  x =  -1, (r1, pi, Y1),  and  P.R.2  x =  1, (r2, P2, Y2),

21

(a)  The saddle case  (b)  The elliptic case

Figure 2.5:  Common blow-up of the nilpotent singularity

while the upper part of the sphere r  =  0,  p  >  0 is studied in the chart

F.R.  p  =  1,  (x,  y,  r)

yielding
 y =  fli  + (fl3 + x)y  + rli(x, y,  r, fl),  (2.4.14)

r =  o,

where ii(x, y,  r, fl)  is C 00  in (x,  y,  r, fl).  Especially, on {r =  O}, we have

_  {  x = fl2 + y + ax
2 ,
Xµ=l:
 fJ  = fli + (fl3 + x)y.
 (2.4.15)

In  [53],  the  complete bifurcation analysis of (2.4.15) was  given and  phase portraits

for the different values of fl  E  § 2  were studied and presented.  Together with the regular

part of the graphics, we have a list oflimit periodic sets for which finite cyclicity must be

22

proved.  In [53], Zhu and Rousseau listed all the possible limit periodic sets of HH-type

for the saddle case, and PP-type, HP-type and HH-type for the elliptic case.  As the limit

periodic sets ofHH-type for the saddle case and elliptic case will be needed in our proof,

so we recall them in the following Table 2.1  and Table 2.2.

family Sxhh 1  family Sxhh2  family Sxhh3  family Sxhh4

family Sxhh5  family Sxhh6  family Sxhh7  family Sxhh8

family Sxhh9  family SxhhlO

Table 2.1:  Convex limit periodic sets ofHH-type for the saddle case [53]

23

family Ehhl  family Ehh2  family Ehh3  family Ehh4

family Ehh5  family Ehh6  family Ehh7  family Ehh8

family Ehh9  family Ehh I 0  family Ehh 11  family Ehh12

Table 2.2:  Limit periodic sets of HH-type for the elliptic case [53]

2.5  Dulac maps  near~ (i  ==  1, 2, 3, 4)

For saddle and elliptic case, the family of vector fields  at each point Pi  ( i =  1,  2,  3, 4)

has the same form.  Due to the special form of the family, after dividing by a C 00  positive

function, the system is linear in rand p.  If necessary, one can reverse the time (t 1---+  -t),

so  that one will have two negative eigenvalues and the third eigenvalue  is  positive.  So

24

for the three eigenvalues at each point, there are only two possibilities

-1,  1,  -a(a)

or
 1,  -1,  -a(a)

where a(a)  =
 2(1  - 2a),  at P3  and P4 •

By exchanging the roles of r and p,  one only need to consider the following system

r  = -r,

X(a,p,)  p  = p,  (2.5.16)

fj  = -a(a)y  + f(a,µ)(r,  p, y),

where

fca,µ)(r,  p,  y)
 (2.5.17)

with the parameters (a,µ)  E  A  x  § 2 •

Remark 2.5.1. For the quadratic systems,  we have h2  = 0 in (2.5.17).

Proposition 2.5.2.  [53] Consider the family Xca,µ)  in the form of (2.5.16) with param-

eters (a,µ)  E  Ax § 2.  Then V(a0 , µ)  E  Ax § 2  and Vk  E  N,  there  exists A 0  C  A,  a

25

neighborhood of a0,  N ( k)  E  N and a Ck -transformation

W(a,µ):  (r,p,y)----+  (r,p,'l/J(a,µ)(r,p,f})),

where
 'l/J(a,µ)(r,  p,  y)  = f} + o(l(r, p,  y)I)

such that \/(a, p,)  E  A0  x  § 2,  the map 'l/J(a,µ)  transforms  X(a,µ)  into one of the following

normal forms:

•  if a(ao)  ~ Q
 r  = -r,

X(a,µ)  p  =p,

iJ  = -a(a, P,,  v)y,

r  = -r,

x  p  =  p, (a,µ)

where v = r p > 0 and

a(a,  P,,  v)  = a(a)  - a 0 (a, µ,  v),

N(k)
ao(a,  P,,  v) =  L {ivi,
i=l

a 1 (a, µ,  v) = p - a(a, µ,  v)q,
 (2.5.18)

(2.5.19)

(2.5.20)

26

where /i(a, µ),  ai  and Kare  smooth/unctions de.fined/or (a,µ)  E  A0  x  § 2.  Especially,

K =  0 for q  2::  2.

- Notation 2.5.3.  For  convenience in the notation,  in the following sections and chapters,

let r 0 ,  Po  and y0  be positive constants,  and we always use

Ei  = {ri  = ro},  i  = 1,2,3,4;

IIi  ={Pi=  Po},  i  = 1,2,3,4;  (2.5.21)

Ti  ={Yi= Yo},  i  =  1, 2;

Ti  ={Yi= -yo},  i  = 3,4,

to denote the sections in normal form coordinates  (ri,  Pi, Yi) in the neighborhood of the

singular points I{ (i = 1, 2, 3, 4).

In order to  study  the transition maps  near the  singular point  I{(i  =  1, 2, 3, 4),  one

only need to consider X(a.µ)  with eigenvalues -1, 1, -a(a)  in the normal forms  (2.5.18)

or (2.5.19) and consider the following  two types of Dulac maps:

~(a,µ)= (d,  D):  E  ~II,

8(a,fl)  = (~, 3):  T  ~II,

where E  =  {r = r0 },  II= {p = p0 }  and T  =  {y = y0 }  are sections in the normal form

coordinates.

The  properties and explicit expressions of the two types of Dulac maps are given  in

the following two  theorems, which were studied by Zhu and Rousseau in [53].

27

p  p

r

(a) The first type  (b)  The second type

Figure 2.6: Two  types of Dulac maps

Remark  2.5.4.  To  simplify the notation, for all the maps and vector fields,  we will drop

the index (a,µ).  For example,  the Dulac map ~(v, y)  means ~(a,µ)(v, y).

Firstly we  study  the  first  type  of Dulac map  ~ =  (d, D).  If we  parameterize the

sections~ and II by  (v, y)  with the obvious relation p = .!!_on~ and r = .!!_  on II, then
ro  Po

we have

Theorem  2.5.5.  [53]  For  any  a0  E  A  and fl  E  § 2,  consider  the family  X(a,µ)  with

eigenvalues -l, 1, a(a0 )  in normal form (2.5.18) or (2.5.19).  Then 'v'Yo  E  JR,  there exist

A 0  C  A,  a  neighborhood of a0,  and v1  >  0  such  that \Iv  E  (0, v1)  and (a, jl, y)  E

Ao  x  § 2  x  [O, Yo],  the Dulac map ~(v, y)  = (d(v, y), D(v, y)) has the form

{
 d(v, y)

D(v, y)
 =v,
 28
 (2.5.22)

where v0  =  r 0 p0  > 0 is a constant and

if a(ao)  i  Q,  T/  = ¢ = O;

if a(ao)  E  Q \  N,  TJ  = O;

if a(a 0 )  = ~ E Q  p, q EN and (p, q)  = 1,  then cp(v, w(~, -a 1 ), y)  is C 00  and

a<P  = O(v'Pwq(..!!....  -a1) ln ..!!....)
f)y  vo'  vo  '

f)i~ = o(v'fi(1+[¥])wq-j+l+q[¥l(~ -a  )  ln ~)
fJyJ  '  1  ' Vo  Vo  j?.  2,
 (2.5.23)

where
 _  {  qa(a,·v),
p=
 p,  a1  < 0.

Also all the partial  derivatives with respect to the parameters  (a,  P,)  are  of order

Now  we  cons.ider the  second  type  Dulac map  8  =  (~, 3).  If we  parameterize r

by  (r,  p)  and  II  by  (v, y)  with  the  relation rp  =  v  and r  =  :O  on  the  two  sections

respectively, then we have

Theorem  2.5.6.  [53]  For  any a0  E  A, consider  X(a,µ)  with eigenvalues -l, 1, -a(a 0 )

in the normal form (2.5.18) or (2.5.19).  Then for r,  p  > 0 sufficiently small,  there  exist

29

A0  C  A,  a neighborhood of a0,  and v 1  > 0 such that 'ti( a,µ)  E  A0  x  § 2  and v  E  (0, v 1),

the Dulac map 8 ( r,  p)  has the form

{
 ~(r,p)  = v,

~(r,p)  = 17(v,w(L,a1)) + (_e_t[Yo + ()(r,p,w(_e_, -0:1))],
Po  Po  Po
 (2.5.24)

where

•  if a(ao)  ¢:_  N,  then T/  = 0; if a(ao)  = p EN,  then

- K,  p  (  p  )·
T/  - rP v  w  - ' D'.1  '
Po  Po

•  ifa(ao)  ¢:_  Q  then()=  O;  ifa(ao)  =  ~ E  Q,  then ()(r,p,w(L,-ai))  is  0 00  in
q  PO

(a,µ)  and (r,  p, w( L, -a 1 )),  and also satisfies
PO

()  =  0  (pPw(fo, a 1 )  [ 1 + K,rPw2(fo, -ai) J) ,

pi~~  =  0  (pPw(fo, 0:1)) [ 1 + K,rPw2(fo, -a 1)]) ,  j  ~ 1.
 (2.5.25)

which are  uniformly valid for (a,µ)  E  Ao x  § 2  and r,  p > 0 sufficiently small.

Remark 2.5.7. For  the quadratic  systems, we have 17(v, w(~, -a 1 )) = 0 in (2.5.22) and

17(v,w( L, a 1 ))  = 0 in (2.5.24).  For  the second type Dulac map,  the inverse of8 has the
PO

same form and properties as (2.5.24) and (2.5.25).

30

3  Finite  cyclicity of ( !{2)

For the graphic (!{2 ), it is an HH-type graphic with a nilpotent saddle of multiplicity 3 at

infinity  and an invariant parabola as shown in Fig. 3.1.

Figure 3.1: The graphic (!{2 ).

In this chapter, firstly  we prove the general theorem 3 .1.1  for the finite  cyclicity of a

convex graphic through a nilpotent saddle of multiplicity 3 in section 3 .1-3 .3. According

to the general theorem, to prove the finite  cyclicity  of (Jl2 ),  we  only  need to check that

the first return map P along the invariant parabola satisfies P'(O)  =/=  1, which is given  in

section 3.4.
 31

3.1  Main  theorem

Theorem  3.1.1.  A  convex graphic through a nilpotent saddle of multiplicity 3 has finite

cyclicity provided that the derivative of the.first return map P'(O)  =/=  1.

For the  nilpotent  saddle of multiplicity  3,  it  can  be  of codimension  3  or 4.  The

theorem with  codimension  3 nilpotent saddle was proved in  [53].  When  a0  =  -~,the

nilpotent  saddle  is  of codimension  4.  In  this  special case,  only  the  limit  periodic set

Sxhh 1 used  the  hypothesis  a0  =/=  - ~, so  we  only  need  to  treat the  case  Sxhh 1 with

The finite  cyclicity  of the upper boundary graphic of Sxhh 1 was proved in  [ 5 3 ], and

Cycl(Sxhhla)  ::;  1.  Therefore,  we. need  to  prove  that the  iritermediate graphics an~

the lower boundary graphic of Sxhh 1 have finite  cyclicity,  and the proof is given  in the

section 3 .2 and section 3 .3.

3.2  Preliminaries

Let r be  any  intermediate or lower boundary graphic of Sxhh 1.  To  study  its  cyclicity,

as  shown  in  Fig.  3.2,  take  sections Ili =  {Pi  =  p0 }  in  the  normal form  coordinates

(ri, Pi, fh)  in  the  neighborhood of the  singular point  ~(i =  3, 4).  We  will  study  the

32

Figure 3.2:  Transition maps for the HR-graphics of saddle type

displacem_ent map

L =  R- 1 -T
'

where R  : II3  ~ II4  is  the transition map along the  regular orbit in  the normal  form

coordinates,  and T  :  II4  ~ II3  is  the  transition  map  passing through  the  blown-up

singularity.  We will study the maximum number of small roots of L  = 0.

For the transition map R,  it has been studied in [53], and we recall it here as a propo-

sition.

Proposition 3.2.1.  [53) For any k  E  N  and \:/a0  E  A  =  (-~, 0),  there  exist A 0  C  A,

a  neighborhood of ao  and v 1  >  0  such  that \:/(a, P,)  E  A0  x  § 2  and \:/v  E  (0, v 1),

33

R(v, ih)  = (R1(v,  ih), R2(v,  ih))  is Ck  and Rl(v, ih)  = v,  R2(v,  ih)  takes the following

form

(1)  if ao  ¢ Q,

R2(v,f)3)  = mo(v)C~)-a
4 + b* + O(vln  ~))y3

k  (3.2.1)
+ L O(v(i-l)a3)y~ + ow:+l);

i=2

2) if ao  E  Q,
 (3.2.2)

where
 "Yo=  mo(v)( ~ )-a 4  + K,3rg
3 (7*  - l)w( ~' -/31)) + K,30(va 3w2( ~'-{Ji)),
Vo  Vo  Vo
v  - v  v
71  = 1* + 0  ( v ln - ) + 0  ( vP 3 wq
3 (  - ,  - {31 )  ln - ) ,
Vo  Vo  Vo

"Yi=  O(vln ~) + O(J5
3(1+[i~

2 ])wq
3+l-i+q
3[i~
21 ( ~' -f31) ln ~) i  2::  2.
~  ~  ~

Here 1*  =  P'(O)  and {31  =  p3  - a3 (a)q3.  Also R2 1(v, y4 )  is Ck  and has the same form

Remark 3.2.2. The  above proposition was proved in  [53]  by straightforward calcula-

tions of the transition map R, which can be decomposed as

-1  -R = Ll 4  o  R o  Ll 3 ,

where  Lli  : Ili  ~ :Ei ( i  =  3, 4)  are  two  Dulac transition maps of the first type  in the

34

normal form coordinates  near  P3  and P4 ,  respectively.  R  :  E 3  ----t  E 4  is the  regular

transition  map,  and we can write it as

{
 Ri(v, y3)  =  v,

R2(v, y3)  = mo(v) + m1(v)y3  + O(y~),

where m0(0)  = 0,  and m1 (0)  = 1* + O(v).
 (3.2.3)

In the proof, only the fact a 3 (a) =  2(1  - 2a)  > 0 was used.  So as long as a<  ~'the

three  maps ~3, Rand ~4 keep the same expressions as the case for a0  E  (-~, 0).  There-

fore,  the  interval  A  =  (-~, 0)  in  the  above proposition  can  be  extended to  (-oo, ~).

Hence,  if a0  E  ( -oo, ~ ),  R 2 (v,  ih)  has the same form as (3.2.1) or (3.2.2).

Figure 3.3: Transition maps for the lower boundary graphic Sxhhlc

In  this  chapter, we  use  V  E  § 2  to  denote  the  set  of the  parameter µ in  which  the

family  Sxhhl  exists.  Family Sxhhl  has a lower boundary graphic Sxhhlc  which  passes

35

through a hyperbolic saddle point as shown in Fig 3.3.  Let Ao  be the hyperbolicity ratio

at this saddle point when r = 0 for fl= flo  and a= a0 •

For the case  Ao  f  1,  it was treated in  [53],  so we restrict ourself to the case  Ao  =  1

i.e., the divergence of system X p=I in (2.4.15) vanishes.  Note that a0  = - ~, so we have

p,3  = 0.  Then in this case family Sxhhl  exists if and only V  ={fl E  § 2 lfl3  = O}.

Let the saddle point be ( x0 , y0 ).  After translating the singular point to the origin, by

a linear transformation and Ck  changes of coordinates, we can bring the system (2.4.14)

in the neighborhood of the saddle point into a normal form

i=i,  N(k)
y = fj [ - 1 + L ai(r, fl, a)(ifj)i],  (3.2.4)

i=O
r = o.

Take sections E 1  =  {fj =  1} and E 2  =  { i  =  1}  in the normal form coordinates. Let

D(v,i)  =  (D1(v,x),D2(v,x)):  E1  ~ E2  be the transition map.  ThenD1(v,i) = v,

and D 2 (v,  i) is the Dulac map in the neighborhood of the saddle point.  There exist Vo,  a

neighborhood of jl0 ,  and c  >  0,  v0  >  0 sufficiently small, such that Va  E  ( - ~ - c,  ~ +

c)  C  A, Vv  E  (0, v0 )  and V fl  E  Vo,  D(v, i) : E 1  ~ E 2  can be written as
 (3.2.5)

where ai are functions of (v,  jl, a)  given in (3.2.4), a1 (v)  = A(v )-1 and w = w(i, a1 (v))

is the Leontovich-Andronova-Ecalle-Roussarie compensator defined in (2.2.4).

36

Let T1  :  Il4  ~ :E1  and T2  :  :E2  ~ Il3 .  They are the compositions of normal form

coordinate changes and regular transition maps.  Therefore, T1 (v,  y4 )  can be written as

(3.2.6)

and T2 (v,  y)  can be written as
 (3.2.7)

where e0 (0)  = 0, b0 (0)  = 0,  ei (0)  > 0 and b1 (0)  > 0.

In  the  following,  we  study  the  lower  boundary  graphic  Sxhhlc  and  intermediate

graphics Sxhh 1 b.

3.3  Proof of the main theorem

We  treat  the  lower  boundary  graphic  Sxhh 1 c  and  intermediate  graphics  Sxhh 1 b  sepa-

rately.

3.3.1  The lower boundary graphic Sxhhlc

For the transition map T,  we have
 37

Performing a  change of parametrization on Il4 ,  the  displacement map  L  : Il4  ---+  Il3

will be defined as

L(v, 94)  = R- 1(v, Y4 + ((v)) - T(v, 94),  (3.3.8)

where ((v) = T121(v, 0)  with ((0) = 0,  and T = T2 o Do S1. For Si, we have

{
 Su(v, }4)  =  v,

B12(v, }4)  = ei(v)f4 + e2(v)Yl + O(Yl),

where ei (0)  = ei (0)  >  0.

By (3.2.5), (3.2.7) and (3.3.9), for T  we have

f2(v, Y4)  = bo(v)  +  e~-a
1 (v)b1(v)a1(v)[94w(Y4, ai) + ... ]

+e1(v)b1(v)Y4 + · · · .

By (3.2.2), (3.3.8) and (3.3.10), we have

{
 L1(v, 94)  = 0,  .

L2(v, 94)  = eo(v)  + c1(v)[94w(94, 0:1)  + · · ·]  + c2(v)Yt + · · · ,

where
 v
eo(v)  = ~o(v, w(-, -/31)) + O(((v)) - bo(v),
Vo

In order to prove the cyclicity of Sxhhlc, we need the follow lemma.

38
 (3.3.9)

(3.3.10)

(3.3.11)

Lemma 3.3.1.  e1 (0)b1 (0)  =  lfor v  =  0,  P,30  =  0 and a0  =  -!.

Proof  To calculate ei ( v) b1 ( v)  for v  =  0,  P,30  =  0 and a0  =  - ! , we can restrict ourself

on the blown-up sphere r  =  0 to study maps i\(O, ·)and T2 (0, ·).

Since ao  =-~,and P,30  =  0,  in the chart F.R. on r  =  O,we have system Xp=1'  which

becomes
{ : : ;~: :y-:~x~(: :i'.x, y),  (3.3.12)

We can use the quasi-homogeneous compactification

{  x =  ±l
Pi'

y= ~'
 (i  =  3, 4),  (3.3.13)

to study the singularities P3  and P4  at infinity of system (3 .3 .12), and obtain the normal

forms in the neighborhood of P3  and P4  in the chart F.R. on r  =  0.  Near P3  =  (0, 1), we

have
 (3.3.14)

where K 3  is the function ofµ.  Similarly, in the neighborhood of P4  =  (0, 1), we have

{
 p4  =  p4,  (3.3.15)
Y4  = 4y4 - K3p!.

Let 1ri  =  {Pi  =  p0 }(i  =  3, 4)  be the two  line  sections  in  the chart F.  R.  on  r  =  0

parameterized by Yi(i  =  3, 4), respectively.  Let a1  =  {y =  1} and a2  =  {x  =  1}  be the

39

two line sections near the saddle point in the chart F.  R. on r  =  0 parameterized by x and

y, respectively. Then we are reduced to study the one dimensional transition maps

Figure 3.4:  Transition maps for Sxhhlc in the chart F.R.  on r  = 0

To  calculate the maps T12 (0, y4 )  and T22 (0, y),  we  introduce two auxiliary line  sec-

tions fri  =  {Pi  =  p00 }  in  the  normal  form  coordinates  (pi, Yi)  near  Pi(i  =  3, 4)  with

0 < Poo  < po, which are expressed as follows.

ir3  = {(x, :Y)I  x =  f3(y3)  =  P~o,

Y = g3(y3)  =  P~ (1  + Y3 + ¢(y3) + Poo'l/J3(Poo, y3))  },
00  (3.3.16)

ir4  = {(x,y)I  x =  f4(y4)  = - P~o'

y = g4(y4)  =  -:2P1 (1  + Y4 + ¢(y4) + Poo'l/J4(Poo, y4))  },
00
 40

We also introduce another two auxiliary line sections 8-1  = {y  = d00 }  and 8-2  = { x =

d00 }  in the normal form coordinates ( x, y)  with 0 < d00  < 1.

As we k(n:~· :~e)r translating the singular point to the origin, by a linear transforma-

tion T  =  and  Ck  normal change of coordinates,  we can bring the  system

t3  t4

(3.3.12) into normal form  near the saddle point (x 0 , y0 ).  Hence, on the blown-up sphere

r  =  0,  8-1  and 8-2  can be expressed in the original coordinates (x,  y)  as follows.

Therefore, the map T12 (0, y4 )  :  7r4  ------+  0-1  can be calculated by the decomposition

where Tz  : 7r4  ------+  7f4,  Tz  : 7f4  ------+  8-1  and Tz  : 8-1  ------+  a1  are one dimensional regular

transition maps.  The map T22 ( 0, y)  : 0-2  ------+  7r3  can be calculated by the decomposition

where Tr  : a2  ------+  8-2,  Tr  : 8-2  ------+  ?f 3  and Tr  : ?f 3  ------+  7r3  are one dimensional regular

transition maps.
 41

For 1l and Tn form  (3.3.14) and (3.3.15), we have

,..  ,.,.., ( _ )  ( Pao )
4  _  4  1  ( Pao )
Y4  =  .L  l  Y4  =  Po  Y4  - K,3Poo  n  Po  ,  (3.3.17)
_  ,.,..,(")  (Po) 4 ,..  41  (Pao) Y3  = .Lr  Y3  =  - Y3  + K,3Po  n  - ·
Pao  Po  (3.3.18)

For Tz  and Tn using the formula in Theorem 2.2.1, we have

T/(O)  = doo  and  i';(o) = d0a1.  (3.3.19)

Next, we study transition maps Ti  : if 4 ---+ B-1  and Tr  : B-2  ---+ 7f3.

Let
 P(f4(0),  g4(0)  f~(O)

~i(O) =  P(f1(0),g1(0))  f{(O)
and  L°ii(O)  =

by the formula in Theorem 2.2.1, we have

-I
Ti(O)  =
 (3.3.20)

where T(7r4 ---+  0-1 )  denotes the time taken to travel along the lower graphic r from  7r4  to

Let
 P(h(O), 92(0)  f~(O)

~r(O) =
 42

Similar to Ti(o),  for T~(O) we have
 (3.3.21)

where T(a 2  ---+  -IT3 )  denotes the time taken to travel along the lower graphic r from a2  to

From (3.2.6) and (3.2.7), we have

_ (O)b  (O)  =  (O)b  (O)  =  aT12(0, 0) aT22(0, 0)
ei  1  ei  1  a- a- .
Y4  Y

Therefore, by (3.3.17), (3.3.18), (3.3.19), (3.3.20) and (3.3.21), we have

ei(O)b1(0)  =  lim  T((o)Ti(o)T!(O)  r;(o)T~(o)t;(o) = 1.
(poo,doo)---+(0,0)
 D

End of proof for  Sxhhlc

From (3.3.11), we have

Here  we  use  the  symbol  * to  replace  any  continuous  function  of (v,  P,, a),  which  is

nonzero at (v,  P,, a)  =  (0, P,0 , a0 ).  Let
 43

The  zeros  of  aL~;~Y
4
)  are  zeros  of the  function  6 (v,  Y4 )  in  a  small  neighborhood  of

Y4  = 0.

Differentiate ~1 (v,  Y4 )  with respect to }4, and we have

86 (v, }4)  (  ) 94-1-01  + . . .  1
--- - =  *C2  V  - + · · · .
8Y4  *1 + · · ·  w 2 (Y4, a 1 )

Let

then we have
 6(v, Yt)  =  *C2(v) + · · · .  (3.3.22)

Since  ry*  =/=  1,  so  c2 (0)  =  ~* - el (O)b1 (0)  =  1
1
*  - 1  =/=  0  for  v  =  0,  P,30  =  0

and  a0  =  -~.  Because  the  remainder  in  (3.3.22)  is  o(l).  Hence,  there  exist  A 0 ,  a

neighborhood of a0 ,  Vo,  a neighborhood of P,0 ,  and v1  > 0,  such that V( a,µ)  E  A0  x  Vo

and Vv  E  (0, v1 ), we have 6(v, Y4 )  =/=  0 in a small neighborhood of Y4  =  0.

By Rolle's Theorem, V(a, µ)  E  A0  x  Vo  and Vv  E  (0, v1), the map L2(v, ¥4)  =  0 has

at most 2 zeros in a small neighborhood ofY4  =  0,  i.e., Cycl(Sxhhlc)  ::; 2.

3.3.2  The intermediate graphics Sxhhl b

For the intermediate graphics Sxhh 1 b, we can write the regular transition map T  as

{
 T1(v, y4)  = v,

T2(v, y4)  =  eo(v) + c1(v)y4 + O(y~),

44
 (3.3.23)

where eo(O)  = 0 and c1 (0)  f- 0.

Hence, by (3.2.2) and (3.3.23), the displacement map L  = R- 1 -T has the following

form
 L1 (v,  fj4)  = 0,

L 2 (v,fj4)  =  70 (v,w(;
0 ,  -,83 )) + [ ~* + O(vP 3wq3 (:a,  -,81 )  ln :a)]iJ4  (3.3.24)

+O(iJD - [eo(v) + c1(v)fj4 + O(YD].

In order to prove the cyclicity of Sxhhl b, we need the follow lemma.

Lemma 3.3.2.  T2 (0, y4 )  is an identity for v  = 0,  P,30  = 0 and ao  =  -~.

Proof  Just as we did for Sxhh 1 c,  let 7ri  = {Pi  = p0 }( i  = 3, 4) be the two line sections in

the chart F. R. on r  = 0 parameterized by Yi(i  = 3, 4), respectively.  Then we are reduced

to study the one dimensional transition map

To calculate the map T2 (0, y4 ), again we introduce two auxiliary sections -fti  = {Pi  =

p 00 }( i  = 3, 4)  in the normal form coordinates in the chart F.R. on r  = 0 with 0  < p00  <

p0 •  Then the map T2 (0, y4 )  can be calculated by the decomposition

where 1l  : 7r4 --+  n4,  T  : n4  --+  -fi-3 and Tr  : 'fi-3 --+  7r3 are one dimensional regular

transition maps as shown in Fig 3.5.
 45

Figure 3.5:  Transition maps for the family Sxhhlb in the chart F.R.  on r  = 0

The transition maps 1l and Tr  have been explicitly given in (3.3.17) and (3.3.18).

Next,  we  study the transition map T  : 1f4  -----+  1f3 .  For sections 1f3  and  7f4,  we  can

write  them  in  the  original  coordinates  (x,  y)  with  1f3  =  {x  =  f3(f;3), fj  =  g3(f;3)},

(3.3.16).

System (3.3.12) is Hamiltonian with the first integral

46

By implicit function theorem, when y4  is  in a small neighborhood of y4  = 0, we have

(3.3.25)

Therefore, by (3 .3 .17), (3 .3 .18) and (3 .3 .25), we have

So T2 (0, fj4)  is an identity for v = 0, P,3  = 0 and ao  =  -~.
 D

End of proof for  Sxhhlb

Hence, for the displacement map L  =  R- 1  - T,  by (3.3.24), we have

From Lemma 3.3.2, we have c1(0)  =  1 for v  = 0,  P,30  = 0 and ao  =  -~. Since 1*  -=/=  1,

so there exist A 0 ,  a neighborhood of a0 ,  Vo,  a neighborhood of P,o,  and  v1  > 0,  such that

V(a, µ)  E  A0  x  V0  and \Iv  E  (0, v1 ),  we have  aL~~Y
4
)  -=/=  0 in a small neighborhood of

fj4  = 0.

By Rolle's Theorem, V(a, µ)  E  A 0  x  V0  and Vv  E  (0, v1 ), the map L 2 (v,  fj4 )  = 0 has

at most one zero in a small neighborhood of fj4 = 0,  i.e., Cycl(Sxhhlb)  :::; 1.

Altogether,  we  obtain  that  all  the  generic  convex  graphics  with  a  nilpotent  saddle

point of multiplicity 3 have finite cyclicity, thus completing the proof of Theorem 3 .1.1.

47

3.4  Finite  cyclicity of (Jf2)

Theorem  3.4.1.  The graphic (!{2 )  has finite cyclicity.

Proof  For (!{2 ),  it  is  an HH-type  graphic with  a nilpotent  saddle of multiplicity  3  at

infinity  and an invariant parabola as shown in Fig 3.1.

To  prove the finite  cyclicity  of (Jl2 ), we only need to check that the first return map

P along the invariant parabola satisfies  P'(O)  #- 1.  By  [15], the graphic (!{2 )  occurs in

the family
{ :
 (3.4.26)

rescaling we can assume that c:1  = 1.  Then (3.4.26) becomes

{
 i;  =  ,,\x - y + x 2 ,

iJ  = x + ,,\y + ,,\(3  - 82)x2 + 82xy,
 (3.4.27)

with  ~0 = (1  + ,,\2)82 - 4,,\2 > 0 and ,,\  #- 0.  System  (3.4.27) has an invariant parabola

82  2  1 (  2) y = (1  - - )x  - AX - - 1 + A  .
2  2  (3.4.28)

48

Along the invariant parabola (3.4.28), we have

P'(O)
 :f 1.

Therefore, we finish the proof.
 D

49

4  Finite  cyclicity of ( Ih)

For the graphic (!{3 ),  it  is  an HH-type graphic with  a nilpotent saddle at infinity.  Com-

pared to the graphic (Jf2 ),  there is  an additional attracting saddle-node on the  invariant

parabola for the graphic (If 3)  as shown in Fig. 4.1  .

Figure 4.1: The graphic (If3 ).

In this chapter, firstly  we  will  give  a main theorem  that the  graphic (Jf3 )  has finite

cyclicity  in  section  4.1,  and then  we  prove  the  main  theorem  by  showing  that all the

upper boundary graphics have finite  cyclicity  in section 4.2, and all the lower boundary

graphics and intermediate graphics have finite  cyclicity  in section 4.3.

50

4.1  Main  theorem

Theorem  4.1.1.  The graphic ( Ji3 )  has finite eye/icily inside quadratic systems.

Since  the graphics (Ji3 )  has a nilpotent singular point at infinity,  we  can limit  our-

selves  to  the  limit  periodic sets  which  have  an  invariant line  ("{11  = 0).  Moreover the

connection along this line is fixed.  Therefore, we  only need to look to the limit periodic

sets Sxhh 1,  Sxhh4-Sxhh8.

To  prove  the  finite  cyclicity  of graphic (Ji3 ),  we  have  to  prove  that all  the  upper

boundary  graphics, the  intermediate graphics and  lower  boundary graphics of Sxhh 1,

Sxhh4-Sxhh8  have finite  cyclicity.

We  begin with the upper boundary graphics.

4.2  The  upper  boundary  graphic

Proposition  4.2.1.  For the graphic (Ii3 ),  Cycl(Sxhhia)  ::; 1, i  = 1, 2, · · ·  , 10.

- -
Proof  As  shown  in  Fig.  4.2,  let  E 3  =  { X 3  =  1}  and E 4  =  { X 3  = -1}  be  the  two

sections  transversal to  the  graphics in  the  normal  form  coordinates (X3 , Y3 )  near the

saddle-node point.

We  consider the Poincare first return map P defined  on the section E 4 :

51

Figure 4.2:  Upper boundary graphics of saddle type

which can be calculated by the composition
 (4.2.1)

where

•  8i : Ti  -----+  Ei are the second type of Dulac maps in the neighborhood of Pi  ( i  =

3, 4).  The second type of Dulac maps 8i =  (~i, Si) (i  =  3, 4)  have the expression

52

•  U  : 74  --+  7 3  is a regular transition map which can be written as

{
 U1(r4, p4)  = r4(~(v) + O(lr4, p41)),

U2(r4,  p4)  =  p4(J(v) + O(lr4, p41)),  (4.2.3)

where j(O)  = 1 was calculated in Proposition 5.8 of [53] and ](O)  = j(o)- 1  = 1.

•  R1  :  E 3  --+  E 3  is a regular transition map which  can be written as
 (4.2.4)

where l0 (0)  =  0 and li(O)  > 0.

•  R  : E 3  --+  E 4  is a central transition map near the attracting saddle-node point in

the normal form  coordinates (X3 , Y3 ),  which can be written as
 (4.2.5)

where m(v)-+  0 as v-+ 0.

• R2  :  E 4  --+  E 4  is a regular transition map which can be written as
 (4.2.6)

where n 0 (0)  = 0 and n 1 (0)  >  0.
 53

Define
 (4.2.7)

fJ  = 83 o u o e4 1 .

For  its  first  component of fJ,  we  have  fJ1 (v,  y4 )  =  v.  For the  second  component

U2 (v,  y4 ), it has already been shown in  [53] that

afJ2~0, o)  =  i.
8y4

Define

For R(v,  y3 ), by (4.2.4), (4.2.5) and (4.2.6), we have

where
 n0 (v)  = n0 (v)  + O(m(v)l 0 (v)),

n1(v)  = li(v)n 1(v)  + O(m(v)l 0 (v)).

Therefore,

BR
2
(~, Y3)  = m(v)[li(v)n 1(v)  + O(m(v)lo(v))]  + O(y3).
8y3  .

54
 (4.2.8)

(4.2.9)

(4.2.10)

So there exist A 0 ,  a  neighborhood of a0  and  v1  > 0,  such that V( a,µ,  v)  E  A 0  x  § 2  x

(0, 1.11 ),  aR.~~,ya) is sufficiently small in a small neighborhood of y3  =  0.
Ya
 ~  ~
For the first return map P  defined by (4.2.1), by the definition Rand U,  we have

P(v,  y4)  =Ro U(v,  y4).

The first component of P satisfies Pi (v, y4 )  = v.  Let y3  = U2(v,  y4 ), then for the second

component P2(v, y4 ), we have

By (4.2.8) and (4.2.10), we have that V( a,µ,  v)  E  A0 x § 2 x (0, 1.11 ),  oP~(~,y
4
) is sufficiently
Y4

small in a small neighborhood of y4  = 0.  Hence, by Rolle's theorem, the first return map

P  has at most 1 fixed point in the neighborhood of (v, y4 )  =  (0, 0), i.e., Cycl(Sxhhia)  :::;

1,i= 1,2,··· ,10.
 D

Remark 4.2.2. In  the proof of Proposition 4.2.1,  we  only use  the fact a3 (a)  =  2(1  -

2a)  > 0,  so for the  elliptic  case  with  a  E  (0,  ~ ),  the  same proof gives that for  upper

boundary HR-graphic of elliptic type,  Cycl(Ehhia)  :::; 1, i =  1, 2, · · · , 12.

4.3  The intermediate and lower boundary graphics

Let r be any intermediate or lower boundary graphic.  To  study its cyclicity, as shown in

Fig.  4.3, take sections Ili =  {Pi  =  p0 }  in the normal form  coordinates (ri, Pi, fh)  in the

55

neighborhood of the singular point Pi (i=3, 4).  We  will study the displacement map

L:  Il3~Il4

L =  R-T- 1 ,

where R  : Il3  ~ Il4 is the transition map along the  regular orbit in the normal form

coordinates,  and  T  :  Il4  ~ Il3  is  the  transition  map  passing through  the  blown-up

singularity.  We  study the number of small roots  of L  =  0.  The maximum  number of

roots bounds the cyclicity.

We  begin with the transition map R.

Figure 4.3:  Transition maps for the RH-graphics of saddle type

56

Proposition  4.3.1.  For  any  k  E  N  and Va0  E  A  =  (-oo, ~), there  exist  A 0  C  A,

a  neighborhood of a0 and  v 1  >  0  such  that V(a, µ)  E  A0  x  § 2  and Vv  E  (0, v 1 ),

R(v, fh)  = (R1(v, fh), R2(v, ih)) is Ck  and Ri(v, fh)  = v,  R2(v, ih) takes the following

form

(1)  if ao  rt:  Q,

R2(v, ih)  =  ( no(v) + O(m)) ( ~ t"'

2) if ao  E  Q,

where
 +m(v) [ti(v)n1(v) + O(vln ~) + O(m)]Ya

k
+m(v) [L O(v(i-I)u3)y; + O(Y~+l)J;

i=2

v
'Yo(v, w(-, -!31), m(v))
Vo

k
+m(v) [L 'Yi(v,w(~, -{31),m(v))y; + O(y~+
1
)J,
i=l  0

'Yo=  (no(v) + O(m))( !!_ )-u
4  + K30(rg3w( !!_, -!31)), mvu3w2( !!_, -{31)),
Vo  Vo  Vo
v  - v  v
7 1  = li (v)n 1(v)  + O(m(v)) + O(v ln -) + O(vP3wq3(-, -{31 )  ln -),
Vo  Vo  Vo
 (4.3.11)

Proof  We  only consider the second case a0  E  Q.  The transition map R can be calculated

by the composition
 (4.3.12)

57

where

•  ~i :  IIi  ~ Ei  are the  first  type of Dulac maps  in  the  neighborhood of ~ ( i  =

3, 4). The first type of Dulac maps ~i = (di, Di)(i = 3, 4)  have the expressions

{
 di(v, Yi)  =  v,  (4.3.13)
Di(v,yi)  = 1/i(v,w(;
0 ,  -/31)) + C~}
7
i[Yi + 'l/Ji(v,yi,w(:a,  -/31))],

where /3  = p3  - ih(a)q3  and 'l/Ji(i  = 3, 4)  have the property (2.5.23).

•  The transition maps R1,  Rand R2  are given by ( 4.2.4), ( 4.2.5) and ( 4.2.6).

•  ~41  :  E 4  ~ II4  is the inverse of the first type of Dulac map in the neighborhood

of P4 •  It has the expression

{
 d-1(  ::::  )
4  v, Y4  =  v,

D4 1 (v,  y4)  =  Y4  + ~4(v, w( :a, -/31), fJ4),
 (4.3.14)

where fJ4 = (:a)-o- 4 (y4  - 7J4 (v,w(:a,  -/31))), and ~4 satisfies property (2.5.23).

Hence,  for  the  second component of transition  map  R,  by  (4.2.4),  (4.2.5),  (4.2.6),

(4.3.12), (4.3.13), (4.3.14), and Lemma 4.13 in [53], a straightforward calculation yields

the result.
 D

For each family of graphic Sxhhi ( i  =  1, 3, 4, 5, 6, 7, 8), we use Vi  c  § 2  to denote the

set ofµ  =  (P,1, P,2, P,3)  in  which the family  Sxhhi exists, and  use Via  to denote a  small

neighborhood of p,0 ,  where µ0  E  \,'i.
 58

4.3.1  Family  Sxhhl

Family Sxhh 1 has a lower boundary graphic Sxhh 1 c which  passes through a hyperbolic

saddle point as shown  in Fig 4.4.  Let  .\0  be the hyperbolicity  ratio at this saddle point

when  r  = 0  for µ = p,0  and a  = a0  E  A.  In the chart F.R.,  by translating the  saddle

point to the origin, a linear transformation and Ck  changes of coordinates, we can bring

the system  (2.4.14) in the neighborhood of the saddle point into a normal form.

Figure 4.4: Transition maps for the family  Sxhhl

Take  sections E 1  = {y = 1}  and E 2  = { x = 1}  in the normal form  coordinates near

the saddle point. Let D(v, x)  = (D1(v, x),  D2 (v, x))  : E 1  ~ E 2  be the Dulac map near

the saddle point.  There exist A0 ,  a neighborhood of a0 ,  Vio,  a neighborhood of P,0 ,  and

v1  >  0,  such that V(a, µ)  E  Ao  x  Vio  and Vv  E  (0, v1),  the  inverse of the Dulac map

59

D(v, x)  : 'E1  ~ 'E2  can be written as

which has the following  form

1
iJXM (1  + </>(iJ, v)),  iL\o  -=/=  1,

D}1(v, fj)  =  v,

D21(v,jj) =  {  a1(v)[iJw  + · · ·] + iJ  + odv)[iJ 2w + · · ·] + · · · ,  iL\ 0  = 1,

(4.3.15)

where  </>(iJ, v)  E  10 , -X(v)  and ai(v)  are functions  of (v,  jl, a),  a 1 (v)  =  1 - >-.(v)  and

w =  w(fj, a1 (v))  is the Leontovich-Andronova-Ecalle-Roussarie compensator defined  in

(2.2.4).

Let T1  :  Il3  ~ 'E2 and T2 : 'E1  ~ Il4.  They  are the compositions of normal form

coordinate changes and a regular transition map. T1 (v,  iJ3 )  can be written as
 (4.3.16)

and T2 (v,  x)  can be written as

{
 Tk1 (v,  x)  = v,

T22(v,  x)  =  bo(v)  +bi (v)x  + O(i2 ),
 (4.3.17)

60

where e0(0)  =  0,  b0 (0)  =  0,  e1 (0)  > 0 and b1 (0)  > 0.  Then for r- 1 : II3 ~ II4, we

have

We treat two cases Ao  f.  1 and Ao  = 1 separately.

4.3.1.1  Ao  f.  1

Firstly, we study the lower boundary graphic Sxhhlc. By (4.3.15), (4.3.16) and (4.3.17),

we have
 (4.3.18)

1
where ci(O)  =  O(i  =  1, 2),  h(O)  =  e1(0)>-ob1(0)  f.  0 and ¢0  E  I0 .  Therefore,  from

( 4.3.11) and ( 4.3.18), the displacement map L  has the following form

k
L2(v,  fh)  = 'Yo(v,  w( _!!___'  -/31), m(v))  + m(v)  [ ~ 'Yi(v,  w( ~' -/31), m(v))y;
vo  ~  M
i=l  0

Then
 v
=  m(v)['Y1(v,w(-,  -/31),m(v)) + O(Y3)]
Vo
-~i~~ (ch)+ Ya)xbi-1 [1 + ¢1 (Ya, v)],  (4.3.19)

where ¢1  E  I0 .
 61

•Ao> 1.

Since 7 1(v,  wC~, -{33), m(v))  is bounded and m(v)  --t  0 as v  --t  0,  so

v
lim  m(v)b1(v,w(-,  -{33),m(v)) + O(ih)] = 0.
(v,y3,jl,a)-+(O,O,µo,ao)  Vo

For (v,  fl, a)  in a small neighborhood of (0, flo, a0 ), we have  >Jv)  - 1 < 0, r(v) and h(v)

are all bounded and bounded from  zero.  Hence,

lim  - ~((v)) (c2(v)  + :i/3)~-l[l + 4>1(f)3,  v)]  = oo.
(v,jjJ,P,,a)-+(0,0,P,o,ao)  A  V

Hence,  there exist  A 0 ,  a neighborhood of a0 ,  V].0 ,  a neighborhood of flo,  and v1  >

0,  such  that V(a,  fl)  E  Ao  x  Vio  and Vv  E  (0, v1),  we  have  oL~(~,ii
3
)  -=/=  0  in  a  small
Y3

neighborhood of ih  = 0.

By  Rolle's Theorem,  V(a,  fl)  E  Ao  x  Vio  and Vv  E  (0, v1 ),  the map L2 (v,  f)J)  = 0

has at most one zero in a small neighborhood of ih  = 0,  i.e., Cycl(Sxhhlc)  :::; 1.

•Ao< 1.

By  ( 4.3.19), zeros of &L~(~,ii
3
) are the same zeros of
Y3

where ¢2  E  Igo.
 62

Differentiate L 2 (v,  ih)  with respect to fh,  and we have

where ¢3  E  J(I°.  Since  1
~~
0 > 0 and m(v)  ~ 0 as v  ~ 0,  so

Therefore,  there  exist  A0 ,  a  neighborhood  of a0 ,  Vio,  a  neighborhood  of p,0 ,  and

8L2(v,y3)  .
V1  > 0,  such that V(a, µ)  E  Ao  x  Vio  and Vv  E  (0, v1),  we have  a- =I- 0 for ih  m
Y3

a small neighborhood of y3  = 0.

By Rolle's theorem, V(a, P,)  E  A0  x  Vio  and Vv  E  (0, v1),  L2 (v, y3 )  = 0 has at most

two roots in a small neighborhood ofjh = 0,  i.e., Cycl(Sxhhlc):::;  2.

Now we study the  intermediate graphics Sxhhl b  for  Ao  =I- 1.  Note that for v  =  0,

a= a0  and p,  = p,0 ,  from  (4.3.18) we have

1
T2- 1 (0, y3)  = h(O)y-:0  [1  + o(l)].

1
Since  h(O)  =  e1 (0) -'obi (0)  =/:- 0  and  Ao  =I- 1,  so  for  V( a,µ)  E  Ao  x  Vio,  r2- 1 (0, y3 )

is  nonlinear.  By analytic extension principle  [11, 52, 53], r2- 1(0, j}J)  is  nonlinear  in  its

analytic extension domain.

From proposition 4.3.1, we know that any ith derivative of the second component of

transition  map R(v,  y3)  is  close to zero.  Suppose that r 2- 1 (0, y3)  has  its  nth  derivative

63

nonvanishing,  then  by  Rolle's  theorem,  V(a, µ)  E  A 0  x  Vio  and  v  >  0  sufficiently

small,  L2(v, fh)  =  0  has  at  most  n  roots  in  a  small  neighborhood  of ih  =  0  i.e.,

Cycl(Sxhhlb)  ::; n.

4.3.1.2  --\0  = 1

Performing a change of parametrization on II3 ,  the displacement map L will be defined

as
 (4.3.20)

where ((v) = f1-;/(v, 0)  with ((0)  = 0,  and f- 1 = f2  0  n-1
0  S1.  The maps n-1 and

T2  are given by (4.3.15) and (4.3.17), respectively. For Si, we have
 (4.3.21)

where ei (0)  = ei (0)  > 0.

By ( 4.3.15), ( 4.3.17) and ( 4.3.21 ),  for f- 1  we have

f 2- 1(v, Y3)  = bo(v)  + e~-cti(v)b1(v)a1(v)[f;w(Y3, a1) + · · ·]

ei (v)b1  (v)Y3  + e~-
01 (v)b1  (v)a2(v)[Y3
2w(f;, a1) + · .. ] + ....

(4.3.22)

64

Therefore, for the displacement map L(v, YJ), by (4.3.11), (4.3.20) and (4.3.22), we have

L2(v,  Y3)  = eo(v)  + c1(v)[YJw(Y3, a1) + ... ]  (4.3.23)

+c2(v)Y3 + c3(v)[Ylw(Y3, a1) + · · ·]  + · · · ,

where
 v
Co ( v)  = lo ( v,  w ( - , - f31), m ( v))  + 0 ( ( ( v))  - b0 ( v) ,
Vo
 v  -
c2(v)  =  m(v)T1(v,  w(-, -f31), m(v))  + O(((v)) - ei(v)b 1(v),
Vo

We will treat the following three cases separately depending on the parameters (a,µ).

•  a0 -:/=  -~and P,30  = 0.

Since p, 10  =  0, if p,30  =  0, then in the chart F.R. on the blown-up sphere r =  0, system

Xp=l  in (2.4.15) is symmetric with respect to the y-axis, so we have e1 (0)b1 (0)  = 1.

Differentiate L 2(v,  Y3)  with respect to Y3,  and we have

Let

c (  Y- )  ·- 8L2(v,  Y3)  w-1
(Y3, a1)  _  (  )  (  ) *1  + ·..  1
1:,l  V,  3  .- - - C1  V  + C2  V  - + · · · .
ay;  * 1 + · · ·  * 1 + · · · w(Y  a  ) 3  3,  1

65

The zeros of aL~;~Ya) are zeros of the function ~1 (v, Y3 )  in some neighborhood off3 = 0.

Differentiate 6 (v,  ¥3)  with respect to }3, and we have

Let

then we have

Since c2(0)  = -e1(0)b1(0)  = -1 =J  0, and the remainder is o(l), so there exist A 0 ,  a

neighborhood of a0, Vio, a neighborhood of P,0, and ZJ1  > 0,  such that V(a, µ)  E  A 0 x  Vio

and Vv  E  (0, v1), 6(v, Y3)  =J  0 in some neighborhood of }3  =  0.  By Rolle's Theorem,

V(a, µ)  E  A0  x  Vio  and Vv  E  (0, v1), the displacement map L(v, Y3 )  has at most 2 zeros

in some neighborhood of Y3  = 0,  i.e., Cycl(Sxhhlc)  ::;; 2.

For the  intermediate  graphics,  if P, 10  =  0  and  P,30  =  0,  because  of the  symmetry,

r 2- 1(0, y3)  is  an  identity.  From  proposition  4.3.1,  we  know that  any  ith  derivative  of

the second component of transition map R(v,  y3 )  with respect to y3  is close to zero.  By

Rolle's theorem, V(a, P,)  E  A0 x  Vio  and v  > 0 sufficiently small,  L(v, y3) has at most

one root in a small neighborhood ofy 3  = 0, i.e., Cycl(Sxhhlb)::;;  1.

•  ao  =J  -~and P,30  =J  0.
 66

For a0  f  -~ and p,30  f  0,  it has been calculated in [53] that the first saddle quantity

Differentiate L 2 (v, Y3 )  with respect to Y3 ,  and we have

Let

t  (  ,/-)  ·- 8L2(v, Y3)  w- 1(Y3,  a1)  =  (  )  (  ) *1 + · · ·  1  ...
~1 V,  I  3  .- - C1  1/  + C2  1/  - +  .
8Y  * 1 + · · ·  * 1 + · · · w(Y  a  ) 3  3,  1

The zeros of oL~~~Y
3
) are zeros of the function 6 (v,  Y3 )  in some neighborhood off; = 0.

Differentiate 6(v, Y3 )  with respect to Y3 ,  and we have

Let

then we have

Since  c2 (0)  =  -e1 (O)b1 (0)  f  0  and  the  remainder  is  o(l),  so  there  exist  A 0 ,  a

neighborhood of a0 ,  Vio, a neighborhood of µ0 ,  and v1  >  0,  such that V(a, µ)  E  A 0  x  Vio

and Vv  E  (0, v1), 6(v, Y3 )  f  0 in some neighborhood of Y3  = 0.

67

By  Rolle's  Theorem, \:/(a,µ)  E  A0  x  Via  and \:Iv  E  (0, v1 )  the  displacement map

L(v, YJ) has at most 2 zeros in some neighborhood of Y3  =  0,  i.e., Cycl(Sxhhlc)  :::; 2.

2- 1  -
For the intermediate graphics, since a 2  f  0,  from  (4.3.22), we have  8  T~i~'Y
3
) f  0.
3

Hence, f 2- 1(0, Y3 )  is nonlinear.  By analytic extension principle [11, 52, 53], f 2- 1(0, Y3 )

is nonlinear in its analytic extension domain.

From proposition 4.3.1, we know that any ith derivative of the second component of

transition map R(v,  Y3  + ((v)) with respect to Y3  is  close to zero.  lff2- 1(0, Y3 )  has  its

nth  derivative  nonvanishing,  then  by  Rolle's theorem,  V( a,µ)  E  A0 x  Via  and  v  > 0

sufficiently small,  L(v, Y3 )  has at most n  roots  in  a small neighborhood of Y3  =  0,  i.e.,

Cycl(Sxhhlb)  :::; n.

•  ao  =  -~.

Since  Ao  =  1,  so the divergence of X p=l  vanishes,  i.e.,  (1  + 2a0 )x 0  + P,30  =  0.  If

a0  =  -k,  then  P,30  =  0.  Note that P,10  =  0,  so  again  system  X p=l  is  symmetric with

respect to the y-axis.  Exactly as we did for the case a0  f  -k  and "fl30  =  0,  we can prove

that Cycl(Sxhhlb)  :::; 1 and Cycl(Sxhhlc)  :::; 2.

4.3.2  Families Sxhh4 and Sxhh6

The family Sxhh4 exists if and only if

Vi={µ  E § 2IP,1  =  o,µ3  > O,P,2  > ap,n,

68

and the family Sxhh6 exists if and only if

Figure 4.5:  Transition maps for the family Sxhh4

For families  Sxhh4 and Sxhh6, the lower boundary graphic has a saddle connection

8 18 2  as shown Fig.  4.5. At 8 1  and 8 2 ,  the hyperbolicity ratios are

We first consider the lower boundary graphics.

In  the  chart  F.R.,  in  the  neighborhood  of 8 1,  take  sections  E 1  =  {y1  =  1}  and

i31  = { i 1  = 1} in the normal form coordinates. In the neighborhood of 8 2,  take sections

69

E 2  = { x2  = 1} and E2  = {112  = 1}  in the normal form  coordinates.

The transition map r- 1  :  II3  ~ II4  can be calculated by the composition

where

• T1  :  II3  ~ ~2 is a composition of normal form coordinate changes and a regular

transition map, which can be written as
 (4.3.24)

where e0 (0)  = 0 and e1 (0)  >  0.

•  fJ- 1  :  E 2  ~ E2  is  the  Dulac  map  in  the  neighborhood  of 8 2 ,  which  has  the

expression
 (4.3.25)

where¢ E  / 0 .

• T3  :  E2  ~ E1  is  the  composition  of normal  form  coordinates  changes  and  a

transition map.  Since x axis is fixed  for X p=l, so T3  can be written as
 (4.3.26)

70

where k1 (0)  > 0.

•  D- 1  :  ~1 ~ ~1 is  the  Dulac  map  in  the  neighborhood  of Si,  which  has  the

expression
 (4.3.27)

where¢ E  10 .

•  T2  :  ~1 ~ Il4  is a composition of normal form  coordinate changes and a regular

transition map, which can be written as

{
 T21(v, x)  = v,

T22(v, x)  = bo(v)  + b1 (v)x  + O(x 2),
 (4.3.28)

where b0 (0)  =  0, and b1 (0)  > 0.

Then by (4.3.24), (4.3.25), (4.3.26), (4.3.27) and (4.3.28), for the transition map r- 1,  we

have
 (4.3.29)

71

1.  If P,0  E  l/4,  then  .X1 (O).X2(0)  <  1.  Exactly as  we  did  for the case  .X0 (P,0 )  < 1 of

graphic Sxhhl, we have Cycl(Sxhh4b)  ~ n and Cycl(Sxhh4c)  ~ 2.

2.  If P,0  E l/6, we have .X1 (0).X2(0)  >  1.  Exactly as  we did for the case .X0 (p,0 )  >  1 of

graphic Sxhhl, we have Cycl(Sxhh6b)  ~ n  and Cycl(Sxhh6c)  ~ 1.

4.3.3  Family Sxhh5

The family  Sxhh5  exists if and only if P,0  =  (0, 1, 0).  Then system X  p=l  is  symmetric

with respect to y-axis as shown in Fig 4.6.

4.3.3.1  Sxhh5b

For  the  intermediate  graphics,  the  transition  map  T2- 1(0, y3 )  is  an  identity  for  p,0  =

(0, 1, 0).  Since the derivative of the second component of transition map  R(v,  y3 )  with

respect to y3  is close to zero, so by Rolle's theorem, we have Cycl(Sxhh5b)  ~ 1.

4.3.3.2  Sxhh5c

Now we  consider the  graphic  Sxhh5c.  The  hyperbolicity ratio  .X1  and  .X2 satisfy  .X1  =

- 2
~, .X2  = -2a and .X1.X2 =  1.

In  the  chart  F.R.,  in  the  neighborhood  of Si,  take  sections  E 1  =  {y1  =  1}  and

i51  = { x1  = 1} in the normal form coordinates. In the neighborhood of 8 2 ,  take sections

72

Figure 4.6:  Transition maps for the family Sxhh5

~
2 = { x2  = 1} and }32  = {y2  = 1}  in the normal form coordinates.

The transition map r- 1  :  113  ---+ 114  can be calculated by the composition

.......  .......  .......  --1  .......
where the transition maps T 1,  n-1,  T 3 ,  D  and T 2  have the same definitions  and ex-

pressions as those in Family Sxhh4.

Performing a change of parametrization on 113 ,  the displacement map  L  will be de-

fined as

where ((v) = T
12
1 (v, 0)  with ((0) = 0,  and f- 1  = T2  o D- 1  o T3  o fJ- 1  o S1 .

73
 (4.3.30)

For Si, we have
 (4.3.31)

where e1 (0)  = e1 (0)  > 0.

By (4.3.25), (4.3.26), (4.3.27), (4.3.28), (4.3.30) and (4.3.31), for f- 1  we.have

(4.3.32)

- 1  1
where h(O)  =  e1 (0) >-1(o)>-2(o)  k1 (0) >-1(o)  b1 (0)  f.  0 and 'l/Jo  E  10 .

As  --\1(0)--\2 (0)  =  1,  if we let  >-.i(v)\.2 (v)  =  1 - &(v), then &(O)  =  0.  We  introduce a

compensator w  defined as  follows.

{
 Y3-&(v)  - 1

w(Y3,  v)  =  &(v)
-In Y3 ,
 if &(v) f.  0,

if&(v)  =  0.

This yields

1
f;>- 1>-2  =  Y;
1-& =  [1 + &(v)w(Y3,  v)]Y3.

By (4.3.32) and (4.3.33), f- 1  has the form

f 2- 1(v, Y3)  = bo(v)  + &h(v)Y3w(Y3,  v)[l + 'l/Jo(Y3,  v)]

+h(v)Y3[l + 'l/Jo(f3, v)].

74
 (4.3.33)

(4.3.34)

For R(v,  Y3 + ((v)), by (4.3.11), we have
 (4.3.35)
{
 R(v,  Y3 + ((v)) = v,

R(v,  Y3 + ((v)) ='Yo+ O(m(v)) + m(v)[('Y1(v) + O(())YJ + O(Yl)].

By (4.3.30), (4.3.32) and (4.3.35), we have

L2(v,  Y3)  ='Yo+ O(m(v)) - bo(v)  - &(v)h(v)Y3w(Y3,  v)[l + 'l/lo(Y3, v)]

- - (  )  -
-h(v)Y3[1 - r;:(:) ('Y1 (v) + 0(()) + Wo(Y3, v)],

where '110  E  Igo.

Differentiating L2 (v,  YJ)  with respect to Y;, we have

-&(v)h(v)[*w(Y3, v)  + 'l/71 (Y3, v)]

- m(v)  -
-h(v)[I - h(v)  ('Y1(v) + 0(()) + \J!1(Y3, v)],

where 'l/71, \Jf 1 E  Igo.  Let

where  '112  E  Igo.  The  zeros  of  aL~;/;,.
3
)  are  zeros  of the  function  6(v, Y3)  in  some

neighborhood ofY3 = 0.  Differentiate 6(v, Y3) with respect to Y3, and we have

75

where  '113  E 1r. Let

then  the  roots  of 6(v, Y3 )  are  the  same  roots  of ae~'i{
3
)  in  a  small  neighborhood  of

Y3  =  0,  and we have

when (Y3 , v, P,, a)~ (0, 0, P,o, ao).

Hence, there exist A 0 ,  a neighborhood of a0 ,  Vso,  a neighborhood of P,0 ,  and v1  > 0,

such that V(a, fl)  E  A0  x  Vso  and Vv  E  (0, v1 ), 6(v, Y3 )  =f  0 in a small neighborhood of

Y3  =  0.  By Rolle's Theorem, V(a, fl)  E  A0  x  V50 and Vv  E  (0, v1 ), the map L(v, Y3 )  has

at most 2 zeros in a small neighborhood off; =  0,  i.e., Cycl(8xhh5c)  :::;  2.

4.3.4  Family Sxhh7

For the  graphics  Sxhh7,  as  shown  in  Fig.  4.7,  there  is  a  repelling  saddle-node  8 1  and

a saddle point 8 2  on the lower boundary graphic Sxhh7c.  Graphics Sxhh7 exists if and

only if

The hyperbolicity ratio of the saddle 8 2  is .X2  = -a :::;  ~.

76

Figure 4.7:  Transition maps for the family Sxhh7

4.3.4.1  Sxhh7c

We first consider the lower boundary graphic Sxhh7c.

In the chart F.R.,  in  the neighborhood of the saddle-node point, take  sections E 1  =

{y1  =  1}  and ~1 = { x1  =  1}  in the normal form coordinates (xi, y1).  In the neighbor-

hood of saddle point S2, take sections E2 = { i2 = 1} and E2 = {Y2  = 1}  in the normal

form coordinates (x 2 , y2).  We study the displacement map
 (4.3.36)
L=W-W.  --For the transition map W,  we calculate it by making the following decomposition

77

where

• T1  :  ~2 ~ Il3 ,  which  is  the compositions of normal  form  coordinate changes

and a regular transition map.  It can be written as
 (4.3.37)

where e0 (0)  = 0 and e1 (0)  > 0.

•  R  : Il3  ~ Il4  is a transition map, which is given in Proposition 4.3.1.

• T2  :  Il4  ~ ~1 is  the  composition  of normal  form  coordinates  changes  and  a

regular transition map, which is given as follows
 (4.3.38)

where b0 (0)  = 0 and b1 (0)  > 0.
 ..-
Then by  straightforward calculation from  (4.3.11),  (4.3.37) and (4.3.38),  for W,  we

have
 (4.3.39)

78

where

(o(v)  =  bo(v)  + O(!o(v))  + O(m(v)),

(1(v)  = ei(v)b1(vh1(v) + O(eo(v))  + O(!o(v))  + O(m(v)),

For the transition map W,  we calculate it by making the following decomposition

- ,,....__  -1
W=~oT3 oD,

where

•  n- 1  :  E 2  -----+  E 2  is  the  Dulac  map  in  the  neighborhood  of S2 ,  which  has  the

expression
 (4.3.40)

where ¢0  E  10 .

• T3  :  E2  -----+  E1  is  the  composition of normal  form  coordinates  changes  and  a

regular transition map.  Since x axis is fixed for X p=b  so T3  can be written as

(4.3.41)

where k 1 (0)  > 0.
 79

........
•  ~ :  E 1  ~ E 1  is  the  stable-centre transition map  in  the  neighborhood of the

saddle-node 8 1.  Obviously,  the  first  component  ~ 1(v, y1)  = v.  For the  second

component  ~2(v, :Y1),  the  graph x1  =  ~2(v, y1)  is  a  solution  of the  following

differential equation
 (4.3.42)

where F(Y 1 , v,  jl, a)  = O(v)  + w(v)yi + O(Yf) and w(v)  = -2~ R, + O(v).

Hence, by (4.3.40), (4.3.41) and (4.3.42), the transition map W  has the following  form

{
 W1(v,  Y2)  = v,  (4.3.43)
W 2(v, Y2)  = ~2(v, Y1),

where
 1
YI  = ki(v)y; 2 <v)  [1 + ¢1(Y2,  v)]

Now  we study the displacement map L  =  W  - W.  Obviously,  we  see L 1 (v,  x2 )  =

0.  By  (4.3.36),  (4.3.39)  and (4.3.43),  the  equation L 2 (v, x2 )  =  0  is  equivalent to  the

(4.3.44)

Since  ~ 2(v, y1)  is a connected graph, the Khovanskii  procedure [32] shows that the

number of solutions of (4.3.44) is at most 1 plus the number of solutions of the following

80

system

This above system is equivalent to

-1  )
F(f)I,v,p,,a)  = O.
 (4.3.45)

Eliminating x1  from the equations ( 4.3.45), we have an equivalent equation
 (4.3.46)

Differentiating (4.3.46) with respect to x2 ,  we have

8L2  =  (i - oF(yi,v,p,,a))  8W2(v,y2)  _  F(- _  )o
2
W2(v,y2)
~- ~- ~- Yi, v, µ,a  ~-2
~  ~  ~  ~

=  m(v)  [ ( 1 - 2w(v)k~(v) A
2
~v) 11;',-\1 + ¢2(112, v))) ( (1 (v)  + O(Y2))

- ( O(v)  + w(v )k~(v)11i'~") (1 + ¢3(112, v))) ( 2(2(v) + O(Y2))]

= m(v)  [ (1 (v)  - O(v)(2(v) + O(y2) J,

which has the same number of small roots as of

Since  ( 1(0)  =  el(O)b1(0)li(O)n1(0)  -=/:- 0 and  (2(v)  is  bounded  for  (v,  P,,  a)  in  a

small neighborhood of (0, p,0 , a0 ).  Therefore, there exist A0 ,  a neighborhood of a0 ,  Via,

81

a  neighborhood  of P,0 ,  and  v1  >  0,  such  that V( a,µ)  E  A 0  x  Vio  and Vv  E  (0, v1),

L2 (v,  ih)-/:- 0 in a small neighborhood of ih  = 0.

Therefore,  by  Rolle's  theorem,  V(a, µ)  E  A0  x  Vio  and  Vv  E  (0, v1),  equation

L 2 (v,  fh)  = 0 has at most 2 small zeroes,  i.e., Cycl(Sxhh7c)  ~ 2.

4.3.4.2  Sxhh7b

We  study the transition map r- 1  :  II3  ----+  II4 .  In the chart F.  R.  on r  =  0,  II3  and II4

are two line sections parameterized by Yi(i  =  3, 4), respectively.  The second component

T2- 1(0, fJ3)  maps (0, +oo) to  (0, +oo ).

1fT2- 1 (0, y3 )  is in the neighborhood of the graphic Sxhh7c, since the Dulac map n- 1

is attracting and the map~ has flatness property, then we have limy3 ___.0  °~g~

1 (0, y3 )  =  0.

If T2- 1 (0, fJ3 )  is  in  the  neighborhood  of the  graphic  Sxhh'Zfl,  then  by  (4.2.3),  we  have

limy3 --->+oo  a-;3~

1
(0, fJ3 )  =  1.  so T2- 1 (0, fJ3 )  has to be nonlinear.  Therefore,  it is nonlinear

for f)3  E  JR+.

From proposition 4.3.1, we know that any ith derivative of the second component of

transition map R(v,  f)3) is close to zero.  IfT2- 1 (0, fJ3) has its nth derivative nonvanishing,

then by Rolle's theorem, V(a, µ)  E  Ao  x  Vio  and  v  > 0 sufficiently small,  L(v, y3 )  has

at most n roots in a small neighborhood of f)3  = 0,  i.e., we have Cycl(Sxhh7b)  ~ n.

82

4.3.5  Family  Sxhh8

As  shown  in Fig.  4.8, there is a saddle point 8 1  and an attracting saddle node 82  on the

lower boundary graphic Sxhh8c.  In this case

The hyperbolicity ratio at 8 1  is  -A1  = -~ 2::  2.

Figure 4.8: Transition maps for the family  Sxhh8

4.3.5.1  Sxhh8c

We  first  consider the  lower boundary graphic Sxhh8c.  In the  chart F.R.,  in  the  neigh-

borhood of 8 1,  take  sections  E 1  = {Y1  = 1}  and El  =  { x1  = 1}  in  the normal form

83

coordinates. In the neighborhood of saddle-node point, take sections E 2  = {ih = 1} and

}32  = { x2  = -1} in the normal form  coordinates.  We  study the first return map

For the Poincare return map P,  we calculate it by making the following decomposi-

ti on
 .......  .......  .......
P  = ~ o T3  o  Do T2  o Ro T1 ,

where

•  T1  :  E 2  ~ ll3,  which  is  the  compositions of normal  form  coordinate changes

and a regular transition map.  It can be written as
 (4.3.47)

where e0 (0)  = 0 and e1 (0)  > 0.

•  R: ll3  ~ ll4  is a transition map, which is given by Proposition 4.3.1.

• T2  :  ll 4  ~ E 1  is  the  composition  of normal  form  coordinate  changes  and  a

regular transition map, which is given as  follows
 (4.3.48)

where b0 (0)  = 0 and b1 (0)  > 0.
 84

•  D  :  E 1  ~ E1  is the Dulac map near the attracting saddle 8 1 ,  which  is given as

follows
 (4.3.49)

where J E  IQ°.

• T3  :  E1  ~ E2  is  the  composition  of normal  form  coordinates changes and  a

regular transition map.  Since x axis is fixed  for X p=b  so T3  can be written as

(4.3.50)

where k 1 (0)  >  0.

•  ~ : E2  ~ E 2  is the stable-centre transition map near saddle-node point 8 2 •  Ob-

viously,  the first component ~ 1 (v,  y2 )  = v.  For the second component ~2(v, y2 ),

Vp, q  EN, we have the flatness property:
 (4.3.51)

Then by (4.3.11), (4.3.47), (4.3.48), (4.3.49) and (4.3.50), for the return map P,  we have

(4.3.52)

85

8b.2(v, ih)  aT32(v, ih)  8D2(v, i1)  aT22(v, fi4)
8fi2  8fi1  8i1  8y4
8R2(v, y3)  &f12(v, i2)
x  .
8y3  8i2  (4.3.53)

From proposition 4.3.1, we know that any ith derivative of the second component of

transition map R(v, y3) is close to zero for v > 0 sufficiently small and (v, µ)sufficiently

near (a,µ)  =  (a0 , p,0 ).  Dis the Dulac map near an attracting saddle, and b.  is the stable-

centre transition map with flatness property (4.3.51).

Therefore, for any 0 < c «  1, there exist A0 ,  a neighborhood of a0 ,  l/80 ,  a neighbor-

hood of P,0 ,  v1  > 0,  neighborhoods U0 (xi)  of xi= O(i  = 1, 2) and neighborhoods U0 (yi)

of yi  =  O(i  =  1, 2, 3, 4), such that if (a,µ)  E  Ao  x  Vso  and v  E  (0, v1), and x2  E  U0 (x 2 ),

then we have i1  E  Uo(i1),  Yi  E  Uo(Yi)(i  = 1, 2, 3, 4) and
 (4.3.54)

Also, if (a,µ)  E  A0  x V80  and v  E  (0, v1 ), U0 (xi)  and U0 (yi)  are sufficiently small, there

exist a M  > 0 such that

0 < I af3~~· ih) I· I af2~~ j/4) I· I af1~~: X2) I < M.  (4.3.55)

I
8P2(v, i2) I
Hence, by (4.3.53), (4.3.54) and (4.3.55), we have  ax
2  «  1.  Therefore,  by

Rolle's theorem, V(a, µ)  E  Ao  x  Vso  and Vv  E  (0, v1), the first return map P has at most

1 fixed point in a small neighborhood of x2  = 0,  i.e., Cycl(Sxhh8c)  ~ 1.

86

4.3.5.2  Sxhh8b

We  study  the transition map T  : II4  ~ II3 •  In the  chart F.  R.  on r  =  0,  II3  and II4

are two  line sections parameterized by Yi(i  = 3, 4), respectively.  The second component

T 2 (0, y4 )  maps (0, +oo) to (0, +oo ).

If T2 (0, y4 )  is  in the neighborhood of the graphic Sxhh8c,  since the Dulac map D  is

attracting and the map~ is flat,  then we  have limg 4-o ~~ (0, y4)  = 0.  If n(o, y4) is in

the neighborhood of the graphic Sxhh8a,  by  (4.2.3),  we have limg 4 -+oo ~~~ (0, y4 )  = 1.

Since  T2 (0, y4 )  is analytic, there exists a constant M 0  > 0,  such that l~(O, y4)1  < M 0

for y4  E  (0, oo ).

Define the Poincare return map

p:  Il3  ~ Il3

(v, y3)  ~ (v, P2(v, y3))  (4.3.56)

P=ToR.

For the first  component P 1,  we have P 1 (v,  y3 )  = v.  For the second component P 2 ,

we have P2(v, y3)  = T2  o  R2(v, y3).

Since the derivative ofT 2 (0, y4 )  is bounded for fj4  E  (0, oo ), and any ith derivative of

R2(v, y3 )  is close to zero, so V(a, P,)  E  A0  x  V80 and v > 0 sufficiently  small,  ~~: (v, y3 )

is sufficiently  small in a small neighborhood of y3 = 0.  Therefore, the first return map P

has at most  1 fixed  point, i.e., Cycl(Sxhh8b)  ~ 1.

87

Altogether, we finish the proof of Theorem 4.1.1.

88

5  Finite  cyclicity of (!Jb)

For the graphic (!Jb),  it is an HH-type graphic with a nilpotent elliptic point of multiplic-

ity  3 at infinity  and an invariant parabola as shown  in Fig 5 .1, and this nilpotent elliptic

point could be of codimension 3 or 4.

Figure 5.1:  The graphic (I§b).

In this chapter, firstly  we  identify  the codimension of the nilpotent singularity point

of the graphic (!Jb)  in section 5.1. If the nilpotent elliptic point is of codimension 3, then

we  only  need to verify  the generic condition of Theorem  2.1.2.  If the nilpotent elliptic

point is  of codimension 4,  by calculation of the second derivative of the transition map

89

along the invariant parabola we prove that the graphic ( !Jb)  has finite cyclicity in section

5.2 and section 5.3.

5.1  Lemmas

Lemma  5.1.1.  The graphic ( !Jb)  occurs in the family

{
 i:  =  .Ax - y + x2  := P( x, y),

iJ  =  x + .Ay + c5ix
2  + 02XY  := Q(x,  y),
 (5.1.1)

where ,\ f  0,  1 < 82 < 2,  81  = .A(3 - 82) > 0 and 4,\2 - (1 + ,\2)82 < 0.

1.  If 82  f  ~' the nilpotent elliptic point is of codimension 3.

2.  If 82  = ~,the nilpotent elliptic point is of codimension 4,  type 2.

Proof  For the family (5.1.1), the triple nilpotent singular point is at infinity, so we intro-

duce the coordinates ( v, z)  =  ( ~, ~). Then we have

{ v  = -z + (1  - 82)v2 - .A(3 - 82)v3  - v 2 z,

z  =  -82vz - .Az2 - .A(3 - 82)v2 z  - vz2.

By a near-identity transformation
{:
 90
 (5.1.2)

and change of coordinates v1  ---+  -v 1  and z1  ---+  z1 ,  we have

{  ~I

Z1
 = Z1,

Let

we rescale the system (5.1.3) into

{  ~

2 = z
 2
 , 3  (3J2-2)  A(9J2-l6)  2  O(I  l4)
Z2  - -V2  +  y'l82(82-l)I V2Z2  - 182(82-l)I V2Z2  +  V2, Z2  .

By a near-identity transformation

{
 v  =  v  (I + .x(so~-
1182+4) v  + O(v2 )) 2  3  5y'l82(82-l)l 3  3  3  '

Z2  =  Z3,

and rescaling the time, we bring system (5.1.5) into a "standard form"

where
 b  Jl82(82 - 1)1  '
2A(282 - 3)(82  - 4)
5 I 82 ( 82  - 1) 1
2
 (5.1.3)

(5.1.4)

(5.1.5)

(5.1.6)

(5.1.7)

So for A =I= 0 and 82  E  (1, 2),  if 82  =I=  ~,the nilpotent elliptic point is of codimension

3; if 82  =  ~, the nilpotent elliptic point is of codimension 4, type 2.  D

91

Lemma  5.1.2.  Inside  quadratic systems,  the  graphics  (!Jb)  have finite  cyclicity if the

nilpotent singular point is of codimension 3.

Proof  If the nilpotent singular point is of codimension 3 [i.e., 82  E (1,  2) and 82  -:f  ~ in

family (5.1.1)], to prove that the graphic (!Jb)  has finite cyclicity, by Theorem 2.1.2, we

only need to check that for the first return map P along the invariant parabola, it satisfies

P'(O)  -:f  1.

The equation of the invariant parabola is given as follows.

(  82)  2  1 (  2) y=  1-- x  -,,\x-- l+,,\  .
2  2  (5.1.8)

Along the graphic (the invariant parabola), we have

P'(O)  =exp (  f
 00  div X(r(t))I  dt)
}  _ 00  (5.1.1 ),(5.1.8)

1
.  (jxo  4,,\  + 2(2 + '52)x  ) =  im  exp  dx
xo---+oo  -xo  82x2 + 4,,\x + 1 + ,,\2
1.  [( 82x6 + 4-Xxo  + 1 + ,,\
2  )  Wf  (  16,,\  82xo + 2,,\) lxo  ] =  im  2  exp  arctan ----
xo---+oo  t52x0  - 4-Xxo + 1 + ,,\2  <52~  ~  -xo

(  16.X7r  )
=exp  82~

t- 1.

where ~o =  (1  + .X2)82 - 4,,\2 > 0 and ,,\ -/=  0.

So, the graphics ( !Jb)  have finite cyclicity if the nilpotent point has codimension 3.

0

92

5.2  Main theorem

Theorem 5.2.1.  The graphics (!Jb)  have.finite cyclicity inside quadratic systems.

By Lemma 5 .1.2, we only need to prove that ( !Jb)  have finite cyclicity when the nilpo-

tent singular point is of codimension 4 [i.e., 82  =  ~ in family ( 5 .1.1) ], which corresponds

to a0  =  ~ in (2.4.15).

If the  nilpotent  singular point  is  of codimension 4,  the  finite  cyclicity  of the  limit

periodic sets Ehh 1 a, Ehh2-Ehh 12 is the direct consequence of Theorem 2.1.2 and the fact

P' ( 0)  =I 0 in Lemma 5 .1.2, except the case Ehh 1 b and Ehh 1 c,  for which the hypothesis

a0  #- ~ is used.

Therefore,  we  only  need  to  prove  that  the  intermediate  graphic  Ehh 1 b  and  lower

boundary graphic Ehhlc have finite cyclicity when a0  =  ~ [i.e., 82  =  ~in family (5.1.1)].

5.3  Proof of the main theorem

We  begin  with  the  lower  boundary  graphic  Ehh 1 c.  We  study  the  displacement  maps

defined on the sections T1  and T2  with images on the sections II1 and ~4 as shown in Fig.

5.2.

The procedure of the proof is the same as the proof for the case Ehh 1 c of codimension

3, which consists of several steps, so we recall the common steps (1}--(IV) as follows.

(I) Parameterization of sections T1  and T2

93

Figure 5.2:  Transition maps for the graphic Ehhlc of (IJb)

On Ti,  the coordinates are  (ri, p1)  with r 1p1  = .v  for  v  > 0 small.  Now.we want to

cover the domain hi < c,  IPil < c for c  > 0 small. Then v  ~ c2 .  So Vu  E  (0, 1), on the

curve v  = uc 2,  we have r 1p1  = uc 2 •  Hence ri, P1  E  ( uc, c). Let

then  we  parameterize  the  section  T1  with  the  coordinates  (v,  c)  E  (0, c2 )  x  Iv  where

I  = ( lnE  lnue:)  C  (0  1).
v  In v '  ln v  '

Similarly, on the section T2 ,  we have
 d
P2  = v'

and we use coordinates (v,  d)  E  (0, c2 )  x  Iv  to parameterize the section T2 •

94

For graphic Ehhl, we use V 1  c  § 2  to denote the set ofµ=  (P,1 , P,2 , P,3 )  in which the

family Ehh 1 exists, and use V 10  to denote a small neighborhood of P,0 ,  where P,0  E  V 1•

We  use Ao to denote a small neighborhood of a0 ,  where a0  E  (0,  ~).

We will study the number of roots of the following system
 (5.3.9)

for  (a,µ)  E  A0  x  V 10  with  ( c, d)  E  Iv  x  Iv  and v,  c  sufficiently small.  The transition

maps 7i(i =  1, 2, 3, 4) will be developed in the next step.

(II) Transition  maps 1i  (i  = 1, 2, 3, 4)

(11-1) The transition  map T1

The map T1  :  T 1  ----t  I11  is the second type ofDulac map near P 1 .  For r 1  =  v1-c and

p1  =  vc,  it has the following expression
 (5.3.10)

(}1 (v, ve, w( vc, -ai) is Ck  and satisfies the following properties:
PO

8iB_1(v  Ve  w(vc  -a)= 0  (vpicw(vc  -a )(lnv)i)  i  >_  1.
8ci  '  '  PO  '  l  PO  '  l  '

(11-2) The transition  map T 2
 95

The transition map T2  :  T2  ~ Il 1  can be factorized as

where

•  8 2  :  T2  ~ I12  is the second type of Dulac map in the neighborhood of P2 •  For

r2 = v1-d and p2 = vd,  it has the following expression

is Ck  and satisfies the same properties as of 81  in ( 5 .3 .11 ).

• s- 1  :  I12  ~ I11  is a regular transition map, which can be written as

where k0 (0)  = 0,  k1 (0)  = e - v':~!~o, and k2(0)  = *P,30  by Proposition 6.1  in [53].

Therefore, for T2 ,  we have

T21 (v,  d)  = v,

T22(v, d)  =  m20(v, w(~:, a1)) +  vuid [m21(v, w(~:, a1)+  (5.3.12)

k  d  d
~  v  (i-l)u1d  d  v  J
~m2i(v,w(-,a1)v  +B21(v,v  ,w(-,-a1)),
i= 2  Po  Po

96

where

and ()21  is Ck  and has the same properties as of B1 in ( 5 .3 .11 ).

(11-3) The  transition  map  T 3

The transition map T 3  :  7 2  ~ 1:4  can be factorized as

where

•  V  : 7 2  ~ 7 3  is a regular transition map, which can be written as

r3  = Vi(vl-d, vd)

= vI-d [ m141 (v)  + m142(v)v1-d + m143(v)vd  + O(v 2(I-d), v 2d) J,

p3  = Vi(vI-d, vd)

= Ve [ m141 (v)  + m142(v)v1-d + m143(v)vd  + O(v 2(I-d)' v 2d)]'

(5.3.13)

and m143 (0)  =  *fL30 •  The symbol* denotes any continuous function of (v,  µ,a),

which is nonzero at (v,  µ,a)  =  (0, P,0 , a0 ).

•  8 3  :  7 3  ~ II3  is the second type of Dulac map  in the neighborhood of P3  with

97

•  The regular transition map R  : E 3  ---t  E 4  is Ck,  which can be written as

N(k)
R2(v,  ih)  = mo(v)  + L mj(v)ih + O(y:(k)+l),
j=l

where m0 (0)  = 0, m1 (0)  > 0.

Therefore, for T 3 ,  we have

where
 T31 (v,  d)  = v,

T32(v, d)  = m3o(v,  w(r3,  ,81))  +  vo-3(l-d) [ m 31 (v,  w(m;
0
41 v1-d,  ,81))

+m32(v)v1-d +  m33(v)vd  +  O(v2Cl-d), v2d)

N(k)
+  L  mj(v)va-3(1-d)j  +  O(va-3(1-d)(N(k)+l))

j=l

+8  (v  vl-d  w( m141 vl-d  -,B  ))] 31  ,  ,  ro  ,  1  '
 m31 (0)  -=/=  0,

and 831  is Ck  and has the same properties as of 81 in ( 5 .3 .11 ).

98
 (5.3.14)

(5.3.15)

(11-4) The  transition  map  T4

The transition map T4  :  7 1  ~ :E4  can be factorized as

T4  = 8 4 0  U,

where

•  U : 7 1  ~ 7 4  is a regular transition map, which can be written as

T4  =U1(v1-c,vc)

= vl-c [ m141 (v)  + m142(v)v 1-c + m143(v)vc  + O(v2<1-c), v2c) J,

p4  = U2(vl-c,vc)

= vc [ m141 (v)  + m142(v)v 1-c + m 143(v)vc  + O(v2
<1-c), v2c)],

(5.3.16)

where  m141(v),  m141(v),  m142(v),  m142(v),  m143(v)  and m143(v)  are defined  in

(5.3.13).

•  8 4  :  7 4  ~ :E4  is the  second type  of Dulac map in  the neighborhood of P4  with

Therefore, for T 4 ,  we  have

T41 (v,  c)  = v,

T42(v,c)  = 1]4(v,w(;:,,81)) + vo-a(l-c) [m41(v)  + m42(v)v 1-c

+m43(ZJ )vc + O(v2{1-c)'  ZJ2c)  + 841 (v, vl-c' w(mr~11 vl-c' -,81))]'

99

the same property as of 81  in ( 5 .3 .11 ).

(111) study  Fv( c, d)  and  Gv( c, d)

To  obtain  the  cyclicity  of Ehh 1 c,  one  needs  to  study  the  number of roots  for  the

following system

{
 Fv(c, d)  :.~ T12(v, c) - T22(v, d)  ~ 0,

Gv(c, d)  .- T42(v, c)  - T32(v, d)  - 0,
 (5.3.17)

for (a,µ)  E  A0  x  V 10  with ( c, d)  E  Dv where Dv  =Iv x  Iv and v, c sufficiently small.

For 0  < v  < c 2 ,  Fv(c, d)  and Gv(c, d)  are continuous on Dv  and smooth in Vv.  For

V(c, d)  E  Dv  with c  >  0 sufficiently small, it has been proved in [53] that

a
ac Fv(c, d)  f  0,

Denote the  number of roots of Fv(c, d)  =  0  and Gv(c, d)  =  0  in the  region Dv  by

#(F, G), and let

Then  for  0  < v  < c2  and V( c, d)  E  Vv  with  c  >  0  sufficiently  small,  by generalized

100

Rolle's Theorem (Theorem 6.  11  in [53]), one can have

where
 #(F, G)  ~ #(F, J[F, G]) + 1

= #(F,G 2 )  + 1

~ #(G2, J[F, G2])  + 2

= #(G2, G3)  + 2,
 (5.3.18)

G  (  d)  =  a3z/;3 [(8F) u1!u3 (8G)-u 1!u3  _(BF) u1!u3 (8G)-u 1!u3 ]
2  l/' c,  (j 1  8c  ac  ad  8d  '

_  (8G2 8G2)- 1
G3 (v,  c, d)  =  -a1li  Be  Bd  J[F, G2].

(IV) Calculation of#( G2 , G3)

In order to study the number of the roots of the system G 2 (v,  c, d)  = 0,  G 3 (v,  c, d)  = 0,

one can eliminate the variable c, and obtain a scalar equation with variables (v,  d),  which

was given in [53], and we recall it as follows.

g(v,  d)  = !'( v)  + C1 ( v )v<Tid + C2 (v )vl-d + C3 (v )vd + 0( v2(1-d)' v2d)

N(k)
+ L  c4j(v)vu3(l-d)j  + O(vu3(l-d)(N(k)+l))

j=l

+H(  d  1-d  ( vd  )  (!!!lil..  1-d  a  )) v, l/  'l/  'W  Po' -a1  'W  ro  l/  '-,vi  '

101
 (5.3.19)

where
 1
f'(ll)  =  1 - ( mf
1 (11)kf3 (11))  ui +a3 '

c2(0)  = *m142(0)(k1(0)  - m1(0))  = *€2,

In order to obtain the cyclicity of Ehh 1 c  , we will  study the number of roots of the

equation g(v,  d)  =  ford  E  Iv,  11  >  0  sufficiently  small and \:/(a,µ)  E  A0 x  V 10.  We

need the following two lemmas.

Lemma 5.3.1.  [53] If a0  =  H a 1  =  1 ),  then in the chart FR.  on r  =  0,  the first saddle

quantity a2  of P1  satisfies a2  = * [l30.

Lemma 5.3.2. The  regular transition map R  : E3  ~ E4  defined in  (5.3.14) satisfies

a2R
that  a-2 2 (0, 0)  #- 0 infamily (5.1.1).
Y3

Proof  From  Lemma 5.1.1,  if 82  =  ~'the nilpotent elliptic point is  of codimension 4,

and system ( 5 .1. 7) becomes
 (5.3.20)

102

where b =  ~. By the near-identity transformation,

{
 V3  = X1,

Z  _  "\/  + b-v'b2=Bx2
3  -II  4  ll
 (5.3.21)

and rescaling
x- x
1  - H b + Jb2  - s)  ,  (5.3.22)

we bring system (5.3.20) into a "standard form"

{  X  = Y  + a0X 2 ,

Y  = Y(X  +  tX 2  +  X 3 h1(X)) +  X 4h 2 (X) +  Y2Q(X, Y),
 (5.3.23)

where a0  =  1
~ [b  - Jb2 - 8] 2  =  ~ and t  = 0.  h1 (X), h 2 (X) and Q(X, Y) are C 00 •

To obtain the normal form near the singular point P4 ,  we make the following blow-up

X=-r,  (5.3.24)

then we have
 (5.3.25)

where h1  and h2  are C 00  functions.

We divide the above system (5.3.25) by~+ y.  By the transformation
 (5.3.26)

103

we obtain the normal form near the singular point P 4

where ~i is the coefficient of the term  r
2
iy~i+
1 •

If we make the blow-up

X=r,  (5.3.27)

similarly we will obtain the normal form  near the singular point P3

f3  = r3,

ih  = - [ ~ + t \;(r
2Yi)i]  1}3.

Let E 3  =  E 3  n {p  =  0}  and  E 4  =  E 4  n {p  =  O},  where {p  =  O}  is the blow-up of

the fiber  jl =  0.  Then by  a sequence of changes of coordinates (5.1.2),  (5.1.4),  (5.1.6),

(5.3.21), (5.3.22), (5.3.24), (5.3.25) and (5.3.27),  E 3  and E 4  can be parameterized by y3

and y4 ,  respectively.  Therefore, we have

E3  ={(x, y)I

x  =  f3(Y3)  =  -~ [1 + O(ro)  - (6 + O(ro))y3 + (12 + O(ro))iii + O(yi)],
ro

y = g3(Y3)  =  ~ [1  + O(ro)  - (6 + O(ro))y3 + (12 + O(ro))iii + O(Y~)] },
ro
 104

E4  ={(x, y)I

x  =  f4(y4)  =  ~ [1  + O(ro)  - (6 + O(ro))y4 +  (12 +  O(ro))y~ + O(yD],
ro

y = g4(y4)  =  ~ [1  + O(ro)  - (6 + O(ro))y4 +  (12 +  O(ro))y~ + O(Yl)]  }.
ro

Now we study the regular transition map <I>  : E 3  -----7  E 4  along the invariant parabola

(5.1.8). By the formula in Theorem 2.2.1, we have

_~(y
3
)  exp  (  fT divX(r(t)) I  dt)
~(<I>(Y3
))  lo  (5.1.1),(5.I.8)

~(y3)  (J,f4(<P(y
3 ))  divX (r( t)) I  ) ---exp  dx  ,
~(<I>(y3
))  f3(y 3 )  P(x, y)  (5.1.1),(5.t.8)  (5.3.28)

where T  is time to travel from  ~3 to E 4  along the invariant parabola,

and

For simplicity, we let

:F(x)  := di~X(7(t)) I  =  __ 4_-X_+_2_(8_2_+_2_)x __
P(x, y)  (5.1.1),(5.I.8)  82x2 + 4-Xx + 1 + ,\2

Since
 lim  <I>' (0)
ro-+O  =  lim  ~exp  :F(x)dx
~(O)  (J,f4(o)  )

ro-+O  ~(O)  h(O)

=  exp (1: F(x)dx)  =exp ( - 8~~ ),

105

then we have
 (  16.-\7r  )
<I>'(O)  =exp  82
~  + </>(ro),

where </>(r0 )  = o(l) as ro---+ 0.

From (5.3.28), we have

Therefore,

<I>"(O)  =  Ll'(O)L°i(O)  ~ Ll(O)L°i'(O)<I>'(O) exp (J,f4(o) F(x) dx)
Ll2 (0)  /3(0)

+  ~(O) exp (J,!

4 (o))  F(x) dx)  [F(/4(0))/~(0)<I>'(O) - F(/3(0))/~(o)J.
Ll(O)  f3(o)

Since

lim  <I>" ( 0)
ro--+O

=  lim  [Ll'(O)  - L°i'(O)<I>'(O)] <I>'(O)  +  [F(f4(0))f~(O)<I>'(O) - F(/3(0))/~(o)] <I>'(O)
ro--+O  Ll(O)  Ll(O)

=  lim  [ Ll' ( 0)  + 12 ( 82  + 2) J <I>' ( 0) ( 1 _  <I>' ( 0))
ro--+O  Ll(O)  82
 ) ] f  0,

106

so we have

<I>"(O)  = 12 exp (  16.A7r  )  ]
<52\/~  + 'lf;(ro),

where 'lj;(r0 )  = o(l) as r0 -+ 0.

Since ~o > 0 and A =!=  0,  so for the transition map R  : ~3 -----t  ~4, we have

aa2 ~2 (o, o)  =  <I>" (o)  =I=  o.
Y3

Therefore, we finish the proof of the  lemma.  D

End of proof for  Theorem 5.2.1

We treat the following two cases jl30  ~ 0 and jl30  < 0 separately.

(1). fl30  ~ 0.

For the graphic Ehhlc, we have
 1
1'(0) =  1 - ( mf
1 (O)kf3 (0)) ui +ua.

If jl30  ~ 0, then by Proposition 6.1  in  (53], we have k1 (0)  S  1.  Since m1 (0)  =  <I>'(O)  <

1, then we have 1'(0)  =!=  0.  Hence, Cycl(Ehhlc)  S  2.

(2).  fl30  < 0.
 107

Since a0  =  ~,so a 1  = p1  = 1 and a3  =  ~· The the function g(v, d)  in  (5.3.19) has

the form

g(v,d)

where 811 (0)  can vanish, 812(0)  = *a2 and c41 (0)  = *m2(0).

By Lemma 5 .3 .1  and Lemma 5 .3 .2, we have

C41 (0)

Now we study the  root of g(v, d)  for  (v, d)  E  (0, c2 )  x  Iv  with c  >  0  sufficiently

small.  Firstly,  we  can  kill  the  term  !'(v).  Differentiate  g(v, d)  with  respect  to  d,  and

divide by In v, then we have

1  a
9o(v, d)  : =  Inv f}dg(v, d)
 vd  vd  vd
= *811 (v)vd + *812(v)vdw(-, a1) + O(vw 2(-, -a1)w(-, a 1))
Po  Po  Po
+ *C41 (v )vu3(l-d) + o( vu3(l-d)).

Then we can kill the vd term as follows.

vd  a (  )
91(v, d)  : =  Inv f}d  9o(v, d)v-d
 d  d
=  *812(v)v171d + O(vw2(-~-, -a1)w(~, a 1)) + *C41(v)v173(I-d) + o(v173(I-d)).
Po  Po
108

Denote
 Z1(v)  := *D12(v),  Z2(v)  := *C41(v),

and we have Z1(0)  f  0 and Z2(0)  f  0.

1.  If Z1 (O)Z2(0)  > 0, then g1 (v,  d)  f  0 for (v,  d)  E (0, c-2) x  Iv  with c  > 0 sufficiently

small.

2.  IfZ1 (0)12(0)  < 0, then ~(v, d)  f  0 for (v,  d)  E (0, c-2) x Iv  with c  > 0 sufficiently

small.

By Rolle's Theorem, \:/(a, fl)  E  A0 xV 10 ,  g(v,  d)  has at most 3 zeros in (v,  d)  E  (0, c-
2 )  x

Iv.  Therefore, by (5.3.18), system (5.3.9) has at most 5 zeros,  i.e., Cycl(Ehhlc)  ~ 5.

For the  intermediate graphics Ehh 1 b,  its finite  cyclicity has  been proved  in  [ 5 3]  by

showing that the transition map T  : II3  ~ II4  passing through the blown-up sphere is

nonlinear.

Therefore, we finish the proof of Theorem 5 .2.1.

109

6  Finite  cyclicity of (I} Ib)

For the graphic (!fib),  it is an HH-type graphic with a nilpotent elliptic point is at infin-

ity.  Compared to the  graphic (!Jb),  there is  an additional attracting saddle-node on the

invariant parabola as shown in Fig. 6.1  .

Figure 6.1: The graphic (Ji1b).

In this chapter, firstly  we will  give a main theorem stating that the graphic (J{1b)  has

finite  cyclicity  in  section 6.1,  and then we  prove the main theorem  by  showing that all

the  upper boundary graphics, intermediate graphics and lower boundary graphics have

finite  cyclicity  in  section 6.2,  6.3  and 6.4, respectively.  Finally, we has an open case for

110

the cyclicity of Ehh3e of ( fi1b)  and we leave it as future work.

6.1  Main  Theorem

Theorem  6.1.1.  The graphic (Ii1b)  has.finite cyclicity inside quadratic systems.

Since the graphics  ( Ji1b)  has a nilpotent singular point at  infinity,  we can  limit our-

selves to  the  limit periodic  sets  which  have  an  invariant  line  (fl1  =  0).  Moreover the

connection along this line is fixed.  Therefore, we only need to look to the limit periodic

sets Ehhl-Ehh8.

To prove the finite cyclicity of the graphic (Ji1b), we have to prove that all the upper

boundary  graphics,  the  intermediate  graphics  and  lower  boundary  graphics  of Ehh 1-

Ehh8 have finite cyclicity.

We  begin with the upper boundary graphics.

6.2  The  upper  boundary  graphic

Proposition  6.2.1.  For the graphic (Ii1b),  Cycl(Ehhia)  ::;;  1, i  = 1, 2, · · ·  , 12.

Proof  By Remark 4.2.2.  D

111

6.3  The  lower  boundary  graphic

For each family  of graphic Ehhi  ( i  =  1, 2, · · · , 8),  we  use  Vi  c  § 2  to  denote  the  set

ofµ  =  (P,i, P,2 , p,3 )  in  which  the  family  Ehhi  exists,  and  use  ViO  to  denote  a  small

neighborhood of p,0 ,  where µ0  E  Vi.  We  use always A0  to denote a small neighborhood

of a0 ,  where a0  E  (0,  ~).

6.3.1  Ehhlc,  Ehh2e  and  Ehh3e

We  study  the  displacement maps defined  on the  sections  T 1  and  T2  with  images on the

sections II1  and E 4  as shown  in Fig. 6.2.

Exactly  as we  did for the lower boundary graphic Ehhlc of (IJb),  firstly  we  param-

eterize the  sections II1  and E 4 .  On the  section  Ti,  the coordinates are (r1 , p1),  and we

have
 r1  = l/1-c,

with  (v, c)  E  (0, c2 )  x  Iv  where Iv  = U~~,

1
~~) c  (0, 1).

Similarly, on the section T 2,  we have
 d
P2  = v  ,

with  (v, d)  E  (0, c2 )  x  Iv  to parameterize the  section  T2 •  Then  we  study  the number of

112

Figure 6.2:  Transition maps for the graphics Ehhlc, Ehh2e and Ehh3e of (!fib)

roots of the system
 (6.3.1)

for (a,µ)  E  Ao  x  Vio( i  = 1, 2, 3) with ( c, d)  E  Iv  x  Iv  and v, c sufficiently small.

The transition maps 7i(i =  1, 2, 3, 4) have the same definitions as those ofEhhlc for

graphic (I§b).  The transition maps ei(i = 1, 2, 3, 4), U,  V  and s- 1  are the same as those

defined for (!Jb),  except the transition map R:  E 3  --+  E 4 •

For (IJb),  R  is  merely a regular transition  map,  while  for  (I{1b)  here,  R  can  be de-

113

composed as

R:  ~3----+ ~4
 (6.3.2)

.......  - .......
where the transition maps Ri, Rand R 2  are given by (4.2.4), (4.2.5) and (4.2.6).  There-

fore, we have
 (6.3.3)

where
 mo(v)  = no(v)  + O(m),
 i  = 1, 2, ....

By equation (5.3.18), the number of solutions of system (6.3.1) is at most 2 plus the

number of solutions of the  scalar equation g(v,  d)  =  0 ford  E  Iv,  v  >  0  sufficiently

small and V(a,  µ)  E  A 0  x  ViO(i  =  1, 2, 3), and g(v,  d)  = 0 is given as follows  [53].

g(v,  d)  = ry(v)  + c1 (v )viiid + c2 (v )v 1-d + c3 (v )vd + O(v2(t-d), v 2d)

N
+m(v) L C4j(v)vaa(t-d)j  + O(m(v)vaa(t-d)(N(k)+1))

j=l
+ H(v  vd  vl-d  w( vd  -a )  w( m141 vl-d  -/3  ))
'  '  '  Po  '  1  '  ro  '  1  '

114
 (6.3.4)

where
 1
r(v)  = 1 - ( mf
1 (v)kf 3(v))  ui+u3 '

and H  is Ck  H  =  0  (vP 1dw(  vd  a  )  vP3(I-d)w(  m 141 v 1-d  {3  )) .
'  Po'  1  '  ro  '  1

6.3.1.1  Ehhlc and Ehh2e

Since
 1
r(v)  = 1- ( mf
1 (v)kf 3 (v)) ui+u3 '  (6.3.5)

for graphic Ehhlc, we have k1 (v)  is  bounded and m1(v)  ---+  0 as  v  ---+  0,  so r(O)  =  1.

Hence, V(a,  µ)  E  A 0  x  V 10 ,  g(v,  d)  -/- 0 for  (v,  d)  E  (0, c-2 )  x  Iv.  Therefore,  system

(6.3.1) has at most 2 small zeros,  i.e., Cycl(Ehhlc)  ::; 2.

For graphic  Ehh2e,  we  have  k1(v)  ---+  0 and m1(v)  ---+  0 as  v  ---+  0,  so  r(O)  =  1.

Hence, V(a,p,)  E  A0  x  V 20 ,  g(v,d)-/- 0 for  (v,d)  E  (O,c-2 )  x  Iv.  Therefore,  system

(6.3.l) has at most 2 small zeros,  i.e., Cycl( Ehh2e)  ::; 2.

115

6.3.1.2  Ehh3e

The  family  Ehh3  exists  if and only  if P,0  :=  (0, 0, -1).  We  treat the  following  cases

depending on the value of a0 •

•  Case a0  E  ( 0,  ~) \  Q

Let  N  = L
73[ao)]. In this case, the function 9(v, d)  can be simplified  to

9(v, d)  =  !'(v) + c1 (v)v<hd + O(va1d) + c2 (v)v 1-d + c3 (v)vd + O(v 2(I-d), v 2d)

!u13l
+m(v) L C4j(v)va3(I-d)j + O(m(v)va3(l-d)([u~l+I)).

j=l

We  define the following  procedure

{
 9o(v, d)  = 1!;v :d9(v, d),
DD:  . (  d)  =  vu3(I-d)i  8  (  .  (  d)  -a3 (1-d)j)
91  v,  Inv  8d  91-l  v,  V  '  j  =  1, ... 'LiJ

Then after [a~] + 1 steps of successive derivation and division, we get

Denote
 116
 (6.3.6)

1.  I2 (0)l3 (0)  >  0, then 9[-J-J(v, d)  f- 0 for (v, d)  E  (0, £
2 )  x Iv  with£> 0 sufficiently
u3

small;

- - a  2
2.  l2 (0)l 3 (0)  < 0,  then  ad9[-J-j(v,  d)  f- 0 for  (v,  d)  E  (0, £  )  x  Iv  with£  >  0 suffi-
u3

ciently small.

If ii1  < 1,

1.  l 1 (O)l2 (0)  >  0, then 9[-J-J(v, d)  f- 0 for (v,  d)  E  (0, £
2 )  x Iv  with£ >  0 sufficiently
u3

small;

- - a  2
2.  li (O)l2(0)  < 0,  then  ad9[a131 (v,  d)  f- 0 for  (v,  d)  E  (0, £  )  x  Iv  with£  >  0 suffi-

ciently small.

Hence, 9(v,  d)  = 0 has at most [iJ + 2 roots.  Therefore, system (6.3.1) has at most

[JJ + 4 zeros, i.e.,Cycl(Ehh3e)  ::; (i
3 ]  + 4.

•Case a0  E  (0,  ~) n Q  \  {n~2
,
2
~~

1 }

In this case, we have q1  ~ 2,  a 1  < p1  and p 3  ~ 2.  For v  >  0 sufficiently small, we

have ii1  < p 1  and (i
3 ]  < p 3 ,  then the function 9(v,  d)  can be simplified to

q3
+m(v) L c4j(v)vu3 (I-d)i.

j=l

Exactly as we did forthe case a0  E  (0, ~) \  Q, we obtain Cycl(Ehh3e)::;  q3  + 4.

117

•  Case a0  =  nl2 , n  E  N, n  =/=  1, 2

In  this  case,  we  have  a 1 (a0 )  < p 1  =  n  > 1 and  a3 (a 0 )  =  ::  =  n2
_;-2  E  (1,2),  so

q3  2::  2.  Then the function g(v,  d)  can be simplified to

g(v,  d)  = r(v) +  c2(v)v1-d +  C3(v)vd  +  O(v2(l-d)' v2d).

Apply DD process for one step to kill the 1'( v)  term,  similar to the argument of the case

a0  E  (0,  ~) \  Q, we obtain Cycl(Ehh3e)  ::;  4.

•  Case a0  =  2
~~
1 , n  E  N, n  =I=  1

In this case, we have a 1(ao)  =  2n2_1'  p1 =  2,  q1 =  2n - 1 and a 3 (a 0 )  =  ~' p 3  =  1,

q3  = n. Since o-1  < 1, the function g(v,  d)  can be simplified to

n-1
g(v,  d)  =  r(v) +  c1(v)va1d  +  O(vaid)  +  m(v)  L C4j(v)va3(l-d)j  +  b31(v)vl-d
j=l

+8  (v)vl-dw(m141 vl-d  (3  ) +  0  (vw2(m141 vl-d  -(3  )w(!!!l.il..vl-d  (3  ))
32  ro  '  1  ro  '  1  ro  '  1  '

where c1 (0)  = *fl30  =!= 0, 831 (0)  can vanish, and 832(0)  = *f32. Here {32 is the first saddle

quantity of P3  in the chart F.R.  on r  =  0,  and (32  =I= 0 by Lemma 6.14 in  [53].

Apply DD process for n  steps to kill the r(v) term and va3(l-d)j (j  =  1, 2, · · ·  , n-1)

terms, then we get

9n(v,  d)  = *C1(v)va1d  +  O(vaid)  +  *831(v)vl-d +  *832(v)vl-dw(m/041 vl-d, f31)

+O (vw2(m;
0
41 vl-d,  -f3i)w(m;
0
41 vl-d, f3i)).

118

(  )  - 1.11-d  8  (  -(1-d)  (  )) Let gn+l  v, d  - Inv  ad  v  gn  v, d  , then

gn+1(v, d)  =  *C1(v)vo-1d +  O(vo-1d)  +  *832(v)v(l-d)o-3

+O (vw2(m;
0
41 vl-d, -,Bi)w(":.~41 vl-d, ,Bi)),

so V( a,µ)  E  Ao  x  Vj3 ,  either gn+l (v, d)  f- 0 or  89i);1 (v, d)  f- 0 for (v, d)  E  (0, c2 )  x  Iv

with c  > 0 sufficiently small, so we obtain Cycl(Ehh3e)  ::;  n  + 4.

•Case a0  =  ~

In this case  a1(~) =  2,  p1 =  2,  q1 =  1 and  a3(~) =  1,  p 3  =  q3  =  1.  the function

g(v, d)  can be simplified to

+0 (v2w2( vd v1-d  -a )w( vd v1-d  a  )) + 8  (v)vl-d
PO  '  1  PO  '  1  31

+8  (v)vl-dw(m141 vl-d  a  )  + 0  (vw2(!!!lll.vl-d  _a  )w(!!!lll.vl-d  a  ))
32  ro  ' /Jl  ro  '  /Jl  ro  ' /Jl  '

where 811(0)  and 831(0)  can vanish, 812(0)  = *fl30  f- 0 and 832(0)  = *,82  f- 0.

Apply DD process for 2 steps to kill the 7(v)  term and vd term, then we get

gi(v,d)  = *8u(v)v2d +  *812(v)v
2
dw(~:v
1
-d,a1)

+O (v2w2( vd vl-d  -a  )w( vd vl-d  a  )) + *8  (v)vl-d
PO  '  1  PO  '  1  31

+ * 8  (v)vl-dw(m141 vl-d  a)+ 0  (vw2(m141 vl-d  _a  )w(m141 vl-d  a  ))
32  ro  ' /Jl  ro  '  /Jl  ro  ' /Jl  '

Let
 (  )  v2d  8  (  - 2d  (  ) )
g2  V' d  =  Inv 8d  V  gl  V' d  '

(  )  _  v 1-d  8  (  -(1-d)  (  ))
g3  V' d  - ln v  8d  V  g2  V' d  '

119

then
 g3(v,d)  = *<h2(v)va1d +  o(v2w2(~:1/1-d, -a1)w(~:l/1-d,a1))

+  * 832 ( v) v(l-d)a3  +  0 ( vw2 ( m::1 vl-d, -,61 )w ( ~1
0
41 vl-d, ,a1)) .

Then V(a, µ)  E  A0  x  Vi3 ,  either g3(v,  d)  i=  0 or  ~(v, d)  i=  0 for  (v,  d)  E  (0, c:2 )  x  Iv

with c:  > 0 sufficiently small, so we obtain Cycl(Ehh3e)  ::;;  7.

•Case a0  =  ~

If a0  =  ! , the nilpotent elliptic point at infinity is of codimension 4,  and the graphic

(fi1b)  occurs in the following system

{  x  =  V[5" x  - y + x 2 ,

Y.  = x  +  v'l5y  +  3v'i5x2 +  .:1xy
5  10  2  '
 (6.3.7)

which determines the regular part of the graphic.

For the passage near the blown-up sphere, on r  = 0 in the chart F.R., we have

_  { x = fJ  + ~x
2
,
Xµ=l:  y = ( -1 + x)fJ,  (6.3.8)

Furthermore, we have a 1  =  1 and a3  =  ~' so function g(v,  d)  defined  in (6.3.4) has the

form
 g(v,d)  1/d  1/d  1/d
f'(v)  +  811 (v)vd  +  812(v)vdw(-,  ai) +  O(vw2(-, -a1)w(-, 0:1)),
Po  Po  Po

+c2(v )vl-d +  m(v )c4j (v )va3(l-d)  +  O(v2(1-d)' mv2a3(l-d))'

120

m(v)  is sufficiently  small for (v, µ,a)  close to (0, p,0 , a0 ).

Therefore,  we  need  an  additional generic  condition  to  prove  the  cyclicity  of the

graphic Ehh3e,  which  we  may  derive  from  the  high order term  of the transition maps.

This  is the most difficult  case for the graphic (Jf 1b),  and we  leave it for future work.

6.3.2  Ehh4c

For the  lower  boundary graphic Ehh4c,  it  is  the  same  as  the  lower  boundary graphic

Sxhhlc of (fi3 ), so Ehh4c has finite  cyclicity.

6.3.3  Ehh5c

The  Lower  boundary of Family  Ehh5  passes through a hyperbolic  saddle point  in  the

chart F. R.  as shown  in Fig.  6.3.  Let ..\(v)  be the hyperbolicity ratio at this saddle point.

Take  sections E 1  = {y = 1}  and E 3  =  { i  = 1}  in the normal form  coordinates of the

saddle point.

We  are going to study the displacement map defined  on the section r 1 :

......  -
L  = T-T.
 121

Figure 6.3:  Transition maps for the graphic Ehh5c

The transition map T  can be factorized as

T  = 8 4 oU,

where

•  U:  T 1  ---t  T 4  is a regular transition map, which is given by (5.3.16).

•  8 4  :  7-4  ---t  ~4 is the second type of Dulac map in  the neighborhood of P4  with

122

Therefore, for T,  we have

{
 T1(v, c)  = v,

f. (v  c)  =  _ ..11.JLma3  (v)v<1-c)a3 [l + O(vc  v1-c) + e  (v  v1-c  w( m141 v1-c  -/3  ))]
2  '  ru3  141  '  41  '  '  ro  '  1  '
0
 (6.3.9)

where 0 41  satisfies the same properties as of 01  in ( 5 .3 .11 ).

For the transition map T, we calculate it by the following decomposition

where

•  8 1  :  T 1  ---t  II1  is the second type of Dulac map in  the neighborhood of Pi  with

•  8 1  :  II1  ---t  E 1 is a regular transition map.  Since x axis is fixed  for  X p=l,  so  8 1

can be written as

where e1 (0)  > 0.

•  D  : E 1  ---t  E 3  is the Dulac map near the saddle point, which has the expression

(3.2.5).
 123

•  8 2  :  ~3 ~ II3  is a regular transition map, which can be written as

{
 821 (v,  iJ)  = v,

822(v, iJ)  = bo(v)  + b1 (v)iJ  + O(fj2),

where b0 (0)  = 0 and b1 (0)  > 0.

•  ~3 : II3 ~ ~3 are the first type of Dulac maps in the neighborhood of P3  with

•  The transition maps R1 ,  Rand R2  are given by (4.2.4), (4.2.5) and (4.2.6).

Hence, for T, we have T1 (v,  c)  = v.  Let

Ve  - Ve
Y1  =  (- )°"
1 [Yo+ 811 (v, ve, w(-, -a1) )],
·  Po  ·Po

i)3  = bo(v)  + b1(v)e1(v),\iJ~[l + </>1(v,x)],

where ¢1 ( v, x)  E 18°, 811  satisfies the same properties as of 81 in ( 5 .3 .11) and 831  satisfies

.......
the properties (2.5.23).  Then the second component ofT can be written as

T2(v,  c)  = no(v)  + O(m) + m(v)[(li(v)n 1 (v)  + O(m(v)))y3  + O(YD].  (6.3.10)

124

By (6.3.9) and (6.3.10), the first derivative of L2(v, c) with respect to c is given as follows.

8L2(v, c)  aT2(v, c)  aT2(v, c)
8c  8c  8c

[  ,..  J (  v  )  a

3
 [  8831  _  v  J = m(v)  li(v)n1(v)  + O(m(v)) + O(y3)  Vo  1 + 8f)3  (v,y3,w(vo' -/3i))

bi ( v)  ( ei ~:Yo r VAUic M1 [ 1+4>2(v, X) l [ 1 + l'12(v, Ve, w( ~:, -a1) + O(v"
1c)] 1n v

+ y:3 mrl1 (v)v(l-c)a3a3 [i + O(vc, v1-c) + 842(v, v1-c, w( m 141 v1-c, -/31))]  ln v,
r0  ro

where </h(v, x)  E  I0 , and 812, 842  satisfy the same properties as of 81 in (5.3.11 ), also

8831  - 0  (  j.53  q3  (  v  /3  ) 1  v  ) ---- v  w  -,- 1  n-.
8y31  Vo  Vo

8L2(v  c)
8c'  has the same number of small roots as of

- v-(l-c)a3  8L2(v, c)
L 2 ( v, c)  =  l  .  8 nv  c

_  Yo  a3  (  )- + O(  c  1-c) + 8  (  1-c  (m141  1-c  /3  )) - -a:-m141  v  a3  v  , v  42  v, v  , w  --v  , - 1
r 0 3  ro

at  most  one  small  root  for  (v,  c)  E  (0, c:2 )  x  Iv  with  c:  >  0  sufficiently  small,  i.e.,

Cycl(Ehh5c)  ~ 1.

6.3.4  Ehh6c

Compared to  the  lower boundary  graphic  Ehh5c,  Ehh6c passes through  a  saddle-node

point as shown in Fig 6.4.  In the neighborhood of saddle-node point, take sections E 1  =

125

{y = 1}  and Ea  = { x = 1}  in the normal form  coordinates.  The  other transition maps

are the same as those of Ehh5c.

Figure 6.4: Transition maps for the graphic Ehh6c

D  : E 1  ---t  Ea is the stable-centre transition map near the saddle-node point.  Obvi-

ously, the first component D 1 (v, i) = v.  For the second component D2 (v, i), Vp, q E  N,

we have

For the displacement function  L

.......
L=T-T,
 126

we have L 1(v,  c)  = v,  and
 1-c
Yo  a-3  (  )  (l-c)a-3  - [i  O(  c  1-c)  ()  (  1-c  ( m141V  f3  ))] l +  0-3  m141  v  v  a3  +  v  ' v  +  42  v, v  'w  ' - 1  n v.
ro  ro

8L2(v, c) oc  has the same number of small roots as of

Yo  0-3  (  )- + 0(  c  1-c) + (}  (  1-c  (m141  1-c  Q  )) =  a-3  m141  v  a3  v  , v  42  v, v  , w  --v  , -JJ1
ro  ro

at  most  one  small  root  for  (v,  c)  E  (0, c2 )  x  Iv  with  c  >  0  sufficiently  small,  i.e.,

Cycl(Ehh6c)  ::; 1.

6.3.5  Ehh7c

The Lower boundary graphic of Ehh7 passes through a repelling saddle-node as shown

in Fig 6.5.  In the neighborhood of saddle-node, take sections E 2  =  { i  =  1} and  E 4  =

{y =  1} in the normal form coordinates.
 127

Figure 6.5:  Transition maps for the graphic Ehh7c

We  are going to study the displacement map defined on the section II2 : ·

,,,.....
L  = T-T.

The transition map T  can be factorized as

where

•  8 1  :  II2  ----t  ~2 is a regular transition map.  Since x axis is fixed  for X p=l, so 8 1

128

Let
 can be written as
 {
 Su (v, fh)  = v,

S12(v, ih)  = ei (v)fh + O(Y~),

where e1 (0)  > 0.

•  D : E 2  -t E4  is the stable-centre transition map near the semi-hyperbolic point.

Obviously, the first component D 1(v, fj)  =  v.  The second component D 2 (v, fj)  is

a solution of the following differential equation

F(Y, v, jl, a)dx - xdfj = 0,  (6.3.11)

where F(Y, v, jl, a)  = eo(v, jl, a)+ c2 (v, jl, a)y2 + o(y2 )  with eo(O, Jlo, a0 )  = 0 and

•  82  :  E4  -t II4  is a regular transition map, which can be written as

{
 821 (v, y)  = v,

S22(v, y)  = bo(v)  + b1 (v)fj + O(y 2),

where b0 (0)  = 0 and b1 (0)  > 0.

•  ~4 :  II4  -t E4  are the first type of Dulac maps in the neighborhood of P4  with

hv(i/2)  := D2  o S12(v, Y2)  =  exp (- [1  _  F(~jj ) )  ,
j S12(v,y2)  y,  V

Y4  = S22(v, hv(i/2)).
 129

Therefore, for T,  we have
 (6.3.12)

where ¢4  satisfies the properties (2.5.23).

The first derivative ofT2 (v, ih) with respect to fh  is given as follows.

(::_)u
3  [1 + O(vii3 wq( .!:___,  -{31 )  ln( .!:___ )]
~  ~  ~
8822(v, fj)  hv(Y2)  812(v, fJ2) x-----------
8fj  F(812(v, fJ2), v)  8fJ2

and

where

H(v  - ) = 82
822 h  (-) (8812) 2  8822  (8812) 2
- 8822 8F(fj) (8812)2
, Y2  !'.l-2  v  Y2  !'.l- +  !'.l- !'.l- !'.l- !'.l- !'.l-uy  uy2  uy  uy2  uy  uy  uy2

8822F(8  (  - )  )82
812  0(  P3  q-1(  v  {3) 1  v) - ~  12  v,  Y2  , v  ~ +  v  w  -, - 1  n - .
uy  uy2  Vo  Vo

Since F(812(v, fJ2), v)  # 0 and hv(fJ2)  >  0,  and

lim  H(v, fJ2)  = b1 (O)e1 (0)2 > 0,
(ih ,v,P,,a)--+(0,0,P,o  ,ao)

So for v  > 0 small and (fl, a)  sufficiently close to  (flo, ao), we have  02T~~ !h)  > 0 in
Y2

the small neighborhood of fj2 =  0, i.e., T2(v, fJ2)  is convex.

130

........
For the transition map T,  we calculate it by the following  decomposition

where

•  82 1  :  112  ~ T 2  is the  inverse of the second type  of Dulac map in the neighbor-

hood of P2  which can be written as
 (6.3.13)

where N 1  = ?i and B21  E  10 .
Yo

•  V:  T 2  ~ T3  is a regular transition map, which is given by (5.3.13).

•  8 3  :  r 3  ~ E 3  is the  second type  of Dulac map in the neighborhood of P3  with

•  The transition maps Ri, R and R2  are given by ( 4.2.4), ( 4.2.5) and ( 4.2.6).

Hence, we have T1 (v,  c)  = v and the second component off can be written as

T2(v,y2)  = no(v)  + O(m(v))  + m(v)[(li(v)n1(v)  + O(m(v)))y3  + O(yi)],

where
 131

and N2 = - ~
3 and 022  E  I0 . Then the first derivative ofT2(v, fh)  with respect to fh  is
To

given as follows.

where B23  E  I0 . The second derivative ofT2(v, ih) with respect to fh  is
 (6.3.14)

where
 - 1  u3
H(v,f12)  =  [ti(v)n2(v) +  O(m(v)) +  O(y3)] ;: (vii;ui)  (1+824(v,fi2))

+  [11 (v)n 1(v)  + O(m(v))  + 0(1h}j(:: + 1)(1+02s(v, ih)),

Note that on the section 7 2, the coordinates are (r2, p2) with r2P2  = v for v  > 0 small,

so we only need to consider the domain h I < c  and I P2 I < c  for c  > 0  small.  In fact,

1  1
from  (6.3.13), we have P2  = y;
1  (N1  +  821(v, ii2)),  and r2  = vy; ui N! 1(1+021 (v, ii2))

with 021  E  I0 . Therefore, we study the graphic on section 72 for sufficiently small E  > 0

_  _..!_
such that vy2  ui  «  1.  Hence,  for v > 0 small and  (P,, a)  sufficiently close to  (P,0 , a0 ),

we have H(v, y2 )  > 0 in the small neighborhood of fh  = 0

Since N2 < 0, by (6.3.14), we have  82
f~~·
7
'2) < 0, i.e., T2 (v,  y2 )  is concave. Note that

fH v, y2 )  is convex, so for V (a, P,)  E  A0  x V 10 and v >  0 sufficiently small, £ 2 ( v, y2 )  has

132

at most two small roots in the small neighborhood of y2  = 0,  i.e., Cycl(Ehh7c)::;  2.

6.3.6  Ehh8c

The Lower boundary  graphic  of Ehh8  passes through  a  hyperbolic  saddle  point  in  the

chart F.  R.  as  shown in Fig.  6.6.  Let A(v)  be the hyperbolicity ratio at this saddle point.

Take sections ~2 =  { x =  1}  and  ~4 =  {y =  1}  in the normal form  coordinates of the

saddle point.
 Figure 6.6:  Transition maps for the graphic Ehh8c

We are going to study the displacement map defined on the section T2 :

L=T-T.
 133

The transition map T  can be factorized as

where

•  V  : 7 2  ------+  7 3  is a regular transition map, which is given by (5.3.13).

•  8 3  :  7 3  ------+  E 3  is the  second type of Dulac map in the neighborhood of P3  with

•  The transition maps Ri, Rand R2  are given by ( 4.2.4), ( 4.2.5) and ( 4.2.6).

Therefore, for T,  we have

{
 f1 (v,  c)  = v,  (6.3.15)

T2(v,  c)  = no(v)  + O(m(v)) + m(v)  [(l1(v)n1(v) + O(m))ih  + O(y~)],

where

~  _ _ ]!.!!._  a3  (  )  (1-c)a3 [l + 0(  c  1-c) + O  (  1-c  (m141  1-c  -/3 ))) Y3  - a-
3 m141  v  v  v  , v  31  v,  v  , w  v  ,  1  ,
To  To

and 031  satisfies the same properties as of 01  in ( 5 .3 .11)

-..
For the transition map T,  we calculate it by the following decomposition

where
 134

•  8 2  :  T2  --t  II2  is  the second type of Dulac map in  the neighborhood of P2  with

•  8 1  :  II 1  --t E 2  is a regular transition map, which can be written as

where e1 (0)  > 0.

•  n- 1  :  E 2  --t E 4  is the Dulac map near the saddle point, which has the expression

(3.2.5).

•  82  :  E 4  --t II4  is a regular transition map, which can be written as

{
 821 (v,  y)  = v,

822(v,  y)  = bo(v)  + b1 (v)fj + O(fj2),

where b0 (0)  =  0 and b1 (0)  > 0.

•  Li4  :  II4  --t  E 4  are the first type of Dulac maps in the neighborhood of P4  with

Hence, for f, we have T1 (v,  c)  =  v.  Let

el (v)yo  - vc  -
Y- =  1Jcu1  [1 + B  (v  Ve  w(- -a ) + O(vu1c)]
u 1  21  '  '  '  1  ,
Po  Po

f}4  =  bo(v)  + b1(v)fjt  [1 + 'l/J1 (v, y)],

135

where 'ljJ1 ( v, y)  E  I0  and 821  satisfies the same properties as of 81  in ( 5 .3 .11 ).  Then the

......
second component of T  can be written as
 (6.3.16)

By (6.3.16), the first derivative ofT2 (v, c)  with respect to c is given as follows.

where '¢2 (v, y)  E  I0 , and 022  satisfies the same properties as of01  in (5.3.11) also

88 41  - 0  (  jj3  q3 (  v  {3  ) 1  v  ) --- - v  w  -,- 1  n- .
Oy4  Vo  Vo

Then
 ......  - 1
a2T2(v, c)  =  (~)u3 [1+0(vfi3wq3( ~' -!31) ln ~)]b1(v) (0-1 )2 (e1(v)yo) x
8c2  v 0  Vo  Vo  A  p~

1

v"f" [ 1 + /J23(v, vc, w( ~:, -a1) + O(v"'c) + ,P(v, Y)] (In v)2,

where 'lj;(v, y)  E  I0 . So \:/(v, c)  E  (0, c2 )  x  Iv  with c  sufficiently small,  82
~cC:,c) >  0,

i.e., T2(v,  c)  is convex.

By (6.3.15), the first derivative ofT2 (v, c)  with respect to c is given as follows.

&T
2
~~, c)  =  m(v)  [ (l1(v)n1(v) + O(m)) + 0(1)3)] :;, mfJ1 (v)v<t-c)i'3a3

[ 1 + O(vc, v1-c) + /J42(v, vl-c, w( r:~
41 v1-c, -,61))]  in v,

136

where () 42  satisfies the same properties as of B1  in ( 5 .3 .11 ).

82
T2(v  c)  [  ]  Yo  - (1  )- 2 ac
2 '  = -m(v)  (li(v)n1(v)  + O(m)) + O(y 3 )  rg
3 mrl1(v)v  -c a 3 a3

[ 1 + O(vc, vl-c, v(l-c)Ua)  + IJ43(v, vl-c, w( r:~41 vl-c, -,81))] (In v)2.

So V(v, c)  E  (0, c:2 )  x  Iv  with c sufficiently small,  82
~c~,c) < 0,  i.e., T2 (v,  c)  is concave.

Note that T2 (v,  c)  is convex and T2 (v,  c)  is concave, so \/(a,  P,)  E  A 0  x  V 80 ,  L 2 (v,  c)

has  at  most  two  small  roots  for  (v,  c)  E  (0, c:2 )  x  Iv  with  c  sufficiently  small,  i.e.,

Cycl(Ehh8c)  :::;  2.

6.4  The intermediate boundary graphic

Let r be any intermediate HH-graphic of elliptic type.  Similar to the  intermediate con-

cave graphics of saddle type, take sections 113 and114 defined (2.5.21) in the normal form

coordinates in  the neighborhood of P3  and P4  respectively.  We  will  study the displace-

mentmap
 L = R-T- 1
'

where R  : 113  ----+  114  is  the transition map along the regular orbit in  the normal form

coordinates,  and T  :  114  ----+  113  is  the  transition  map  passing through  the  blown-up

singularity.
 137

For the transition map R,  from proposition 4.3.1, we know that for v  > 0 sufficiently

small, any ith derivative of the second component of transition map R(v,  fh)  with respect

to y3  is close to zero.

To  study the transition map Ton the blown-up sphere,  let 'Tri  =  {Pi  =  p0 }(i = 3, 4)

be  the  two  line  sections  in  the  chart  F.  R.  on  r  =  0  parameterized  by  Yi(i  =  3, 4),

respectively.  Then we are reduced to study the one dimensional transition map

or its inverse

6.4.1  Family Ehhl

It has  been proved in  [53]  that T2 (0, y4 )  :  7r4  ---+  7r3  is  either the  identity or nonlinear

for y4 •  Since T 2 (0, y4 )  is analytic and bijective,  so T2 1(0, y3 )  :  7r3  ---+  7r4  is  either the

identity or nonlinear for y3 •  Thus for both cases, the intermediate graphics of the family

Ehh 1 have finite cyclicity.

6.4.2  Families Ehh2 and Ehh3

For family Ehhi  ( i  = 2, 3), we have a family of intermediate graphics Ehhib, Ehhic and

Ehhid as in Fig.  6.8 (a).  For the graphic (!Jb),  it was proved in [53] that Cycl(Ehhic)  ::;

138

Figure 6.7:  Transition maps for the intermediate graphics ofEhhl

1 and Cycl(Ehhid)  ::;;  2(i  =  2, 3).  For the graphic (Ji1b),  the transition near the addi-

tional attracting saddle-node behaves like a transition near P3  which does not influence

the proof of the finite cyclicity of graphics Ehhic and Ehhid ( i  = 2, 3).

To  study the cyclicity of the graphic Ehh2b, we study the transition map r 2- 1 (0, ih)

defined on 7r3  in the neighborhood of the graphic Ehh2c.

Let 71  =  {y  =  y0 }  and 73  =  { x =  x0 }  be two sections in  the neighborhood of the

saddle node.  Then the corresponding transition map r 2- 1  can be factorized as

where

r,,-1  .
.L  2  .
 139

(a)  Family Ehh2  (b)  Family Ehh3

Figure 6.8:  Transition maps for the intermediate graphics ofEhh2 and Ehh3

maps.

•  Do  : 73  ---t  Ti  is  the  stable-centre  transition  in  the  neighborhood of the  saddle

node in the normal form coordinates, and Vni, n 2  E N
 (6.4.17)

•  Di  : 7ri  ---t  Ti  is a Dulac map near the saddle point.

Note that Yi  = W2  o D 0  o Wi (0, y3 )  as the function of y3,  which satisfies the flatness

property (6.4.17),  for r2-i, we have  Jim r 2-i(o, y3)  = -oo.  Hence r2-i maps  (0, +oo)
y3-+0

to  ( -oo, +oo ).  Since T
2-i (0, j}J)  is  analytic and bijective,  it  has  to  be  nonlinear in  f}J,

140

therefore  it  is  nonlinear  for  y3  E  JR+,  thus  any  intermediate  graphic  Ehh2b  has  finite

cyclicity.

Since system X p=l  in (2.4.15) is invariant under the transformation
 (6.4.18)

The family Ehh3 can be obtained from the family Ehh2 by transformation (6.4.18).

Hence, For the graphics Ehh3b, we have T2 (0, y4 )  maps (0, +oo) to (-oo, +oo ), and

T2 (0, y4 )  is analytic,  bijective and nonlinear,  so r 2- 1(0, y3 )  exists and is nonlinear in y3 •

Therefore, any intermediate graphic Ehh3b has finite cyclicity.

6.4.3  Family Ehh4

For the family Ehh4b, the lower boundary graphic passes through a hyperbolic saddle, it

has the same structure as the family Sxhh 1 b of saddle type.  Therefore, any intermediate

graphic of Ehh4 has finite cyclicity.

6.4.4  Families Ehh5-Ehh8

We  first  consider family  Ehh5.  As  shown  in  Fig.  6.9  (a),  the  lower boundary  graphic

Ehh5c passes through two saddle points. One is at infinity, the other lies on the invariant

line fj  = 0.  We have a saddle connection.

In the normal form  coordinates ( x, y)  near the finite saddle, take sections f 1  = { x =

-x 0 }  and f 3  = {y = y0 }.  Let D 0  :  f 1  -----+  f 3  be the Dulac map, then the transition map

141

(a)  Ehh5b  (b)  Ehh6b

Figure 6.9:  Transition maps for the intermediate graphics ofEhh5 and Ehh6

T2  can be factorized as

It was  proved  in  [53]  that T2 (0, y4 ),  which  maps  (-oo, +oo)  to  (0, +oo ),  is  bijective,

analytic and nonlinear.  So r 2- 1 (0, y3 )  exists and should be nonlinear in y3 ,  therefore it is

nonlinear for y3  E  JR+.  Hence, any intermediate graphics Ehh5b have finite cyclicity.

For the family Ehh6b, it has a attracting saddle node on the lower boundary graphic.

By the  similar argument as  Ehh5b,  we  have r 2- 1(0, i/3)  is  nonlinear in  f)3.  Hence,  the

intermediate graphics Ehh6b have finite cyclicity.

The  family  Ehh7  and  Ehh8  can  be  obtained  from  the  family  Ehh5  and  Ehh6  by

the  transformation  (6.4.18)  on the  blown-up  sphere  {r  =  O},  respectively.  Therefore,

142

r 2- 1(0, 113)  exists  and  is  nonlinear in  ih  for  the  family  Ehh7b  and Ehh8b.  Hence,  any

intermediate graphic of Ehh7b and Ehh8b have finite  cyclicity.

Altogether, we finish  the proof of Theorem  6.1.1.

143

Bibliography

[1]  A.  Andronov, E. Leontovich, I. Gordon and A.  Maier, Theory ofBifurcations ofDy-

namical Systems  on a Plane, Israel Program for Scientific  Translations, Jerusalem,

1971.

[2]  N.  Bautin, On the number of limit cycles which appear with the variation of coeffi-

cients from an equilibrium position of focus or center type, Amer.  Math. Soc. Trans.  ·

100 (1954).

[3]  L.  Chen and M.  Wang,  The  relative position,  and the  number of limit cycles of a

quadratic differential system, Acta Math. Sinica 22 (1979) 751-758.

[4]  Z.  Denkowska  and R.  Roussarie, A  method of desingularizationfor analytic two-

dimensional vector fieldfamilies, Bol.  Soc.  Brasil. Mat. (N.S.)  22 (1991), 93-126.

[5]  F.  Dumortier, Singularities of vector fields on the plane,  J.  Differential Equations

23 (1977) 53-106.
 144

[ 6]  F.  Dumortier,  Singularities of Vector Fields,  Monografias de  Matematica [Mathe-

matical Monographs], 32. Instituto de Matematica Purae Aplicada, Rio de Janeiro,

1978.

[7]  F.  Dumortier,  Techniques  in  the  theory  of local  bifurcations:  blow-up,  normal

forms,  nilpotent bifurcations,  singular perturbations, Bifurcations and periodic or-

bits of vector fields  (Montreal,  1992).  19-73,  NATO  Adv.  Sci.  Inst.  Ser.  C  Math.

Phys. Sci., 408, Edited by Dana Schlomiuk. Kluwer Acad. Puhl., Dordrecht,  1993.

[8]  F.  Dumortier and  P.  Fiddelaers,  Quadratic  models for generic  local  3-parameter

bifurcations on the plane, Trans. Amer. Math. Soc. 326 (1991)  101-126.

· [9]  F.  Dumortier,  P.  Fiddelaers  and  C.  Li,  Generic  unfolding of the  nilpotent saddle

of codimension four,  Global  analysis of dynamical  systems,  131-166,  Inst.  Phys.,

Bristol, 2001.

[10]  F.  Dumortier,  A.  Guzman and  C.  Rousseau,  Finite  cyclicity of elementary graph-

ics surrounding a focus  or center  in quadratic systems,  Qualitative  Theory  Dyn.

System 3 (2002) 123-154.

[11]  F.  Dumortier,  Y.  Ilyashenko  and  C.  Rousseau,  Normal forms  near a saddle-node

and applications to finite cyclicity of graphics, Ergodic Theory Dynam. Systems 22

(2002) 783-818.
 145

[12]  F.  Dumortier,  M.  El  Morsalani  and  C.  Rousseau,  Hilbert's  16th  problem  for

quadratic  systems  and  cyclicity  of elementary  graphics,  Nonlinearity  9  (1996)

1209-1261.

[13]  F. Dumortier and C. Rousseau, Cubic Lienard equations with linear damping, Non-

linearity 3 (1990)  1015-1039.

[14]  F.  Dumortier,  R.  Roussarie  and  C.  Rousseau,  Elementary graphics of cyclicity  1

and 2, Nonlinearity 7 (1994)  1001-1043.

[ 15]  F.  Dumortier, R.  Roussarie and C.  Rousseau, Hilbert's 16th problem for quadratic

vector fields,  J. Differential Equations  110 (1994) 86-133.

[16]  F. Dumortier, R. Roussarie and S.  Sotomayor, Generic 3-parameter families of vec-

tor fields  in the plane,  unfolding a singularity with nilpotent linear part.  The  cusp

case, Ergod. Theory Dynam. Sys. 7 (1987) 375-413.

[17]  F. Dumortier, R. Roussarie and S. Sotomayor, Generic 3-parameter families of vec-

tor fields  in  the  plane,  unfoldings of saddle,  focus  and elliptic singularities with

nilpotent linear parts, Lecture Notes in Math., 1480, Springer-Verlag, Berlin,  1991.

[18]  F. Dumortier, R.  Roussarie and S.  Sotomayor, Bifurcations of cuspidal loops, Non-

linearity 10 (1997) 1369-1408.
 146

[19]  F.  Dumortier and C.  Rousseau, Study of the  cyclicity of some degenerate graphics

inside quadratic systems, Commun. Pure Appl. Anal. 8 (2009)  1133-1157.

[20]  J.  Ecalle,  Finitude  des  cycles  limites  et  acce/ero-sommation  de  I 'application  de

retour, 74-159, Lecture Notes in Math.,  1455, Springer, Berlin,  1990.

[21]  M.  El  Morsalani,  Perturbations  of graphics  with  semi-hyperbolic  singularities,

Bull. Sci. Math.  120 (1996) 337-366.

[22]  J. Francoise,and C. C., Pugh, Keeping track of limit cycles, J. Differential Equations

65  (1986)  139-157.

[23]  J.  Guckenheimer and P.  Holmes, Non-linear Oscillations, Dynamical Systems and

Bifurcation of Vector fields,  Appl. Math. Sci. 42, Springer-Verlag,  1983.

[24]  A. Guzman and C. Rousseau, Genericity conditions/or finite cyclicity of elementary

graphics, J.  Differential Equations 155 (1999) 44-72.

[25]  D.  Hilbert, Mathematische Problem (lecture):  The  Second International Congress

of Mathematicians,  Paris  1900.  Nachr.  Ges.  Wiss.  Gottingen  Math.-Phys.  Kl.

(1900), 253-297; Mathematical developments arising from Hilberts problems. Pro-

ceedings of Symposium in  Pure Mathematics F.  Brower Ed.,  28,  pp.50-51. Amer.

Math. Soc. Providence, RI,  1976.
 147

[26]  Y.  11 'yashenko,  Finiteness  theorems for  limit  cycles,  Russian  Math.  Surveys  45

(1990)  129-203.

[27]  Y.  11 'yashenko and S.  Yakovenko, Finite-smooth normal forms of local families of

diffeomorphisms and vector fields,  Russian Math. Surveys 46 (1991)  1-43.

[28]  Y.  11yashenko and S.  Yakovenko,  Concerning the  Hilbert sixteenth problem, Con-

cerning  the  Hilbert's  16th  problem,  1-19,  Amer.  Math.  Soc.  Transl.  Ser.  2,  165,

Amer. Math. Soc., Providence, RI,  1995.

[29]  Y.  11yashenko  and  S.  Yakovenko,  Finite  cyclicity  of elementary  polycycles  in

generic families,  Concerning the Hilbert's  16th problem. 21-95, Amer. Math.  Soc.

Transl. Ser. 2,  165, Amer. Math. Soc., Providence, RI,  1995.

[30]  Y.  11yashenko,  Centennial  history  of Hilbert's  16th problem,  Bull.  Amer.  Math.

Soc., 39 (2002) 301-354.

[31]  P.  Joyal and C.  Rousseau, Saddle quantities and applications, J. Differential Equa-

tions, 78 (1989) 374-389.

[32]  A.G.  Khovanskii,  Cycles  of dynamic  systems  on  a  plane  and Rolle 's  theorem,

Sibirsk. Mat. Zh. 25  (1984) 198-203.

148

[33]  A.  Kotova and  V.  Stanzo,  On few-parameter  generic families  of vector fields  on

the two-dimensional sphere.  Concerning the Hilbert 16th problem, 155-201, Amer.

Math. Soc. Transl. Ser. 2,  165, Amer. Math. Soc., Providence, RI,  1995.

[34]  E. Leontovich-Andronova, On the generation of limit cycle from separatrice, Dokl.

Acad. Nauka 78 (1951) 641-644.

[35]  J.  Li,  Hilbert's  16th problem  and bifurcations of planar polynomial vector fields,

lnternat. J.  Bifur. Chaos Appl. Sci. Engrg.  13  (2003) 47-106.

[36]  M.  Morsalani  and  A.  Mourtada,  Degenerate  and  non-trivial  hyperbolic  2-

polycycles:  two  independant Ecalle-Roussarie compensators and Khovanskii the-

ory, Nonlinearity 7 (1994) 1593-1604.

[3 7]  A.  Mourtada,  Cyclicite finie  des polycycles hyperboliques de  champs de  vecteurs

du plan:  mise  sous forme  normale,  Bifurcations of planar vector fields  (Luminy,

1989), 272-314, Lecture Notes in Math.,  1455, Springer, Berlin,  1990.

[38]  A. Mourtada, Degenerate and non-trivial hyperbolic polycycles with two  vertices,

J. Differential Equations 113 (1994) 68-83.

[39]  R.  Roussarie,  A  note  on finite  cyclicity  property  and  Hilbert's  16th  problem,

Dynamical  systems,  Valparaiso  1986,  161-168,  Lecture  Notes  in  Math.,  1331,

Springer, Berlin,  1988.
 149

[ 40]  R.  Roussarie, On the number of limit cycles which appear by perturbation of sepa-

ratrix loop of planar vector fields,  Bol. Soc. Brasil. Mat.  17 (1986) 67-101.

[41]  R.  Roussarie,  Cyclicite finie  des  lacets  et  des  points  cuspidaux,  Nonlinearity  2

(1989) 73-117.

[ 42]  R.  Roussarie,  Desingularization of unfoldings  of cuspidal  loops,  Geometry  and

analysis in nonlinear dynamics (Groningen, 1989), 41-55, Pitman Res. Notes Math.

Ser., 222, Longman Sci. Tech., Harlow,  1992.

[43]  R. Roussarie, Bifurcations of Planar Vector Fields and Hilbert's Sixteenth Problem,

Progress in Mathematics,  164. Birkhauser Verlag, Basel,  1998.

[ 44]  R. Roussarie and C. Rousseau, Finite cyclicity of nilpotent graphics of pp-type sur-

rounding a center, Bull. Belg. Math. Soc. Simon Stevin 15 (2008), no. 5, Dynamics

in perturbations, 889-920.

[ 45]  C.  Rousseau, Normal forms,  bifurcations and finiteness properties of vector fields.

Normal forms,  bifurcations and finiteness  problems in differential equations, 431-

470, NATO  Sci.  Ser.  II Math.  Phys.  Chem.,  137,  Kluwer Acad.  Puhl.,  Dordrecht,

2004.
 150

[46]  C.  Rousseau  and  H.  Zhu.  PP-graphics  with  a  nilpotent  elliptic  singularity  in

quadratic system and Hilbert's 16th problem, J.  Differential Equations 196 (2004)

169-208.

[47]  S.  Shi, A concrete example of the existence of four limit cycles/or plane quadratic

system, Scientia Sinica 23  (1980)  154- 158.

[ 48]  S.  Sternberg,  On  the  structure of local homeomorphisms of euclidean n-space.  II,

Amer. J.  Math. 80 (1958) 623-631.

[ 49]  F.  Takens,  Unfoldings  of certain singularities of vector fields:  generalized Hopf

bifurcations, 1. Differential Equations 14 (1973) 476-493.

[50]  Y.  Ye,  S.  Cai, L. Chen, K. Huang, D. Luo, Z.  Ma, E. Wang, M. Wang and X. Yang,

Theory of Limit Cycles,  Translated from the Chinese by Chi Y.  Lo. Second edition.

Translations  of Mathematical  Monographs,  66.  American  Mathematical  Society,

Providence, R.I.,  1986. xi+435 pp.

[ 51]  Z. Zhang, T. Ding, W. Huang and Z. Dong, Qualitative Theory of Differential Equa-

tions, Translated from the Chinese by Anthony Wing Kwok Leung. Translations of

Mathematical Monographs,  101. American Mathematical Society, Providence, RI,

1992. xiv+461  pp.
 151

[52]  H. Zhu, Finite cyclicity of graphics with a nilpotent singularity of saddle or elliptic

type,  PhD thesis, Universite de Montreal,  1999.

[53]  H. Zhu and C.  Rousseau, Finite cyclicity of graphics with a nilpotent singularity of

saddle or elliptic type, J. Differential Equations 178 (2002) 325-436.

152
