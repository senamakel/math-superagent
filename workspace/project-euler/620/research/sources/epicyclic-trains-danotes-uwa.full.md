<!-- source: https://danotes.mech.uwa.edu.au/gears/epicyclic/epicyclic.html | converted from HTML -->

DANotes: Spur Gears: Epicyclic trains

```

```

### Epicyclic gear trains

```

```

An epicyclic train is often suitable when a large torque/speed ratio is required in a compact envelope. It is made up of a number of &#160 *elements*which are interconnected to form the train. Each element consists of the three &#160 *components*illustrated below :

- a &#160 *central gear*( **c**) which rotates at angular velocity &#160 &omega; c about the fixed axis O-O of the element, under the action of the torque &#160 T c applied to the central gear's integral shaft; this central gear may be either an **external**gear (also referred to as a *sun*gear) Fig 1a, or an **internal**gear, Fig 1b
- an &#160 *arm*( **a**) which rotates at angular velocity &#160 &omega; a about the same O-O axis under the action of the torque, &#160 T a - an axle A rigidly attached to the end of the arm carries
- a &#160 *planet gear*( **p**) which rotates freely on the axle A at angular velocity &#160 &omega; p, meshing with the central gear at the pitch point P - the torque &#160 T p acts on the planet gear itself, not on its axle, A.

[image: epicyclic kinetics external][image: epicyclic kinetics internal]

[image: epicyclic gear] [1]
The epicyclic gear photographed here without its arms consists of two elements. The central gear of one element is an external gear; the central gear of the other element is an internal gear. The three identical planets of one element are compounded with ( joined to ) those of the second element.

We shall examine first the angular velocities and torques in a single three-component element as they relate to the tooth numbers of central and planet gears, &#160 z c and z p respectively. The kinetic relations for a complete epicyclic train consisting of two or more elements may then be deduced easily by combining appropriately the relations for the individual elements.

All angular velocities, &#160 &omega;, are absolute and constant, and the torques, &#160 T, are external to the three-component element; for convenience all these variables are taken positive in one particular sense, say anticlockwise as here. Friction is presumed negligible, ie. the system is ideal.

Separate free bodies of each of the three components - including the torques which are applied one to each component - are illustrated in Figs 2a and 2b for the external and internal central gear arrangements respectively. Also shown are the shaft centre &#160 O and axle &#160 A, the radii &#160 R c &#038 R p of the central and planet pitch cylinders, the radius of the arm &#160 R a.

There are two contacts between the components :

- the planet engages with the central gear at the pitch point P where the action / reaction due to tooth contact is the tangential force F t, the radial component being irrelevant;
- the free rotary contact between planet gear and axle A requires a radial force action / reaction; the magnitude of this force at A must also be &#160 F t as sketched, for equilibrium of the planet.

With velocities taken to be positive leftwards for example, we have for the external central gear :

- geometry from Fig 2a : &#160 &#160 &#160 R a &#160 = &#160 R c + R p
- velocity of P : &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 v P &#160 &#160 = &#160 v A + v PA &#160 &#160 so with the given senses : &#160 &#160 &omega; c R c &#160 = &#160 &omega; a R a - &omega; p R p
- torques from Fig 2a : &#160 &#160 &#160 &#160 &#160 F t &#160 &#160 = &#160 -T c / R c &#160 = &#160 -T p / R p &#160 = &#160 T a / R a

and for the internal central gear :

- geometry from Fig 2a : &#160 &#160 &#160 R a &#160 = &#160 R c - R p
- velocity of P : &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 v P &#160 &#160 = &#160 v A + v PA &#160 &#160 so with the given senses : &#160 &#160 &omega; c R c &#160 = &#160 &omega; a R a + &omega; p R p
- torques from Fig 2a : &#160 &#160 &#160 &#160 &#160 F t &#160 &#160 = &#160 -T c / R c &#160 = &#160 T p / R p &#160 = &#160 T a / R a

Substituting for &#160 R a from the geometric equations into the respective velocity and torque equations, and noting that &#160 R c /R p &#160 = &#160 z c /z p, leads to the same result for both internal and external central gear arrangements. These are the desired relations for the three-component element :

( **2a**) &#160 &#160 &#160 &#160 ( &omega; c - &omega; a) z c + ( &omega; p - &omega; a) z p &#160 = &#160 0
( **2b**) &#160 &#160 &#160 &#160 T c / z c &#160 = &#160 T p / z p &#160 = &#160 -T a / ( z c + z p) . . . . in which &#160 z c is taken to be a positive integer for an external central gear, and a negative integer for an internal central gear.

It is apparent that the element has **one**degree of kinetic (torque) freedom since only one of the three torques may be arbitrarily defined, the other two following from the two equations ( **2b**). On the other hand the element possesses **two**degrees of kinematic freedom, as any two of the three velocities may be arbitrarily chosen, the third being dictated by the single equation ( **2a**).

From ( **2b**) the net external torque on the three-component element as a whole is :
&#160 &#160 &#160 &#160 &Sigma;T &#160 = &#160 T c + T p + T a &#160 = &#160 T c { 1 + z p / z c - ( z c + z p)/z c } &#160 &#160 = &#160 0
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 which indicates that equilibrium of the element is assured.

