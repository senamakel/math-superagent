<!-- source: https://danotes.mech.uwa.edu.au/gears/meshing/meshing.html | converted from HTML -->

DANotes: Spur gears: Gear meshing

```

```

### Gear meshing

```

```

Involute gears have the invaluable ability of providing conjugate action when the gears' centre distance is varied either deliberately or involuntarily due to manufacturing and/or mounting errors. [image: extending centre distance, fig H]

The exaggerated effect of this is shown in Fig H for gears manufactured to pressure angle &#160 &alpha; without profile shift. On the left, the gears are mounted at the standard centre distance (the sum of the two standard radii given by ( **1**)) with the "cord" line of action wrapped around the base circles whose radii are given by ( **5**).

On the right of Fig H the gears' centre distance is increased - but since the same generating cord is wrapped around the same base circles then it follows that the speed ratio is unaltered and the same involutes (and hence teeth) are involved. Clearly there are practical limits to centre distance variations - eg. the gears may lose contact completely - however provided these limits are not reached then the pitch point and resulting pitch circles are defined by intersection of the lines of action and of centres, exactly as occurred in Fig C above. From the similar triangles of Fig H :-

( **8**) &#160 &#160 &#160 &#160 &#160 &#160 R' i &#160 = &#160 D' i /2 &#160 = &#160 C.z i /&Sigma;z &#160 = &#160 R oi sec &alpha;' &#160 &#160 &#160 ( i = 1,2 ) &#160 &#160 &#160 using ( **5**)

There is an infinite number of possible centre distances for a given pair of profile shifted gears, however we consider only the particular case known as the *extended centre distance*which corresponds to mutual tangency of the two extended pitch circles mentioned above, that is :-

( **9**) &#160 &#160 &#160 &#160 &#160 &#160 C &#160 = &#160 ( R 1 + s 1 ) + ( R 2 + s 2 ) &#160 = &#160 1 / 2 &Sigma; z + &Sigma; s &#160 &#160 &#160 proportionally, using ( **1**), or
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 = &#160 m ( 1 / 2 &Sigma; z + &Sigma; s ) &#160 &#160 dimensionally.

---

*EXAMPLE*
A pair of 20 o full depth gears mesh at extended centres - the 12 tooth pinion's profile shift is 0.5, the 18 tooth wheel's is 0.4. What are the pitch and addendum diameters of the gears and what is the pressure angle ? [image: dimensional example]

No absolute dimensions are given so it is proportions which are relevant in this example.

From ( **1**) the diameters of the standard pitch circles are &#160 D 1 = 12, &#160 D 2 = 18. Corresponding base circle diameters are &#160 D o1 = 12 * cos20 o = 11.28, &#160 D o2 = 18 * cos20 o = 16.92
The pinion's extended pitch radius is &#160 R 1 +s 1 = 12/2 + 0.5 = 6.5 and similarly the wheel's is &#160 18/2 + 0.4 = 9.4
The extended centre distance is thus ( **9**) 6.5 +9.4 = 15.9

From ( **8**) the actual pitch diameters are &#160 D' 1 = 2 * 15.9 * 12/(12+18) = 12.72 and &#160 D' 2 = 2 * 15.9 * 18/(12+18) = 19.08

Note that the actual pitch circles preserve the velocity ratio : &#160 19.08/12.72 &#160 = &#160 16.92/11.28 &#160 = &#160 18/12 &#160 = &#160 1.5

Also from the geometry and ( **8**) the addendum diameters are &#160 D a1 = 2( 6.5 +1.0) = 15.0, &#160 D a2 = 2( 9.4 +1.0) = 20.8, while the actual pressure angle is &#160 &alpha;' = arcos( D oi /D' i ) = arcos( 16.92/19.08) = 27.5 o

---

Without profile shift, the choice of centre distance is limited by the modules available from the standard list and by integral tooth numbers, however the profile shift sum in ( **9**) provides flexibility in the choice of (extended) centre distance - invaluable in a coaxial reduction for example.

