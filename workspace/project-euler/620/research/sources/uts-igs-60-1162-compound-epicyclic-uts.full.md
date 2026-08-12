<!-- source: https://www.uts.com/resources/IGS/IGS60-1162.pdf | converted from PDF -->

Program 60-1162—Compound Epicyclic Gear Design
(Parallel Axis)
Introduction

The compound epicyclic gear unit consists of a central external gear (sun gear)
meshed with one or more external gears (sun planet gears).  The sun planet gears are
part of a two-gear cluster on the same shaft or axis.  The second gear is the ring
planet gear.  The ring planet gears are then meshed with an internal gear (ring gear)
which encloses the system.  The planet gears and planet gear support bearings are
held in a carrier which rotates about the geometrical center of the unit.(The term
“epicyclic” comes from the path of a point on a planet gear which traces out an
epicycloid in space.)

There are three basic types of compound epicyclic gear units.

•  Planetary:  When the ring gear is fixed or grounded and the sun and carrier are
input/output members the unit is called a “planetary gear”.

•  Star:  When the carrier is fixed and the sun and ring are input/output members
the unit is a “star” gear.  The star gear is not an epicyclic gear as the planet gear
centers do not rotate about the unit central axis but since the construction is
basically the same it is included in the family.  For high speed units the star gear
is often used in cases where planetary gears are not practical because of the high
centripetal acceleration loads on the planet gears.

•  Solar:  When the sun is fixed and the carrier and ring are input/output members
the unit is a “solar” gear.

The range of speed reduction ratios for which these units can be designed with
reasonable proportions is as follows:

  Planetary Gear:   6:1 to 25:1
  Star Gear:        5:1 to 24:1
  Solar Gear:    1.05:1 to 2.2:1

Below these ranges the planet gears become quite small and it becomes difficult to
design the gears and planet bearings for reasonable life.  Above these ranges the sun
gear becomes small and the number of planets that can be used without interference
is limited.  This, again, makes the design of the bearings difficult.

If more than one planet gear is used, the number of planets that will assemble
between the sun and ring is limited by the numbers of teeth in the gears and by the
possibility of interference between the tips of the planet gear teeth.  For a number of

UTS Integrated Gear Software
 2

identical planets to assemble equally spaced around the center, the following
relationship between the tooth numbers in the gears must be met:

[(Nring·Npl-sun )+(Nsun·Npl-ring)]/np =integer

 where:   Nring   = Number of teeth in ring gear
Npl-sun   = Number of teeth in sun gear planet
   Nsun   = Number of teeth in sun gear
Npl-ring   = Number of teeth in ring gear planet
   np  = Number of planet gears

The distance between the planet gear centers in the carrier must, of course, be
greater than the outside diameter of the planet gears or tooth tip interference will
result (assuming the planet gears are in the same plane).

It is not necessary that the planets be equally spaced.  However, to make assembly
possible, they must be spaced at multiples of the “least mesh angle”.

 ep/β = integer

  β = 360° / [(Nring·Npl-sun )+(Nsun·Npl-ring)]

  where:  ep  = Angle between adjacent planet gears, deg

β   = Least mesh angle, deg

It is not necessary (or even desirable) that PDring = PDsun+PDpl-sun+PDpl-ring (where PD =
Teeth/(TransPitch)).  If this relationship is met, the center distance is “standard” and
the operating pressure angles at the sun/planet external mesh, φ
ext, and the
planet/ring internal mesh, φ
int,will be equal to the nominal pressure angle of the
systems.  A higher operating pressure angle at the external mesh, φ
ext, will often
increase the strength of the gear set while not affecting the operating characteristics
of the mesh adversely.  (If the ring gear rim thickness is 2 tooth depths or more, a
highφ
int will tend to reduce the bending stress.  If the ring gear rim thickness is 1.5
tooth depths or less, a low φ
int will tend to reduce the bending stress.)

Epicyclic units are often used as differentials.  UTS model 60-1162 is restricted to
systems where one element is fixed, and it does not consider use as a differential.
UTS models 60-1163 and 60-1164 treat simple and compound epicyclic units used as
differentials.
 60-1162—Compound Epicyclic Gear Design (Parallel Axis)

3

Examples

If you are using model 60-1162 for the first time you may wish to run the following
example.

Assume we wish to design a spur gear compound planetary set with about 15.5 to 1
reduction ratio with a ring gear diameter of about 12 inches.  Assume also that the
smallest number of teeth we wish to use is 20 for the sun gear and 28 for the internal
mesh planetary gears.  (The number of teeth would be selected based upon material
and duty cycle.  See UTS model 60-180.)

