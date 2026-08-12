<!-- source: https://www.atlantis-press.com/article/25871492.pdf | converted from PDF -->

Tooth Number Matching and Its Software Development for 2KH Planetary
Gear Mechanism

Jin-Feng SUN, Jun WANG*, Yun-Duan HONG, Hong-Xiu HE, Quan WANG,
Jun REN, Sheng-Lan MAO, Shu-Ting LI, Zheng-Zheng QIN, Xing HONG

School of Mechanical Engineering, Hubei University of Technology, Wuhan, hubei, 430068, China

*junwang@mail.hbut.edu.cn

Keywords: 2K-H, Planetary gear, Tooth number matching, Computation.

Abstract. 2K-H planetary gear is a commonly seen gear structure, but it has proven troublesome to
match its tooth numbers through hand computation. This paper introduces a calculation method for
the  2K-H  planetary  gear  and  develops  a  software  written  with  the  use  of  computer  software
technology for matching gear units, thus greatly reducing the workload in matching tooth numbers.
In addition, they can be applied to tooth number matching for all kinds of 2K-H planetary gears.

Introduction

In calculating the tooth numbers for the 2K-H planetary gear, due to its many limitations, we often
need  to  resort  to  hand  computation,  thus  making  the  tooth  number  matching  extremely  complex.
Moreover,  hand  computation  is  time-consuming,  because  the  2K-H  planetary  gear  involves  four
different  kinds  of  gear  mechanisms.  At  present,  a  growing  number  of  designing  personnel  have
begun  to  complete  this  task  through  computers  since  they  came  out.  This  paper  introduces  the
experience  of  realizing  the  tooth  number  matching  for  2K-H  planetary  gear  through  computer
programs.

2K-H Planetary Gear Mechanism

2K-H planetary gear mechanism is featured by small size, high self-weight transmission efficiency,
light weight, large transmission ratio, low noise and high reliability, etc. With the development of
science and technology, planetary gearing has been widely applied into the machinery of such fields
as metallurgy, mining, lifting, chemical engineering, electrics, textile and oil production. However,
planetary  gearing  is  a  highly  advanced  system,  especially  all  kinds  of  large-scale  reducers.  To
satisfy the work needs and ensure relatively high operating reliability and longer service life of the
mechanical  system,  we  can  not  willfully  choose  the  tooth  number  for  each  gear  in  designing  the
planetary  gear  mechanism;  but  instead,  we  have  to  work  out  the  correct  tooth  number  for  the
planetary gears according to the schematic diagrams and satisfy certain conditions according to the
characteristics of planetary transmission, with a view to guaranteeing normal operation. By virtue of
our  needs,  we  divide  the  planetary  gear  into  four  kinds  as  evidenced  by  the  following  figures,
namely 2KH-NGW, 2KH-WW, 2KH-NW and 2KH-NN, among which N stands for internal gear, W
for external gear and G for composite gear.

Fig1. 2KH-NGW planetary gear mechanism           Fig 2. 2KH-WW planetary gear mechanism

446Advances in Engineering Research (AER), volume 1053rd Annual International Conference on Mechanics and Mechanical Engineering (MME 2016)Copyright © 2017, the Authors.  Published by Atlantis Press.
This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/by-nc/4.0/).

Fig 3. 2KH -NW planetary gear mechanism             Fig 4. 2KH -NN planetary gear mechanism

Restrictive  Conditions for Tooth Number Matching

In designing the 2KH planetary gear mechanism, the tooth number matching of gears must satisfy
the following conditions under normal circumstances:

Condition for  Transmission Ratio

It refers to a condition which must  be satisfied for the  tooth numbers of each  gear to  achieve the
given transmission ratio. And the transmission ratio for 2K-H planetary gear train is:

1
b
aH abii

According  to  the  above  formula,  the  tooth  number  ratio  of  the  two  central  gears  of  the
2KH -NGW planetary gear train can be obtained. And the condition for the transmission ratio should
be:

1
b ab
a

Z i
Z 

