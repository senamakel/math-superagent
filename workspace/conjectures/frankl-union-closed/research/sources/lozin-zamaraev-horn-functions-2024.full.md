<!-- source: https://wrap.warwick.ac.uk/id/eprint/180696/1/1-s2.0-S0097316523000869-main.pdf | converted from PDF -->

Journal of Combinatorial Theory, Series A 202 (2024) 105818

Contents lists available at ScienceDirect

Journal  of  Combinatorial  Theory,
Series  A

journal homepage:  www.elsevier.com/locate/jcta

Union-closed  sets  and  Horn  Boolean  functions

Vadim Lozin a,∗, Viktor Zamaraev b

a Mathematics Institute, University of Warwick, Coventry, CV4 7AL, UK
b Department of Computer Science, University of Liverpool, Ashton Street,
Liverpool, L69 3BX, UK

a  r  t  i  c  l  e  i  n  f  o a  b  s  t  r  a  c  t

Article history:
Received 1 April 2023
Received in revised form 15 August
2023
Accepted 15 September 2023
Available online xxxx

Keywords:
Union-closed sets
Horn Boolean function
Submodular function
 A family F of sets is union-closed if the union of any two sets
from F belongs to F . The union-closed sets conjecture states
that if F is a ﬁnite union-closed family of ﬁnite sets, then there
is an element that belongs to at least half of the sets in F .
The conjecture has several equivalent formulations in terms
of other combinatorial structures such as lattices and graphs.
In its whole generality the conjecture remains wide open, but
it was veriﬁed for various important classes of lattices, such
as  lower  semimodular  lattices,  and  graphs,  such  as  chordal
bipartite graphs. In the present paper we develop a Boolean
approach to the conjecture and verify it for several classes of
Boolean functions, such as submodular functions and double
Horn functions.
© 2023 The Author(s). Published by Elsevier Inc. This is an
open access article under the CC BY license (http://
creativecommons .org /licenses /by /4 .0/).

1.  Introduction

Let U be a ﬁnite set (the universe) and F⊆ 2
U a set system, i.e. a family of subsets
of U . F is union-closed if for any two sets A, B ∈F the union A ∪ B belongs to F. The

* Corresponding author.
E-mail addresses: V.Lozin@warwick.ac.uk (V. Lozin), Viktor.Zamaraev@liverpool.ac.uk
(V. Zamaraev).