Open a new analysis in 60-1162.  Enter 20 in the input column for “Sun Gear Teeth”,
28 for “Ring Planet Teeth” and 15.5 for “Planetary Gear” ratio.  Figure 1 shows the
data input form with this data.  Report 1 shows the solution.

Fig. 1

UTS Integrated Gear Software
 4

Report 1

  Model Title :  Program 60-1162
 Unit System:  US

 MESSAGE FIELD

  ERROR MESSAGE, internal mesh

  ERROR MESSAGE, external mesh

  ERROR MESSAGE, mesh - general

  Prime factors greater than 100

  NUMBER OF TEETH

  Ring Gear Teeth

  Ring Planet Teeth (Internal mesh)  28

  Sun Planet Teeth (External mesh)

  Sun Gear Teeth  20

 RATIOS

  Planetary Gear (Forward rotation)  15.5000

  Star Gear (Reverse rotation)

  Solar Gear (Forward rotation)

 Planet/Sun Ratio

 Ring/Planet Ratio

  EXTERNAL MESH (SUN/PLANET)

 Normal Pitch  1.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

5

  Model Title :  Program 60-1162
 Unit System:  US

 Transverse Pitch  1.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  25.4 mm'

 Transverse Module  25.4 mm'

  Opr Pitch Dia, planet  in

  Opr Pitch Dia, sun gear  in

  INTERNAL MESH (RING/PLANET)

 Normal Pitch  1.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  1.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  25.4 mm'

 Transverse Module  25.4 mm'

  Opr Pitch Dia, ring gear  in

  Opr Pitch Dia, planet  in

The model has set the normal diametral pitch to 1, the normal pressure angle to 20
degrees and the helix angle to 0 degrees since no values were input.  A solution for
the numbers of teeth in the ring gear and sun planet gears requires an iterative
solution, since the equations solved in this direction cannot be solved directly.
We also need to temporarily fix an operating pitch diameter to provide enough input
for the solution.  For now we will set the operating pitch diameter of the sun to the
“standard” pitch diameter.

To do this we must work directly in the TK Solver Variable Sheet.  Toggle to this,
move the mouse pointer to the input column for “Opr Pitch Dia, sun gear” and type
“ns/pt_s”.  When you press the enter key you should have 20 in the input column.  We
will make a guess of 100 teeth for the ring gear.  Type 100 in the input column for
this variable.  Move the mouse pointer to the status column and type “G”, or double-
click the Status cell and pick “Guess” from the drop-down list that appears.  This will

UTS Integrated Gear Software
 6

tell TK  to start an iteration with a first guess of 100.  Your screen should be like
Sheet 1.

Sheet 1
 60-1162 COMPOUND EPICYCLIC (Ver 6.01)

Use ‘Tools’, ‘GwzUnits’ to Change Units

m_i ERROR MESSAGE, internal mesh
m_x ERROR MESSAGE, external mesh
m_g ERROR MESSAGE, mesh - general
m_p Prime factors greater than 100

NUMBER OF TEETH:
G 100 nr Ring Gear Teeth
28 np_r Ring Planet Teeth (Internal mesh)
np_s Sun Planet Teeth (External mesh)
20 ns Sun GearTeeth

RATIOS:
15.5 pl_mg Planetary Gear (Forward rotation)
st_mg StarGear (Reverse rotation)
sl_mg SolarGear (Forward rotation)
mx Planet/Sun Ratio
mi Ring/Planet Ratio

opr_cd in Operating Center Distance
std_cds in "Standard" CD - External mesh
std_cdr in "Standard" CD - Internal mesh
tpa_x deg Opr Press Angle - External mesh
tpa_i deg Opr Press Angle - Internal mesh

