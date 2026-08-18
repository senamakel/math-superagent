<!-- source: https://en.wikipedia.org/wiki/Dehn_invariant | converted from HTML -->

Dehn invariant - Wikipedia

Jump to content

[image: This is a good article. Click here for more information.] [1]

From Wikipedia, the free encyclopedia

Value determined from a polyhedron

Not to be confused with [Dehn function][2].

In [geometry][3], the **Dehn invariant**is a value used to determine whether one [polyhedron][4] can be cut into pieces and reassembled (" [dissected][5] ") into another, and whether a polyhedron or its dissections can [tile space][6]. It is named after [Max Dehn][7], who used it to solve [Hilbert's third problem][8] by proving that certain polyhedra with equal volume cannot be dissected into each other.

Two polyhedra have a dissection into polyhedral pieces that can be reassembled into either one, if and only if their volumes and Dehn invariants are equal. Having Dehn invariant zero is a necessary (but not sufficient) condition for being a space-filling polyhedron, and a polyhedron can be cut up and reassembled into a space-filling polyhedron if and only if its Dehn invariant is zero. The Dehn invariant of a self-intersection-free [flexible polyhedron][9] is invariant as it flexes. Dehn invariants are also an invariant for dissection in higher dimensions, and (with volume) a complete invariant in four dimensions.

The Dehn invariant is zero for the [cube][10] but nonzero for the other [Platonic solids][11], implying that the other solids cannot tile space and that they cannot be dissected into a cube. All of the [Archimedean solids][12] have Dehn invariants that are rational combinations of the invariants for the Platonic solids. In particular, the [truncated octahedron][13] also tiles space and has Dehn invariant zero like the cube.

The Dehn invariants of polyhedra are not numbers. Instead, they are elements of an infinite-dimensional [tensor space][14]. This space, viewed as an [abelian group][15], is part of an [exact sequence][16] involving [group homology][17]. Similar invariants can also be defined for some other [dissection puzzles][18], including the problem of dissecting [rectilinear polygons][19] into each other by axis-parallel cuts and translations.

## Background and history

[[edit][20]]

[21] Dissection of a square and equilateral triangle into each other. No such dissection exists for the cube and regular [tetrahedron][22].

In two dimensions, the [Wallace–Bolyai–Gerwien theorem][23] from the early 19th century states that any two [polygons][24] of equal area can be cut up into polygonal pieces and reassembled into each other. In the late 19th century, [David Hilbert][25] became interested in this result. He used it as a way to axiomatize the [area][26] of two-dimensional polygons, in connection with [Hilbert's axioms][27] for [Euclidean geometry][28]. This was part of a program to make the foundations of geometry more rigorous, by treating explicitly notions like area that **[Euclid's Elements][29] had handled more intuitively. [1] Naturally, this raised the question of whether a similar axiomatic treatment could be extended to [solid geometry][30]. [2]

At the 1900 [International Congress of Mathematicians][31], Hilbert formulated [Hilbert's problems][32], a set of problems that became very influential in 20th-century mathematics. One of those, [Hilbert's third problem][8], addressed this question on the axiomatization of solid volume. Hilbert's third problem asked, more specifically, whether every two polyhedra of equal volumes can always be cut into polyhedral pieces and reassembled into each other. If this were the case, then the volume of any polyhedron could be defined, axiomatically, as the volume of an equivalent cube into which it could be reassembled. However, the answer turned out to be negative: not all polyhedra can be dissected into cubes. [3]

Unlike some of the other Hilbert problems, the answer to the third problem came very quickly. In fact, [Raoul Bricard][33] had already claimed it as a theorem in 1896, but with a proof that turned out to be incomplete. [4] Hilbert's student [Max Dehn][7], in his 1900 [habilitation][34] thesis, invented the Dehn invariant in order to solve this problem. Dehn proved that, to be reassembled into each other, two polyhedra of equal volume should also have equal Dehn invariant, but he found two tetrahedra of equal volume whose Dehn invariants differed. This provided a negative solution to the problem. [2] Although Dehn formulated his invariant differently, the modern approach to Dehn's invariant is to describe it as a value in a [tensor product][35], following Jessen (1968). [5] [6]

## Examples

[[edit][36]]

### Simplified calculation

[[edit][37]]

Defining the Dehn invariant in a way that can apply to all polyhedra simultaneously involves infinite-dimensional vector spaces (see § Full definition, below). However, when restricted to any particular example consisting of finitely many polyhedra, such as the [Platonic solids][11], it can be defined in a simpler way, involving only a finite number of dimensions, as follows: [7]

- Determine the edge lengths and [dihedral angles][38] (the angle between two faces meeting along an edge) of all of the polyhedra.
- Find a subset of the angles that forms a rational [basis][39]. This means that each dihedral angle can be represented as a [linear combination][40] of basis elements, with [rational number][41] coefficients. Additionally, no [rational linear combination of basis elements may sum to zero][42]. Include π {\displaystyle \pi }[image: {\displaystyle \pi }] (or a rational multiple of π {\displaystyle \pi }[image: {\displaystyle \pi }]) in this basis.
- For each edge of a polyhedron, represent its dihedral angle as a rational combination of angles from the basis. Discard the coefficient for the rational multiple of π {\displaystyle \pi }[image: {\displaystyle \pi }] in this combination. Interpret the remaining coefficients as the coordinates of a [vector][43] whose dimensions represent basis angles, and scale this vector by the edge length.
- Sum the vectors for all edges of a polyhedron to produce its Dehn invariant.

Although this method involves arbitrary choices of basis elements, these choices affect only the coefficients by which the Dehn invariants are represented. As elements of an abstract vector space, they are unaffected by the choice of basis. The vector space spanned by the Dehn invariants of any [finite set][44] of polyhedra forms a finite-dimensional subspace of the infinite-dimensional vector space in which the Dehn invariants of all polyhedra are defined. The question of which combinations of dihedral angles are related by rational linear combinations is not always straightforward, and may involve nontrivial methods from [number theory][45]. [7]

### Platonic solids

[[edit][46]]

For the five Platonic solids, the dihedral angles are:

- θ t e t = arccos ⁡ 1 3 ≈ 70.5 ∘ {\displaystyle \theta _{\mathrm {tet} }=\arccos {\tfrac {1}{3}}\approx 70.5^{\circ }}[image: {\displaystyle \theta _{\mathrm {tet} }=\arccos {\tfrac {1}{3}}\approx 70.5^{\circ }}] for the tetrahedron.
- θ c u b e = π / 2 = 90 ∘ {\displaystyle \theta _{\mathrm {cube} }=\pi /2=90^{\circ }}[image: {\displaystyle \theta _{\mathrm {cube} }=\pi /2=90^{\circ }}], a [right angle][47], for the cube.
- θ o c t = arccos ⁡ ( − 1 3) ≈ 109.5 ∘ {\displaystyle \theta _{\mathrm {oct} }=\arccos(-{\tfrac {1}{3}})\approx 109.5^{\circ }}[image: {\displaystyle \theta _{\mathrm {oct} }=\arccos(-{\tfrac {1}{3}})\approx 109.5^{\circ }}] for the octahedron.
- θ d o d e c = 2 arctan ⁡ φ ≈ 116.6 ∘ {\displaystyle \theta _{\mathrm {dodec} }=2\arctan \varphi \approx 116.6^{\circ }}[image: {\displaystyle \theta _{\mathrm {dodec} }=2\arctan \varphi \approx 116.6^{\circ }}] for the dodecahedron, where φ = ( 1 + 5) / 2 {\displaystyle \varphi =(1+{\sqrt {5}})/2}[image: {\displaystyle \varphi =(1+{\sqrt {5}})/2}] is the [golden ratio][48].
- θ i c o s = arccos ⁡ ( − 1 3 5) ≈ 138.2 ∘ {\displaystyle \theta _{\mathrm {icos} }=\arccos(-{\tfrac {1}{3}}{\sqrt {5}})\approx 138.2^{\circ }}[image: {\displaystyle \theta _{\mathrm {icos} }=\arccos(-{\tfrac {1}{3}}{\sqrt {5}})\approx 138.2^{\circ }}] for the icosahedron.

The dihedral angle of a cube is a rational multiple of π {\displaystyle \pi }[image: {\displaystyle \pi }], but the rest are not. The dihedral angles of the regular tetrahedron and regular octahedron are [supplementary angles][49]: they sum \\pi</math>."}},"i":0}}]}'>to π {\displaystyle \pi }[image: {\displaystyle \pi }]. Omitting either the tetrahedron or the octahedron from these five angles produces a rational basis: there are no other rational relations between these angles. [7] If, for instance, the basis that omits θ o c t {\displaystyle \theta _{\mathrm {oct} }}[image: {\displaystyle \theta _{\mathrm {oct} }}] is used, and θ c u b e {\displaystyle \theta _{\mathrm {cube} }}[image: {\displaystyle \theta _{\mathrm {cube} }}] is used as a basis element but then omitted (as a rational multiple of π {\displaystyle \pi }[image: {\displaystyle \pi }]) from the Dehn invariant calculation, then the remaining angle basis elements are θ t e t {\displaystyle \theta _{\mathrm {tet} }}[image: {\displaystyle \theta _{\mathrm {tet} }}], θ d o d e c {\displaystyle \theta _{\mathrm {dodec} }}[image: {\displaystyle \theta _{\mathrm {dodec} }}], and θ i c o s {\displaystyle \theta _{\mathrm {icos} }}[image: {\displaystyle \theta _{\mathrm {icos} }}]. The resulting Dehn invariants will have one dimension for each basis element. With this basis, for Platonic solids with edge length s {\displaystyle s}[image: {\displaystyle s}], the Dehn invariants are: \\langle 3\\rangle_2=-\\theta_{\\mathrm{tet}}/2</math>, <math>\\langle 5\\rangle_1=-\\theta_{\\mathrm{dodec}}</math>, and <math>\\langle 3\\rangle_5=\\theta_{\\mathrm{icos}}/2</math>."}},"i":0}}]}'> [a]

