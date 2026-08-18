<!-- source: https://en.wikipedia.org/wiki/Hilbert%27s_sixteenth_problem | converted from HTML -->

Hilbert's sixteenth problem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

On topology of algebraic curves and surfaces

**Hilbert's 16th problem**was posed by [David Hilbert][1] at the [Paris][2] conference of the [International Congress of Mathematicians][3] in 1900, as part of [his list of 23 problems in mathematics][4]. [1]

The original problem was posed as the *Problem of the topology of algebraic curves and surfaces*(*Problem der Topologie algebraischer Kurven und Flächen*).

Actually the problem consists of two similar problems in different branches of mathematics:

- An investigation of the relative positions of the branches of real [algebraic curves][5] of degree *n*(and similarly for [algebraic surfaces][6]).
- The determination of the upper bound for the number of [limit cycles][7] in two-dimensional [polynomial vector fields][8] of degree *n*and an investigation of their relative positions.

The first problem is yet unsolved for *n*= 8. Therefore, this problem is what usually is meant when talking about Hilbert's sixteenth problem in [real algebraic geometry][9]. The second problem also remains unsolved: no upper bound for the number of limit cycles is known for any *n*> 1, and this is what usually is meant by Hilbert's sixteenth problem in the field of [dynamical systems][10].

The Spanish Royal Society for Mathematics published an explanation of Hilbert's sixteenth problem. [2]

## The first part of Hilbert's 16th problem

[[edit][11]]

In 1876, [Harnack][12] investigated [algebraic curves][5] in the [real projective plane][13] and found that curves of degree *n*could have no more than

n 2 − 3 n + 4 2 {\displaystyle {n^{2}-3n+4 \over 2}}[image: {\displaystyle {n^{2}-3n+4 \over 2}}]

separate [connected components][14]. Furthermore, he showed how to construct curves that attained that upper bound, and thus that it was the best possible bound. Curves with that number of components are called [M-curves][15].

Hilbert had investigated the M-curves of degree 6, and found that the 11 components always were grouped in a certain way. His challenge to the mathematical community now was to completely investigate the possible configurations of the components of the M-curves.