Energy is supplied to the element through any component whose torque and velocity senses are identical. From ( **2**) the total external power being fed into the three-component element is :
&#160 &#160 &#160 &#160 &Sigma;P &#160 = &#160 P c + P p + P a &#160 = &#160 &omega; c T c + &omega; p T p + &omega; a T a &#160 = &#160 T c { &omega; c + &omega; p z p /z c - &omega; a ( z c + z p)/z c }
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160= &#160 T c { ( &omega; c - &omega; a) z c + ( &omega; p - &omega; a) z p } / z c &#160 &#160 = &#160 0
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 confirming that energy is conserved in the ideal element. [image: epicyclic spider]

In practice, a number of identical planets are employed for balance and shaft load minimisation. Since ( **2**) deal only with effects external to the element, this multiplicity of planets is analytically irrelevant provided &#160 T p is interpreted as being the total torque on all the planets, which is shared equally between them as suggested by the sketch here. The reason for the *sun- and- planet*terminology is obvious; the arm is often referred to as the &#160 *spider*or &#160 *planet carrier.*

Application of the element relations to a complete train is carried out as shown in the example which follows. More complex epicyclic trains may be analysed in a similar manner, but the technique is not of much assistance when the problem is one of gear train design - the interested designer is referred to the Bibliography.

---

*EXAMPLE*[image: epicyclic example]

An epicyclic train consists of two three-component elements of the kind examined above. The first element comprises the external sun gear 1 and planet 2; the second comprises the planet 3 and internal ring gear 4. The planets 2 and 3 are compounded together on the common arm axles.
Determine the relationships between the kinetic variables external to the train in terms of the tooth numbers z 1, z 2, z 3 &#038 z 4.

The train is analysed via equations ( **2**) applied to the two elements in turn, together with the appropriate equations which set out the velocity and torque constraints across the interface between the two elements **1-2-arm**and **3-4-arm**. 1-2-arm : ( &omega; 1 - &omega; a) z 1 + ( &omega; 2 - &omega; a) z 2 &#160 = &#160 0 &#160 &#160 &#160 &#160 &#160 &#160 from ( **2a**) T 1 / z 1 &#160 = &#160 T 2 / z 2 &#160 = &#160 - T a2 / ( z 1 + z 2) &#160 &#160 from ( **2b**) 3-4-arm : ( &omega; 4 - &omega; a) ( -z 4) + ( &omega; 3 - &omega; a) z 3 &#160 = &#160 0 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 in which z 4 is a positive integer as T 4 / ( - z 4) &#160 = &#160 T 3 / z 3 &#160 = &#160 - T a3 / ( - z 4 + z 3) &#160 &#160 &#160 central gear is internal T a2 and T a3 are the parts of the total external torque on the arm, T a, which are applied individually to the two elements &#160 1-2-arm and 3-4-arm. Interface : &omega; 3 &#160 = &#160 &omega; 2 &#160 &#160 &#160 since the planets 2 &#038 3 are coupled T 3 &#160 = &#160 - T 2 &#160 &#160 &#160 since the planets 2 &#038 3 are coupled (action/reaction) T a &#160 = &#160 T a2 + T a3 &#160 &#160 as the arm is common to both elements 1-2-arm and 3-4-arm

*Solution*:
The &#160 *basic speed ratio,***i**o, of an epicyclic train is defined as the ratio of input to output speeds when the arm is held stationary.
Neither input nor output is defined here - indeed this terminology can be confusing with multiple degrees of freedom - so for example select gear 1 as input, gear 4 as output.
It follows that &#160 **i**o &#160 = &#160 ( &omega; 1 / &omega; 4) &omega; a =0.
Solving the three velocity equations and the six torque equations leads to the desired relations :
&#160 &#160 &#160 &#160 &#160 &#160 Velocities : &#160 &#160 ( &omega; 1 - &omega; a ) &#160 = &#160 i o ( &omega; 4 -&omega; a ) &#160 &#160 &#160 &#160 where i o = - z 2 z 4 /z 1 z 3
&#160 &#160 &#160 &#160 &#160 &#160 Torques &#160 &#160 : &#160 &#160 T 1 &#160 = &#160 -T 4 /i o &#160 = &#160 T a /( i o - 1 )
Evidently this train possesses the same degrees of freedom as an individual element.

---

```

```

| &#160 ****[Notes contents][2] &#160 | &#160 ****[chapter index][3] &#160 | &#160 ****[previous][4] &#160 | &#160 **top of page**&#160 | &#160 ****[next][5] &#160 |

---

[image: Valid HTML 4.0!] &#160 &#160 Copyright 1999-2005 Douglas Wright
&#160 &#160 *last updated May 2005*

&#160


## Links

[1]: epicyclicBIG.jpeg
[2]: ../../intro/contents.html#top
[3]: ../home.html#top
[4]: ../intro/intro.html#top
[5]: ../toothForm/toothForm.html#top