The meshing of typical gears at extended centres is further detailed in Figs I and J which are particularised for the 12:18 drive of the foregoing example.
Fig I shows the initial no-load situation. The gears are mounted so that the extended pitch circles (of radii 6.5 and 9.4 in the example) are mutually tangential with the pinion tooth symmetrically disposed with respect to the wheel inter-tooth space. Tangency of the extended pitch circles implies that the generating rack (shown dashed) is simultaneously tangent to the tooth profiles of both gears, and leads to a gap - an absence of contact - between the pinion tooth and both adjacent wheel teeth.

[image: fig I][image: fig J]

A subsequent on-load state of affairs when the pinion rotates clockwise is shown in Fig J. The taut generating cord (line of action) extends between the tangent points T 1 and T 2 on the base circles. The cord's intersection with the line of centres defines the actual pitch point P - exactly as in Fig H - and in turn the actual pitch circles whose diameters in the particular case are 12.72 and 19.08.

A pinion tooth touches a wheel tooth at the contact point C (the knot) which moves up the line of action and along the teeth faces as rotation proceeds. Since contact cannot occur outside the teeth, it takes place along the line of action only between the points Q 2 and Q 1 on the line of action and inside both addendum circles. The line segment Q 2 Q 1 is named the *path of contact.*

[image: meshing animation]

The animation shows clearly :

- the contact point marching along the line of action
- the path of contact bounded by the two addenda
- the orthogonality between line of action and involute tooth flanks at the contact point
- how load is transferred from one pair of contacting teeth to the next as rotation proceeds
- relative sliding between the teeth - particularly noticable at the beginning and end of contact
- guaranteed tooth tip clearance due to the dedendum exceeding the addendum
- a significant gap between the non-drive face of a pinion tooth and the adjacent wheel tooth

Gears formed by a milling cutter instead of being generated by a rack cutter as above, may exhibit undercutting or interference (which prevents complete rotation of the two gears due to teeth binding) - these faults result from Q 2 for example lying to the left of T 1 in Fig J.

The gap between the non-drive face of the pinion tooth and the adjacent wheel tooth is known as *backlash.*If the rotational sense of the pinion were to reverse, then a period of unrestrained pinion motion would take place until the backlash gap closed and contact with the wheel tooth re-established impulsively. Shock in a torsionally vibrating drive is exacerbated by significant backlash, though a small amount of backlash is provided in all drives to prevent binding due to manufacturing or mounting inaccuracies and to facilitate lubrication. Backlash may be reduced by subtle alterations to tooth profile or by shortening the centre distance from the extended value, however we consider gears meshing only at the extended centre distance.

Continuous motion transfer requires two pairs of teeth in contact at the ends of the path of contact, though there is only one pair in contact in the middle of the path, as in Fig J. The average number of teeth in contact is an important parameter - if it is too low due to the use of inappropriate profile shifts or to an excessive centre distance for example, then manufacturing inaccuracies may lead to loss of kinematic continuity - that is to impact, vibration and noise. The average number of teeth in contact is also a guide to load sharing between teeth; it is termed the *contact ratio,*&#160 &epsilon; &gamma;, given by :-
&#160 &#160 &#160 &#160 &#160 &#160 &epsilon; &gamma; &#160 = &#160 length of path of contact / distance between teeth along the line of action
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 = &#160 Q 2 PQ 1 / base pitch, p o &#160 &#160 &#160 and for extended centres with ( **6**) for the 20 o system :

( **10**) &#160 &#160 &#160 ( 2&pi; cos&alpha; ) &epsilon; &gamma; &#160 = &#160 &Sigma; i = 1,2 √[ ( z i + 2( 1+s i )) 2 - ( z i cos&alpha; ) 2] - √[ ( &Sigma; z + 2 &Sigma; s ) 2 - ( &Sigma; z cos&alpha; ) 2] [image: contact ratio, Fig K]

