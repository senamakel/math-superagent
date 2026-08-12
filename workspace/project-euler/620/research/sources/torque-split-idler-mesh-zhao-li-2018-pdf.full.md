<!-- source: https://www.jstage.jst.go.jp/article/jamdsm/12/7/12_2018jamdsm0127/_pdf/-char/en | converted from PDF -->

Bulletin of the JSME
Journal of Advanced Mechanical Design, Systems, and Manufacturing

Vol.12, No.7, 2018

Paper No.18-00320 © 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

A general  mathematical  design method of the  torque - split  gear
transmission with idler pinion

Abstract
The  torque - split  gear  transmission  has  been  used  in  the  transmission  system  of  the  rotorcraft,  which
undertaking  high  torque  loads  and  requiring  low  weight.  A  u niversal  mathematical  design  method  of  the
torque - split gear transmission is proposed in this work. The teeth with the same phase of the two gears on the
duplex  idler  are  marked.  And  the  meshing  condition  is  defined  by  the  whole  pitch  number  between  the  tw o
points  along  the  pitch  circle  of  the  output  gear.  Then  the  relationship  between  the  tooth  number  and  gear
positions  is  established  by  using  this  meshing  condition.  Unlike  other  existing  design  method,  this  method
involves  the idlers, input gear  and output gear  that engaged directly, and it is suitable for the design of multiple
types  of  torque - split  gear  transmission.  This  method  is  validated  through  numerical  examples  of  the
torque - split  transmission  with  symmetrical  duplex  idler.  Moreover,  practical  applicatio ns  of  the  torque - split
transmission  with  planetary  duplex  idler,  coplanar  gear  and  concentric  face  gear  are  also  studied  with  this
method. A large number of discrete gear position solutions are observed under the same tooth number design.
And different gea r positions correspond to different dynamic and load sharing characteristics of the torque - split
gear transmission.

Keywords  : Torque - split, Design, Transmission, Duplex idler, Meshing condition

1. Introduction
The  torque - split  gear  transmission  is  mainly  used  in  the  transmission  system  of  the  rotorcraft  ( Filler  et  al.  and
Heath et al. , 20 02 , 201 1 ) , which uses turbines that rotate at a high speed to drive the main rotor that rotates at a lower
speed.  The  unique  characteristic  of  this  application  area  is  transmitting  high  torque  through  the  lowest  weight.  The
torque - split gear transmission divides the input torque into several paths, resulting in the reduction of the contact force
on  gear  teeth,  which  means  smalle r  gears  can  be  used.  The  torque - split  gear  transmission  has  the  advantages  of
compact structure, high power density and large reduction ratio, which are the main demands of the rotorcraft.
Various  types  of  the  torque - split  gear  transmission  are  patented  ( Y uriy,  Todd  et  al.  and  Xiaolan  Ai  et  al.,  2016,
2014a, 2014b) . And  extensive researches  have  focused on the  studies of design, dynamic a nd load  sharing behavior.
White   (1989)   is  one  of  the  first  persons  to  have  studied  the  torque - split  gear  transmission,  an d  he  has  explored  the
advantages of the torque - split gear transmission over the traditional design. The studied topics on the dynamics of the
torque - split  transmission  include  dynamic  model,  natural  frequencies  and  dynamic  response  (Reszuta  et  al.  and
Aydo ğan et al., 2015, 2017). Moreover, because of the asymmetry of the machining and installation errors of each path
of the torque - split gear transmission, the torque of each path is uneven. Gmirya  (2011)  developed an elastic component
load sharing method. An d the dynamic load sharing characteristic studies include the works in  ( Filler  et al. , Mo et al.
and Fu  Ai et al., 2002, 2015a, 2015b) . Its application on the rotorcraft has also received attention  ( Gmirya  and Jose et
al., 2018, 2010) .
The  simultaneous  me shing  design  of  the  torque - split  gear  transmission  has  great  influence  on  the  reliability  and
comfort of the rotorcraft. However, the simultaneous meshing problem, which is quite common in the field of position
analysis of gear mechanisms, has not yet been  fully studied with a universal mathematical design method. Vilán  et al.
(2010)   and  Abraham  et  al.  (2012)   have  studied  the  torque - split  transmission  with  gears  in  the  same  plane  (namely
coplanar gears). They defined the area formed by four coplanar gears,  shown in Fig. 1, as a curvilinear quadrilateral.
And a pitch difference is also defined by the sum pitches in the output and input gears minus the sum of pitches in the

1
 Ning ZHAO* and Wang LI*

*School of Mechanical Engineering, Northwestern Polytechnical University
127 West Youyi Road Xi'an Shaanxi, 710072, China
E-mail: lw201906@126.com

Received: 3 July 2018; Revised: 30 October 2018; Accepted: 28 November 2018
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

