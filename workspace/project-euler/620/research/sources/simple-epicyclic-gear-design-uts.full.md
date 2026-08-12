<!-- source: https://www.uts.com/resources/IGS/IGS60-1161.pdf | converted from PDF -->

Program 60-1161—Simple Epicyclic Gear Design
(Parallel Axis)
Introduction

The simple epicyclic gear unit consists of acentral external gear (sun gear) meshed
with one or more external gears (planet gears).  The planet gears are then meshed
with an internal gear (ring gear) which encloses the system.  The planet gears and
planet gear support bearings are usually held in a carrier which rotates about the
geometric center of the unit.  The term “epicyclic” comes from the path of a point on a
planet gear which traces out an epicycloid in space.  There are three basic types of
simple epicyclic gear units.

When the ring gear is fixed or grounded and the sun and carrier are input/output
members the unit is called a “planetary gear”.

When the carrier is fixed and the sun and ring are input/output members the unit is
a “star” gear.  The star gear is not an epicyclic gear as the planet gear centers do not
rotate about the unit central axis but since the construction is basically the same it is
included in the family.  For high speed units the star gear is often used in cases
where planetary gears are not practical because of the high centripetal acceleration
loads on the planet gears.

When the sun is fixed and the carrier and ring are input/output members the unit is
a “solar” gear.

The range of speed reduction ratios for which these units can be designed with
reasonable proportions is as follows:

  Planetary Gear:  3:1 to 12:1
  Star Gear:  2:1 to 11:1
  Solar Gear:  1.2:1 to 1.7:1

Below these ranges the planet gears become quite small and it becomes difficult to
design the gears and planet bearings for reasonable life.  Above these ranges the sun
gear becomes small and the number of planets that can be used without interference
is limited.  This, again, makes the design of the bearings difficult.  Ratios between
1.7:1 and 2:1 are difficult to design successfully with simple epicyclic gearing,
although it can be done with compound epicyclic units.  (See UTS model 60-1162 for
Compound Epicyclic Gearing.)

Epicyclic units are often used as differentials.  UTS model 60-1161 is restricted to
systems in which one element is fixed and does not consider use as a differential.
UTS models 60-1163 and 60-1164 treat simple and compound epicyclic units used as
differentials.

UTS Integrated Gear Software
 2

If more than one planet gear is used the number of planets that will assemble
between the sun and ring is limited by the numbers of teeth in the sun and ring and
by the possibility of interference between the tips of the planet gear teeth.  For a
number of planets to assemble equally spaced around the center, the sum of the tooth
numbers in the ring and sun divided by the number of planets used must be an
integer:

  (Nring+Nsun)/np = integer

  where: Nring =  Number of teeth in ring gear
   Nsun =  Number of teeth in sun gear
     np =  Number of planet gears

The distance between the planet gear centers in the carrier must, of course, be
greater than the outside diameter of the planet gears or tooth tip interference will
result (assuming the planet gears are in the same plane).

It is not necessary that the planets be equally spaced.  However, to make assembly
possible, they must be spaced at multiples of the “Least mesh angle”.

 ep/β = integer

  β = 360º/(Nring+Nsun)

 where:  ep  =  Angle between adjacent planet gears, deg
β  =  Least mesh angle, deg

For example, suppose we have an epicyclic set with Nring = 68 teeth and Nsun = 18 teeth
and we wish to use 4 planets arranged 90 degrees apart.  (Nring+Nsun)/4 = 21.5, which
is not an integer so we cannot arrange 4 planets 90 degrees apart.(Nring+Nsun)/2 = 43
which is an integer so we can arrange 2 planets 180 degrees apart.  The least mesh
angle, β =360 degrees/(Nring+Nsun) = 4.186 degrees.  When we attempt to place a planet
90 degrees from the first planet we find that we are at 90 degrees/ β = 21.5 least
mesh angles and cannot assemble.  We can, however, place the planet at 21 or 22
least mesh angles.  This would put the planet gear at .5 β or 2.093 degrees from 90
degrees.  Then, because we know that 2 planets will assemble 180 degrees apart, the
4 planets would be placed at 0 degrees, 87.907 degrees, 180 degrees and 267.907
degrees.  The tip clearance should then be checked.  Because we have two sets of
planets 180 degrees apart the (theoretical) summation of the bearing loads on the
sun and ring is still zero.
 60-1161—Simple Epicyclic Gear Design (Parallel Axis)

