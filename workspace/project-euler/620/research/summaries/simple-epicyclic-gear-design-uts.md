> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/simple-epicyclic-gear-design-uts.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 11155 characters not shown — see `research/sources/simple-epicyclic-gear-design-uts.full.md`]*