idler gears at the curvilinear quadrilateral. The meshing condition is satisfied when t he pitch difference coincident with
a whole number. This meshing condition is effective in the design of the configuration with four coplanar gears. While
for  the  torque - split  transmission  with  duplex  idler,  the  curvilinear  quadrilateral,  which  is  the  basi s  of  the  meshing
condition, is unclosed. Different investigations in terms of the torque - split transmission with duplex idler are done by
Li Zhijun  et al. (2012) and Xiangya  et al. (2014) . Their methods are complex and have the possibility of unsolvable.

0.4m

1m
0.4m

0.3m

0.3m
 0.7m

0.7m

1m 1m
 1m 1m

1m

1m1m
1m

1m

1m
 Pinion

Gear
 IdlerIdler

Fig . 1 The mesh ing condition proposed by Vilán  and Abraham.

In  this  paper,  take  the  compatibility  of  geometrical  space  and  simultaneous  meshing  of  gears  into  account,  a
universal mathematical design method is developed. With this method, the torque - split transmission with duplex idler is
studied numerically in two  cases: the external meshing duplex idler and the internal meshing duplex idler. In each case,
solutions for the simultaneous meshing problem of the torque - split gear transmission with symmetrical duplex idler are
calculated. Other types of the torque - split  gear transmission (planetary duplex idler, coplanar gear and concentric face
gear) are also calculated. Applying this universal design method, the meshing phrasing difference between paths, which
affects  the  dynamics  and  load  sharing  behavior  of  the  trans mission  system,  can  be  studied  by  adjusting  the  integral
pitch number of the pinion contained in the closed area that formed by gears.

2. The Meshing Problem
The torque - split transmission with duplex idler is shown in Fig. 2. This transmission system divi des the input torque
of pinion into several paths. The transmission of force is divided between several contact areas, thereby an increase of
available torque. However, this also gives rise to the problem of simultaneous meshing of the gears that engaged.

 Fig. 2 The torque - split transmission with duplex idler.

The input pinion 1 meshes with gears 2 and 4 respectively, and output gear 6 meshes with gears 3 and 5. The two
paths  are  not  independent  of  each  other  when  transmitting  torque  and  movement,  and  redundant  constraints  are
introduced.  The  existence  of  the  redundant  constraints  bring  difficulties  to  the  design  of  the  torque - split  gear
transmission. In order to ensure continuous  transmission of torque and movement, the simultaneous meshing problem
of gears needs to be studied.

3. The Universal Mathematical Design Method
The  gears  discussed  here  refer  to  standard  spur  gears.  Since  the  problem  discussed  is  mainly  about  the  meshing

2

2
 3 4
5

6
 1

 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

phase and geometric compatibility, so the method is still applicable for the standard helical gears. But for nonstandard
gears with modified addendum are excluded from this work.  In the application of the rotorcraft, the two duplex idlers
(Fig.  3 ) are symmetrically arranged with respect to the centerline  of the input and output gear s. Considering the cost of
manufacture  and  maintenance,  the  two  duplex  idlers  should  be  interchangeable   (Li  Zhijun  et  al.  2012) .  T he  phase
between  the  two  marked  idler’s  teeth  on  a  duplex  shaft  can  be  defined  as  location  phase .  Based  on  the
interchangeability requirement , the location phase  of the two duplex idlers should be the same . If the location phase of
one duplex idler is settled, the location phase of the other duplex id ler is also settled. This brings redundant constraints
when  the two duplex idlers  meshing  with the  input and output  gears  simultaneously. For analytical convenience,  the
location phase  is defined as zero.  To obtain a general mathematical design method,  the location phase  of the general
case shown in Fig. 2 is still defined as zero.

Fig.  3  The torque - split gear transmission used in the rotorcraft .

The starting line of gear teeth is defined in Fig.  4 . It is a line through the middle point of the addendum of gear tooth
and gear center (Fig.  4 (a)). From the top view (Fig.  4 (b)) of the duplex idler, the starting lines of the two gears on the
same duplex shaft coincide.

 Fig.  4  The starting line of gear teeth from the view of (a) and (b).

The  universal  mathematical  design  method  is  derived  from  the  general  configuration  of  the  torque - split
transmission  with  duplex  idler.  And  it  is  studied  in  two  cases:  the  external  meshing  duplex  idler  and  the  internal
meshing duplex idler.

3.1 Case 1 ：The External Meshing Duplex idler
The proper meshing condition of the torque - split transmission with duplex  idler is illustrated as follows:
The general configuration of  the  external  meshing duplex idler is  shown in  Fig.  4 , the layout angles of  gears are
defined  by

1 2 3,,
   and

4
 .  Gears  2(4)  and  3(5)  are  connected  by  the  duplex  shaft.  The  two  paths  have  the  same
