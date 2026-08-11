# PE 579 — Mathematical theory for Lattice Points in Lattice Cubes

Research notes (sourced). NOT the published answer; no forum/solution threads used as
sources. One incidental search hit a Project Euler solution GitHub repo; it is **excluded**
as a source/method and is not cited below. The strategy section is synthesized from the
academic references + the run's own (as-yet-unexecuted) derivation.

## 0. Problem restatement and notation

A *lattice cube* = 8 vertices, all in Z^3. Every such cube is determined by a corner
P0 ∈ Z^3 and three pairwise-orthogonal equal-length integer edge vectors u,v,w:
vertices = P0 + a·u + b·v + c·w, a,b,c ∈ {0,1}.

Notation (consistent with the references):
- common (Euclidean) edge length = ℓ  (so |u|=|v|=|w| = ℓ).
- common **squared** length / norm = N = ℓ^2.
- For an edge vector e = (e1,e2,e3), set d(e) := gcd(|e1|,|e2|,|e3|).

C(n) = number of distinct such cubes with all 8 vertices in [0,n]^3.
S(n) = sum, over those cubes, of the number of lattice points in the closed cube.

Target: S(5000) mod 10^9. (Not computed here — theory only.)

## 1. Cataloguing lattice cubes (topic 1)

**Objects.** A set {u,v,w} ⊆ Z^3\0 that is pairwise-orthogonal and equal-norm is a
`3-icube` (Goswick–Kiss–Moussong–Simányi) or the generating set of a `cubic sublattice`
(the lattice it spans). This is exactly what the references below classify.

### 1a. Quaternion (Euler–Rodrigues) parametrization
Every orthogonal matrix with integer entries is obtained from a quaternion (rational
Euler–Rodrigues / Euler parameters). Concretely, with quaternion q=a+bi+cj+dk of norm
N=a^2+b^2+c^2+d^2, the rotation matrix that sends i,j,k to the edge vectors u,v,w is

```
u = ( a^2+b^2-c^2-d^2 , 2(bc - ad)   , 2(bd + ac) )
v = ( 2(bc + ad)      , a^2-b^2+c^2-d^2, 2(cd - ab) )
w = ( 2(bd - ac)      , 2(cd + ab)    , a^2-b^2-c^2+d^2 )
```

with |u|^2=|v|^2=|w|^2 = N = (a^2+b^2+c^2+d^2)^2, i.e. edge length ℓ = N.
Sources: Wikipedia "Euler–Rodrigues formula"
https://en.wikipedia.org/wiki/Euler–Rodrigues_formula ;
Euler (1771)/Rodrigues (1840) attributed in
https://rotations.berkeley.edu/other-representations-of-a-rotation/ ;
MathOverflow discussion of Cremona & Euler's rational parametrization
https://mathoverflow.net/questions/287523/why-is-this-mapping-surjective ;
Ionascu's parametrization (4)/(17) in the cube paper (below).

### 1b. Classification theorem (3D icubes / cubic sublattices)
**Goswick, Kiss, Moussong, Simányi, *Sums of squares and orthogonal integral vectors*,
J. Number Theory 132 (2012) 37–53 (arXiv:0806.3943):**
- Every icube (u,v,w) ∈ Z^3 of edge length m is, up to permuting/negating columns and
  an integer scale, the columns of an *Euler matrix* from a Hurwitz-integral quaternion.
  Corollary 5.12: if (u,v,w) is an icube then there is α ∈ E and an integer d such that
  (u,v,w) and the columns of d·E(α) differ only by column permutation and sign
  changes; edge length = d·N(α). (N(α) = quaternion norm.)
- Theorem 1.5: if x ∈ Z^3 has norm n·m^2 (n squarefree) it lies in a cubic sublattice of
  edge length m; if x is primitive the cubic lattice is unique.
- The edge/norm N of every twin pair (2-icube) is a sum of two squares; the converse is
  false (e.g. norm 17 vector (2,2,3) has no twin).
  Source: https://ar5iv.labs.arxiv.org/html/0806.3943  (arXiv:0806.3943)

**Cubic sublattices (elementary, cross-product proof) — arXiv:2203.01901:**
Every cubic sublattice Γ ⊆ Z^3 has a unique form Γ = k·Γ(v,d) with k,d positive
integers and v primitive (characterization of the whole lattice, not per-vector), and a
vector v ∈ Z^3 whose squared length is divisible by d^2 is contained in a cubic
sublattice of edge d (primitive ⇒ unique).
Sources: https://arxiv.org/pdf/2203.01901 (and MaRDI summary
https://portal.mardi4nfdi.de/wiki/Cubic_sublattices )