3

It is not necessary (or even desirable) that Nring = Nsun+ 2·Nplanet.If this relationship is
met and the center distance is “standard” then the operating pressure angles at the
sun/planet external mesh, φ
ext, and the planet/ring internal mesh, φ
int, will be equal to
the nominal pressure angle of the system.  If φ
ext is made higher than nominal and φint
lower than nominal it will increase the strength of the set and reduce the burst stress
on the ring.  φ
ext and φ
int can be easily controlled by the number of planet teeth and
the operating center distance.

Examples

If you are using model 60-1161 for the first time you may wish to run the following
example.

Assume we wish to design a spur gear planetary set with about 4.95 to 1 reduction
ratio with a ring gear diameter of about 8 inches.  Also, assume the smallest number
of teeth we wish to use is about 17.  (The number of teeth would be selected according
to material and duty cycle;-see UTS model 60-180.)

In the wizard data input form, enter 17 in the input column for “Sun Gear Teeth” and
4.95 for “Planetary Gear” ratio.  The data input form is shown in Figure 1, the
solution in Report 1.

UTS Integrated Gear Software
 4

Fig. 1

  Report 1

  Model Title :  Program 60-1161
 Unit System:  US

  ERROR MESSAGE, internal mesh

  ERROR MESSAGE, external mesh

  ERROR MESSAGE, mesh - general

  Prime factors greater than 100  unknown

  NUMBER OF TEETH

  Ring Gear Teeth  67

60-1161—Simple Epicyclic Gear Design (Parallel Axis)

5

  Model Title :  Program 60-1161
 Unit System:  US

  Planet Gear Teeth  25

  Sun Gear Teeth  17

 RATIOS

  Planetary Gear (Forward rotation)  4.9500

  Star Gear (Reverse rotation)  3.9500

  Solar Gear (Forward rotation)  1.2532

 Planet/Sun Ratio  1.4750

 Ring/Planet Ratio  2.6780

With 17 teeth in the sun and a planetary ratio of about 4.95, we need about 67 teeth
in the ring.  Enter 67 for the ring gear and blank the ratio.  Enter 8 for the operating
pitch diameter of the ring gear.  The completed data input form is shown in Figure 2,
the solved model in Report 2.

UTS Integrated Gear Software
 6

Fig. 2

Report 2

  Model Title :  Program 60-1161
 Unit System:  US

  ERROR MESSAGE, internal mesh

  ERROR MESSAGE, external mesh

  ERROR MESSAGE, mesh - general

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  67

60-1161—Simple Epicyclic Gear Design (Parallel Axis)

7

  Model Title :  Program 60-1161
 Unit System:  US

  Planet Gear Teeth  25

  Sun Gear Teeth  17

 RATIOS

  Planetary Gear (Forward rotation)  4.9412

  Star Gear (Reverse rotation)  3.9412

  Solar Gear (Forward rotation)  1.2537

 Planet/Sun Ratio  1.4706

 Ring/Planet Ratio  2.6800

  CENTER DISTANCE & PRESSURE ANGLES

  Operating Center Distance  2.508 in

  Mid-point Center Distance  2.508 in

  Opr Press Angle - Sun/Planet Mesh  deg

  Opr Press Angle - Ring/Planet Mesh  deg

  NUMBER OF EQUALLY SPACED PLANETS

 P1

 P2

 P3

 P4

 PLANET SPACING

  Least mesh angle  4.2857 deg

  NOMINAL PITCH & PRESSURE ANGLE

 Normal Pitch  1/in

  Normal Pressure Angle  deg

 Helix Angle  deg