definition of the starting line of the gear teeth.
In order to explain the  meshing condition (Fig.  5 ), part of the  gear teeth are represented by pitch circle.  And the
points on which the gear teeth have the same meshing position are marked with yellow dots. As two gears can mesh
with the same gear correctly at any positions along the pitch circle, so it  is well to assume that the pinion 1 has meshed
properly with gears 2 and 4. The gear teeth on the points F and H mesh with the teeth on points E and G at the same
meshing position. To ensure the correct meshing of gears 3(5) and 6, the pitch number between  the two points (F and
H) along the pitch circle of gear 6 must coincident with a whole number. By this meshing condition, the relationship

3

(a)                                                                    (b)
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

between  the  tooth  number  and  gear  positions  is  defined.  If  this  relationship  is  not  satisfied,  the  teeth  of  gears  wi ll
interfere with each other.

 Fig.  5  The torque - split transmission with the external meshing duplex idler.

In general, the three gears 1, 2 and 4 can mesh properly without considering gear 6.  Assuming that gears 3 , 5  and 6
also have been adjusted to the correct engagement.  To illustrate the meshing condition of the gear system shown in Fig.
5 , three  moments (T0, T1 and T2) are defined.  First of all, t he  moment  shown in Fig.  5  is defined as T0 .  As  gear 1
rotates clockwise, the point E on gear 3 will mesh with gear 6 at point F.  Then, t his moment is defined as T1 . As gear 1
continues to rotate clockwise,  the point G on gear 5 will mesh with the output gear 6 at point H. A nd this moment is
defined as T2. The detaile d status of the three moments are described as below:
The  moment  T0:   The  starting  line  BE  and  the  gear  center  line  BC  coincide.  T he  starting  line  DG  is

n
   pitch
number distance  clockwise  from DM. The integral pitch number of gear 1  contained in

2
   is

k
 . And points M and N
will mesh on gear center line DC.
The moment T1:  The point E on gear 3 engages with the point F on gear 6 at the pitch circle.  From T0 to T1, gears
3 and 6 have  rotated the same pitch number.
The moment T2:  The point G on gear 5 engages with the point H on gear 6 at the pitch circle.  The teeth on points
E and G  mesh  with gear 6 at the  same  meshing position.  From T1 to T2, gears 5 and  6 have rotated  the same pitch
number.
T he pitch number of gear 6 contained in

1
   can be expressed as

1
66
2
NUM z

p

     (1)

T he pitch number of gear 3 contained in

3
   can be expressed as

3
36
2
NUM z

p

     (2)

T he pitch number of gear 5 contained  on the green line shown in Fig.  5  can be  derived as follows:

( )4
55
2
 2
NUM z
p   g
p

     (3 )

where

52/nzp
   is the angle of the n pitch number  of gear 5 ,

2 1 4( / 2 ) 2 /z k zg  p p
   is the angle of gear 4 that
meshes with the non - integral pitch number of gear 1 contained in

2
 .
In Fig.  5 , the pitch number s of gears contained in the lines that marked with the same color are equal.  According to
the meshing condition, the pitch number between points F and H is just an integer. Thus, the relationship between the
tooth number and the gear positions is obtained a s follows:

6 5 3NUM NUM NUM Z
     (4 )

where

Z
   is the integral pitch number of gear 6 between points F and H.
For analytical convenience,  Eq. ( 4 ) can be rearranged as follows:

 4 6 1 1 5 2 3 4 3 4 5 4 4 5 4 4 5 2z z z z z z z z Z z k z n z z z    p
     (5 )

Replace the term of

4 5 4 4 5Z z k z n z z z
   with an integer

N
 , we obtain the following:

4 6 1 1 5 2 3 4 3 4 5 4 2z z z z z z z z N    p
     (6 )

4
 2
 3
 1
 4
5

6
 A
1

3B
 H

E
 2
 4

C
 D

F
 G

N M  4

1
 5

C
 D

2
 4

 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

The relationship of the angles (

1 2 3 4, , ,
 ) is obtained from the quadrilateral of ABCD as follows:

1 2 3 4 2    p
     (7)
Imposing the theorem of cos ine to the diagonals, the following equations are derived:

2 2 2 2
122 cos 2 cosAB AD AB AD BC CD BC CD
     (8)

2 2 2 2
342 cos 2 cosBC AB BC AB CD AD CD AD
     (9 )
For the spur gears, k nowing that

/2i i ir z m
     (10)

the final form of Eqs. ( 8) and (9 ) are obtained as follows:

( ) ( ) ( )( ) ( ) ( ) ( )( )
2 2 2 22 2 2 2 2 2
2 3 6 2 5 6 2 3 6 5 6 1 1 1 2 1 1 4 1 1 2 1 4 22 cos 2 cosm z z m z z m z z z z m z z m z z m z z z z
     (11)