- ( 6 s, 0, 0) {\displaystyle (6s,0,0)}[image: {\displaystyle (6s,0,0)}] for the tetrahedron. It has six edges of length s {\displaystyle s}[image: {\displaystyle s}], with tetrahedral dihedral angles.
- ( 0, 0, 0) {\displaystyle (0,0,0)}[image: {\displaystyle (0,0,0)}] for the cube. Its edges have dihedral angles that are expressed only in terms of θ c u b e {\displaystyle \theta _{\mathrm {cube} }}[image: {\displaystyle \theta _{\mathrm {cube} }}], omitted from the Dehn invariant.
- ( − 12 s, 0, 0) {\displaystyle (-12s,0,0)}[image: {\displaystyle (-12s,0,0)}] for the octahedron. Its twelve edges have dihedrals θ o c t = 2 θ c u b e − θ t e t {\displaystyle \theta _{\mathrm {oct} }=2\theta _{\mathrm {cube} }-\theta _{\mathrm {tet} }}[image: {\displaystyle \theta _{\mathrm {oct} }=2\theta _{\mathrm {cube} }-\theta _{\mathrm {tet} }}]. In this combination, the coefficient for θ c u b e {\displaystyle \theta _{\mathrm {cube} }}[image: {\displaystyle \theta _{\mathrm {cube} }}] is discarded, leaving only a coefficient of − 1 {\displaystyle -1}[image: {\displaystyle -1}] \\theta_{\\mathrm{tet}}</math>."}},"i":0}}]}'>for θ t e t {\displaystyle \theta _{\mathrm {tet} }}[image: {\displaystyle \theta _{\mathrm {tet} }}].
- ( 0, 30 s, 0) {\displaystyle (0,30s,0)}[image: {\displaystyle (0,30s,0)}] for the dodecahedron. It has 30 edges with dodecahedral dihedral angles.
- ( 0, 0, 30 s) {\displaystyle (0,0,30s)}[image: {\displaystyle (0,0,30s)}] for the icosahedron. It has 30 edges with icosahedral dihedral angles.

The cube is the only one of these whose Dehn invariant is zero. The Dehn invariants of each of the other four Platonic solids are unequal and nonzero. The Dehn invariant of the octahedron is − 2 {\displaystyle -2}[image: {\displaystyle -2}] times the Dehn invariant of a tetrahedron of the same edge length. [7]

### Related polyhedra

[[edit][50]]

The Dehn invariant of any [parallelepiped][51] is zero, just as it is for the cube. Each set of four parallel edges in a parallelepiped have the same length and have dihedral angles summing to 2 π {\displaystyle 2\pi }[image: {\displaystyle 2\pi }], so their contributions to the Dehn invariant cancel out to zero. [8] The Dehn invariants of the other [Archimedean solids][12] can also be expressed as rational combinations of the invariants of the Platonic solids. [7] In terms of the same basis as before, with the same assumption that these shapes have edge length s {\displaystyle s}[image: {\displaystyle s}], the Dehn invariants are: [a]

- ( − 6 s, 0, 0) {\displaystyle (-6s,0,0)}[image: {\displaystyle (-6s,0,0)}] for the [truncated tetrahedron][52].
- ( 12 s, 0, 0) {\displaystyle (12s,0,0)}[image: {\displaystyle (12s,0,0)}] for the [truncated cube][53], [rhombicuboctahedron][54], and [cuboctahedron][55].
- ( 0, 0, 0) {\displaystyle (0,0,0)}[image: {\displaystyle (0,0,0)}] for the [truncated octahedron][13], which tiles space as the [bitruncated cubic honeycomb][56]. [9]
- ( 0, 0, − 30 s) {\displaystyle (0,0,-30s)}[image: {\displaystyle (0,0,-30s)}] for the [truncated dodecahedron][57].
- ( 0, − 30 s, 0) {\displaystyle (0,-30s,0)}[image: {\displaystyle (0,-30s,0)}] for the [truncated icosahedron][58].
- ( 0, − 30 s, − 30 s) {\displaystyle (0,-30s,-30s)}[image: {\displaystyle (0,-30s,-30s)}] for the [icosidodecahedron][59].
- ( 0, 30 s, 30 s) {\displaystyle (0,30s,30s)}[image: {\displaystyle (0,30s,30s)}] for the [rhombicosidodecahedron][60].
- ( 0, 0, 0) {\displaystyle (0,0,0)}[image: {\displaystyle (0,0,0)}] for the [truncated icosidodecahedron][61]. This does not tile space directly, but as a [zonohedron][62] it can be partitioned into parallelepipeds, which do. [9] [10]

## Applications

[[edit][63]]

[64] Dissection of a cube into [orthoschemes][65]. In the cube, each new edge introduced in this dissection is surrounded by dihedral angles that sum to π {\displaystyle \pi }[image: {\displaystyle \pi }] (for the face diagonals) or 2 π {\displaystyle 2\pi }[image: {\displaystyle 2\pi }] (for the body diagonal), so the total contribution to the Dehn invariant from these edges is zero.

Unsolved problem in mathematics

Is there a dissection between every pair of spherical or hyperbolic polyhedra with the same volume and Dehn invariant as each other?

[More unsolved problems in mathematics][66]

As Dehn (1901) observed, the Dehn invariant is an [invariant][67] for the dissection of polyhedra, in the sense that cutting up a polyhedron into smaller polyhedral pieces and then reassembling them into a different polyhedron does not change the Dehn invariant of the result. If a new edge is introduced in this cutting process, then either it is interior to the polyhedron, and surrounded by dihedral angles totaling 2 π {\displaystyle 2\pi }[image: {\displaystyle 2\pi }], or on a face of the polyhedron, and surrounded by dihedrals totaling π {\displaystyle \pi }[image: {\displaystyle \pi }]; in either case this rational multiple of π {\displaystyle \pi }[image: {\displaystyle \pi }] does not contribute to the Dehn invariant. A similar analysis shows that there is also no change in the Dehn invariant when an existing polyhedron edge is the boundary of a new face created when cutting up the polyhedron. The new dihedral angles on that edge combine to the same sum, and the same contribution to the Dehn invariant, that they had before. Another invariant of dissection is the [volume][68] of a polyhedron: cutting it up into polyhedral pieces and reassembling the pieces cannot change the total volume. Therefore, if one polyhedron P has a dissection into another polyhedron Q, both P and Q must have the same Dehn invariant as well as the same volume. [11] Sydler (1965) extended this result by proving that the volume and the Dehn invariant are the only invariants for this problem. If P and Q both have the same volume and the same Dehn invariant, it is always possible to dissect one into the other. [12] [13]

The Dehn invariant also constrains the ability of a polyhedron to [tile space][6]. Every space-filling tile has Dehn invariant zero, like the cube. For polyhedra that tile space periodically this would follow by using the periodicity of the tiling to cut and rearrange the tile into a parallelepiped with the same periodicity, but this result holds as well for aperiodic tiles like the [Schmitt–Conway–Danzer biprism][69]. [14] [15] The reverse of this is not true – there exist polyhedra with Dehn invariant zero that do not tile space. However, these can always be dissected into another shape (the cube) that does tile space. The [truncated icosidodecahedron][61] is an example. [9] [10]

Dehn's result continues to be valid for [spherical geometry][70] and [hyperbolic geometry][71]. In both of those geometries, two polyhedra that can be cut and reassembled into each other must have the same Dehn invariant. However, as Jessen observed, the extension of Sydler's result to spherical or hyperbolic geometry remains open: it is not known whether two spherical or hyperbolic polyhedra with the same volume and the same Dehn invariant can always be cut and reassembled into each other. [16] Every [hyperbolic manifold][72] with finite [volume][73] can be cut along geodesic surfaces into a hyperbolic polyhedron (a [fundamental domain][74] for the [fundamental group][75] of the manifold), which tiles the [universal cover][76] of the manifold and therefore necessarily has zero Dehn invariant. [17]

More generally, if some combination of polyhedra jointly tiles space, then the sum of their Dehn invariants (taken in the same proportion) must be zero. For instance, the [tetrahedral-octahedral honeycomb][77] is a tiling of space by tetrahedra and octahedra (with twice as many tetrahedra as octahedra), corresponding to the fact that the sum of the Dehn invariants of an octahedron and two tetrahedra (with the same side lengths) is zero. [b]

## Full definition

[[edit][78]]

### As a tensor product

[[edit][79]]

The definition of the Dehn invariant requires a notion of a [polyhedron][4] for which the lengths and [dihedral angles][38] of edges are well defined. Most commonly, it applies to the polyhedra whose boundaries are [piecewise linear manifolds][80], embedded on a finite number of planes in [Euclidean space][81]. However, the Dehn invariant has also been considered for polyhedra in [spherical geometry][70] or in [hyperbolic space][82], [5] and for certain self-crossing polyhedra in Euclidean space. [18]