### 1c. Canonical enumeration (avoiding the 24-fold symmetry) — Kiss–Kutas
**E. W. Kiss, P. Kutas, *Cubes of integral vectors in dimension four*,
Studia Sci. Math. Hungar. 49 (2012) 525–537 (arXiv:1108.3113).**
In Z^4 (and the machinery applies to 3-icubes), one icube corresponds to many
representations. A **primary** quaternion selects a canonical representative so that each
cube (orientation) is generated **exactly once**. A quaternion is primary if its real
part has parity different from the other three components AND a+b+c+d ≡ 1 (mod 4).
Sources: https://doi.org/10.1556/sscmath.49.2012.4.1225 ,
https://ar5iv.labs.arxiv.org/html/1108.3113

> Practical consequence: loop over primary quaternions (bounds on a,b,c,d from N ≤ n^2),
> build (u,v,w) once, then handle translations and integer scaling algebraically.

## 2. Lattice points in a lattice cube / parallelepiped (topic 2)

### 2a. Ehrhart theorem (topic 4)
**Ehrhart's theorem:** Let P ⊆ R^d be a *lattice* polytope (vertices in Z^d). Then
L(P,t) := |t P ∩ Z^d| is a **polynomial** in t of degree d (leading coeff = d-volume,
constant term 1). If P is merely *rational* (denominator q = least k with kP integral),
L(P,t) is a **quasipolynomial** of period dividing q.
**Ehrhart reciprocity:** the interior count L(P°,t) = (−1)^d L(P,−t).
Sources: Beck–Robins, *Computing the Continuous Discretely*, Springer (cited within the
papers below); DeLoera survey https://www.math.ucdavis.edu/~deloera/RECENT_WORK/semesterberichte.pdf ;
Paffenholz lecture notes
https://www2.mathematik.tu-darmstadt.de/~paffenholz/daten/preprints/20220826_integer_points_polyhedra.pdf ;
"An Invitation to Ehrhart Theory" https://doi.org/10.48550/arxiv.1405.7647

### 2b. Ehrhart polynomial of a lattice cube — Ionascu, Theorem 3.1
**E. J. Ionascu, *Ehrhart polynomial for lattice squares, cubes and hypercubes*,
Rev. Roumaine Math. Pures Appl. 64 (2019) 57–80.**
For a lattice cube in R^3 with edge vectors (rows) of common length ℓ and edge-gcds
d1,d2,d3 (d_i = gcd of the coordinates of edge vector i), the Ehrhart polynomial is

```
L(t) = ℓ^3 t^3 + ℓ(d1+d2+d3) t^2 + (d1+d2+d3) t + 1
```

and by reciprocity the interior count is L°(t) = −L(−t)
= ℓ^3 t^3 − ℓ(d1+d2+d3) t^2 + (d1+d2+d3) t − 1.
Source: https://imar.ro/journals/Revue_Mathematique/pdfs/2019/1/6.pdf

**Verification against both worked examples (done by hand here):**

Cube A (axis-aligned, side 3): u=(3,0,0), v=(0,3,0), w=(0,0,3), ℓ=3, d1=d2=d3=3.
L(1) = 27 + 3·9 + 9 + 1 = 64 ✓ (matches 64).
Interior: L°(1) = 27 − 27 + 9 − 1 = 8 ✓ (problem says 8 interior).
Surface = 64−8 = 56 ✓.

Cube B: u=(1,2,2), v=(2,−2,1), w=(2,1,−2), all |v|=3 ⇒ ℓ=3; d1=d2=d3=1 (each vector
primitive). L(1) = 27 + 3·3 + 3 + 1 = 40 ✓ (problem says 40).
Interior: L°(1) = 27 − 9 + 3 − 1 = 20 ✓. Surface 40−20 = 20 ✓.

So Theorem 3.1 exactly reproduces the statement's lattice-point counts, and separates
surface vs interior (via reciprocity).

### 2c. Closed form for a lattice parallelepiped (matching the above)
For a parallelepiped spanned by integer vectors u,v,w,
# lattice points in the closed parallelepiped =
`1 + Σ_gcd(edge) + Σ_gcd(face-normal cross products) + |det|`
i.e. the t-coefficient is Σ (gcd of each edge vector), the t^2-coefficient is Σ (gcd of
the three cross products u×v, v×w, w×u), and the t^3-coefficient is |det| = volume.
For a *cube*, u×v = ±ℓ·w so gcd(u×v) = ℓ·d3, hence the t^2 coefficient Σ gcd = ℓ(d1+d2+d3)
and t-coefficient Σ gcd(edge) = d1+d2+d3 — consistent with Ionascu's Theorem 3.1.
Sources: Beck–Robins / Paffenholz notes (fundamental-parallelepiped index = |det|,
Proposition 2.26); the identity is the Ehrhart polynomial of the cube ((3,1) of Ionascu);
Ionascu also gives the analogous **square** result Thm 2.2: E2(t) = D t^2 + (d+d′) t + 1.