( ) ( ) ( )( ) ( ) ( ) ( )( )
2 2 2 22 2 2 2
1 1 2 2 3 6 1 2 1 2 3 6 3 1 1 4 2 5 6 1 2 1 4 5 6 42 cos 2 cosm z z m z z m m z z z z m z z m z z m m z z z z
     (12)

wh ere

ir
   is the pitch radius of gear

i
   (

1,2i
 ),

1m
   is the module of the gears 1, 2 and 4, and

2m
   is the module of
gears 3, 5 and 6.
Thus,  we  obtain  four  equations  (Eqs.  ( 6 ),  (7),  (11)  and  (12))  with  four  variables

1 2 3 4( , , , )
 .  The  unknown
parameter  (

1
 )  is  expressed  in  function  of  the  tooth  number  according  to  the  following  transcendental  equation
(

2 4 3 5, z z z z
 ):
 11
11
cos cos
cos arccos 2 cos arccos 2
c a b c a b
e f u v w g h x y z
dd

 p  p

     (13)

wh ere

( ) ( )
2222
2 3 6 2 5 6a m z z m z z
     (14)

( )( )
2
2 3 6 5 62b m z z z z
     (15)

( ) ( )
2222
1 1 2 1 1 4c m z z m z z
     (16)

( )( )
2
1 1 2 1 42d m z z z z
     (17)

( ) ( )
2222
1 1 2 2 3 6e m z z m z z
     (18)

( )( )1 2 1 2 3 62f m m z z z z
     (19)

( ) ( )
2222
1 1 4 2 5 6g m z z m z z
     (20)

( )( )1 2 1 4 5 62h m m z z z z
     (21)

56

35

zz
u zz

     (22)

1 5 4 5

3 4 4 5

z z z z
v z z z z

     (23)

45

3 4 4 5

N z z
w z z z z

     (24)

36

35

zz
x zz

     (25)

1 5 3 4

3 4 4 5

z z z z
y z z z z

     (26)

34

3 4 4 5

N z z
z z z z z

     (27)

New ton iterative method is used to gain the root of Eq. ( 13). Then

2 3 4,  and
   are obtained from Eqs. (2 8)- (30 ).

1
2 cos
arccos c a b
d

     (28)

3 1 2 2u v w   p
     (29)

4 1 2 2x y z   p
     (30)

3.1.1 Nume rical Validation  1: Symmetrical Duplex idler
The method established above is applied to the resolution of the configuration of the torque - split transmission with
external  meshing  symmetrical  duplex  idler s  (Fig.  6 ).  The  tooth  number  of   gears  are  as  follows:

1 2 4 3 5 619   30   17   100z z z z z z     , , ,
 . The gears are 2 module (

12 2mm
 , it would be well if

12 ).mm

5
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

In this configuration

3 4 2 4 3 5( ,  ,  ),z z z z
   the starting equations of Eqs. ( 6 ) and (7) become

2 6 1 1 3 2 2 3 322z z z z z z N   p
     (31 )

1 2 322   p
     (32 )

where

2 2 3 2 3 .N Z z k z n z z z

 Fig.  6  The torque - split transmission with external meshing symmetrical duplex idler.

Still, by the theorem of cosine to the diagonals, the Eqs.  (11) and (12) are reduced to the following equation:

( ) ( ) ( ) ( )
2 2 2 22 2 2 2
2 3 6 2 3 6 1 1 1 2 1 1 2 2cos cosm z z m z z m z z m z z
     (33 )

Similarly, the transcendental equation for

1
   is obtained as follows:

11
2 6 1 1 3 2 3 1
cos cos
arccos 2 2 arccos 2
b a a b a a
z z z z z z N
bb

 p  p

     (34 )

where

( )
22
2 3 6a m z z
     (35 )

( )
22
1 1 2b m z z
     (36 )

Once  the  angle

1
   has  been  determined,  the  other  unknown  parameters  (

23,
 )  are  calculated  by  Eqs.  (3 7)  and
(3 8).
 1
2 cos
arccos b a a
b

     (37 )

12
3 2 2
p

     (38 )

Figure 7 is t he representation of  Eq. (34). The function value and  that the root of N=0 is shown. When the right side
of Eq. (34) is 0, only one point on the x axis is shown in the illustration.  The limit positions (shown in the first and the
last pictures of Fig. 8) of g ear 1 are obtained as the two endpoints of the curve intersect with the horizontal line of y=0.
Part of the solutions are listed in Table 1, and the corresponding configurations are shown in Fig.  8. Since there is a
turning point on the equation curve, the  same N may has two different solutions (for example N=402).

 2 4 7

- 4000

- 3000

- 2000

- 1000
 0

1000
2000
3000
 61 3 5 x

y

Fig.  7 The  representation  of Eq. (3 4 ) for N=0.

6
 2 3
 1
 4
5

6 1

3 4

4
 A