The values of the Dehn invariant belong to an [abelian group][15] [19] defined as the [tensor product][35] R ⊗ Z R / 2 π Z. {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} .}[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} .}] The left factor of this tensor product is the set of real numbers (in this case representing lengths of edges of polyhedra) and the right factor represents [dihedral angles][38] in [radians][83], given as numbers modulo rational multiples of 2 π. [12] (Some sources take the angles modulo π instead of modulo 2 π, [5] [19] [20] or divide the angles by π and use R / Z {\displaystyle \mathbb {R} /\mathbb {Z} }[image: {\displaystyle \mathbb {R} /\mathbb {Z} }] in place \\R/2\\pi\\Z</math>,{{r|dupont}}"}},"i":0}}]}'>of R / 2 π Z {\displaystyle \mathbb {R} /2\pi \mathbb {Z} }[image: {\displaystyle \mathbb {R} /2\pi \mathbb {Z} }], [21] but this makes no difference to the resulting tensor product, as any rational multiple of π in the right factor becomes zero in the product.)

The Dehn invariant of a polyhedron with edge lengths ℓ i {\displaystyle \ell _{i}}[image: {\displaystyle \ell _{i}}] and edge dihedral angles θ i {\displaystyle \theta _{i}}[image: {\displaystyle \theta _{i}}] is the sum [12] ∑ i ℓ i ⊗ θ i. {\displaystyle \sum _{i}\ell _{i}\otimes \theta _{i}.}[image: {\displaystyle \sum _{i}\ell _{i}\otimes \theta _{i}.}]

Its structure as a tensor gives the Dehn invariant additional properties that are geometrically meaningful. In particular, it has a [tensor rank][84], the minimum number of terms ℓ ⊗ θ {\displaystyle \ell \otimes \theta }[image: {\displaystyle \ell \otimes \theta }] in any expression as a sum of such terms. Since the expression of the Dehn invariant as a sum over edges of a polyhedron has exactly this form, the rank of the Dehn invariant gives a lower bound on the minimum number of edges possible for any polyhedron resulting from a dissection of a given polyhedron. [22]

### Using a Hamel basis

[[edit][85]]

An alternative but equivalent description of the Dehn invariant involves the choice of a [Hamel basis][86], an infinite subset B {\displaystyle B}[image: {\displaystyle B}] of the real numbers such that every real number can be expressed uniquely as a sum of finitely many rational multiples of elements of B {\displaystyle B}[image: {\displaystyle B}]. Thus, as an additive group, R {\displaystyle \mathbb {R} }[image: {\displaystyle \mathbb {R} }] is [isomorphic][87] to Q ( B) {\displaystyle \mathbb {Q} ^{(B)}}[image: {\displaystyle \mathbb {Q} ^{(B)}}], the [direct sum][88] of copies of Q {\displaystyle \mathbb {Q} }[image: {\displaystyle \mathbb {Q} }] with one summand for each element of B {\displaystyle B}[image: {\displaystyle B}]. If B {\displaystyle B}[image: {\displaystyle B}] is chosen to have π (or a rational multiple of π) is one of its elements, and B ′ {\displaystyle B'}[image: {\displaystyle B'}] is the rest of the basis with this element excluded, then the tensor product R ⊗ R / 2 π Z {\displaystyle \mathbb {R} \otimes \mathbb {R} /2\pi \mathbb {Z} }[image: {\displaystyle \mathbb {R} \otimes \mathbb {R} /2\pi \mathbb {Z} }] can be described as the (infinite dimensional) real [vector space][43] R ( B ′) {\displaystyle \mathbb {R} ^{(B')}}[image: {\displaystyle \mathbb {R} ^{(B')}}]. The Dehn invariant can be expressed by decomposing each dihedral angle θ i {\displaystyle \theta _{i}}[image: {\displaystyle \theta _{i}}] into a finite sum of basis elements θ i = ∑ j = 0 k i q i, j b i, j {\displaystyle \theta _{i}=\sum _{j=0}^{k_{i}}q_{i,j}b_{i,j}}[image: {\displaystyle \theta _{i}=\sum _{j=0}^{k_{i}}q_{i,j}b_{i,j}}] where q i, j {\displaystyle q_{i,j}}[image: {\displaystyle q_{i,j}}] is rational, b i, j {\displaystyle b_{i,j}}[image: {\displaystyle b_{i,j}}] is one of the real numbers in the Hamel basis, and these basis elements are numbered so that b i, 0 {\displaystyle b_{i,0}}[image: {\displaystyle b_{i,0}}] is the rational multiple of π that belongs to B {\displaystyle B}[image: {\displaystyle B}] but not B ′ {\displaystyle B'}[image: {\displaystyle B'}]. With this decomposition, the Dehn invariant is ∑ i ∑ j = 1 k i ℓ i q i, j e i, j, {\displaystyle \sum _{i}\sum _{j=1}^{k_{i}}\ell _{i}q_{i,j}e_{i,j},}[image: {\displaystyle \sum _{i}\sum _{j=1}^{k_{i}}\ell _{i}q_{i,j}e_{i,j},}] where each e i, j {\displaystyle e_{i,j}}[image: {\displaystyle e_{i,j}}] is the standard [unit vector][89] in R ( B ′) {\displaystyle \mathbb {R} ^{(B')}}[image: {\displaystyle \mathbb {R} ^{(B')}}] corresponding to the basis element b i, j {\displaystyle b_{i,j}}[image: {\displaystyle b_{i,j}}]. The sum here starts at j = 1 {\displaystyle j=1}[image: {\displaystyle j=1}], to omit the term corresponding to the rational multiples of π. [23]

This alternative formulation shows that the values of the Dehn invariant can be given the additional structure of a real [vector space][43]. [24] Although, in general, the construction of Hamel bases involves the [axiom of choice][90], this can be avoided (when considering any specific finite set of polyhedra) by restricting attention to the finite-dimensional vector space generated over Q {\displaystyle \mathbb {Q} }[image: {\displaystyle \mathbb {Q} }] by the dihedral angles of the polyhedra. [4]

### Hyperbolic polyhedra with infinite edge lengths

[[edit][91]]

For an [ideal polyhedron][92] in hyperbolic space, the edge lengths are infinite, making the usual definition of the Dehn invariant inapplicable. Nevertheless, the Dehn invariant can be extended to these polyhedra by using [horospheres][93] to truncate their vertices, and computing the Dehn invariant in the usual way for the resulting truncated shape, ignoring the extra curved edges created by this truncation process. The result does not depend on the choice of horospheres for the truncation, as long as each one cuts off only a single vertex of the given polyhedron. [25]

## Realizability

[[edit][94]]

Although the Dehn invariant takes values in R ⊗ Z R / 2 π Z, {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} ,}[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} ,}] not all of the elements in this space can be realized as the Dehn invariants of polyhedra. The Dehn invariants of Euclidean polyhedra form a real linear subspace of R ⊗ Z R / 2 π Z {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }]: one can add the Dehn invariants of polyhedra by taking the disjoint union of the polyhedra (or gluing them together on a face), negate Dehn invariants by making holes in the shape of the polyhedron in large cubes, and multiply the Dehn invariant by any positive real scalar by scaling the polyhedron by the same number. The question of which elements of R ⊗ Z R / 2 π Z, {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} ,}[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} ,}] are realizable was clarified by the work of Dupont and Sah, who showed the existence of the following [exact sequence][16] of [abelian groups][15] (not vector spaces) involving [group homology][17]: [26] 0 → H 2 ( SO ⁡ ( 3), R 3) → P ( E 3) / Z ( E 3) → R ⊗ Z R / 2 π Z → H 1 ( SO ⁡ ( 3), R 3) → 0 {\displaystyle 0\to H_{2}(\operatorname {SO} (3),\mathbb {R} ^{3})\to {\mathcal {P}}(E^{3})/{\mathcal {Z}}(E^{3})\to \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} \to H_{1}(\operatorname {SO} (3),\mathbb {R} ^{3})\to 0}[image: {\displaystyle 0\to H_{2}(\operatorname {SO} (3),\mathbb {R} ^{3})\to {\mathcal {P}}(E^{3})/{\mathcal {Z}}(E^{3})\to \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} \to H_{1}(\operatorname {SO} (3),\mathbb {R} ^{3})\to 0}] Here, the notation P ( E 3) {\displaystyle {\mathcal {P}}(E^{3})}[image: {\displaystyle {\mathcal {P}}(E^{3})}] represents the [free abelian group][95] over Euclidean polyhedra modulo certain relations derived from pairs of polyhedra that can be dissected into each other. Z ( E 3) {\displaystyle {\mathcal {Z}}(E^{3})}[image: {\displaystyle {\mathcal {Z}}(E^{3})}] is the subgroup generated in this group by the triangular [prisms][96], and is used here to represent volume (as each real number is the volume of exactly one element of this group). The map from the group of polyhedra to R ⊗ Z R / 2 π Z {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }] is the Dehn invariant. SO ⁡ ( 3) {\displaystyle \operatorname {SO} (3)}[image: {\displaystyle \operatorname {SO} (3)}] is the [Euclidean point rotation group][97], and H {\displaystyle H}[image: {\displaystyle H}] is the group homology. Sydler's theorem that volume and the Dehn invariant are the only invariants for Euclidean dissection is represented homologically by the statement that the group H 2 ( SO ⁡ ( 3), R 3) {\displaystyle H_{2}(\operatorname {SO} (3),\mathbb {R} ^{3})}[image: {\displaystyle H_{2}(\operatorname {SO} (3),\mathbb {R} ^{3})}] appearing in this sequence is the [trivial group][98] (represented elsewhere in the sequence by the notation 0). If it were nontrivial, its image in the group of polyhedra would give a family of polyhedra that are not dissectable to a cube of the same volume but that have zero Dehn invariant. By Sydler's theorem, such polyhedra do not exist. [26]

The group H 1 ( SO ⁡ ( 3), R 3) {\displaystyle H_{1}(\operatorname {SO} (3),\mathbb {R} ^{3})}[image: {\displaystyle H_{1}(\operatorname {SO} (3),\mathbb {R} ^{3})}] appearing towards the right of the exact sequence is isomorphic to the group Ω R / Q 1 {\displaystyle \Omega _{\mathbb {R} /\mathbb {Q} }^{1}}[image: {\displaystyle \Omega _{\mathbb {R} /\mathbb {Q} }^{1}}] of [Kähler differentials][99], and the map from tensor products of lengths and angles to Kähler differentials is given by ℓ ⊗ θ ↦ ℓ d cos ⁡ θ sin ⁡ θ = i ℓ d e i θ e i θ, {\displaystyle \ell \otimes \theta \mapsto \ell {\frac {d\cos \theta }{\sin \theta }}=i\ell {\frac {de^{i\theta }}{e^{i\theta }}},}[image: {\displaystyle \ell \otimes \theta \mapsto \ell {\frac {d\cos \theta }{\sin \theta }}=i\ell {\frac {de^{i\theta }}{e^{i\theta }}},}] where d {\displaystyle d}[image: {\displaystyle d}] is the universal derivation R → Ω R / Q 1 {\displaystyle \mathbb {R} \to \Omega _{\mathbb {R} /\mathbb {Q} }^{1}}[image: {\displaystyle \mathbb {R} \to \Omega _{\mathbb {R} /\mathbb {Q} }^{1}}] (or C → Ω C / Q 1 {\displaystyle \mathbb {C} \to \Omega _{\mathbb {C} /\mathbb {Q} }^{1}}[image: {\displaystyle \mathbb {C} \to \Omega _{\mathbb {C} /\mathbb {Q} }^{1}}]). This group H 1 ( SO ⁡ ( 3), R 3) = Ω R / Q 1 {\displaystyle H_{1}(\operatorname {SO} (3),\mathbb {R} ^{3})=\Omega _{\mathbb {R} /\mathbb {Q} }^{1}}[image: {\displaystyle H_{1}(\operatorname {SO} (3),\mathbb {R} ^{3})=\Omega _{\mathbb {R} /\mathbb {Q} }^{1}}] is an obstacle to realizability: its nonzero elements come from elements of R ⊗ Z R / 2 π Z {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }] that cannot be realized as Dehn invariants. [27] Jessen notes, more specifically, that the rank-one tensor ℓ ⊗ θ {\displaystyle \ell \otimes \theta }[image: {\displaystyle \ell \otimes \theta }] can be realized as a Dehn invariant if and only if sin ⁡ θ {\displaystyle \sin \theta }[image: {\displaystyle \sin \theta }] is an [algebraic number][100]. [28] Matthias Görner has conjectured that, when a tensor of this form is realizable as a Dehn invariant, it can be realized by a polyhedron having a single dihedral angle of length ℓ {\displaystyle \ell }[image: {\displaystyle \ell }] and dihedral angle θ {\displaystyle \theta }[image: {\displaystyle \theta }], with all other angles [right angles][47], but this is known only for a limited set of dihedral angles. [29]