RATIO RANGE: (Speed Reduction Gears)
ms_pl Planetary Range (Normal=6to25)
In: Sun Fixed: Ring Out: Carrier
ms_st Star Range (Normal=5to24)
In: Sun Fixed: Carrier Out: Ring
ms_sl Solar Range (Normal = 1.05 to 2.2)
In: Ring Fixed: Sun Out: Carrier
PLANETSPACING:
lma deg Least mesh angle (IDENTICAL planets
must be spaced at increments of
the least mesh angle for assembly)
NUMBER OF EQUALLY SPACED PLANETS
p1 (These are the 1st 4 up to 50 that
p2 will assemble without interference -
p3 planets will assemble equally if
p4 (ring*sun planet)+(sun*ring planet)
divided by planets is an integer
EXTERNAL MESH (Sun/Planet):
pn_s 1 1/in Normal Pitch
npa_s 20 deg Normal Pressure Angle
ha_s 0 deg Nominal helix Angle
pt_s 1 1/in Transverse Pitch
tpa_s 20 deg Transverse Press Angle

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

7

mod_n_s 25.4 mm Normal Module
mod_t_s 25.4 mm Transverse Module
opr_pdp in Opr Pitch Dia, planet
20 opr_pds in Opr Pitch Dia, sun gear

Solve and you should have Report 2.

Report 2

  Model Title :  Program 60-1162
 Unit System:  US

 MESSAGE FIELD

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  non_integer_teeth

  Prime factors greater than 100  unknown

  NUMBER OF TEETH

  Ring Gear Teeth  117

  Ring Planet Teeth (Internal mesh)  28

  Sun Planet Teeth (External mesh)  69

  Sun Gear Teeth  20

 RATIOS

  Planetary Gear (Forward rotation)  15.5000

  Model Title :  Program 60-1162
 Unit System:  US

  Star Gear (Reverse rotation)  14.5000

UTS Integrated Gear Software
 8

Solar Gear (Forward rotation)  1.0690

 Planet/Sun Ratio  3.4626

 Ring/Planet Ratio  4.1876

  EXTERNAL MESH (SUN/PLANET)

  Opr Pitch Dia, sun gear  20.0000 in

With 20 teeth in the sun, 28 teeth in the ring planet and a planetary ratio of about
15.5 we need about 117 teeth in the ring and about 69 teeth in the sun planet.  We
enter the tooth numbers and blank the ratio and the operating pitch diameter of the
sun.  The completed data input form is shown in Figure 2.

 60-1162—Compound Epicyclic Gear Design (Parallel Axis)

9

Fig. 2

When we solve with these numbers, however, we get a general mesh error message.
Enter 118 for the number of ring gear teeth and solve again.  Report 3 shows the
solved model.

UTS Integrated Gear Software
 10

Report 3

  Model Title :  Program 60-1162
 Unit System:  US

 MESSAGE FIELD

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  118

  Ring Planet Teeth (Internal mesh)  28

  Sun Planet Teeth (External mesh)  69

  Sun Gear Teeth  20

 RATIOS

  Planetary Gear (Forward rotation)  15.5393

  Star Gear (Reverse rotation)  14.5393

  Solar Gear (Forward rotation)  1.0688

 Planet/Sun Ratio  3.4500

 Ring/Planet Ratio  4.2143

  Operating Center Distance  44.7500 in

  Standard CD - External mesh  44.5000 in

  Standard CD - Internal mesh  45.0000 in

  Opr Press Angle - External mesh  20.8617 deg

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

11

  Model Title :  Program 60-1162
 Unit System:  US

  Opr Press Angle - Internal mesh  19.1012 deg

  RATIO RANGE (SPEED REDUCTION GEARS)

  Planetary Range (Normal = 6 to 25)  normal

  Star Range (Normal = 5 to 24)  normal

  Solar Range (Normal = 1.05 to 2.2)  normal

 PLANET SPACING

  Least mesh angle  0.0414 deg

  NUMBER OF EQUALLY SPACED PLANETS

  Number of equally spaced  planets  2.0000

  Number of equally spaced  planets  #

  Number of equally spaced  planets  #

  Number of equally spaced  planets  #

This time there is no error message.

The ratio with this arrangement is 15.5393. We can use only 2 equally spaced planets
with this tooth combination.  The unit would share the load between planets better if
we had 3 planets and floated one member.  Increase the number of ring gear teeth to
119 and decrease the number of sun planet teeth to 68 (to hold the ratio about the
same).  Solve again for Report 4.

UTS Integrated Gear Software
 12

Report 4

  Model Title :  Program 60-1162
 Unit System:  US

 MESSAGE FIELD

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  119

  Ring Planet Teeth (Internal mesh)  28

  Sun Planet Teeth (External mesh)  68

  Sun Gear Teeth  20

 RATIOS

  Planetary Gear (Forward rotation)  15.4500

  Star Gear (Reverse rotation)  14.4500

  Solar Gear (Forward rotation)  1.0692

 Planet/Sun Ratio  3.4000

 Ring/Planet Ratio  4.2500

 No Group

  Operating Center Distance  44.7500 in

  Standard CD - External mesh  44.0000 in

  Standard CD - Internal mesh  45.5000 in

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

13

  Model Title :  Program 60-1162
 Unit System:  US

  Opr Press Angle - External mesh  22.4904 deg

  Opr Press Angle - Internal mesh  17.1683 deg

  RATIO RANGE (SPEED REDUCTION GEARS)

  Planetary Range (Normal = 6 to 25)  normal

  Star Range (Normal = 5 to 24)  normal

  Solar Range (Normal = 1.05 to 2.2)  normal

 PLANET SPACING

  Least mesh angle  0.0416 deg

  NUMBER OF EQUALLY SPACED PLANETS

  Number of equally spaced  planets  2.0000

  Number of equally spaced  planets  3.0000

  Number of equally spaced  planets  #

  Number of equally spaced  planets  #

  EXTERNAL MESH (SUN/PLANET)

 Normal Pitch  1.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  1.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  25.4 mm'

 Transverse Module  25.4 mm'

  Opr Pitch Dia, planet  69.1591 in

  Opr Pitch Dia, sun gear  20.3409 in

UTS Integrated Gear Software
 14

  Model Title :  Program 60-1162
 Unit System:  US

  INTERNAL MESH (RING/PLANET)

 Normal Pitch  1.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  1.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  25.4 mm'

 Transverse Module  25.4 mm'

  Opr Pitch Dia, ring gear  117.0385 in

  Opr Pitch Dia, planet  27.5385 in

With this tooth combination we can assemble 3 planets equally spaced around the
axis of the unit. With a normal diametral pitch of 1 the operating pitch diameter of
the ring gear is 117 inches. Since we want about a 12-inch ring, we need to change
the normal pitch to 10.  Input 10 for the normal pitch of both meshes and solve. The
completed data input form is shown in Figure 3, the solved model in Report 5.

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

15

Fig. 3

Report 5

  Model Title :  Program 60-1162
 Unit System:  US

 MESSAGE FIELD

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

UTS Integrated Gear Software
 16

  Model Title :  Program 60-1162
 Unit System:  US

  NUMBER OF TEETH

  Ring Gear Teeth  119

  Ring Planet Teeth (Internal mesh)  28

  Sun Planet Teeth (External mesh)  68

  Sun Gear Teeth  20

 RATIOS

  Planetary Gear (Forward rotation)  15.4500

  Star Gear (Reverse rotation)  14.4500

  Solar Gear (Forward rotation)  1.0692

 Planet/Sun Ratio  3.4000

 Ring/Planet Ratio  4.2500

  Operating Center Distance  4.4750 in

  Standard CD - External mesh  4.4000 in

  Standard CD - Internal mesh  4.5500 in

  Opr Press Angle - External mesh  22.4904 deg

  Opr Press Angle - Internal mesh  17.1683 deg

  RATIO RANGE (SPEED REDUCTION GEARS)

  Planetary Range (Normal = 6 to 25)  normal

  Star Range (Normal = 5 to 24)  normal

  Solar Range (Normal = 1.05 to 2.2)  normal

 PLANET SPACING

  Least mesh angle  0.0416 deg

 60-1162—Compound Epicyclic Gear Design (Parallel Axis)

17

  Model Title :  Program 60-1162
 Unit System:  US

  NUMBER OF EQUALLY SPACED PLANETS

  Number of equally spaced  planets  2.0000

  Number of equally spaced  planets  3.0000

  Number of equally spaced  planets  #

  Number of equally spaced  planets  #

  EXTERNAL MESH (SUN/PLANET)

 Normal Pitch  10.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  10.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  2.54 mm'

 Transverse Module  2.54 mm'

  Opr Pitch Dia, planet  6.9159 in

  Opr Pitch Dia, sun gear  2.0341 in

  INTERNAL MESH (RING/PLANET)

 Normal Pitch  10.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  10.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  2.54 mm'

 Transverse Module  2.54 mm'

  Opr Pitch Dia, ring gear  11.7038 in

  Opr Pitch Dia, planet  2.7538 in

UTS Integrated Gear Software
 18

With a center distance of 4.475 inches, φext is about 22.5 degrees and φint is about 17
degrees.  (The “Operating Center Distance” is defaulted to the mid-point between the
“standard” center distances for the two meshes if the operating center distance is not
entered.)  If we wish we can use this center distance.  If we want to increase φext and
φint all we need do is increase the operating center distance.  Let's bring φint up to
nominal.  Change the operating center distance to the “standard” center distance for
the internal mesh.  Input 4.55 for the operating center distance and solve.  Figure 4
is the completed data input form and Report 6 shows the result.

Fig. 4

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

19

Report 6

  Model Title :  Program 60-1162
 Unit System:  US

 MESSAGE FIELD

  ERROR MESSAGE, internal mesh  none

  ERROR MESSAGE, external mesh  none

  ERROR MESSAGE, mesh - general  none

  Prime factors greater than 100  none

  NUMBER OF TEETH

  Ring Gear Teeth  119

  Ring Planet Teeth (Internal mesh)  28

  Sun Planet Teeth (External mesh)  68

  Sun Gear Teeth  20

 RATIOS

  Planetary Gear (Forward rotation)  15.4500

  Star Gear (Reverse rotation)  14.4500

  Solar Gear (Forward rotation)  1.0692

 Planet/Sun Ratio  3.4000

 Ring/Planet Ratio  4.2500

  Operating Center Distance  4.5500 in

  Standard CD - External mesh  4.4000 in

  Standard CD - Internal mesh  4.5500 in

  Opr Press Angle - External mesh  24.6718 deg

UTS Integrated Gear Software
 20

  Model Title :  Program 60-1162
 Unit System:  US

  Opr Press Angle - Internal mesh  20.0000 deg

  RATIO RANGE (SPEED REDUCTION GEARS)

  Planetary Range (Normal = 6 to 25)  normal

  Star Range (Normal = 5 to 24)  normal

  Solar Range (Normal = 1.05 to 2.2)  normal

 PLANET SPACING

  Least mesh angle  0.0416 deg

  NUMBER OF EQUALLY SPACED PLANETS

  Number of equally spaced  planets  2.0000

  Number of equally spaced  planets  3.0000

  Number of equally spaced  planets  #

  Number of equally spaced  planets  #

  EXTERNAL MESH (SUN/PLANET)

 Normal Pitch  10.000000 1/in

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  10.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  2.54 mm'

 Transverse Module  2.54 mm'

  Opr Pitch Dia, planet  7.0318 in

  Opr Pitch Dia, sun gear  2.0682 in

  INTERNAL MESH (RING/PLANET)

 Normal Pitch  10.000000 1/in

60-1162—Compound Epicyclic Gear Design (Parallel Axis)

21

  Model Title :  Program 60-1162
 Unit System:  US

  Normal Pressure Angle  20.000000 deg

  Nominal helix Angle  0.000000 deg

 Transverse Pitch  10.0000 1/in

  Transverse Press Angle  20.0000 deg

 Normal Module  2.54 mm'

 Transverse Module  2.54 mm'

  Opr Pitch Dia, ring gear  11.9000 in

  Opr Pitch Dia, planet  2.8000 in

  APPROXIMATE GEAR MESH EFFICIENCY

  External mesh loss (gears only)  0.500 %

  Internal mesh loss (gears only)  0.295 %

 Planetary efficiency  99.26 %

 Star efficiency  99.20 %

 Solar efficiency  99.95 %

  RELATIVE POWER (% OF INPUT)

  Relative power planetary  93.53 %

 Relative power star  100.00 %

 Relative power solar  6.47 %

  REACTION TORQUE (% OF INPUT)

  Reaction torque Planetary  1445.00 %

  Reaction torque star  1545.00 %

  Reaction torque solar  6.92 %

  OUTPUT TORQUE (% OF INPUT)

  Output torque Planetary  1545.00 %

  Output torque star  1445.00 %

  Output torque solar  106.92 %

UTS Integrated Gear Software
 22

φext is now about 24.7 degrees and φint is 20 degrees, which is nominal.  The higher
pressure angle at the external mesh will result in lower bending and compressive
stress and, since the number of load cycles imposed on the external mesh is higher
than the internal mesh, this might be an advantage.

This completes the solution, and all design data for the geometry of the gear set is
solved for in the model.  Note that there are no error or caution messages in the error
message block.  Of course, this is not the only solution to this design problem.  The
model was solved progressively to obtain this solution.  With the “backsolving”
capability of TK Solver, you might wish to investigate other solutions.

To consider K-factor and unit loads at the same time as the unit geometry, see UTS
gear model 60-1164.

NOTE:  The relative power of a true epicyclic unit is often misunderstood.  The input,
output and reaction torques of any gear unit must balance.  The carrier of a
planetary or solar reduction unit is rotating in the same direction as the input
number.  Therefore, the mesh velocity of the teeth is less than in a non-eipcyclic gear.
The power at the teeth is a product of load and linear velocity.  Since the linear
velocity is less than rotation speed multiplied by pitch radius, the relative power is
less than the shaft transmitted power.  When relative power is used in calculations,
the relative speed must also be used.