B
 C
 D

 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

Table 1    Solutions of Eqs. (34), (37) and (38) in sexagesimal degrees

N(x 0)  - 510(1)   - 80(1)  50(1)   190(1)   323(1)   380(1)   402(1)   402(6)   323(6)
θ1  0  25.95   32.99   39.38   43   40.67   36.74   27.74   0
θ2  0  76.50   103.02   136.57   180  213.25   239.32   277.27  360
θ3  180  128.78  112.00  92.02   68.50   53.04   41.97   27.50   0
θ4  180  128.78  112.00  92.02   68.50   53.04   41.97   27.50   0

N=-510
=1x 0 N=- 80
=1x 0 N= 50
=1x 0

N=190
=1x 0 N=323
=1x 0 N=380
=1x 0

N=323
=1x 0
N=402
=6x 0
N=402
=1x 0

Fig. 8 Solutions for the torque - split transmission with external meshing symmetrical duplex idler.

It  is  noteworthy  that  the  integer

n
 ,  which  indicates  the  position  of  the  starting  line  of  gear  4,  determines  the
installation  phase  of  gear  tooth  of  the  duplex  idler.  Between  the  two  limit  positions,  there  are  numerous  of  the  gear
positions (corresponding to N and the initial value of

0x
 ). Among those gear positions, only the gear positions with an
integer pitch number of input pinion contained in

2
   have no meshing phase difference between  the first stage of the
two  paths.  And  the  meshing  phas e  difference  has  great  influence  on  the  dynamic  and  load  sharing  behavior  of  the
torque - split gear transmission.

3.2  Case 2 ：The Internal Meshing Duplex idler
The general configurations of the torque - split transmission with internal meshing duplex idler are shown in Fig. 9.
It has two types: noncrossed gear center line (Fig. 9(a)) and crossed gear center line (Fig. 9(b)).

Fig.  9  General configurations of the torque - split transmission with internal meshing duplex idler: (a) noncrossed gear center
line; (b) crossed gear center line.

3.2.1 Type 1 : Noncrossed Gear Center Line
In this configuration (Fig.  9 (a)), the starting equations of Eqs. ( 6 ) and (7) become

( ) ( )4 6 1 1 5 2 3 4 3 4 5 4 2z z z z z z z z N  p  p  p
     (39 )

1 2 3 4 2    p
     (40 )

where

4 5 4N Z z k z n z
 .
Once again, by the theorem of cosine to the diagonals, the  following equations are derived.

7
 1
A

3 42
B C
 DE
 F
 H

G

1

2 3 4 5

6

1 A

B
 C
 D

3
 4

2

F

E HG

1

2 3
 4

5

6

(a)                                                                                  (b)
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

( ) ( ) ( )( ) ( ) ( ) ( )( )
2 2 2 22 2 2 2 2 2
2 6 3 2 6 5 2 6 3 6 5 1 1 1 2 1 1 4 1 1 2 1 4 22 cos 2 cosm z z m z z m z z z z m z z m z z m z z z z
     (41)

( ) ( ) ( )( ) ( ) ( ) ( )( )
2 2 2 22 2 2 2
1 1 2 2 6 3 1 2 1 2 6 3 3 1 1 4 2 6 5 1 2 1 4 6 5 42 cos 2 cosm z z m z z m m z z z z m z z m z z m m z z z z
     (42)

From   the  four  equations  above,  the  transcendental  equation  for

1
   and  the  equations  for

2 3 4,,
   are  the  same
with Eqs. ( 13 ) and (28)- (30 ). The differences are the following expressions.

( ) ( )
2222
2 6 3 2 6 5a m z z m z z
     (43)

( )( )
2
2 6 3 6 52b m z z z z
     (44)

( ) ( )
2222
1 1 2 1 1 4c m z z m z z
     (45)

( )( )
2
1 1 2 1 42d m z z z z
     (46)

( ) ( )
2222
1 1 2 2 6 3e m z z m z z
     (47)

( )( )1 2 1 2 6 32f m m z z z z
     (48)

( ) ( )
2222
1 1 4 2 6 5g m z z m z z
     (49)

( )( )1 2 1 4 6 52h m m z z z z
     (50)

56

35

zz
u zz

     (51)

1 5 4 5

3 4 4 5

z z z z
v z z z z

     (52)

45

3 4 4 5 2
N z z
w z z z z
pp

     (53)

36

35

zz
x zz

     (54)

1 5 3 4

3 4 4 5

z z z z
y z z z z

     (55)

34

3 4 4 5 2
N z z
z z z z z
pp

     (56)

3.2.2 T ype 2: Crossed Gear Center Line
In the configuration shown in Fig.  9 (b), Eqs. (3 9 ) and (40 ) become

( ) ( )4 6 1 1 5 2 3 4 3 4 5 4 2z z z z z z z z N  p  p  p
     (57)