In hyperbolic or spherical space, the realizable Dehn invariants do not necessarily form a vector space, because scalar multiplication is no longer possible. However, they still form a subgroup of the tensor product in which they are elements. Analogously, Dupont and Sah prove the existence of the exact sequences [26] 0 → H 3 ( SL ⁡ ( 2, C), Z) − → P ( H 3) → R ⊗ Z R / 2 π Z → H 2 ( SL ⁡ ( 2, C), Z) − → 0 {\displaystyle 0\to H_{3}(\operatorname {SL} (2,\mathbb {C} ),\mathbb {Z} )^{-}\to {\mathcal {P}}({\mathcal {H}}^{3})\to \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} \to H_{2}(\operatorname {SL} (2,\mathbb {C} ),\mathbb {Z} )^{-}\to 0}[image: {\displaystyle 0\to H_{3}(\operatorname {SL} (2,\mathbb {C} ),\mathbb {Z} )^{-}\to {\mathcal {P}}({\mathcal {H}}^{3})\to \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} \to H_{2}(\operatorname {SL} (2,\mathbb {C} ),\mathbb {Z} )^{-}\to 0}] and 0 → H 3 ( SU ⁡ ( 2), Z) → P ( S 3) / Z → R ⊗ Z R / 2 π Z → H 2 ( SU ⁡ ( 2), Z) → 0. {\displaystyle 0\to H_{3}(\operatorname {SU} (2),\mathbb {Z} )\to {\mathcal {P}}(S^{3})/\mathbb {Z} \to \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} \to H_{2}(\operatorname {SU} (2),\mathbb {Z} )\to 0.}[image: {\displaystyle 0\to H_{3}(\operatorname {SU} (2),\mathbb {Z} )\to {\mathcal {P}}(S^{3})/\mathbb {Z} \to \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} \to H_{2}(\operatorname {SU} (2),\mathbb {Z} )\to 0.}] Here SL {\displaystyle \operatorname {SL} }[image: {\displaystyle \operatorname {SL} }] denotes the [special linear group][101], and SL ⁡ ( 2, C) {\displaystyle \operatorname {SL} (2,\mathbb {C} )}[image: {\displaystyle \operatorname {SL} (2,\mathbb {C} )}] is the group of [Möbius transformations][102]; the superscript minus-sign indicates the (−1)-eigenspace for the involution induced by complex conjugation. SU {\displaystyle \operatorname {SU} }[image: {\displaystyle \operatorname {SU} }] denotes the [special unitary group][103]. The subgroup Z {\displaystyle \mathbb {Z} }[image: {\displaystyle \mathbb {Z} }] in P ( S 3) / Z {\displaystyle {\mathcal {P}}(S^{3})/\mathbb {Z} }[image: {\displaystyle {\mathcal {P}}(S^{3})/\mathbb {Z} }] is the group generated by the whole sphere. [26] Again, the rightmost nonzero group in these sequences is the obstacle to realizability of a value in R ⊗ Z R / 2 π Z {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} /2\pi \mathbb {Z} }] as a Dehn invariant.

This algebraic view of the Dehn invariant can be extended to higher dimensions, where it has a [motivic][104] interpretation involving [algebraic K-theory][105]. [17] In four dimensions, the group of polyhedra modulo dissections is isomorphic to the three-dimensional group. Every four-dimensional polytope can be dissected to a prism over a three-dimensional polytope, and two four-dimensional polytopes can be dissected to each other when their volumes and Dehn invariants are equal. In dimensions higher than four, it remains open whether the existence of dissections is completely described by volumes and Dehn invariants, or whether other information is needed to determine whether a dissection exists. [30]

## Related results

[[edit][106]]

[107] Three-piece dissection of a Greek cross to a rectangle, using only axis-parallel cuts and translations. A Dehn-like invariant shows that neither of these shapes can be dissected to a square, with this kind of restricted dissection.

An approach very similar to the Dehn invariant can be used to determine whether two [rectilinear polygons][19] can be dissected into each other only using axis-parallel cuts and translations (rather than cuts at arbitrary angles and rotations). An invariant for this kind of dissection uses the tensor product R ⊗ Z R {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} }[image: {\displaystyle \mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} }] where the left and right terms in the product represent height and width of rectangles. [4] [20] [31] [32] The invariant for any given polygon is calculated by cutting the polygon into rectangles, taking the tensor product of the height and width of each rectangle, and adding the results. A dissection is possible if and only if two polygons have the same invariant, which implies that they also have equal areas. [22] This invariant can be used to prove another result of Dehn from 1903: two rectangles of the same area can be dissected into each other if and only if their [aspect ratios][108] are rational multiples of each other. [31] It follows that a [polyomino][109] formed from a union of n {\displaystyle n}[image: {\displaystyle n}] squares can only be dissected in this way to a square when n {\displaystyle n}[image: {\displaystyle n}] is a square number. For this version of the Dehn invariant, the tensor rank equals the minimum number of rectangles into which a polygon can be dissected. [22]

