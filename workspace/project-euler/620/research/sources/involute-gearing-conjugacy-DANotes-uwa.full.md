<!-- source: https://danotes.mech.uwa.edu.au/gears/toothForm/toothForm.html | converted from HTML -->

DANotes: Spur gears: Conjugacy of involute teeth

```

```

### Conjugate tooth action

We have seen that one essential for correctly meshing gears is that the size of the teeth ( the module ) must be the same for the two gears. We now examine another requirement - [image: conjugacy requirements] the shape of teeth necessary for the speed ratio to remain constant during an increment of rotation; this behaviour of the contacting surfaces (ie. the teeth flanks) is known as *conjugate action.*

Consider the two rigid bodies 1 and 2 which rotate about fixed centres, O, with angular velocities &omega;. The bodies touch at the contact point, C, through which the common tangent and normal are drawn.
The absolute velocity v of the contact point reckoned as a point on either body, is perpendicular to the radius from that body's centre O to the contact point. For the bodies to remain in contact, there must be no component of relative motion along the common normal, so that from the velocity triangles :-
&#160 &#160 &#160 &#160 &#160 &#160 v 2 cos&theta; 2 &#160 = &#160 v 1 cos&theta; 1 &#160 &#160 &#160 where &#160 v 1 = &omega; 1 . O 1 C &#160 ; &#160 &#160 &#160 v 2 = &omega; 2 . O 2 C
Note that the tangential components of velocity are generally different, so sliding must occur. For the speed ratio to be constant therefore, from the above and similar triangles :-

( **3**) &#160 &#160 &#160 &omega; 2 /&omega; 1 &#160 = &#160 v 2 . O 1 C/v 1 . O 2 C &#160 = &#160 O 1 C.cos&theta; 1 /O 2 C.cos&theta; 2
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 = &#160 O 1 C 1 /O 2 C 2 &#160 = &#160 O 1 P / O 2 P &#160 &#160 &#160 ie. this ratio also must be constant.
This indicates that, since the centres are fixed, *the point P is fixed*too.

In general therefore, whatever the shapes of the bodies, the contact point C will move along some locus as rotation proceeds; but if the action is to be conjugate then the body geometry must be such that the common normal at the contact point passes always through one unique point lying on the line of centres - this point is the pitch point referred to above, and the pitch circles' radii are O 1 P and O 2 P.

There exists a host of shapes which ensure conjugacy - indeed it is possible, within certain restrictions, to arbitrarily choose the shape of one body then determine the shape of the second necessary for conjugacy. But by far the most common gear geometry which satisfies conjugacy is based on *the involute,*in which case both gears are similar in form, and the contact point's locus is a simple straight line - the *line of action.*

```

```

[image: string unwinding from fixed base cylinder]

### The involute tooth

```

```

One method of generating an involute is shown in Fig A. A generating cord, in which there is a knot C, is wrapped around a fixed cylinder - the *base cylinder*(idiomatically circle ) of radius R o.
When the taut cord is subsequently unwound as shown in this ****[animation][1], the knot traces out an involute whose polar coordinates may be expressed implicitly in terms of the variable generating angle &psi;, reckoned from the radius through the initial knot position, C**'**. The coordinate origin is taken at the circle centre, O, with a fixed reference direction defined at some constant angle &gamma;, also from the initial radius. The tangent, TC, is normal to the involute at C, and since the tangent length TC is equal to the arc length TC**'**, the polar coordinates of C ( r, &theta;) are :-

( **4**) &#160 &#160 &#160 r &#160 = &#160 R o √ ( 1 + &psi; 2 ) &#160 ; &#160 &#160 &#160 &theta; &#160 = &#160 &gamma; - &psi; + arctan &psi; [image: string unwinding from rotating base cylinder]

In order to see how the involute leads to gear teeth and conjugate action, we place a slightly different interpretation on the above model.
The cord is wrapped around the base cylinder which in Fig B is now free to rotate about its centre as the cord is pulled off in a fixed direction. This fixed cord direction forms the line of action, tangent to the base cylinder at the fixed point T, and clearly satisfies conjugacy by cutting the fixed reference at the fixed pitch point P through which the pitch cylinder passes. The line of action is inclined to the pitch point tangent at the *pressure angle,*&alpha;. The knot C always moves along the line of action, tracing out an involute with respect to the rotating cylinder. The relation between the base and pitch circle radii is evidently :- [image: involute line of action]

( **5**) &#160 &#160 &#160 R o &#160 = &#160 R cos &alpha;

Extending this to two cylinders - representing meshing gears, 1 & 2 Fig C - the taut cord winds off one base cylinder and onto the other to form the line of action inclined at the pressure angle &alpha;. The knot, C, on the mating involutes coincides with the contact point and moves along the line of action as the gears and base cylinders rotate. The pitch cylinders extend to the pitch point P situated at the intersection of the lines of action and of centres.
Evidently the distance between the cylinders does not affect the speed ratio since the base cylinder diameters are fixed.

The distance between knots - ie. between tooth flanks along the line of action, Fig C - is the *base pitch,*p o, given by :-

( **6**) &#160 &#160 &#160 p o &#160 = &#160 &pi; D o / z &#160 = &#160 p cos &alpha; &#160 = &#160 &pi; m cos &alpha; &#160 &#160 &#160 . . . . . from ( **1**)

For continuous motion transfer, at least two pairs of teeth must be in contact as one of the pairs comes into or leaves mesh. The teeth in Fig C are truncated in practice to permit rotation.

Involute generation by knotted cord is all very well conceptually, but hardly practicable as a basis for manufacturing. Only one of the many methods of gear manufacture is considered here - the ****[rack generation][2] technique is fundamental to the understanding of gear behaviour.

```

```

| &#160 ****[Notes contents][3] &#160 | &#160 ****[chapter index][4] &#160 | &#160 ****[previous][5] &#160 | &#160 **top of page**&#160 | &#160 ****[next][6] &#160 |

---

[image: Valid HTML 4.0!] &#160 &#160 Copyright 1999-2005 Douglas Wright
&#160 &#160 *last updated May 2005*

&#160


## Links

[1]: involuteAnimation.html
[2]: ../generation/generation.html
[3]: ../../intro/contents.html#top
[4]: ../home.html#top
[5]: ../epicyclic/epicyclic.html#top
[6]: ../generation/generation.html#top