1 2 3 4 0
     (58)

With   the  quadrilateral  cosine  theorem,  the  equations  obtained  are  the  same  with  Eqs.  ( 41 )  and  (42 ).  From  the
equations above, the same equations for

1 2 3 4, , ,
   are obtained with the following  expressions:

56

35

zz
u zz

     (59)

1 5 4 5

3 4 4 5

z z z z
v z z z z

     (60)

3 4 4 5 2
N
w z z z z
pp

     (61)

36

35

zz
x zz

     (62)

1 5 3 4

3 4 4 5

z z z z
y z z z z

     (63)

3 4 4 5 2
N
z z z z z
pp

     (64)

3.2.3 Nume rical Validation  2: Symmetrical Duplex idler
Like wise, the method established in this section is applied to the resolution of the configuration of the torque - split
transmission with external meshing symmetrical duplex idler (Fig.  10) which is a specific instance. The tooth number
of gears are also as follows:

1 2 4 3 5 619,  30,  17, 100z z z z z z
 . The gears are 2 module (

12 2mm
 , it would be
well if

12 ).mm

8
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

 Fig. 10 The torque - split transmission with internal meshing symmetrical duplex idler.

The  torque - split  transmission  with  internal  meshing  symmetrical  duplex  idler  is  a  type  of  noncrossed  gear  center
line. In this configuration,

3 4 2 4 3 5,  ,, z z z z
   Eqs. (3 9 ) and (40 ) become

2 6 1 1 3 2 2 3 322z z z z z z N   p
     (65 )

1 2 322   p
     (66 )

Eq uations (41 ) and (42 ) are reduced to the following equation:

( ) ( ) ( ) ( )
2 2 2 22 2 2 2
2 6 3 2 6 3 1 1 1 2 1 1 2 2cos cosm z z m z z m z z m z z
     (67 )

The transcendental equation for

1
   is obtained as follows:

11
2 6 1 1 3 2 3 1
cos cos
arccos 2 arccos 2
b a a b a a
z z z z z z N
bb

 p  p

     (68 )

where

( )
22
2 6 3a m z z
     (69 )

( )
22
1 1 2b m z z
     (70)

Once  N  is  given,

1
   is  solved  through  the  Newton  iterative  method.  The  angle s

23,
   are  calculated  by  the
following equations:

1
2 cos
arccos b a a
b

     (71)

12
3 2 2
p

     (72)

Figure 11 is t he representation of  Eq. (68). The function value and  that the root of N=0 is shown. When the right
side of Eq. (68) is 0, only one point on the  x axis  is  shown in the  illustration.  When the two  endpoints of the  curve
intersect with the horizontal line of y=0, the limit positions (shown in the first and the last pictures of Fig. 12) of gear  1
are obtained.  Nine different solutions are listed in Table 2, and the corresponding configuration are sho wn in Fig. 12.
Since  there  is  a  turning  point  on  the  curve  of  Eq.  (68),  the  same  N  may  has  two  different  solutions  (for  example
N=640).

- 3000

- 2000

- 1000
 0

1000

2000

3000
4000
5000
 2 4 761 3 5

y
 x

Fig. 11 The  representation  of Eq. (65) for N=0.

9
 1
2
3 4

4 5

1

6

2 3
 A

B
 C
 D

 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

Table 2    Solutions of Eqs . (68), (71) and (72) in sexagesimal degrees

N(x 0)  510(1)   640(1)   650(1)   640(6)   593(6)   530(6)   400(6)   200(6)   - 323(6)
θ1  0  47.76   53.40   70.15   72  70.73   62.94   47.11   0
θ2  0  86.59   99.13   153.52   180  202.77  235.68   274.79   360
θ3  180  112.82  103.73   68.17   54   43.25   30.69   19.05   0
θ4  180  112.82  103.73   68.17   54   43.25   30.69   19.05   0

N=510
=1x 0

N=640
=6x 0

N=400
=6x 0
 N=650
=6x 0

N=530
=6x 0

N=-323
=6x 0

N=640
=1x 0

N=593 =6x 0

N=200
=6x 0

Fig. 12 Solutions for the torque - split transmission with internal meshing symmetrical duplex idler.

4. Applications with Simplified Mathematical Method
4.1 The  Planetary Duplex idler

Fig. 13 The planetary duplex idler.

The  planetary  duplex  idler  (Fig.  13)  is  studied  as  a  particular  case  of  the  torque-split  transmission  with  internal
meshing symmetrical duplex idler. In this case, the axes of gear 1 and gear 6 coincide, and the following equations are
obtained.

12 2
q p

     (73)

34 0
     (74)

wh ere q is the number of the duplex idler.
Eq uation (6 5 ) becomes

1 3 2 6z z z z q N
     (75)