UTS Integrated Gear Software
 8

  Model Title :  Program 60-1161
 Unit System:  US

 Transverse Pitch  8.375000 1/in

  Transverse Press Angle  deg

 Normal Module  mm'

 Transverse Module  3.0328358208955 mm'

  OPERATING PITCH DIAMETERS

 Ring gear  8.000 in

  Planet with ring gear  2.985 in

  Planet with sun gear  2.985 in

 Sun gear  2.030 in

The ratio with this arrangement is 4.9412 and the transverse pitch is 8.375.  We will
use 8 normal pitch, 20 degrees normal pressure angle and 0 degrees helix angle.
Enter these values, blank the 8 inch ring pitch diameter and solve.  The completed
data input form is shown in Figure 3, the solved model in Report 3.

60-1161—Simple Epicyclic Gear Design (Parallel Axis)

9

Fig. 3

Report 3

  Model Title :  Program 60-1161
 Unit System:  US

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  67

UTS Integrated Gear Software
 10

  Model Title :  Program 60-1161
 Unit System:  US

  Planet Gear Teeth  25

  Sun Gear Teeth  17

 RATIOS

  Planetary Gear (Forward rotation)  4.9412

  Star Gear (Reverse rotation)  3.9412

  Solar Gear (Forward rotation)  1.2537

 Planet/Sun Ratio  1.4706

 Ring/Planet Ratio  2.6800

  CENTER DISTANCE & PRESSURE ANGLES

  Operating Center Distance  2.625 in

  Mid-point Center Distance  2.625 in

  Opr Press Angle - Sun/Planet Mesh  20.0000 deg

  Opr Press Angle - Ring/Planet Mesh  20.0000 deg

  NUMBER OF EQUALLY SPACED PLANETS

 P1  2

 P2  3

 P3  4

 P4  #

 PLANET SPACING

  Least mesh angle  4.2857 deg

  NOMINAL PITCH & PRESSURE ANGLE

 Normal Pitch  8.000000 1/in

  Normal Pressure Angle  20.000000 deg

 Helix Angle  0.000000 deg

60-1161—Simple Epicyclic Gear Design (Parallel Axis)

11

  Model Title :  Program 60-1161
 Unit System:  US

 Transverse Pitch  8.000000 1/in

  Transverse Press Angle  20.000000 deg

 Normal Module  3.175 mm'

 Transverse Module  3.175 mm'

  OPERATING PITCH DIAMETERS

 Ring gear  8.375 in

  Planet with ring gear  3.125 in

  Planet with sun gear  3.125 in

 Sun gear  2.125 in

  RATIO RANGE: (Speed Reduction Gears)

  Planetary Range (Normal = 3 to 12)  normal

  Star Range (Normal = 2 to 11)  normal

  Solar Range (Normal = 1.2 to 1.7)  normal

With a 25 tooth planet gear and a center distance of 2.625 inches, φ
ext and φint are both
“standard” at 20 degrees.  (The “Operating Center Distance” is defaulted to the “Mid-
Point Center Distance” if the operating center distance is not entered.  If the sun and
ring are both odd or both even the mid-point distance will be “standard”.)  We can
assemble 2, 3 or 4 planet gears with equal spacing.

Since we want φ
ext to be about 25 degrees, we need to change the number of planet
teeth.  (In this case, the condition Nring = Nsun +2·Nplanet is met.)  Enter 24 for the
number of planet teeth and solve (Report 4).

UTS Integrated Gear Software
 12

Report 4

  Model Title :  Program 60-1161
 Unit System:  US

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  67

  Planet Gear Teeth  24

  Sun Gear Teeth  17

 RATIOS

  Planetary Gear (Forward rotation)  4.9412

  Star Gear (Reverse rotation)  3.9412

  Solar Gear (Forward rotation)  1.2537

 Planet/Sun Ratio  1.4118

 Ring/Planet Ratio  2.7917

  CENTER DISTANCE & PRESSURE ANGLES

  Operating Center Distance  2.625 in

  Mid-point Center Distance  2.625 in

  Opr Press Angle - Sun/Planet Mesh  23.4628 deg

  Opr Press Angle - Ring/Planet Mesh  15.8319 deg

 60-1161—Simple Epicyclic Gear Design (Parallel Axis)

