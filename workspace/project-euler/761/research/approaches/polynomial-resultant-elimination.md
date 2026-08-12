```approach
idea: Polynomial resultant elimination — derive the exact minimal polynomial of V_hexagon² directly from the coordinate geometry of the hexagon boundary-time equalization condition, using computational algebraic elimination (resultants / Gröbner bases) in place of trigonometric machinery. No K-index, no acos, no trigonometric inequality — pure algebraic elimination via polynomial ideals.

mechanism: The hexagon (inradius 1, flat-top) has vertex coordinates and edge equations involving only √3, so every geometric quantity is algebraic of degree at most 2 over Q. Parameterize the exit point Q on one edge by a single rational parameter t ∈ [0,1] (or by coordinate x along the edge). The swimmer's staging point P is on the 1/v-scaled homothetic inner hexagon, centrally opposite the runner at R′ on the outer boundary. The chord distance |PQ|² is a quadratic polynomial in t with coefficients involving v and √3. The runner's perimeter distance from R′ to Q along the hexagon boundary is piecewise-linear in the edge index and linear in t. The critical-speed condition is:

  max_{edge e, t∈[0,1]} [perim(R′ → Q_e(t))] / |P − Q_e(t)| = v

At the maximizing t (interior to the edge), the derivative of the ratio with respect to t vanishes, giving the first-order condition d/dt [perim/|PQ|] = 0. After clearing denominators, this is a polynomial equation in t and v² (and √3). Isolate √3 by squaring, then use resultants to eliminate t, yielding the minimal polynomial for v². For n=6 the result should be the known quadratic 9v⁴ − 240v² + 256 = 0, recovered by a route that never references K, α, arccos, or tan(xθ) = (x+n)tanθ.

The key structural advantage: the hexagon's critical exit point lies on an edge adjacent to the edge opposite the runner's position (established pattern from the square case and the known K=2 result). So only a small number of edge candidates need to be checked, and the elimination can be done edge-by-edge with sympy's resultant or groebner.

status: adopted
first-step: | Write `code/hexagon_resultant.py`.  Define the hexagon in coordinates:
| - inradius 1, flat-top orientation.
| - Runner R′ starts at right-edge midpoint: (cos 30°, 0) = (√3/2, 0) in
|   the (x along edge, y perpendicular) frame, or equivalently at boundary
|   arc-length s=0.
| - The 1/v-scaled inner hexagon has vertices at (1/v)·(outer vertices).
|   The point opposite R′ on the inner hexagon is P = (√3/(2v), 0) scaled
|   from the outer midpoint's opposite point, or more carefully the point
|   on the inner hexagon that is centrally opposite the runner — this is
|   the homothetic image of the runner's position under scaling by 1/v
|   about the center.
| - Parameterize the candidate exit edge (the one adjacent to the opposite
|   edge, following the K=2 / square pattern) by a rational parameter t:
|   Q(t) = (1−t)·V_i + t·V_{i+1} for the edge from vertex i to i+1.
| - Write |PQ|² as a polynomial in t with coefficients in ℚ[√3][v].
| - Write the runner's perimeter distance from R′ (s=0) to Q(t) as a
|   piecewise-linear function of t: on each edge, it is a_0 + a_1·t.
| - At the critical speed, the maximizing t is interior to the edge, so
|   d/dt (perim / |PQ|) = 0.  Write this as numerator = 0 after clearing
|   denominators, producing a polynomial in t, v, √3.
| - Isolate √3 by moving terms: express as A + B√3 = 0, square to get
|   A² − 3B² = 0, a polynomial in t and v with rational coefficients.
| - Use `sympy.resultant(poly_t, poly_deriv, t)` to eliminate t, yielding
|   the minimal polynomial of v (or v²).  Expect 9v⁴ − 240v² + 256 = 0.
| - Extract the positive root > 1, confirm it matches 5.05505046, and
|   reduce to the closed form 2 + 2√21/3.
|
| This is an independent algebraic derivation: no K-index, no acos, no
| trigonometric inequality — pure polynomial elimination over ℚ[√3].
| It confirms the closed form by a completely different computational path.
```