[Flexible polyhedra][9] are a class of polyhedra that can undergo a continuous motion that preserves the shape of their faces. By [Cauchy's rigidity theorem][110], they must be non-convex, and it is known (the ["bellows theorem"][111]) that the volume of the polyhedron must stay constant throughout this motion. A stronger version of this theorem states that the Dehn invariant of such a polyhedron must also remain invariant throughout any continuous motion. This result is called the " [strong bellows theorem][112] ". It has been proven for all non-self-intersecting flexible polyhedra. [33] However, for more complicated flexible polyhedra with self-intersections the Dehn invariant may change continuously as the polyhedron flexes. [34]

The total [mean curvature][113] of a smooth surface can be generalized to polyhedral surfaces using a definition similar to the Dehn invariant, as the sum over the edges of the edge lengths multiplied by the exterior dihedral angles. It has also been proven to remain constant for any flexing polyhedron. [35]

## Notes

[[edit][114]]

1. 1 2 These values can be found in table 3 of Conway, Radin & Sadun (1999). The basis used by this reference has basis vectors ⟨ 3 ⟩ 2 = − θ t e t / 2 {\displaystyle \langle 3\rangle _{2}=-\theta _{\mathrm {tet} }/2}[image: {\displaystyle \langle 3\rangle _{2}=-\theta _{\mathrm {tet} }/2}], ⟨ 5 ⟩ 1 = − θ d o d e c {\displaystyle \langle 5\rangle _{1}=-\theta _{\mathrm {dodec} }}[image: {\displaystyle \langle 5\rangle _{1}=-\theta _{\mathrm {dodec} }}], and ⟨ 3 ⟩ 5 = θ i c o s / 2 {\displaystyle \langle 3\rangle _{5}=\theta _{\mathrm {icos} }/2}[image: {\displaystyle \langle 3\rangle _{5}=\theta _{\mathrm {icos} }/2}].
2. ↑ This argument applies whenever the proportions of the tiles can be defined as a limit point of the numbers of tiles within larger polyhedra; see Lagarias & Moews (1995), Equation (4.2), and the surrounding discussion.

## References

[[edit][115]]

<a href=\"./Dehn_invariant#cite_note-30lectures-25\" id=\"mwAqw\"><span class=\"mw-reflink-text\" id=\"mwAq0\"><span class=\"cite-bracket\" id=\"mwAq4\">[</span>23<span class=\"cite-bracket\" id=\"mwAq8\">]</span></span></a></sup>\n<sup about=\"#mwt325\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwArA\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"ac11\"},\"body\":{\"id\":\"mw-reference-text-cite_note-ac11-36\"}}'><a href=\"./Dehn_invariant#cite_note-ac11-36\" id=\"mwArE\"><span class=\"mw-reflink-text\" id=\"mwArI\"><span class=\"cite-bracket\" id=\"mwArM\">[</span>34<span class=\"cite-bracket\" id=\"mwArQ\">]</span></span></a></sup>\n<sup about=\"#mwt328\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwArU\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"alexander\"},\"body\":{\"id\":\"mw-reference-text-cite_note-alexander-37\"}}'><a href=\"./Dehn_invariant#cite_note-alexander-37\" id=\"mwArY\"><span class=\"mw-reflink-text\" id=\"mwArc\"><span class=\"cite-bracket\" id=\"mwArg\">[</span>35<span class=\"cite-bracket\" id=\"mwArk\">]</span></span></a></sup>\n<sup about=\"#mwt331\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAro\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"alexandrov\"},\"body\":{\"id\":\"mw-reference-text-cite_note-alexandrov-20\"}}'><a href=\"./Dehn_invariant#cite_note-alexandrov-20\" id=\"mwArs\"><span class=\"mw-reflink-text\" id=\"mwArw\"><span class=\"cite-bracket\" id=\"mwAr0\">[</span>18<span class=\"cite-bracket\" id=\"mwAr4\">]</span></span></a></sup>\n<sup about=\"#mwt334\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAr8\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"benko\"},\"body\":{\"id\":\"mw-reference-text-cite_note-benko-4\"}}'><a href=\"./Dehn_invariant#cite_note-benko-4\" id=\"mwAsA\"><span class=\"mw-reflink-text\" id=\"mwAsE\"><span class=\"cite-bracket\" id=\"mwAsI\">[</span>4<span class=\"cite-bracket\" id=\"mwAsM\">]</span></span></a></sup>\n<sup about=\"#mwt337\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAsQ\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"cghn\"},\"body\":{\"id\":\"mw-reference-text-cite_note-cghn-27\"}}'><a href=\"./Dehn_invariant#cite_note-cghn-27\" id=\"mwAsU\"><span class=\"mw-reflink-text\" id=\"mwAsY\"><span class=\"cite-bracket\" id=\"mwAsc\">[</span>25<span class=\"cite-bracket\" id=\"mwAsg\">]</span></span></a></sup>\n<sup about=\"#mwt340\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAsk\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"crs\"},\"body\":{\"id\":\"mw-reference-text-cite_note-crs-7\"}}'><a href=\"./Dehn_invariant#cite_note-crs-7\" id=\"mwAso\"><span class=\"mw-reflink-text\" id=\"mwAss\"><span class=\"cite-bracket\" id=\"mwAsw\">[</span>7<span class=\"cite-bracket\" id=\"mwAs0\">]</span></span></a></sup>\n<sup about=\"#mwt343\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAs4\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"debrunner\"},\"body\":{\"id\":\"mw-reference-text-cite_note-debrunner-15\"}}'><a href=\"./Dehn_invariant#cite_note-debrunner-15\" id=\"mwAs8\"><span class=\"mw-reflink-text\" id=\"mwAtA\"><span class=\"cite-bracket\" id=\"mwAtE\">[</span>14<span class=\"cite-bracket\" id=\"mwAtI\">]</span></span></a></sup>\n<sup about=\"#mwt346\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAtM\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"dehn\"},\"body\":{\"id\":\"mw-reference-text-cite_note-dehn-12\"}}'><a href=\"./Dehn_invariant#cite_note-dehn-12\" id=\"mwAtQ\"><span class=\"mw-reflink-text\" id=\"mwAtU\"><span class=\"cite-bracket\" id=\"mwAtY\">[</span>11<span class=\"cite-bracket\" id=\"mwAtc\">]</span></span></a></sup>\n<sup about=\"#mwt349\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAtg\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"dehn2\"},\"body\":{\"id\":\"mw-reference-text-cite_note-dehn2-33\"}}'><a href=\"./Dehn_invariant#cite_note-dehn2-33\" id=\"mwAtk\"><span class=\"mw-reflink-text\" id=\"mwAto\"><span class=\"cite-bracket\" id=\"mwAts\">[</span>31<span class=\"cite-bracket\" id=\"mwAtw\">]</span></span></a></sup>\n<sup about=\"#mwt352\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAt0\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"ds90\"},\"body\":{\"id\":\"mw-reference-text-cite_note-ds90-32\"}}'><a href=\"./Dehn_invariant#cite_note-ds90-32\" id=\"mwAt4\"><span class=\"mw-reflink-text\" id=\"mwAt8\"><span class=\"cite-bracket\" id=\"mwAuA\">[</span>30<span class=\"cite-bracket\" id=\"mwAuE\">]</span></span></a></sup>\n<sup about=\"#mwt355\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAuI\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"ds00\"},\"body\":{\"id\":\"mw-reference-text-cite_note-ds00-5\"}}'><a href=\"./Dehn_invariant#cite_note-ds00-5\" id=\"mwAuM\"><span class=\"mw-reflink-text\" id=\"mwAuQ\"><span class=\"cite-bracket\" id=\"mwAuU\">[</span>5<span class=\"cite-bracket\" id=\"mwAuY\">]</span></span></a></sup>\n<sup about=\"#mwt358\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAuc\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"dupont\"},\"body\":{\"id\":\"mw-reference-text-cite_note-dupont-23\"}}'><a href=\"./Dehn_invariant#cite_note-dupont-23\" id=\"mwAug\"><span class=\"mw-reflink-text\" id=\"mwAuk\"><span class=\"cite-bracket\" id=\"mwAuo\">[</span>21<span class=\"cite-bracket\" id=\"mwAus\">]</span></span></a></sup>\n<sup about=\"#mwt361\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAuw\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"eom\"},\"body\":{\"id\":\"mw-reference-text-cite_note-eom-13\"}}'><a href=\"./Dehn_invariant#cite_note-eom-13\" id=\"mwAu0\"><span class=\"mw-reflink-text\" id=\"mwAu4\"><span class=\"cite-bracket\" id=\"mwAu8\">[</span>12<span class=\"cite-bracket\" id=\"mwAvA\">]</span></span></a></sup>\n<sup about=\"#mwt364\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAvE\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"eppstein\"},\"body\":{\"id\":\"mw-reference-text-cite_note-eppstein-24\"}}'><a href=\"./Dehn_invariant#cite_note-eppstein-24\" id=\"mwAvI\"><span class=\"mw-reflink-text\" id=\"mwAvM\"><span class=\"cite-bracket\" id=\"mwAvQ\">[</span>22<span class=\"cite-bracket\" id=\"mwAvU\">]</span></span></a></sup>\n<sup about=\"#mwt367\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAvY\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"gi18\"},\"body\":{\"id\":\"mw-reference-text-cite_note-gi18-35\"}}'><a href=\"./Dehn_invariant#cite_note-gi18-35\" id=\"mwAvc\"><span class=\"mw-reflink-text\" id=\"mwAvg\"><span class=\"cite-bracket\" id=\"mwAvk\">[</span>33<span class=\"cite-bracket\" id=\"mwAvo\">]</span></span></a></sup>\n<sup about=\"#mwt370\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAvs\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"giovannini\"},\"body\":{\"id\":\"mw-reference-text-cite_note-giovannini-1\"}}'><a href=\"./Dehn_invariant#cite_note-giovannini-1\" id=\"mwAvw\"><span class=\"mw-reflink-text\" id=\"mwAv0\"><span class=\"cite-bracket\" id=\"mwAv4\">[</span>1<span class=\"cite-bracket\" id=\"mwAv8\">]</span></span></a></sup>\n<sup about=\"#mwt373\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAwA\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"goncharov\"},\"body\":{\"id\":\"mw-reference-text-cite_note-goncharov-18\"}}'><a href=\"./Dehn_invariant#cite_note-goncharov-18\" id=\"mwAwE\"><span class=\"mw-reflink-text\" id=\"mwAwI\"><span class=\"cite-bracket\" id=\"mwAwM\">[</span>17<span class=\"cite-bracket\" id=\"mwAwQ\">]</span></span></a></sup>\n<sup about=\"#mwt376\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAwU\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"gruber\"},\"body\":{\"id\":\"mw-reference-text-cite_note-gruber-3\"}}'><a href=\"./Dehn_invariant#cite_note-gruber-3\" id=\"mwAwY\"><span class=\"mw-reflink-text\" id=\"mwAwc\"><span class=\"cite-bracket\" id=\"mwAwg\">[</span>3<span class=\"cite-bracket\" id=\"mwAwk\">]</span></span></a></sup>\n<sup about=\"#mwt379\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAwo\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"hartshorne\"},\"body\":{\"id\":\"mw-reference-text-cite_note-hartshorne-21\"}}'><a href=\"./Dehn_invariant#cite_note-hartshorne-21\" id=\"mwAws\"><span class=\"mw-reflink-text\" id=\"mwAww\"><span class=\"cite-bracket\" id=\"mwAw0\">[</span>19<span class=\"cite-bracket\" id=\"mwAw4\">]</span></span></a></sup>\n<sup about=\"#mwt382\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAw8\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"intuitive\"},\"body\":{\"id\":\"mw-reference-text-cite_note-intuitive-9\"}}'><a href=\"./Dehn_invariant#cite_note-intuitive-9\" id=\"mwAxA\"><span class=\"mw-reflink-text\" id=\"mwAxE\"><span class=\"cite-bracket\" id=\"mwAxI\">[</span>8<span class=\"cite-bracket\" id=\"mwAxM\">]</span></span></a></sup>\n<sup about=\"#mwt385\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAxQ\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"jessen\"},\"body\":{\"id\":\"mw-reference-text-cite_note-jessen-6\"}}'><a href=\"./Dehn_invariant#cite_note-jessen-6\" id=\"mwAxU\"><span class=\"mw-reflink-text\" id=\"mwAxY\"><span class=\"cite-bracket\" id=\"mwAxc\">[</span>6<span class=\"cite-bracket\" id=\"mwAxg\">]</span></span></a></sup>\n<sup about=\"#mwt389\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAxk\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"lm95\"},\"body\":{\"id\":\"mw-reference-text-cite_note-lm95-16\"}}'><a href=\"./Dehn_invariant#cite_note-lm95-16\" id=\"mwAxo\"><span class=\"mw-reflink-text\" id=\"mwAxs\"><span class=\"cite-bracket\" id=\"mwAxw\">[</span>15<span class=\"cite-bracket\" id=\"mwAx0\">]</span></span></a></sup>\n<sup about=\"#mwt392\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAx4\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"recreations\"},\"body\":{\"id\":\"mw-reference-text-cite_note-recreations-10\"}}'><a href=\"./Dehn_invariant#cite_note-recreations-10\" id=\"mwAx8\"><span class=\"mw-reflink-text\" id=\"mwAyA\"><span class=\"cite-bracket\" id=\"mwAyE\">[</span>9<span class=\"cite-bracket\" id=\"mwAyI\">]</span></span></a></sup>\n<sup about=\"#mwt395\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAyM\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"schwartz\"},\"body\":{\"id\":\"mw-reference-text-cite_note-schwartz-26\"}}'><a href=\"./Dehn_invariant#cite_note-schwartz-26\" id=\"mwAyQ\"><span class=\"mw-reflink-text\" id=\"mwAyU\"><span class=\"cite-bracket\" id=\"mwAyY\">[</span>24<span class=\"cite-bracket\" id=\"mwAyc\">]</span></span></a></sup>\n<sup about=\"#mwt398\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAyg\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"shephard\"},\"body\":{\"id\":\"mw-reference-text-cite_note-shephard-11\"}}'><a href=\"./Dehn_invariant#cite_note-shephard-11\" id=\"mwAyk\"><span class=\"mw-reflink-text\" id=\"mwAyo\"><span class=\"cite-bracket\" id=\"mwAys\">[</span>10<span class=\"cite-bracket\" id=\"mwAyw\">]</span></span></a></sup>\n<sup about=\"#mwt401\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAy0\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"spandaw\"},\"body\":{\"id\":\"mw-reference-text-cite_note-spandaw-34\"}}'><a href=\"./Dehn_invariant#cite_note-spandaw-34\" id=\"mwAy4\"><span class=\"mw-reflink-text\" id=\"mwAy8\"><span class=\"cite-bracket\" id=\"mwAzA\">[</span>32<span class=\"cite-bracket\" id=\"mwAzE\">]</span></span></a></sup>\n<sup about=\"#mwt404\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAzI\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"stillwell\"},\"body\":{\"id\":\"mw-reference-text-cite_note-stillwell-22\"}}'><a href=\"./Dehn_invariant#cite_note-stillwell-22\" id=\"mwAzM\"><span class=\"mw-reflink-text\" id=\"mwAzQ\"><span class=\"cite-bracket\" id=\"mwAzU\">[</span>20<span class=\"cite-bracket\" id=\"mwAzY\">]</span></span></a></sup>\n<sup about=\"#mwt407\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAzc\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"sydler\"},\"body\":{\"id\":\"mw-reference-text-cite_note-sydler-14\"}}'><a href=\"./Dehn_invariant#cite_note-sydler-14\" id=\"mwAzg\"><span class=\"mw-reflink-text\" id=\"mwAzk\"><span class=\"cite-bracket\" id=\"mwAzo\">[</span>13<span class=\"cite-bracket\" id=\"mwAzs\">]</span></span></a></sup>\n<sup about=\"#mwt410\" class=\"mw-ref reference\" rel=\"dc:references\" typeof=\"mw:Extension/ref\" id=\"mwAzw\" data-mw='{\"name\":\"ref\",\"attrs\":{\"name\":\"zeeman\"},\"body\":{\"id\":\"mw-reference-text-cite_note-zeeman-2\"}}'><a href=\"./Dehn_invariant#cite_note-zeeman-2\" id=\"mwAz0\"><span class=\"mw-reflink-text\" id=\"mwAz4\"><span class=\"cite-bracket\" id=\"mwAz8\">[</span>2<span class=\"cite-bracket\" id=\"mwA0A\">]</span></span></a></sup>\n"}}'>