Co nsidering the geometrical constraints of the planetary wheel, the following equation is obtained.

( ) ( )1 1 2 2 6 3m z z m z z
     (76)

Th e tooth number s of gears 2 and 3 can be solved by the following equations.

10
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

2
2 1 6 1 1 2
2 1 1 2 6

m z z m z m q N
z m z m z

     (77)

( )
1
3 6 1 2
2

m
z z z z
m

     (78)

4.2 The Configurations with Coplanar Gears
Given  the  same  tooth  number  of  the  gears  on  the  duplex  idler  shafts  in  Sec.  3,  namely

23 ,zz

45 ,zz
   the
configuration  discussed  here  becomes  the  configuration  of  torque - split  transmission  with  coplanar  gears.  This
configuration has been fully studied  with a different method  (Vilán et al. and Abraham et al., 2010, 2012 ). So only the
meshing condition, which is different from their works, is studied in this section.

4.2.1 The External Meshing Coplanar Gears
The torque - split  transmission with external meshing coplanar gears is shown in Fig. 1 4 . With the same method in
Sec. 3, the following equation is derived.

( )4 1 1 2 2 3 3 4 3 2z z z z Z k z    p
     (79 )

Replace the term of

3Z k z
   with an integral number (N), the final form of Eq. (7 9 ) is as follows:

4 1 1 2 2 3 3 4 2z z z z N    p
     (80)

When

2 0,
   the  integral  numbers  (Z  and  k)  are  equal  to  zero,  and

3Nz
   is  obtained.  When

2 2 ,p
   the
integral numbers are equal to

3z
 , and

1Nz
   is obtained.

 Fig. 1 4  The torque - split transmission with external meshing coplanar gears.

4.2.2 The Internal Meshing Coplanar Gears

 Fig. 15 The torque - split transmission with internal meshing coplanar gears: (a) noncrossed gear center line; (b) crossed gear
center line.

The torque - split  transmission with internal meshing coplanar gears is shown in Fig. 1 5 , Eq. ( 79 ) becomes

11
 1

3 4

2

F

C
 D
B E
 G
 H
A

1
2
 3

4

3 1
4

2

A

B
 C
 D

E
 F
 G H

2

4 1

3

1

3 42

A

B
 C D
E
 F
 G
 H

1

2
 3

4

(a)                                                              (b)
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

( ) ( ) ( )4 1 1 2 2 3 3 4 2z z z z Z k  p  p  p
     (81)

where

 (+,  - ) correspond to Fig. 1 5 (a) and Fig. 1 5 (b).
Replace the term of Z - k with an integral number (N), the final form of Eq. ( 81) is:

( ) ( )4 1 1 2 2 3 3 4 2z z z z N  p  p  p
     (82)

4.3 The Concentric Face Gear
T he torque - split transmission with concentric face gear is shown in Fig. 1 6 (a). The two face gears arranged face to
face  one  over  the  other.  This  arrangement  has  significant  wei ght  reduction  and  large  reduction  ratio.  Its  meshing
condition is illustrated in Fig. 1 6 (b), with

1 4 2 3 2,  ,  .z z z z p

The meshing condition can be expressed as follows:

1 1
2 z n Z

p
     (83 )

where Z is the integral pitch number between points F and H along the pitch circle of gear 4, and n is the integral pitch
number of gear 3 from the first gear tooth (clockwise  from

1OD
 ) in clockwise direction.

 Fig.1 6  (a) The torque - split transmission with concentric face gear; (b) the meshing condition.

4.3.1 Specific Instance: Equal Spaced Star Gears
For  the  configuration  with  cylindrical  gears  arranged  around  the  face  gear  equally,  Fig.  1 6 (a),  the  following
equation is derived.

1 2/ qp
     (84 )
where q is the number of the cylindrical gears that are arranged around the face gear.
Imposing Eq. (8 4 ), the Eq. ( 83 ) becomes

1 /z q Z n
     (85 )

A  meshing  phase  difference  of

1/ zp
   between  the  upper  and  lower  meshes  of  gear  1  is  observed  as  the  tooth
number  of  the  cylindrical  gear  is  odd.  While  if  the  tooth  number  of  the  cylindrical  gear  is   even,  the  meshing  phase
difference  is  zero.  The  meshing  phase   difference  leads  to  the  unsynchronized  meshing  stiffness  of  paths,  and  has
influence on the dynamics and load sharing behaviors of the transmission system.