Furthermore, he requested a generalization of [Harnack's curve theorem][15] to [algebraic surfaces][6] and a similar investigation of surfaces with the maximum number of components.

## The second part of Hilbert's 16th problem

[[edit][16]]

Here we are going to consider [polynomial vector fields][8] in the [real][17] plane, that is a system of differential equations of the form:

d x d t = P ( x, y), d y d t = Q ( x, y) {\displaystyle {dx \over dt}=P(x,y),\qquad {dy \over dt}=Q(x,y)}[image: {\displaystyle {dx \over dt}=P(x,y),\qquad {dy \over dt}=Q(x,y)}]

where both *P*and *Q*are real polynomials of degree *n*.

These polynomial vector fields were studied by [Poincaré][18], who had the idea of abandoning the search for finding exact solutions to the system, and instead attempted to study the qualitative features of the collection of all possible solutions.

Among many important discoveries, he found that the limit sets of such solutions need not be a [stationary point][19], but could rather be a periodic solution. Such solutions are called [limit cycles][7].

The second part of Hilbert's 16th problem is to decide an upper bound for the number of limit cycles in polynomial vector fields of degree *n*and, similar to the first part, investigate their relative positions.

### Results

[[edit][20]]

It was shown in 1991/1992 by [Yulii Ilyashenko][21] and [Jean Écalle][22] that every polynomial vector field in the plane has only finitely many limit cycles (a 1923 article by [Henri Dulac][23] claiming a proof of this statement had been shown to contain a gap in 1981). This statement is not obvious, since it is easy to construct smooth (C ∞) vector fields in the plane with infinitely many concentric limit cycles. [3]

The question whether there exists a finite upper bound *H*(*n*) for the number of limit cycles of planar polynomial vector fields of degree *n*remains unsolved for any *n*> 1. (*H*(1) = 0 since linear vector fields do not have limit cycles.) [Evgenii Landis][24] and [Ivan Petrovsky][25] claimed a solution in the 1950s, but it was shown wrong in the early 1960s. Quadratic plane vector fields with four limit cycles are known. [3] An example of numerical visualization of four limit cycles in a quadratic plane vector field can be found in. [4] [5] In general, the difficulties in estimating the number of limit cycles by numerical integration are due to the nested limit cycles with very narrow regions of attraction, which are [hidden attractors][26], and semi-stable limit cycles.

## The original formulation of the problems

[[edit][27]]

In his speech, Hilbert presented the problems as: [1]

The upper bound of closed and separate branches of an algebraic curve of degree *n*was decided by Harnack (Mathematische Annalen, 10); from this arises the further question as of the relative positions of the branches in the plane. As of the curves of degree 6, I have – admittedly in a rather elaborate way – convinced myself that the 11 branches, that they can have according to Harnack, never all can be separate, rather there must exist one branch, which have another branch running in its interior and nine branches running in its exterior, or opposite. It seems to me that a thorough investigation of the relative positions of the upper bound for separate branches is of great interest, and similarly the corresponding investigation of the number, shape and position of the sheets of an algebraic surface in space – it is not yet even known, how many sheets a surface of degree 4 in three-dimensional space can maximally have. (cf. Rohn, Flächen vierter Ordnung, Preissschriften der Fürstlich Jablonowskischen Gesellschaft, Leipzig 1886)

Hilbert continues: [1]

{dy \\over dx} = {Y \\over X} </math>\n\nwhere ''X'', ''Y'' are integer, rational functions of ''n''th degree in resp. ''x'', ''y'', or written homogeneously:\n\n:<math>\nX \\left( y {dz \\over dt} - z {dy \\over dt} \\right)\n + Y\\left(z {dx \\over dt} - x {dz \\over dt} \\right)\n + Z\\left(x {dy \\over dt} - y {dx \\over dt} \\right) \n = 0\n</math>\n\nwhere ''X'', ''Y'', ''Z'' means integral, rational, homogenic functions of ''n''th degree in ''x'', ''y'', ''z'' and the latter are to be considered function of the parameter&nbsp;''t''."}},"i":0}}]}"/>

Following this purely algebraic problem I would like to raise a question that, it seems to me, can be attacked by the same method of continuous coefficient changing, and whose answer is of similar importance to the topology of the families of curves defined by differential equations – that is the question of the upper bound and position of the Poincaré boundary cycles (cycles limites) for a differential equation of first order of the form:

d y d x = Y X {\displaystyle {dy \over dx}={Y \over X}}[image: {\displaystyle {dy \over dx}={Y \over X}}]

where *X*, *Y*are integer, rational functions of *n*th degree in resp. *x*, *y*, or written homogeneously:

X ( y d z d t − z d y d t) + Y ( z d x d t − x d z d t) + Z ( x d y d t − y d x d t) = 0 {\displaystyle X\left(y{dz \over dt}-z{dy \over dt}\right)+Y\left(z{dx \over dt}-x{dz \over dt}\right)+Z\left(x{dy \over dt}-y{dx \over dt}\right)=0}[image: {\displaystyle X\left(y{dz \over dt}-z{dy \over dt}\right)+Y\left(z{dx \over dt}-x{dz \over dt}\right)+Z\left(x{dy \over dt}-y{dx \over dt}\right)=0}]

where *X*, *Y*, *Z*means integral, rational, homogenic functions of *n*th degree in *x*, *y*, *z*and the latter are to be considered function of the parameter*t*.

## See also

[[edit][28]]

- [Hilbert–Arnold problem][29]
- [Hilbert's problems][4]

## References

[[edit][30]]

1. 1 2 3 David Hilbert (translated by Maby Winton Newson). ["Mathematical Problems"][31].
2. ↑ ["Sobre el problema 16 de Hilbert"][32].
3. 1 2 Yu. Ilyashenko (2002). ["Centennial History of Hilbert's 16th problem"][33] (PDF). *Bulletin of the AMS*. **39**(3): 301– 354. [doi][34]: [10.1090/s0273-0979-02-00946-1][35].
4. ↑ Kuznetsov N.V.; Kuznetsova O.A.; Leonov G.A. (2011). "Visualization of four normal size limit cycles in two-dimensional polynomial quadratic system". *Differential Equations and Dynamical Systems*. **21**( 1– 2): 29– 33. [doi][34]: [10.1007/s12591-012-0118-6][36]. [S2CID][37] [122896664][38].
5. ↑ Leonov G.A.; Kuznetsov N.V. (2013). ["Hidden attractors in dynamical systems. From hidden oscillations in Hilbert-Kolmogorov, Aizerman, and Kalman problems to hidden chaotic attractor in Chua circuits"][39]. *International Journal of Bifurcation and Chaos in Applied Sciences and Engineering*. **23**(1): 1330002– 219. [Bibcode][40]: [2013IJBC...2330002L][41]. [doi][34]: [10.1142/S0218127413300024][39].

## External links

[[edit][42]]

- [16th Hilbert problem: computation of Lyapunov quantities and limit cycles in two-dimensional dynamical systems][43] [Archived][44] 2013-12-03 at the [Wayback Machine][45]

- [v][46]
- [t][47]
- [e][48]

[Hilbert's problems][4]

 |

- [1][49]
- [2][50]
- [3][51]
- [4][52]
- [5][53]
- [6][54]
- [7][55]
- [8][56]
- [9][57]
- [10][58]
- [11][59]
- [12][60]
- [13][61]
- [14][62]
- [15][63]
- [16][64]
- [17][65]
- [18][66]
- [19][67]
- [20][68]
- [21][69]
- [22][70]
- [23][71]
- ( [24][72])

 |

[Authority control databases][73][image: Edit this at Wikidata] [74]

 |

International |

- [GND][75]

 |

National |

- [France][76]
- [BnF data][77]

 |

Other |

- [IdRef][78]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Hilbert%27s_sixteenth_problem&oldid=1334411038][79] "

[Categories][80]:

- [Hilbert's problems][81]
- [Unsolved problems in geometry][82]
- [Real algebraic geometry][83]
- [Dynamical systems][84]
- [Hidden oscillation][85]

Hidden categories:

- [Articles with short description][86]
- [Short description matches Wikidata][87]
- [Webarchive template wayback links][88]

Search

Hilbert's sixteenth problem

9 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/David_Hilbert
[2]: https://en.wikipedia.org/wiki/Paris
[3]: https://en.wikipedia.org/wiki/International_Congress_of_Mathematicians
[4]: https://en.wikipedia.org/wiki/Hilbert's_problems
[5]: https://en.wikipedia.org/wiki/Algebraic_curve
[6]: https://en.wikipedia.org/wiki/Algebraic_surface
[7]: https://en.wikipedia.org/wiki/Limit_cycle
[8]: https://en.wikipedia.org/wiki/Polynomial_vector_field
[9]: https://en.wikipedia.org/wiki/Real_algebraic_geometry
[10]: https://en.wikipedia.org/wiki/Dynamical_system
[11]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=1
[12]: https://en.wikipedia.org/wiki/Carl_Gustav_Axel_Harnack
[13]: https://en.wikipedia.org/wiki/Real_projective_plane
[14]: https://en.wikipedia.org/wiki/Locally_connected_space
[15]: https://en.wikipedia.org/wiki/Harnack's_curve_theorem
[16]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=2
[17]: https://en.wikipedia.org/wiki/Real_number
[18]: https://en.wikipedia.org/wiki/Henri_Poincaré
[19]: https://en.wikipedia.org/wiki/Stationary_point
[20]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=3
[21]: https://en.wikipedia.org/wiki/Yulii_Ilyashenko
[22]: https://en.wikipedia.org/wiki/Jean_Écalle
[23]: https://en.wikipedia.org/wiki/Henri_Dulac
[24]: https://en.wikipedia.org/wiki/Evgenii_Landis
[25]: https://en.wikipedia.org/wiki/Ivan_Petrovsky
[26]: https://en.wikipedia.org/wiki/Hidden_attractor
[27]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=4
[28]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=5
[29]: https://en.wikipedia.org/wiki/Hilbert–Arnold_problem
[30]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=6
[31]: http://aleph0.clarku.edu/~djoyce/hilbert/problems.html
[32]: https://gaceta.rsme.es/abrir.php?id=1289
[33]: https://www.ams.org/journals/bull/2002-39-03/S0273-0979-02-00946-1/S0273-0979-02-00946-1.pdf
[34]: https://en.wikipedia.org/wiki/Doi_(identifier)
[35]: https://doi.org/10.1090%2Fs0273-0979-02-00946-1
[36]: https://doi.org/10.1007%2Fs12591-012-0118-6
[37]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[38]: https://api.semanticscholar.org/CorpusID:122896664
[39]: https://doi.org/10.1142%2FS0218127413300024
[40]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[41]: https://ui.adsabs.harvard.edu/abs/2013IJBC...2330002L
[42]: /w/index.php?title=Hilbert%27s_sixteenth_problem&amp;action=edit&amp;section=7
[43]: http://www.math.spbu.ru/user/nk/PDF/Limit_cycles_Focus_values.pdf
[44]: https://web.archive.org/web/20131203052309/http://www.math.spbu.ru/user/nk/PDF/Limit_cycles_Focus_values.pdf
[45]: https://en.wikipedia.org/wiki/Wayback_Machine
[46]: https://en.wikipedia.org/wiki/Template:Hilbert's_problems
[47]: https://en.wikipedia.org/wiki/Template_talk:Hilbert's_problems
[48]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Hilbert's_problems
[49]: https://en.wikipedia.org/wiki/Hilbert's_first_problem
[50]: https://en.wikipedia.org/wiki/Hilbert's_second_problem
[51]: https://en.wikipedia.org/wiki/Hilbert's_third_problem
[52]: https://en.wikipedia.org/wiki/Hilbert's_fourth_problem
[53]: https://en.wikipedia.org/wiki/Hilbert's_fifth_problem
[54]: https://en.wikipedia.org/wiki/Hilbert's_sixth_problem
[55]: https://en.wikipedia.org/wiki/Hilbert's_seventh_problem
[56]: https://en.wikipedia.org/wiki/Hilbert's_eighth_problem
[57]: https://en.wikipedia.org/wiki/Hilbert's_ninth_problem
[58]: https://en.wikipedia.org/wiki/Hilbert's_tenth_problem
[59]: https://en.wikipedia.org/wiki/Hilbert's_eleventh_problem
[60]: https://en.wikipedia.org/wiki/Hilbert's_twelfth_problem
[61]: https://en.wikipedia.org/wiki/Hilbert's_thirteenth_problem
[62]: https://en.wikipedia.org/wiki/Hilbert's_fourteenth_problem
[63]: https://en.wikipedia.org/wiki/Hilbert's_fifteenth_problem
[64]: https://en.wikipedia.org/wiki/Hilbert's_sixteenth_problem
[65]: https://en.wikipedia.org/wiki/Hilbert's_seventeenth_problem
[66]: https://en.wikipedia.org/wiki/Hilbert's_eighteenth_problem
[67]: https://en.wikipedia.org/wiki/Hilbert's_nineteenth_problem
[68]: https://en.wikipedia.org/wiki/Hilbert's_twentieth_problem
[69]: https://en.wikipedia.org/wiki/Hilbert's_twenty-first_problem
[70]: https://en.wikipedia.org/wiki/Hilbert's_twenty-second_problem
[71]: https://en.wikipedia.org/wiki/Hilbert's_twenty-third_problem
[72]: https://en.wikipedia.org/wiki/Hilbert's_twenty-fourth_problem
[73]: https://en.wikipedia.org/wiki/Help:Authority_control
[74]: https://www.wikidata.org/wiki/Q2509489#identifiers
[75]: https://d-nb.info/gnd/4391597-8
[76]: https://catalogue.bnf.fr/ark:/12148/cb14591717b
[77]: https://data.bnf.fr/ark:/12148/cb14591717b
[78]: https://www.idref.fr/083420592
[79]: https://en.wikipedia.org/w/index.php?title=Hilbert%27s_sixteenth_problem&amp;oldid=1334411038
[80]: /wiki/Help:Category
[81]: /wiki/Category:Hilbert%27s_problems
[82]: /wiki/Category:Unsolved_problems_in_geometry
[83]: /wiki/Category:Real_algebraic_geometry
[84]: /wiki/Category:Dynamical_systems
[85]: /wiki/Category:Hidden_oscillation
[86]: /wiki/Category:Articles_with_short_description
[87]: /wiki/Category:Short_description_matches_Wikidata
[88]: /wiki/Category:Webarchive_template_wayback_links