1. ↑ Giovannini, Eduardo N. (2021), "David Hilbert and the foundations of the theory of plane area", *[Archive for History of Exact Sciences][116]*, **75**(6): 649– 698, [doi][117]: [10.1007/s00407-021-00278-z][118], [MR][119] [4324749][120]
2. 1 2 [Zeeman, E. C.][121] (July 2002), "On Hilbert's third problem", *[The Mathematical Gazette][122]*, **86**(506): 241– 247, [doi][117]: [10.2307/3621846][123], [JSTOR][124] [3621846][125]
3. ↑ Gruber, Peter M. (2007), "Chapter 16: Volume of Polytopes and Hilbert's Third Problem", *Convex and Discrete Geometry*, Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 336, Springer, Berlin, pp. 280– 291, [doi][117]: [10.1007/978-3-540-71133-9][126], [ISBN][127] [978-3-540-71132-2][128], [MR][119] [2335496][129].
4. 1 2 3 Benko, David (2007), ["A new approach to Hilbert's third problem"][130], *[American Mathematical Monthly][131]*, **114**(8): 665– 676, [doi][117]: [10.1080/00029890.2007.11920458][132], [JSTOR][124] [27642302][133], [MR][119] [2354437][134], [S2CID][135] [7213930][136].
5. 1 2 3 Dupont, Johan L.; Sah, Chih-Han (2000), "Three questions about simplices in spherical and hyperbolic 3-space", *The Gelfand Mathematical Seminars, 1996–1999*, Gelfand Math. Sem., Birkhäuser Boston, Boston, MA, pp. 49– 76, [doi][117]: [10.1007/978-1-4612-1340-6_3][137], [ISBN][127] [978-1-4612-7102-4][138], [MR][119] [1731633][139]. See in particular [p. 61][140].
6. ↑ [Jessen, Børge][141] (1968), "The algebra of polyhedra and the Dehn–Sydler theorem", *Mathematica Scandinavica*, **22**(2): 241– 256, [doi][117]: [10.7146/math.scand.a-10888][142], [JSTOR][124] [24489773][143], [MR][119] [0251633][144].
7. 1 2 3 4 5 [Conway, J. H.][145]; [Radin, C.][146]; Sadun, L. (1999), "On angles whose squared trigonometric functions are rational", *[Discrete and Computational Geometry][147]*, **22**(3): 321– 332, [arXiv][148]: [math-ph/9812019][149], [doi][117]: [10.1007/PL00009463][150], [MR][119] [1706614][151], [S2CID][135] [563915][152], Table 3, p. 331.
8. ↑ [Akiyama, Jin][153]; Matsunaga, Kiyoko (2015), "15.3 Hilbert's Third Problem and Dehn Theorem", **[Treks Into Intuitive Geometry][154], Springer, Tokyo, pp. 382– 388, [doi][117]: [10.1007/978-4-431-55843-9][155], [ISBN][127] [978-4-431-55841-5][156], [MR][119] [3380801][157].
9. 1 2 3 [Rouse Ball, W. W.][158]; [Coxeter, H. S. M.][159] (1947), *Mathematical Recreations & Essays*(11th ed.), Macmillan, pp. 142– 143, 148
10. 1 2 Shephard, G. C. (1974), "Combinatorial properties of associated zonotopes", *Canadian Journal of Mathematics*, **26**(2): 302– 321, [doi][117]: [10.4153/CJM-1974-032-5][160], [MR][119] [0362054][161]; see in particular section 5, "cubical dissections of zonotopes"
11. ↑ [Dehn, Max][7] (1901), ["Ueber den Rauminhalt"][162], *[Mathematische Annalen][163]*(in German), **55**(3): 465– 478, [doi][117]: [10.1007/BF01448001][164], [S2CID][135] [120068465][165]
12. 1 2 3 [Hazewinkel, M.][166] (2001) [1994], ["Dehn invariant"][167], *[Encyclopedia of Mathematics][168]*, EMS Press
13. ↑ [Sydler, J.-P.][169] (1965), ["Conditions nécessaires et suffisantes pour l'équivalence des polyèdres de l'espace euclidien à trois dimensions"][170], *[Commentarii Mathematici Helvetici][171]*(in French), **40**: 43– 80, [doi][117]: [10.1007/bf02564364][172], [MR][119] [0192407][173], [S2CID][135] [123317371][174]
14. ↑ Debrunner, Hans E. (1980), "Über Zerlegungsgleichheit von Pflasterpolyedern mit Würfeln", *[Archiv der Mathematik][175]*(in German), **35**(6): 583– 587, [doi][117]: [10.1007/BF01235384][176], [MR][119] [0604258][177], [S2CID][135] [121301319][178].
15. ↑ \\mathbb{R}^n</math> and scissors congruence"},"volume":{"wt":"13"},"year":{"wt":"1995"},"doi-access":{"wt":"free"}},"i":0}}]}'/> [Lagarias, J. C.][179]; Moews, D. (1995), "Polytopes that fill R n {\displaystyle \mathbb {R} ^{n}}[image: {\displaystyle \mathbb {R} ^{n}}] and scissors congruence", *[Discrete & Computational Geometry][180]*, **13**( 3– 4): 573– 583, [doi][117]: [10.1007/BF02574064][181], [MR][119] [1318797][182].
16. ↑ Dupont (2001), p. 6.
17. 1 2 Goncharov, Alexander (1999), "Volumes of hyperbolic manifolds and mixed Tate motives", *Journal of the American Mathematical Society*, **12**(2): 569– 618, [doi][117]: [10.1090/S0894-0347-99-00293-3][183], [MR][119] [1649192][184].
18. ↑ Alexandrov, Victor (2010), "The Dehn invariants of the Bricard octahedra", *Journal of Geometry*, **99**( 1– 2): 1– 13, [arXiv][148]: [0901.2989][185], [doi][117]: [10.1007/s00022-011-0061-7][186], [MR][119] [2823098][187], [S2CID][135] [17515249][188].
19. 1 2 [Hartshorne, Robin][189] (2000), **[Geometry: Euclid and beyond][190], Undergraduate Texts in Mathematics, Springer-Verlag, New York, pp. 232– 234, [doi][117]: [10.1007/978-0-387-22676-7][191], [ISBN][127] [0-387-98650-2][192], [MR][119] [1761093][193].
20. 1 2 [Stillwell, John][194] (1998), **[Numbers and geometry][195], Undergraduate Texts in Mathematics, Springer-Verlag, New York, p. 164, [doi][117]: [10.1007/978-1-4612-0687-3][196], [ISBN][127] [0-387-98289-2][197], [MR][119] [1479640][198].
21. ↑ Dupont, Johan L. (2001), **[Scissors congruences, group homology and characteristic classes][199], Nankai Tracts in Mathematics, vol. 1, River Edge, New Jersey: World Scientific, p. 4, [doi][117]: [10.1142/9789812810335][200], [ISBN][127] [981-02-4507-6][201], [MR][119] [1832859][202], archived from [the original][203] on 2016-04-29.
22. 1 2 3 [Eppstein, David][204] (2025), "Orthogonal dissection into few rectangles", *Discrete & Computational Geometry*, **73**: 129– 148, [arXiv][148]: [2206.10675][205], [doi][117]: [10.1007/s00454-023-00614-w][206]
23. ↑ Fuchs, Dmitry; Tabachnikov, Serge (2007), **[Mathematical Omnibus: Thirty lectures on classic mathematics][207], Providence, RI: American Mathematical Society, p. 312, [doi][117]: [10.1090/mbk/046][208], [ISBN][127] [978-0-8218-4316-1][209], [MR][119] [2350979][210]. This source uses the Hamel basis formulation of the Dehn invariant, but with tensor notation used for the unit vectors.
24. ↑ [Schwartz, Rich][211] (June 10, 2013), ["The Dehn–Sydler theorem explained"][212] (PDF), *Math Notes*, Brown University Department of Mathematics, retrieved 2023-03-13
25. ↑ Coulson, David; Goodman, Oliver A.; Hodgson, Craig D.; Neumann, Walter D. (2000), ["Computing arithmetic invariants of 3-manifolds"][213], *Experimental Mathematics*, **9**(1): 127– 152, [doi][117]: [10.1080/10586458.2000.10504641][214], [MR][119] [1758805][215], [S2CID][135] [1313215][216]
26. 1 2 3 4 Dupont (2001), p. 7.
27. ↑ Dupont (2001), Theorem 6.2(a), p. 35. Dupont states that this is "a reformulation of a result of Jessen (1968) ".
28. ↑ Jessen (1968), Theorem 6, p. 255.
29. ↑ Görner, Matthias, ["α-polyhedra"][217], *Unhyperbolic*, retrieved 2024-06-26
30. ↑ Dupont, Johan L.; Sah, Chih-Han (1990), "Homology of Euclidean groups of motions made discrete and Euclidean scissors congruences", *Acta Mathematica*, **164**( 1– 2): 1– 27, [doi][117]: [10.1007/BF02392750][218], [MR][119] [1037596][219]
31. 1 2 Dehn, Max (1903), "Über Zerlegung von Rechtecken in Rechtecke", *Mathematische Annalen*, **57**(3): 314– 332, [doi][117]: [10.1007/BF01444289][220]
32. ↑ Spandaw, Jeroen (2004), "Dissecting cuboids into cuboids", *[The American Mathematical Monthly][221]*, **111**(5): 425– 429, [doi][117]: [10.2307/4145269][222], [JSTOR][124] [4145269][223], [MR][119] [2057392][224]
33. ↑ Gaifullin, Alexander A.; Ignashchenko, Leonid S. (August 2018), "Dehn invariant and scissors congruence of flexible polyhedra", *Proceedings of the Steklov Institute of Mathematics*, **302**(1): 130– 145, [arXiv][148]: [1710.11247][225], [doi][117]: [10.1134/s0081543818060068][226], [MR][119] [3894642][227]
34. ↑ Alexandrov, Victor; [Connelly, Robert][228] (2011), "Flexible suspensions with a hexagonal equator", *Illinois Journal of Mathematics*, **55**(1): 127– 155, [arXiv][148]: [0905.3683][229], [doi][117]: [10.1215/ijm/1355927031][230], [MR][119] [3006683][231], [S2CID][135] [12302514][232].
35. ↑ Alexander, Ralph (1985), "Lipschitzian mappings and total mean curvature of polyhedral surfaces. I", *Transactions of the American Mathematical Society*, **288**(2): 661– 678, [doi][117]: [10.2307/1999957][233], [JSTOR][124] [1999957][234], [MR][119] [0776397][235].