Gears having a contact ratio below about 1.2 are not normally recommended as the gears themselves, their shafts and bearings would all require especial care in design and manufacture to preserve conjugacy. The effect of tooth number on contact ratio is shown in Fig K for two identical gears with a profile shift which varies between the practical limits of Fig G. Evidently it becomes more difficult to achieve an acceptable contact ratio as tooth numbers decrease - hence the statement above that 12 teeth are the usual minimum. The plot further indicates that contact ratio increases as profile shift decreases.

In design, &Sigma;s is often taken as zero; or, if the centre distance is closely specified, by the selection of &Sigma;s for use in ( **9**) - the individual profile shifts may be estimated from a specified &Sigma;s as follows :-

( **11**) &#160 &#160 &#160 &#160 &#160 &#160 s 1 &#160 = &#160 [ &lambda; z 2 + ( &Sigma; s - &lambda; ) z 1] / &Sigma; z &#160 ; &#160 &#160 &#160 s 2 = &Sigma; s - s 1 &#160 ; &#160 &#160 &#160 where &#160 0.5 &#160 ≤ &#160 &lambda; &#160 ≤ &#160 0.75
&#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 which tends to balance the strengths of the gears.

---

*EXAMPLE*
Outline a procedure for selecting a spur gear pair on kinematic/geometric grounds, for the front end of a general design program whose later segments could examine fatigue and reliability. Input data are : minimum and maximum bounds of speed ratio ( ≥ 1 ) and of extended centre distance ( mm ) while output is : module ( mm), with corresponding tooth numbers, &#160 z 1 &#038 z 2 ( say 12 ≤ z 1 ≤ 25), and profile shifts, &#160 s 1 &#038 s 2, to give a speed ratio and extended centre distance falling within the specified bounds, and a contact ratio no less than some stipulated critical value ( eg. 1.2 ).

The procedure might take the form of a number of nested loops, each assigning a trial value to one of the design variables. For example the outermost loop would select a module from the standard list and the next would assume a trial pinion tooth number between the limits suggested above. The wheel tooth number would be assigned in the next inner loop, corresponding to the pinion teeth and a speed ratio between the specified limits. [image: design example]
The innermost loop would consider both profile shifts simultaneously and is best understood through a graph of s 2 versus s 1, realising that the module and tooth numbers have been settled in outer loops prior to this aspect being examined. The tooth numbers will define practical limits to the profile shifts ( **7**), hence solutions must lie within the known rectangular region of the graph.

In addition to these limitations, there are further bounds, &#160 &Sigma; s c min and &Sigma; s c max, corresponding to the centre distance limits from ( **9**) - these appear as the straight boundaries superimposed on the graph; and a high bound, &Sigma; s e max, corresponding to the critical contact ratio via ( **10**), which appears as the curved boundary. The actual disposition of all these boundaries on the graph - which may or may not enclose a viable solution space - depends of course on the problem in hand and the values of module and tooth numbers assigned in outer loops. Having defined any such solution space, the procedure could output any solution lying within it - any point on the line between the two extreme points 'lo' and 'hi' would appear to be a suitable compromise - or alternatively ( **11**) might be implemented.

---

```

```

Spur gears' fundamental geometry having been discussed, it is appropriate to now consider the kinetics.
The typical question we seek to answer is "What life can be expected from a given pair of gears if a known power is transmitted through them ?"
We therefore start by considering ****[gear failure][1].

```

```

| &#160 ****[Notes contents][2] &#160 | &#160 ****[chapter index][3] &#160 | &#160 ****[previous][4] &#160 | &#160 **top of page**&#160 | &#160 ****[next][5] &#160 |

---

[image: Valid HTML 4.0!] &#160 &#160 Copyright 1999-2005 Douglas Wright
&#160 &#160 *last updated May 2005*

&#160


## Links

[1]: ../failure/failure.html
[2]: ../../intro/contents.html#top
[3]: ../home.html#top
[4]: ../generation/generation.html#top
[5]: ../failure/failure.html#top