5. Conclusions
T he  torque - split gear transmission is  mainly developed for the rotorcraft to achie ve high power density and large
reduction  ratio.  It  reduces  the  contact  force  of  gear  teeth  by  dividing  the  force  between  several  contact  areas.  This
results in an increase of available torque and smaller gears. In this work, a universal mathematical desig n method of the
torque - split  gear  transmission  is  proposed.  Unlike  other  existing  method s,  this  method  is  proved  to  be  suitable  for
multiple  types  of  torque - split  gear  transmission.  This  method  is  applied  to  the  calculation  of  the  torque - split
transmission  with  duplex  idler,  planetary  duplex  gear,  coplanar  gear  and  concentric  face  gear.  Numerous  discrete
solutions of the gear positions are observed. And these solutions of gear position cor respond to different meshing ph ase
difference between paths. The mesh ing phase  difference, which has great influence on the dynamics and load sharing
behaviors of the torque - split gear transmission, can be  changed by adjusting the pitch number of pinion contained in the
area formed by gears. Moreover, an even tooth number o f the cylindrical gear of the concentric face gear transmission
is recommended for the reason of minimizing the meshing  phase  difference.

12

A
B C H
F

E G

1

O 2 O 1

2 3

4
 1 1
 D

(a)                                              (b)
 2
© 2018 The Japan Society of Mechanical Engineers[DOI: 10.1299/jamdsm.2018jamdsm0127]

Zhao and Li, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.12, No.7 (2018)

Acknowledgments
The authors gratefully acknowledge the support of the National Natural Science Foundation of China (Grant No.
51675424).

References
Abraham  Segade  Robleda,  José  A.  Vilán  Vilán,  Marcos  López  Lago,  et  al.,  Split  torque  gearboxes:  requirements,
performance and applications, Mechanical Engineering, (2012), DOI: 10.5772/37258.
Aydoğan  M  Ö,  Saribay  Z  B,  Özgüven  H  N,  Dynamic  Modelling  of  Split - Torque  Face - Gear  Drive  Systems,
International  Design  Engineering  Technical  Conferences  &  Computers  and  Information  in  Engineering
Conference, (2017).
Filler R R, Heath G F, Slaughter S C, et al., Torque splitting by a conc entric face gear transmission, Proceedings of the
ASME Mechanisms and Robotics Conference (2002).
Filler  R  R,  Heath  G  F,  Slaughter  S  C,  et  al.,  Torque  splitting  by  a  concentric  face  gear  transmission,  American
Helicopter Society 58th Annual Forum, (2002).
Fu C, Zhao N, Zhao Y, Load Sharing Multiobjective Optimization Design of a Split Torque Helicopter Transmission,
Mathematical Problems in Engineering, (2015b), pp.1 - 15.
Gmirya Y, Woodbridge C T, Multi - path rotary wing air craft gearbox, Patent 7918146B2, U SA, (2011).
Gmirya  Y,  Split  torque  gearbox  for  rotary  wing  rotorcraft  with  translational  thrust  system,  Patent  7413142  USA,
(2018).
Heath G F, Slaughter S C, Fisher D J, et al., Helical face gear development under the enhanced rotorcraft drive system
progr am, Report, NASA Glenn Research Center, USA, (2011).
Jose  A,  Abraham  R,  Feasible  geometrical  configurations  for  split  torque  gearboxes  with  idler  pinions,  Journal  of
Mechanical Design, (2010), pp.1 - 8.
José A. Vilán Vilán, Abraham Segade Robleda, Marcos  López Lago, et al., Feasible geometrical configurations for split
torque gearboxes with idler pinions, ASME. J. Mech. Des. (2010), DOI:10.1115/1.4002977.
Li  Zhijun,  ZHU  Rupeng,  BAO  Heyun,  et  al.,  Tooth  matching  of  torque - split  transmission,  Journal  of  Cent ral  South
University, (2014), pp.414 - 420 (in Chinese).
Mo  S,  Zhang  Y,  Wu  Q,  Research  on  multiple - split  load  sharing  of  two - stage  star  gearing  system  in  consideration  of
displacement compatibility, Mechanism & Machine Theory, (2015a), pp.1 - 15.
Reszuta  K,  Dr ewniak  J,  Computer - aided  modeling  of  dynamics  of  split - path  gearboxes,  Mechanik,  (2015),  DOI:
10.17814.
Todd A. Garcia, Torque split gearbox for rotary wing rotorcraft, Patent 9,278,760 B2, USA, (2016).
White  G,  Split  torque  helicopter  transmissions  with  w idely  separated  engines,  Proceedings  of  the  Institution  of
Mechanical Engineers, Part G: Journal of Aerospace Engineering, (1989), pp.53−65.
Xiaolan Ai, Orkin, P. Kruse, et al., Load split mechanism for gear transmission, Patent 8,647,229 B2, USA, (2014b).
Xiang  Ya,  Wang  Sanmin,  Yuan  Ru,  Research  on  tooth  matching  condition  of  the  four - path  torque - splitting  gear
transmission, Journal of Mechanical Transmission, (2012), pp.10 - 13 (in Chinese).
Yuriy Gmirya, Split - torque gear box, Patent 8,683,892 B2, USA, (20 14a).

13