## 3. General efficient-summing strategy (topic 3)

These are general techniques synthesized from the classified theory + own derivation
(no final answer is produced; no solution repo used):

1. **Enumeration of orientations once.** Loop over primary Hurwitz quaternions with
   N = a²+b²+c²+d² ≤ n² (Kiss–Kutas canonical form), build edge vectors (u,v,w) via the
   Euler–Rodrigues columns. This enumerates each cube *orientation* (edge triple up to
   rotation, not yet translation or scale) exactly once.

2. **Scale factor.** A base orientation with edge length ℓ gives, for each integer scale
   t ≥ 0, the cube with edges t·u,t·v,t·w and edge length t·ℓ. Max t is bounded by
   fitting the cube in the box (below).

3. **Translation count.** For a fixed orientation and scale t, define coordinate spans
   s_x = t(|u_x|+|v_x|+|w_x|), s_y = t(|u_y|+|v_y|+|w_y|), s_z = t(|u_z|+|v_z|+|w_z|).
   (These are the full x/y/z extents of the 8-vertex set over a corner, independent of
   corner; own derivation.) A valid corner z∈[0,n]^3 (so the whole cube fits) is any
   point of the box [0, n−s_x]×[0, n−s_y]×[0, n−s_z], giving
   `(n+1−s_x)(n+1−s_y)(n+1−s_z)` translations, a polynomial of degree ≤3 in t.

4. **Lattice-point count per cube.** Use Ionascu's Ehrhart polynomial (2b): a degree-3
   polynomial in t.

5. **Sum over t.** For each orientation, S-contribution = Σ_{t≥1}^{T}
   [L_cube(t) · translation_count(t)], a polynomial of degree 6 in t, and the
   C-contribution = Σ translation_count(t), degree 3. Sum both with precomputed power
   sums Σ t^k (k=0..6) via Faulhaber / closed forms — O(1) per orientation after the
   power sums are built. Complexity is then dominated by the orientation count
   (bounded by the number of (a,b,c,d) with N ≤ n², poly in n), not by n or by
   enumerating cubes/points directly — this is what makes n = 5000 feasible without
   enumerating S(5000) points.

Techniques for lattice-points-in-boxes for rotated cubes generally fall back on Ehrhart
polynomials (exact, polynomial in the dilation/scale) + polynomial summation with power
sums: these are exactly the structure used above and are standard (Beck–Robins; the
power-sum / Faulhaber reduction is elementary).

## 4. Source list (all academic)
- arXiv:0806.3943 — Goswick, Kiss, Moussong, Simányi, "Sums of squares and orthogonal integral vectors"
  https://ar5iv.labs.arxiv.org/html/0806.3943
- arXiv:2203.01901 — "Cubic sublattices" (cross-product characterization)
  https://arxiv.org/pdf/2203.01901 ; MaRDI https://portal.mardi4nfdi.de/wiki/Cubic_sublattices
- arXiv:1108.3113 / Studia Sci. Math. Hungar. 49 (2012) — Kiss, Kutas, "Cubes of integral vectors in dimension four" (primary quaternions)
  https://doi.org/10.1556/sscmath.49.2012.4.1225 ; https://ar5iv.labs.arxiv.org/html/1108.3113
- Ionascu, "Ehrhart polynomial for lattice squares, cubes and hypercubes", Rev. Roumaine Math. Pures Appl. 64 (2019) 57–80
  https://imar.ro/journals/Revue_Mathematique/pdfs/2019/1/6.pdf
- Beck & Robins, "Computing the Continuous Discretely" (Ehrhart theory, reciprocity) — Springer.
- DeLoera survey: https://www.math.ucdavis.edu/~deloera/RECENT_WORK/semesterberichte.pdf
- Paffenholz notes: https://www2.mathematik.tu-darmstadt.de/~paffenholz/daten/preprints/20220826_integer_points_polyhedra.pdf
- "An Invitation to Ehrhart Theory": https://doi.org/10.48550/arxiv.1405.7647
- Euler–Rodrigues formula: https://en.wikipedia.org/wiki/Euler–Rodrigues_formula ;
  https://rotations.berkeley.edu/other-representations-of-a-rotation/ ;
  https://mathoverflow.net/questions/287523/why-is-this-mapping-surjective

## 5. Caveats
- No code could be executed in this run (no shell tool); the "verification" of the two
  worked examples and the translation-count / power-sum identities are hand-checked.
  They should be confirmed by the implementer's small brute force (n=1,2,4,5,10,50)
  before trusting the full pipeline.
- I did NOT compute or seek S(5000). The final answer must come from the implementers'
  own run.