To the planetary gear train with planetary gears being the dual gears (g  -5) of 2KH -NW(WW, NN)
types, the condition for the transmission ratio should be:

1
gb b
aH
af

ZZ i
ZZ   

In  the  formula,  the  “+”  symbol  applies  to  minus-sign  gear train  ( NW)  while  the  “-”  symbol
applies to plus -sign gear train ( WW or NN).

Condition for  Concentricity

It refers to a condition to ensure the axial alignment of basic building blocks. The center distance
for two pairs of gears must be identically equal, that is,

''
ag bfaa

Or
 ''
cos cos
( ) ( )
cos cos
ag a g bf b f
ag bf
m Z Z m Z Z


  

After calculation:

''
( ) ( )

cos cos

ag a g bf b f

ag bf

m Z Z m Z Z





In  the  formula,  the  “+”  symbol  applies  to  external  gearing  while  the  “-”  symbol  applies  to

447Advances in Engineering Research (AER), volume 105

internal gearing;  α stands for the pressure angle of the reference circle; α’ag and α’bf   stand for the
generating  angles  after  changes  to  the  angles  of  the  two  pairs  of  gears; mag and  mbf stand  for  the
modulus of the two pairs of gears. Different standards can be adopted, but in practical application,
mag=m bf.

''
( ) ( )

cos cos

a g b f

ag bf

Z Z Z Z





2

ba
g ZZ
Z 


Condition for Fitting

To fit the several planetary gears on the tumbler H (planetary frame) into the spaces between two
central  gears  evenly,  the  condition  to  be  satisfied  by  each  tooth  number  of  gears  is  known  as  the
condition for fitting.
The unified formula for 2KH planetary gear train with dual gears as the planetary gears is:

a f g b

p

Z Z Z Z
q n



 an  integer

In  the  formula,  Zf  and  Z g  stand  for  tooth  numbers,  the  values  of  which  are  obtained  through
dividing them by the common divisor m.

' ()ab

p

ZZ
q n


 an integer

For the 2KH- NGW  planetary gear train, due to Zf=Z g with matching together, the following can
be obtained from the formula (3- 7).  This is the condition for fitting.

Condition for Adjacency

In order to avoid collisions between the planetary gears, certain spaces must be reserved; that is to
say,  the  center  distance  L  of  the  central  gears  in  two  adjacent  lines  must  be  larger  than  the  tip
diameter dag of the planetary gear in the digest lines. The formula is:

agLd

Software Development

The  limitations  in  tooth  number  matching  for  planetary  gears  present  a  great  deal  of  difficulties.
Therefore, we, on the basis of the VC2008 programming software, have written a special program
for tooth number matching, named the program of tooth number matching for 2KH planetary gear
mechanism.  According  to  the  input  transmission  ratio  and  the  number  of  planetary  gears  to  be
matched, the program can automatically work out the tooth number matching scheme meeting the
above- mentioned restrictive conditions for gear and gear ring as well as the transmission ratio errors
for corresponding gears.

448Advances in Engineering Research (AER), volume 105

Fig.5: Program flowchart of tooth number matching for 2KH planetary gear mechanism

In  accordance  with  the  above  flowchart,  the  main  interface  of  our  software  for  tooth  number
matching  is  shown  as  in  the  following  Fig.  Firstly,  we  choose  the  types  of  2KH  planetary  gears,
then type in the transmission ratio, number of planetary gears and gear modulus (three conditions to
be input by the user) in the middle, and finally the tooth number matching result we need will be
pop up at the right side. The software interface is shown in Fig.6.

Fig.6: program software interface of tooth number matching for 2KH planetary gear mechanism

Calculation Examples

If it is to design a 2 KH- NGW planetary gear train with a transmission ratio of iaH
b = 4.55, the tooth
number for each gear shall be determined.
According  to  the  requirements  of  the  question,  we  should  firstly  start  the  software,  click  the
button of 2KH- NGW, and then assign 4.55, 4 and 3 to the values of the transmission ratio, number
of  planetary  gears and  gear  modulus.  After  the  input,  when we  click  the  calculate  button,  several

449Advances in Engineering Research (AER), volume 105