## External links

[[edit][236]]

- [Video about Dehn invariants][237] on [Numberphile][238]

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Dehn_invariant&oldid=1353872475][239] "

[Categories][240]:

- [Geometric dissection][241]
- [Polyhedra][242]

Hidden categories:

- [Good articles][243]
- [Articles with short description][244]
- [Short description is different from Wikidata][245]
- [Use mdy dates from March 2023][246]
- [Use list-defined references from March 2023][247]
- [Pages that use a deprecated format of the math tags][248]
- [CS1 German-language sources (de)][249]
- [CS1 French-language sources (fr)][250]

Search

Dehn invariant

5 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Wikipedia:Good_articles*
[2]: https://en.wikipedia.org/wiki/Dehn_function
[3]: https://en.wikipedia.org/wiki/Geometry
[4]: https://en.wikipedia.org/wiki/Polyhedron
[5]: https://en.wikipedia.org/wiki/Dissection_problem
[6]: https://en.wikipedia.org/wiki/Honeycomb_(geometry)
[7]: https://en.wikipedia.org/wiki/Max_Dehn
[8]: https://en.wikipedia.org/wiki/Hilbert's_third_problem
[9]: https://en.wikipedia.org/wiki/Flexible_polyhedron
[10]: https://en.wikipedia.org/wiki/Cube
[11]: https://en.wikipedia.org/wiki/Platonic_solid
[12]: https://en.wikipedia.org/wiki/Archimedean_solid
[13]: https://en.wikipedia.org/wiki/Truncated_octahedron
[14]: https://en.wikipedia.org/wiki/Tensor_space
[15]: https://en.wikipedia.org/wiki/Abelian_group
[16]: https://en.wikipedia.org/wiki/Exact_sequence
[17]: https://en.wikipedia.org/wiki/Group_homology
[18]: https://en.wikipedia.org/wiki/Dissection_puzzle
[19]: https://en.wikipedia.org/wiki/Rectilinear_polygon
[20]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=1
[21]: https://en.wikipedia.org/wiki/File:Triangledissection.svg
[22]: https://en.wikipedia.org/wiki/Tetrahedron
[23]: https://en.wikipedia.org/wiki/Wallace–Bolyai–Gerwien_theorem
[24]: https://en.wikipedia.org/wiki/Polygon
[25]: https://en.wikipedia.org/wiki/David_Hilbert
[26]: https://en.wikipedia.org/wiki/Area
[27]: https://en.wikipedia.org/wiki/Hilbert's_axioms
[28]: https://en.wikipedia.org/wiki/Euclidean_geometry
[29]: https://en.wikipedia.org/wiki/Euclid's_Elements
[30]: https://en.wikipedia.org/wiki/Solid_geometry
[31]: https://en.wikipedia.org/wiki/International_Congress_of_Mathematicians
[32]: https://en.wikipedia.org/wiki/Hilbert's_problems
[33]: https://en.wikipedia.org/wiki/Raoul_Bricard
[34]: https://en.wikipedia.org/wiki/Habilitation
[35]: https://en.wikipedia.org/wiki/Tensor_product_of_modules
[36]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=2
[37]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=3
[38]: https://en.wikipedia.org/wiki/Dihedral_angle
[39]: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
[40]: https://en.wikipedia.org/wiki/Linear_combination
[41]: https://en.wikipedia.org/wiki/Rational_number
[42]: https://en.wikipedia.org/wiki/Rational_dependence
[43]: https://en.wikipedia.org/wiki/Vector_space
[44]: https://en.wikipedia.org/wiki/Finite_set
[45]: https://en.wikipedia.org/wiki/Number_theory
[46]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=4
[47]: https://en.wikipedia.org/wiki/Right_angle
[48]: https://en.wikipedia.org/wiki/Golden_ratio
[49]: https://en.wikipedia.org/wiki/Supplementary_angles
[50]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=5
[51]: https://en.wikipedia.org/wiki/Parallelepiped
[52]: https://en.wikipedia.org/wiki/Truncated_tetrahedron
[53]: https://en.wikipedia.org/wiki/Truncated_cube
[54]: https://en.wikipedia.org/wiki/Rhombicuboctahedron
[55]: https://en.wikipedia.org/wiki/Cuboctahedron
[56]: https://en.wikipedia.org/wiki/Bitruncated_cubic_honeycomb
[57]: https://en.wikipedia.org/wiki/Truncated_dodecahedron
[58]: https://en.wikipedia.org/wiki/Truncated_icosahedron
[59]: https://en.wikipedia.org/wiki/Icosidodecahedron
[60]: https://en.wikipedia.org/wiki/Rhombicosidodecahedron
[61]: https://en.wikipedia.org/wiki/Truncated_icosidodecahedron
[62]: https://en.wikipedia.org/wiki/Zonohedron
[63]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=6
[64]: https://en.wikipedia.org/wiki/File:Triangulated_cube.svg
[65]: https://en.wikipedia.org/wiki/Orthoscheme
[66]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[67]: https://en.wikipedia.org/wiki/Invariant_(mathematics)
[68]: https://en.wikipedia.org/wiki/Volume
[69]: https://en.wikipedia.org/wiki/Schmitt–Conway–Danzer_biprism
[70]: https://en.wikipedia.org/wiki/Spherical_geometry
[71]: https://en.wikipedia.org/wiki/Hyperbolic_geometry
[72]: https://en.wikipedia.org/wiki/Hyperbolic_manifold
[73]: https://en.wikipedia.org/wiki/Hyperbolic_volume
[74]: https://en.wikipedia.org/wiki/Fundamental_domain
[75]: https://en.wikipedia.org/wiki/Fundamental_group
[76]: https://en.wikipedia.org/wiki/Universal_cover
[77]: https://en.wikipedia.org/wiki/Tetrahedral-octahedral_honeycomb
[78]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=7
[79]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=8
[80]: https://en.wikipedia.org/wiki/Piecewise_linear_manifold
[81]: https://en.wikipedia.org/wiki/Euclidean_space
[82]: https://en.wikipedia.org/wiki/Hyperbolic_space
[83]: https://en.wikipedia.org/wiki/Radian
[84]: https://en.wikipedia.org/wiki/Tensor_rank
[85]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=9
[86]: https://en.wikipedia.org/wiki/Hamel_basis
[87]: https://en.wikipedia.org/wiki/Group_isomorphism
[88]: https://en.wikipedia.org/wiki/Direct_sum_of_modules
[89]: https://en.wikipedia.org/wiki/Unit_vector
[90]: https://en.wikipedia.org/wiki/Axiom_of_choice
[91]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=10
[92]: https://en.wikipedia.org/wiki/Ideal_polyhedron
[93]: https://en.wikipedia.org/wiki/Horosphere
[94]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=11
[95]: https://en.wikipedia.org/wiki/Free_abelian_group
[96]: https://en.wikipedia.org/wiki/Prism_(geometry)
[97]: https://en.wikipedia.org/wiki/Rotation_group_SO(3)
[98]: https://en.wikipedia.org/wiki/Trivial_group
[99]: https://en.wikipedia.org/wiki/Kähler_differential
[100]: https://en.wikipedia.org/wiki/Algebraic_number
[101]: https://en.wikipedia.org/wiki/Special_linear_group
[102]: https://en.wikipedia.org/wiki/Möbius_transformation
[103]: https://en.wikipedia.org/wiki/Special_unitary_group
[104]: https://en.wikipedia.org/wiki/Motive_(algebraic_geometry)
[105]: https://en.wikipedia.org/wiki/Algebraic_K-theory
[106]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=12
[107]: https://en.wikipedia.org/wiki/File:Greek_cross_to_rectangle.svg
[108]: https://en.wikipedia.org/wiki/Aspect_ratio
[109]: https://en.wikipedia.org/wiki/Polyomino
[110]: https://en.wikipedia.org/wiki/Cauchy's_theorem_(geometry)
[111]: https://en.wikipedia.org/wiki/Bellows_conjecture
[112]: https://en.wikipedia.org/wiki/Strong_bellows_conjecture
[113]: https://en.wikipedia.org/wiki/Mean_curvature
[114]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=13
[115]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=14
[116]: https://en.wikipedia.org/wiki/Archive_for_History_of_Exact_Sciences
[117]: https://en.wikipedia.org/wiki/Doi_(identifier)
[118]: https://doi.org/10.1007%2Fs00407-021-00278-z
[119]: https://en.wikipedia.org/wiki/MR_(identifier)
[120]: https://mathscinet.ams.org/mathscinet-getitem?mr=4324749
[121]: https://en.wikipedia.org/wiki/Christopher_Zeeman
[122]: https://en.wikipedia.org/wiki/The_Mathematical_Gazette
[123]: https://doi.org/10.2307%2F3621846
[124]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[125]: https://www.jstor.org/stable/3621846
[126]: https://doi.org/10.1007%2F978-3-540-71133-9
[127]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[128]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-71132-2
[129]: https://mathscinet.ams.org/mathscinet-getitem?mr=2335496
[130]: https://scholar.archive.org/work/nrjfvgmzwjgjxc7qhyztxrnu3u
[131]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[132]: https://doi.org/10.1080%2F00029890.2007.11920458
[133]: https://www.jstor.org/stable/27642302
[134]: https://mathscinet.ams.org/mathscinet-getitem?mr=2354437
[135]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[136]: https://api.semanticscholar.org/CorpusID:7213930
[137]: https://doi.org/10.1007%2F978-1-4612-1340-6_3
[138]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-4612-7102-4
[139]: https://mathscinet.ams.org/mathscinet-getitem?mr=1731633
[140]: https://books.google.com/books?id=1xI6j05m7NUC&amp;pg=PA61
[141]: https://en.wikipedia.org/wiki/Børge_Jessen
[142]: https://doi.org/10.7146%2Fmath.scand.a-10888
[143]: https://www.jstor.org/stable/24489773
[144]: https://mathscinet.ams.org/mathscinet-getitem?mr=0251633
[145]: https://en.wikipedia.org/wiki/John_Horton_Conway
[146]: https://en.wikipedia.org/wiki/Charles_Radin
[147]: https://en.wikipedia.org/wiki/Discrete_and_Computational_Geometry
[148]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[149]: https://arxiv.org/pdf/math-ph/9812019
[150]: https://doi.org/10.1007%2FPL00009463
[151]: https://mathscinet.ams.org/mathscinet-getitem?mr=1706614
[152]: https://api.semanticscholar.org/CorpusID:563915
[153]: https://en.wikipedia.org/wiki/Jin_Akiyama
[154]: https://en.wikipedia.org/wiki/Treks_Into_Intuitive_Geometry
[155]: https://doi.org/10.1007%2F978-4-431-55843-9
[156]: https://en.wikipedia.org/wiki/Special:BookSources/978-4-431-55841-5
[157]: https://mathscinet.ams.org/mathscinet-getitem?mr=3380801
[158]: https://en.wikipedia.org/wiki/W._W._Rouse_Ball
[159]: https://en.wikipedia.org/wiki/Harold_Scott_MacDonald_Coxeter
[160]: https://doi.org/10.4153%2FCJM-1974-032-5
[161]: https://mathscinet.ams.org/mathscinet-getitem?mr=0362054
[162]: https://zenodo.org/record/2327856
[163]: https://en.wikipedia.org/wiki/Mathematische_Annalen
[164]: https://doi.org/10.1007%2FBF01448001
[165]: https://api.semanticscholar.org/CorpusID:120068465
[166]: https://en.wikipedia.org/wiki/Michiel_Hazewinkel
[167]: https://www.encyclopediaofmath.org/index.php?title=Dehn_invariant
[168]: https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics
[169]: https://en.wikipedia.org/wiki/Jean-Pierre_Sydler
[170]: https://eudml.org/doc/139296
[171]: https://en.wikipedia.org/wiki/Commentarii_Mathematici_Helvetici
[172]: https://doi.org/10.1007%2Fbf02564364
[173]: https://mathscinet.ams.org/mathscinet-getitem?mr=0192407
[174]: https://api.semanticscholar.org/CorpusID:123317371
[175]: https://en.wikipedia.org/wiki/Archiv_der_Mathematik
[176]: https://doi.org/10.1007%2FBF01235384
[177]: https://mathscinet.ams.org/mathscinet-getitem?mr=0604258
[178]: https://api.semanticscholar.org/CorpusID:121301319
[179]: https://en.wikipedia.org/wiki/Jeffrey_Lagarias
[180]: https://en.wikipedia.org/wiki/Discrete_&amp;_Computational_Geometry
[181]: https://doi.org/10.1007%2FBF02574064
[182]: https://mathscinet.ams.org/mathscinet-getitem?mr=1318797
[183]: https://doi.org/10.1090%2FS0894-0347-99-00293-3
[184]: https://mathscinet.ams.org/mathscinet-getitem?mr=1649192
[185]: https://arxiv.org/pdf/0901.2989
[186]: https://doi.org/10.1007%2Fs00022-011-0061-7
[187]: https://mathscinet.ams.org/mathscinet-getitem?mr=2823098
[188]: https://api.semanticscholar.org/CorpusID:17515249
[189]: https://en.wikipedia.org/wiki/Robin_Hartshorne
[190]: https://books.google.com/books?id=C5fSBwAAQBAJ&amp;pg=PA232
[191]: https://doi.org/10.1007%2F978-0-387-22676-7
[192]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-98650-2
[193]: https://mathscinet.ams.org/mathscinet-getitem?mr=1761093
[194]: https://en.wikipedia.org/wiki/John_Stillwell
[195]: https://books.google.com/books?id=5Db0BwAAQBAJ&amp;pg=PA164
[196]: https://doi.org/10.1007%2F978-1-4612-0687-3
[197]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-98289-2
[198]: https://mathscinet.ams.org/mathscinet-getitem?mr=1479640
[199]: https://web.archive.org/web/20160429152252/http://home.math.au.dk/dupont/scissors.ps
[200]: https://doi.org/10.1142%2F9789812810335
[201]: https://en.wikipedia.org/wiki/Special:BookSources/981-02-4507-6
[202]: https://mathscinet.ams.org/mathscinet-getitem?mr=1832859
[203]: http://home.math.au.dk/dupont/scissors.ps
[204]: https://en.wikipedia.org/wiki/David_Eppstein
[205]: https://arxiv.org/pdf/2206.10675
[206]: https://doi.org/10.1007%2Fs00454-023-00614-w
[207]: https://books.google.com/books?id=IiG9AwAAQBAJ&amp;pg=PA312
[208]: https://doi.org/10.1090%2Fmbk%2F046
[209]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-4316-1
[210]: https://mathscinet.ams.org/mathscinet-getitem?mr=2350979
[211]: https://en.wikipedia.org/wiki/Richard_Schwartz_(mathematician)
[212]: https://www.math.brown.edu/reschwar/MathNotes/jessen.pdf
[213]: https://projecteuclid.org/euclid.em/1046889596
[214]: https://doi.org/10.1080%2F10586458.2000.10504641
[215]: https://mathscinet.ams.org/mathscinet-getitem?mr=1758805
[216]: https://api.semanticscholar.org/CorpusID:1313215
[217]: https://www.unhyperbolic.org/sydler.html
[218]: https://doi.org/10.1007%2FBF02392750
[219]: https://mathscinet.ams.org/mathscinet-getitem?mr=1037596
[220]: https://doi.org/10.1007%2FBF01444289
[221]: https://en.wikipedia.org/wiki/The_American_Mathematical_Monthly
[222]: https://doi.org/10.2307%2F4145269
[223]: https://www.jstor.org/stable/4145269
[224]: https://mathscinet.ams.org/mathscinet-getitem?mr=2057392
[225]: https://arxiv.org/pdf/1710.11247
[226]: https://doi.org/10.1134%2Fs0081543818060068
[227]: https://mathscinet.ams.org/mathscinet-getitem?mr=3894642
[228]: https://en.wikipedia.org/wiki/Robert_Connelly
[229]: https://arxiv.org/pdf/0905.3683
[230]: https://doi.org/10.1215%2Fijm%2F1355927031
[231]: https://mathscinet.ams.org/mathscinet-getitem?mr=3006683
[232]: https://api.semanticscholar.org/CorpusID:12302514
[233]: https://doi.org/10.2307%2F1999957
[234]: https://www.jstor.org/stable/1999957
[235]: https://mathscinet.ams.org/mathscinet-getitem?mr=0776397
[236]: /w/index.php?title=Dehn_invariant&amp;action=edit&amp;section=15
[237]: https://www.youtube.com/watch?v=eYfpSAxGakI
[238]: https://en.wikipedia.org/wiki/Numberphile
[239]: https://en.wikipedia.org/w/index.php?title=Dehn_invariant&amp;oldid=1353872475
[240]: /wiki/Help:Category
[241]: /wiki/Category:Geometric_dissection
[242]: /wiki/Category:Polyhedra
[243]: /wiki/Category:Good_articles
[244]: /wiki/Category:Articles_with_short_description
[245]: /wiki/Category:Short_description_is_different_from_Wikidata
[246]: /wiki/Category:Use_mdy_dates_from_March_2023
[247]: /wiki/Category:Use_list-defined_references_from_March_2023
[248]: /wiki/Category:Pages_that_use_a_deprecated_format_of_the_math_tags
[249]: /wiki/Category:CS1_German-language_sources_(de)
[250]: /wiki/Category:CS1_French-language_sources_(fr)
