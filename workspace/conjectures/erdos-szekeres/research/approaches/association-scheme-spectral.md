```approach
idea: Recover the exact 2^{n-2} as a SPECTRAL / association-scheme bound rather
than a count. Put the convexity data on a Boolean-cube/Hamming association
scheme {0,1}^{n-2} (the ES construction's own index space: |T_i| = C(n-2,i) =
#i-subsets), assemble a symmetric "convexity interaction" matrix A over the
points, and bound |X| by the rank / by a Delsarte-style linear-programming
inequality whose extremal eigenvector is the flat (2^{n-2}-filling) one. The
2^{n-2}+1 constant is then a spectral threshold, structurally different from a
Ramsey count.

mechanism: The Boolean cube with Hamming distance is an association scheme whose
(j-th) adjacency matrices commute and diagonalize jointly by Krawtchouk
polynomials — the standard spectral machinery of binary codes (Delsarte;
MacWilliams–Sloane). Build A from the 4-point convexity relation: A_{pq} = a
fixed function of whether {p,q} completes many/few convex 4-sets. "No convex
n-gon" forces a bounded-norm, low-rank, or sign-structured condition on A (a
no-convex n-gon means the convexity "energy" cannot concentrate — every
n-tuple has a non-convex 4-tuple, giving a locality/2-distance constraint that
bounds the spectrum). Delsarte's LP then caps the size of a configuration
whose convexity matrix has a prescribed eigenvalue **first-feasible at
2^{n-2}** — the extremal (flat, cube-filling) set saturating it. This is
DIFFERENT from every closed route: not Sperner (no antichain inequality), not
a 4^n grid count, not an f-vector/Kruskal–Katona (no shadow), not a
rational-identity Möbius/β bound (that computes interior, closed), not
order-dimension, not allowable-sequence. It is a pure eigen/association-scheme
inequality, and the host of size exactly 2^{n-2} is the feature the counted
routes lacked.

status: refuted
killed-by: Delsarte LP / Krawtchouk / Hamming-scheme bounds constrain CODE SIZES at
a Hamming/rank-distance threshold; planar convexity is ORDER-TYPE data, not a
metric, so a convexity interaction matrix over a point set is not an
association-scheme matrix and Delsarte's LP cannot even be posed. This is the
weakest-grounded of the three proposed candidates and is closed as a proof
route: the 2^{n-2} host is the extremal construction's own index space, not an
a-priori indexing of arbitrary sets, and the same injection-loading problem that
killed boolean-lattice-injection-compression applies. No published source frames
ES as a spectral threshold; the empirical alignment check was the only surviving
fragment.

precedent: The association-scheme / Delsarte LP / Krawtchouk machinery is REAL
and standard, but its domain is coding theory: P. Delsarte, "An algebraic
approach to the association schemes of coding theory", Philips Res. Repts.
Suppl. 10 (1973); F.J. MacWilliams and N.J.A. Sloane, "The Theory of
Error-Correcting Codes", North-Holland 1977; a partial ordered set and q-Krawtchouk
polynomials (JCTA 1981, doi 10.1016/0097-3165(81)90023-6); Delsarte LP bounds for
codes reconstructed in modern work (e.g. "New Solutions to Delsarte's Dual Linear
Programs", IEEE Trans. Inform. Theory 2024, doi 10.1109/TIT.2024.3476974;
eigenvalue bounds for sum-rank-metric codes, IEEE Trans. Inform. Theory 2023,
doi 10.1109/TIT.2023.3339808). All of these bound the SIZE OF CODES (independent
sets at Hamming/rank distance ≥ d) in association schemes; NONE applies an
association-scheme spectral inequality to POINT-SET CONVEXITY or to the
Erdős–Szekeres problem. The empirical content — that a convexity interaction
matrix over planar points has Delsarte-type extremal structure capping the point
count at an eigenvalue threshold first-feasible at 2^{n-2} — could not be
grounded: no reference frames convex-position configurations as association-scheme
points, and nothing in the Delsarte/coding literature carries over because a
planar point set is not a code at Hamming distance under a convexity relation
(there is no natural metric; the convexity relation is order-type data, not a
Hamming-distance threshold). The surveys of the ES problem (Morris–Soltan BAMS
2000, doi 10.1090/S0273-0979-00-00877-6; Suk JAMS 2016, doi 10.1090/jams/869;
Mubayi–Suk "ES problem and an induced Ramsey type", doi 10.1112/s0025579319000135)
list no spectral/Delsarte attack. The open precedent question the inventor flagged
is answered: NO ONE has framed ES's 2^{n-2} as a Delsarte/spectral threshold; but
equally there is no evidence the framing can work — the matrix would have to
encode convexity as a distance-threshold scheme, which planar order types are not.

caveat (must be read before adopting): The mechanism's own falsifier — "a proof
that the matrix's eigenvalue spectrum is compatible with size ~2^n" — is the
likely outcome, because the Hamming-scheme structure of the Boolean cube indexes
the ES construction's BLOCKS (the sizes of the lower-bound construction), which
is a statement about the extremal example, not a mechanism that bounds an
arbitrary set. Nothing in the literature suggests the convexity interaction matrix
obeys a Delsarte linear program with extremal ratio exactly 2^{n-2}/(2^{n-2}+1);
the coding-theoretic origin of Delsarte bounds (minimum-distance thresholds) has
no analogue in convexity of point configurations. As with polynomial-rank-
nullstellensatz, the host {0,1}^{n-2} is the size of the extremal construction,
not an a-priori indexing of arbitrary sets, so the same loading problem that killed
boolean-lattice-injection applies. This is the weakest-grounded of the three
candidates as a proof mechanism, though its first-step (an empirical check of the
extremal structure on es_construct) is cheap and legitimate.

first-step: (tool_builder, today, exact) On the verified es_construct n=5,6,7,
index the points into the Hamming scheme by their block index (i = |subset|),
build the convexity interaction matrix A (exact integers: A_{pq} = number of
convex 4-sets through p,q, computed with lib/es_geom), and empirically check
whether the ES construction is the extremal point of a Delsarte-type LP — i.e.
whether the flat (equal-weight) vector is the only configuration meeting the
eigenvalue constraints at size 2^{n-2}. Then state the specific inequality
"rank / spectral-norm(A) ≤ 2^{n-2}" and test tightness and whether it is
violated by any no-convex-n-gon set of size 2^{n-2}+1 (positive control:
ES(4)=5, ES(5)=9 at the spectral level). Speculative core to attack first:
whether the convexity matrix truly has the Delsarte/LP extremal structure or
gives only a weaker (≥2^n) bound — if it cannot push below ~2^n, record that
as the refutation.

falsified-by: an n-avoiding set of 2^{n-2}+1 points whose convexity matrix
satisfies the same Delsarte/eigen constraints (i.e. the spectral inequality is
not tight at 2^{n-2}), or a proof that the matrix's eigenvalue spectrum is
compatible with size ~2^n. FARTHER (meta) falsifier: a demonstration that the
convexity interaction matrix is not an association-scheme matrix at all (no
Hamming-distance threshold structure), so Delsarte's LP cannot even be posed —
this is the most likely outcome given that planar convexity is order-type data,
not a distance relation.
```