results will be produced. Take the result of “the transmission ratio error is 0.10%, the tooth number
of  external  gear  rings  is  78,  the  number  of  planetary  gears  is  28  and  the  tooth  number  of  central
gears is 22” as one example. We can choose the optimal result and thus complete the whole process
of tooth number matching for 2KH planetary gear mechanism.

Conclusions

In light of the composition features of 2KH planetary gear mechanism and the restrictive conditions
for  its  tooth  number  matching,  the  mathematical  calculation  method  for  2KH  planetary  gear
mechanism  is  established.  Through  this  method,  we  work  out  the  tooth  number  matching  of
planetary  gears,  and  transfer  it  into  computer  languages.  With  the  help  of  VC  software
programming,  the  tooth  number  of  planetary  gears  can  be  calculated  by  computer  programs.  The
developed software is featured by simple operation, strong man- machine interaction, user- friendly
interface and wide usage.

Acknowledgments

We  are  grateful  for  the  support  from  the  Scientific  Research  Program  Funded  Project  (No.:
B2016044) of Hubei Provincial Department o f Education to the research of this paper.

References

1.   Hong- W ei  NI.  Tooth  number  matching  of  planetary  differential  transmission  mechanism[J].
Mechanical Engineer , 2002.
2.   Hong- Y an  SHI,  Hai- Hong  CHEN ,  Yu   ZHENG ,  Xuan   YU.   Optimization  Design  of
2K- H(NGW) - Z  Mix ed  Gear  Train  based  on  Matlab  Genetic  Algorithm[J]. Journal  of
Mechanical Transmission, 2011.
3.   Zhao - Shan YANG , Ming CHEN . The Mesh Efficiency of the Planetary Mechanism of 2K- H[D]
Style[J].  Journal of China Textile University, 1998.
4.   Qi - Min  XIAO ,  Nai - Sen  CAO ,  Xiao - Guang  SUN .  The  Study  on  Optimal  Design  System  of
2K- H Planetary Gear Train[J]. Development & Innovation of Machinery & Electrical Products ,
2006.
5.   Shu- Y an  WANG ,  Peng- F ei  MA .  The  optimization  design  of  the  2K- H  planetary  gear
transmission system[J]. Construction Mechanization, 2002.
6.   Yue  LIU , Ming MAO ,  Ming- C heng WANG . Optimal Design and Accurate Intensity Check of
2K- H Planetary Transmission System[J]. Vehicle & Power Technology , 2011.
7.   Zhen - J ie  ZHAO ,  Yong   ZHANG,  Yu - J un  WANG .  2K - H- based  Multi-stage  Planetary  Gear
Reducer Optimization Design System[J].  Computer Programming Skills & Maintenance , 2011.
8.   Xiao - C hun HUANG .  Design  and  Application  of  Planetary  Gear  Transmission  Mechanism[J].
Electro-Mechanical Engineering , 1997.
9.   Lai - Hu Yu . Optimal Design of 2K- H Planetary Gear Mechanism[J]. Journal of Hebei Radio &
TV University, 1999.
10.   Ruo - Hui WANG . The Planet Gear- Driven Optimum Programming[J]. Journal of Electric Power,
2002.
11.   Nan GE , Jun  ZHANG . Finite Element Analysis of Internal Gear in High- Speed Planetary Gear
Units[J]. Transactions of Tianjin University, 2008.
12.   Ying   YU ,  B o  YU .  Analysis  and  Design  of  Gear  Train[M].  Harbin:  Harbin  Engineering
University Press, 2007.
13.   Chao  HU . Visual C++ the Easy Way[M]. Electronic Industry Press, 2013.
14.   Wei   WANG ,  Xiao - J ian  WANG .  M echanical  Design(2
nd  edition)[M].  Huazhong  University  of
Science and Technology Press, 2012.
15.   Bing   WEI,  Quan - Y u  YU ,  Wei   SUN .  Mechanical  Principles[M].  Huazhong  University  of
Science and Technology Press, 2011.

450Advances in Engineering Research (AER), volume 105