13

  Model Title :  Program 60-1161
 Unit System:  US

  NOMINAL PITCH & PRESSURE ANGLE

 Normal Pitch  8.000000 1/in

  Normal Pressure Angle  20.000000 deg

 Helix Angle  0.000000 deg

This brings φ
ext up to about 23.5 degrees and φ
int down to about 15.8 degrees.  A small
change in operating center distance should finish the job.  Enter 2.65 for the
operating center distance and solve once again (Figure 4 and Report 5).

Fig. 4

UTS Integrated Gear Software
 14

Report 5

  Model Title :  Program 60-1161
 Unit System:  US

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  67

  Planet Gear Teeth  24

  Sun Gear Teeth  17

 RATIOS

  Planetary Gear (Forward rotation)  4.9412

  Star Gear (Reverse rotation)  3.9412

  Solar Gear (Forward rotation)  1.2537

 Planet/Sun Ratio  1.4118

 Ring/Planet Ratio  2.7917

  CENTER DISTANCE & PRESSURE ANGLES

  Operating Center Distance  2.650 in

  Mid-point Center Distance  2.625 in

  Opr Press Angle - Sun/Planet Mesh  24.6785 deg

  Opr Press Angle - Ring/Planet Mesh  17.6380 deg

  NUMBER OF EQUALLY SPACED PLANETS

 P1  2

 P2  3

 P3  4

 P4  #

60-1161—Simple Epicyclic Gear Design (Parallel Axis)

15

  Model Title :  Program 60-1161
 Unit System:  US

 PLANET SPACING

  Least mesh angle  4.2857 deg

  NOMINAL PITCH & PRESSURE ANGLE

 Normal Pitch  8.000000 1/in

  Normal Pressure Angle  20.000000 deg

 Helix Angle  0.000000 deg

 Transverse Pitch  8.000000 1/in

  Transverse Press Angle  20.000000 deg

 Normal Module  3.175 mm'

 Transverse Module  3.175 mm'

  OPERATING PITCH DIAMETERS

 Ring gear  8.258 in

  Planet with ring gear  2.958 in

  Planet with sun gear  3.102 in

 Sun gear  2.198 in

  RATIO RANGE: (Speed Reduction Gears)

  Planetary Range (Normal = 3 to 12)  normal

  Star Range (Normal = 2 to 11)  normal

  Solar Range (Normal = 1.2 to 1.7)  normal

  APPROXIMATE GEAR MESH EFFICIENCY

  External mesh loss (gears only)  0.500 %

  Internal mesh loss (gears only)  0.19 %

 Planetary efficiency  99.45 %

 Star efficiency  99.31 %

 Solar efficiency  99.86 %

  RELATIVE POWER (% of input power)

 Planetary  79.76 %

 Star  100.00 %

UTS Integrated Gear Software
 16

  Model Title :  Program 60-1161
 Unit System:  US

 Solar  20.24 %

  REACTION TORQUE (% of input torque)

 Planetary  394.12 %

 Star  494.12 %

 Solar  25.37 %

  OUTPUT TORQUE (% of input torque)

 Planetary  494.12 %

 Star  394.12 %

 Solar  125.37 %

This completes the solution and all design data for the geometry of the epicyclic gear
set is solved for in the model.  Note that there are no error or caution messages in the
error message block.  Of course, this is not the only solution to this design problem.
The model was solved progressively to obtain this solution.  With the ”backsolving”
capability of TK Solver you may wish to investigate other solutions.

NOTE:  The relative power of a true epicyclic unit is often misunderstood.  The input,
output and reaction torques of any gear unit must balance.  The carrier of a
planetary or solar reduction unit is rotating in the same direction as the input
member.  Therefore, the mesh velocity of the teeth is less than in a non-epicyclic
gear.  The power at the teeth is a product of load and linear velocity.  Since the linear
velocity is less than rotation speed multiplied by pitch radius, the relative power is
less than the shaft transmitted power.  When relative power is used in calculations
the relative speed must also be used.