https://doi.org/10.1016/j.jcta.2023.105818
0097-3165/© 2023 The Author(s).  Published by Elsevier Inc.  This is an open access article under the CC
BY license (http://creativecommons .org /licenses /by /4 .0/).

2 V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818

following conjecture is known as union-closed sets conjecture and sometimes is referred
to as Frankl’s conjecture.

Conjecture 1. Any ﬁnite union-closed family F ̸= {∅} of ﬁnite sets contains an element
that belongs to at least half of the sets in the family.

For an equivalent formulation, let us say that F is intersection-closed if for any two
sets A, B ∈F the intersection A ∩B belongs to F. Also, assume without loss of generality
that every element of the universe appears in at least one set of F. Then F is intersection-
closed if and only if the family {U −A  : A ∈F} is union-closed. Therefore, Conjecture 1
admits the following equivalent formulation.

Conjecture 2. Any ﬁnite intersection-closed family of at least two ﬁnite sets contains an
element that belongs to at most half of the sets in the family.

The  conjecture  admits  various  other  equivalent  formulations,  in  particular,  in  the
language of lattice theory [8]and in the terminology of graph theory [2].
In spite of its simple formulation, the conjecture is wide open and was veriﬁed only
for  some  special  classes  of  sets,  lattices  or  graphs.  In  the  present  paper,  we  develop  a
Boolean approach to the conjecture and verify it for several classes of Boolean functions,
such as submodular functions and double Horn functions.

2.  Horn Boolean functions

Let F be an intersection-closed family over the universe U = {x1, x2, ..., xn}, and let
A ∈F be a member-set of F, i.e. a subset of U that belongs to F. We represent A by its
characteristic vector cA, i.e. a 0-1 vector of length n in which the i-th coordinate equals
1if and only if xi ∈ A. This allows us to interpret F as a Boolean function over variables
{x1, x2, ..., xn} whose false points are precisely the member-sets of F. According to the
following theorem proved in [7](also see [3]) this is a Horn function.

Theorem 1. A Boolean function is Horn if and only if the set of its false points is closed
under conjunction.

We denote the set of false points of a Horn Boolean function f by F = F (f ). Adapting
set  theory  terminology,  we  will  say  that  a  variable  xi belongs  to  a  Boolean  point  X ∈
{0, 1}n if it appears in X with xi =1, i.e. if the i-th coordinate of X equals 1. Therefore,
in the terminology of Boolean functions Frankl’s conjecture can be restated as follows:
any Horn Boolean function with at least two false points contains a variable that belongs
to at most half of the false points of the function.
We  denote  the  set  of  true  points  of  a  Horn  Boolean  function  f by  T = T (f )and
associate with T one more set system, denoted T , over the same universe U , such that
a set A ⊆ U belongs to T if and only if the characteristic vector cA belongs to T .

V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818 3

We observe that a variable belongs to at most half of the false points if and only if it
belongs to at least half of the true points of the function, which suggests that the relation
between F and T is similar to the relation between intersection-closed and union-closed
families. However, in general T is neither intersection-closed nor union-closed.
In  the  terminology  of  set  systems,  an  element  that  appears  in  at  least  half  of  the
member-sets is known as abundant and an element that appears in at most half of the
member-sets  is  known  as  rare.  In  the  terminology  of  Boolean  functions,  every  variable
that is abundant for true points is rare for false points, and vice versa. In our study of
Boolean functions we will frequently switch between the two roles of the same variable.
To  avoid  any  ambiguities,  we  will  call  such  a  variable  good,  i.e.  a  variable  is  good  if  it
belongs to at most half of the false points, or equivalently, if it belongs to at least half of
the true points of the function. In this terminology Frankl’s conjecture can be restated
as follows.

Conjecture 3. Any Horn Boolean function with at least two false points contains a good
variable.

We  will  say  that  a  Horn  Boolean  function  satisﬁes  Frankl’s  conjecture  if  it  satisﬁes
Conjecture 3.
Up to now, we just translated Frankl’s conjecture to a diﬀerent language, but we did
not discuss the advantage of this translation. In addition to possibility of playing simulta-
neously with two set systems in the search for a good element (variable), the importance
of Boolean formulation is that Horn functions admit a very speciﬁc disjunctive normal
form (DNF) representation. By deﬁnition, a Boolean function is a Horn function if it can
be represented by a DNF in which every term contains at most one negated literal. We
use this representation in order to verify Conjecture 3 for some special classes of Horn
functions  in  Sections 4 and 5.  All  preliminary  information  can  be  found  in  Section 3.
Section 6 concludes the paper with open problems.

3.  Preliminaries

In this section, we ﬁx terminology and notation and prove some preliminary results.
Given  a  Boolean  function  f and  a  variable  x,  we  denote  by  f|x=0 and  f|x=1 the
restriction of f to x =0 and to x =1, respectively, i.e. these are the functions obtained
from f by restricting it to the sets of Boolean points with x =0 and x =1, respectively.
With  this  notation,  good  variables  can  be  characterized  as  follows:  a  variable  x of  a
function f is good

•if the number of true points of f|x=0 does not exceed the number of true points of
f|x=1, or equivalently,
•if the number of false points of f|x=1 does not exceed the number of false points of
f|x=0, or equivalently,

4 V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818

•if there is an injective mapping from the set of true points of f|x=0 to the set of true
points of f|x=1, or equivalently,
•if there is an injective mapping from the set of false points of f|x=1 to the set of false
points of f|x=0.

A literal is either a Boolean variable or its negation. We will refer to literals as positive
or negative depending on whether they are unnegated or negated, respectively.
A term is a conjunction (product) of literals. Any variable that does not appear as a
literal in a term t, neither positively nor negatively, will be called a free variable for t.
A term is linear if it consists of one literal, and quadratic if it consists of two literals.
A term is Horn if it contains at most one negated literal, and pure  Horn if it contains
exactly one negated literal.
We will say that a term t covers a Boolean point X if t(X) =1, i.e. t evaluates to 1
at X. A term t is an implicant of a Boolean function f if every point covered by t is a
true point of f . Also, t is a prime implicant of f if no proper subset of literals of t is an
implicant of f .
A DNF is a disjunction of terms. A DNF is Horn if each of its terms is Horn, and it is
pure Horn if each of its terms is pure Horn. A Horn function is a Boolean function that
admits  a  Horn  DNF  representation.  A  pure  Horn  function is  a  Boolean  function  that
admits a pure Horn DNF representation. It is not diﬃcult to see that a Horn function f
is pure Horn if and only if f (1, 1, ..., 1) =0. If f is not pure Horn, then by changing its
value at the point (1, 1, ..., 1) from 1to 0we obtain a pure Horn function f ′ such that
if f ′ has a good variable, then so does f . Therefore, Conjecture 3 is valid if and only if
it is valid for pure Horn functions.
We now translate to the language of Boolean functions some facts that are known in
non-Boolean terminology (see e.g. [1]).

Lemma 1. If Conjecture 3 holds for Horn functions without linear prime implicants, then
it holds for all Horn functions.

Proof. If  a  Horn  function  f has  a  linear  prime  implicant  x,  then  x is  a  good  variable,
because f|x=1 ≡ 1and hence x does not belong to any false point. If f has a linear prime
implicant  x,  then  f|x=0 ≡ 1and  x belongs  to  every  false  point.  In  this  case,  f can  be
restricted to f|x=1, and a good variable for the function f|x=1 is also good for f . 

Lemma 2. Let  f be  a  Horn  function  represented  by  a  Horn  DNF  Df .  If  a  variable  x of
f does not appear in Df negatively, then x is a good variable for f .

Proof. If the function f|x=0 does not have true points, then the number of false points
of f containing x cannot be larger than the number of false points that do not contain
x, and hence x is a good variable for f .
Now let X be a true point of f with x =0, and let t be a term of Df with t(X) =1.
Then t does not contain x, since x does not appear in Df negatively. Therefore, for the

V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818 5

point X ′ obtained from X by changing x to 1, we have t(X ′) =1. This establishes an
injective  mapping  φ  : X → X ′ from  the  set  of  true  points  of  f|x=0 to  the  set  of  true
points of f|x=1, and shows that x is good. 

Lemmas 1 and 2 allow  us  to  restrict  ourselves  to  Horn  functions  that  have  no  lin-
ear prime implicants and in which every variable appears negatively in all Horn DNFs
representing f . We call such functions non-trivial.

The  book  [3] distinguishes  four  special  classes  of  Horn  functions:  submodular  func-
tions, bidual Horn functions, double Horn functions and acyclic Horn functions.
For the acyclic Horn functions, the validity of Conjecture 3 follows directly from the
deﬁnition with the help of Lemma 2. To deﬁne this notion, let us associate with a pure
Horn  DNF  φ representing  a  function  f of  n variables  x1, ..., xn a  directed  graph  Gφ,
the  implicant  graph, with vertex set {x1, ..., xn} containing an arc (xi, xj) whenever φ
contains a term involving both xi and xj. A pure Horn function is called acyclic if Gφ
is acyclic. Since any acyclic graph contains a sink vertex, i.e. a vertex with no out-going
arcs, we conclude with the help of Lemma 2 that every acyclic Horn function contains a
good variable.
For  submodular  functions  and  double  Horn  (and  more  general)  functions,  we  verify
Conjecture 3 in Sections 4 and 5, respectively. For bidual Horn functions the conjecture
remains open and we discuss it in Section 6.

4.  Submodular functions

In this section we study a subclass of Horn functions known as submodular.

Deﬁnition 1. A function f (X)is called submodular if f (X ∨Y ) ∨f (X ∧Y ) ≤ f (X) ∨f (Y ).

To reveal a relationship between submodular functions and Horn functions, let us say
that a Boolean function f (x1, ..., xn)is co-Horn if the function f (x1, ..., xn)is Horn.
The following characterization of submodular functions was proved in [6].

Theorem 2. A Boolean function is submodular if and only if it is both Horn and co-Horn.
All prime implicants of a submodular function are either linear or quadratic pure Horn.

Theorem 3. Submodular Boolean functions satisfy Frankl’s conjecture.

Proof. Let  f (x1, x2, ..., xn)be  a  submodular  function.  Without  loss  of  generality  we
assume  that  f is  non-trivial  and  that  Df is  a  DNF  representation  of  f in  which  every
term is quadratic pure Horn.
Let  Gf be  the  implicant  graph  associated  with  Df .  Given  a  Boolean  point  X =
(α1, ..., αn), we denote by Gf (X)a labelled graph obtained from Gf by assigning label
αi to vertex xi for each i. It is not diﬃcult to see that

6 V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818

(∗) X is a true point of f if and only if there is an arc (or equivalently, a directed path)
in Gf (X)from a 0-vertex (i.e. a vertex labelled 0) to a 1-vertex.

Now  we  contract  each  strongly  connected  component  of  Gf into  a  single  vertex  ob-
taining  in  this  way  a  directed  acyclic  graph  G∗
f .  By  Theorem 2,  this  graph  represents
a new submodular function f ∗ with a DNF Df ∗ whose terms correspond to the arcs of
G∗
f .
For a vertex x of Gf we denote by cx the strongly connected component of the graph
containing x. Note that cx is a subset of V (Gf ), as well as a vertex of G∗
f and a variable
of f ∗.
If  X is  a  false  point  of  f ,  then,  according  to  (∗),  within  each  strongly  connected
component of Gf (X)either all vertices are labelled 0or all vertices are labelled 1. This
can be viewed as a 0-1 labelling of the vertices of G∗
f , and we denote a labelled graph G∗
f
corresponding to a false point X of f by G∗
f (X). Also, since X is false, there is no directed
path from a 0-vertex to a 1-vertex in G∗
f (X), since otherwise such a path could be found
in Gf (X). Therefore, the 0-1 labelling of the vertices of G∗
f corresponding to a false point
of f deﬁnes a false point of the function f ∗. Similarly, a false point of f ∗ corresponds to a
false point of f . It is not diﬃcult to see that this is a one-to-one correspondence, showing
that  |F (f )| = |F (f ∗)|.  Moreover,  for  any  variable  x of  f ,  |F (f|x=0)| = |F (f ∗
|cx=0)| and
|F (f|x=1)| = |F (f ∗
|cx=1)| in view of the above discussion.
Since G∗
f is acyclic, it contains sink vertices, i.e. vertices with no out-going arcs. Sink
variables  do  not  appear  in  Df ∗ negatively  and  hence,  by  Lemma 2,  each  of  them  is  a
good variable of f ∗.
Let x be a vertex of Gf such that cx is a sink vertex of G∗
f . Since cx is a good variable
of f ∗, we have |F (f ∗
|cx=1)| ≤|F (f ∗
|cx=0)|. Therefore,

|F (f|x=1)| = |F (f ∗
|cx=1)|≤|F (f ∗
|cx=0)| = |F (f|x=0)|

and hence x is a good variable. 

5.  Double Horn and more general functions

A Boolean function f is double Horn if both f and f are Horn. According to [4], double
Horn functions admit a DNF representation where each variable appears negatively at
most once. We will show that any such Horn function satisﬁes Frankl’s conjecture. More
generally,  we  will  verify  the  conjecture  for  Horn  Boolean  functions  that  admit  a  Horn
DNF  satisfying  the  following  property,  which  we  call  dependency:  for  each  variable  x
there  is  a  variable  d(x)such  that  d(x) appears  (positively)  in  every  term  containing
x negatively. Clearly, any non-trivial Horn DNF containing each variable negatively at
most once satisﬁes the dependency property.

Theorem 4. Let  f be  a  non-trivial  Boolean  function  that  admits  a  Horn  DNF  D = Df
satisfying the dependency property. Then Frankl’s conjecture is valid for f .

V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818 7

Proof. Each true point of f is covered by at least one term in D. To prove the theorem,
we  construct  a  binary  matrix  M with  n rows  corresponding  to  the  variables  of  f and
|T (f )| columns representing the true points of f . A good variable (if exists) corresponds
to a row of the matrix containing at least as many 1s as 0s. To prove that such a variable
exists, we will show that the entire matrix M contains at least as many 1s as 0s. To this
end,  we  will  map  the  set  of  0s  of  M injectively  to  the  set  of  1s  of  M according  to  the
following procedure. Consider a 0in M and denote it by z. Also, we denote by i the row
containing z and by X the column containing z. In other words, X is a true point with
a zero in the i-th coordinate.

(a) If the true point X is covered by a term t of D for which xi is free, then the point
X ′ obtained by switching the i-th coordinate to a 1also is a true point covered by
t and we map the zero z to the 1in X ′ in the same row (coordinate). We call it a
horizontal map.
(b) If  X is  not  covered  by  any  term  of  D for  which  xi is  free,  then  it  is  covered  by
some term t containing xi negatively. According to the dependency property, t also
contains  (positively)  the  variable  xj = d(xi),  i.e.  the  j-th  coordinate  of  X is  a  1,
in which case we map the zero z to the 1in the j-th coordinate of X. We call it a
vertical map (mapping a 0to a 1in the same column).

It remains to show that the mapping described above is injective. It is not diﬃcult to
see that no two horizontal maps send two diﬀerent 0s to the same 1. The same is true
for  any  two  vertical  maps.  Indeed,  when  we  apply  a  vertical  map  to  a  zero  in  column
X, this zero represents a negative literal xi in some term t. Any other zero in the same
column corresponds to a variable xj which is free for t, since otherwise either X is not
a true point (if xj appears in t positively) or D is not a Horn DNF (if xj appears in t
negatively). Therefore, when we apply a vertical map to a zero in column X, all other
zeros in the same column are mapped horizontally.
Now assume that a vertical map sends a zero z1 to a 1, denote it by u, and a horizontal
map sends a zero z2 to the same u. We denote the row containing z1 by i and the column
containing z1 (and u) by X1. Also, let j be the row containing z2 (and u) and let X2 be
the  column  containing  z2.  Finally,  let  t1 be  a  term  covering  X1,  as  in  the  deﬁnition  of
the vertical map applied to z1, and let t2 be a term covering X2, as in the deﬁnition of
the horizontal map applied to z2.
According to the deﬁnition of the horizontal map, X1 and X2 diﬀer only in the j-th
coordinate, and xj is free for t2, i.e. t2 also covers X1. Also, according to the deﬁnition
of the vertical map, xi appears in t1 negatively, and xj = d(xi) appears in t1 positively.
Since t2 does not contain xj, and t1 contains xj, the two terms t1 and t2 are diﬀerent.
We  know  that  t2 contains  xi,  since  otherwise  we  had  to  apply  a  horizontal  map  to
z1. Moreover, t2 contains xi negatively, because the i-th coordinate of both X1 and X2
is zero. But then, by the dependency property, t2 also contains (positively) xj, which is

8 V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818

not possible, since the j-th coordinate of X2 is zero, and t2 covers X2. This contradiction
completes the proof. 

6.  Concluding remarks and open problems

According to [1], one of the major obstacles for proving the conjecture is that we do
not  know  where  to  expect  a  good  element.  Theorem 3 suggests  that  such  an  element
should be expected in a strongly connected component C of the implicant graph, which
becomes a sink vertex after contracting each strongly connected component to a single
vertex. Theorem 4, on the other hand, suggests a possible way of proving the existence
of  a  good  element  in  C by  showing  that  the  matrix  M of  true  points  restricted  to  the
elements of C contains at least as many 1s as 0s.
Taking  into  account  the  special  role  of  duality  in  this  topic,  the  next  natural  step
towards proving the conjecture via a Boolean approach is to consider the class of bidual
Horn  functions  studied  in  [5].  These  are  Horn  functions  f such  that  the  dual  of  f is
also  Horn,  where  the  dual  of  f is  the  function  f d such  that  f d(X)  = f (X)for  all
Boolean points X. We believe that this is the core step towards proving the conjecture.
Even  more  speciﬁcally,  we  believe  that  the  class  of  self-dual  Horn  functions,  i.e.  Horn
functions f such that f = f d, which forms a proper subclass of bidual functions, is a key
to cracking the conjecture. These are functions where an instance of the problem comes
simultaneously in both forms: intersection-closed (over the false points) and union-closed
(over the true points). Proving the conjecture for self-dual Horn functions seems to be a
challenging problem.

Declaration of competing interest

We wish to conﬁrm that there are no known conﬂicts of interest associated with this
publication.

Data availability

No data was used for the research described in the article.

Acknowledgment

The authors are grateful to referees for valuable comments.

References

[1] H.  Bruhn,  O.  Schaudt,  The  journey  of  the  union-closed  sets  conjecture,  Graphs  Comb.  31  (2015)
2043–2074.
[2] H. Bruhn, P. Charbit, O. Schaudt, J.A. Telle, The graph formulation of the union-closed sets con-
jecture, Eur. J. Comb. 43 (2015) 210–219.

V. Lozin, V. Zamaraev / Journal of Combinatorial Theory, Series A 202 (2024) 105818 9

[3] Yves Crama, Peter L. Hammer, Boolean Functions: Theory, Algorithms, and Applications, Cambridge
University Press, 2011.
[4] T. Eiter, T. Ibaraki, K. Makino, Double Horn functions, Inf. Comput. 144 (2) (1998) 155–190.
[5] T. Eiter, T. Ibaraki, K. Makino, Bidual Horn functions and extensions, Discrete Appl. Math. 96/97
(1999) 55–88.
[6] O. Ekin, P.L. Hammer, N.U. Peled, Horn functions and submodular Boolean functions, Theor. Com-
put. Sci. 175 (1997) 257–270.
[7] J.C.C. McKinsey, The decision problem for some classes for sentences without quantiﬁers, J. Symb.
Log. 8 (1943) 61–76.
[8] J. Reinhold, Frankl’s conjecture is true for lower semimodular lattices, Graphs Comb. 16 (1) (2000)
115–116.
