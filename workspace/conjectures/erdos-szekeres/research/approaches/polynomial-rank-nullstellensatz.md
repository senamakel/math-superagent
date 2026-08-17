```approach
idea: Algebraic / polynomial representation of the 4-point convexity criterion,
bounded by a Combinatorial-Nullstellensatz / Alon–Füredi grid rank bound whose
host is the Boolean cube {0,1}^{n-2} — size exactly 2^{n-2}. The ES construction
is literally indexed by the layers of that cube (|T_i| = C(n-2,i) = number of
i-subsets of [n-2]), so a polynomial/grid bound with host 2^{n-2} is
STRUCTURALLY EXACT, unlike every known counting route whose host is a grid
simplex of size ~4^n.

mechanism: Encode "the 4 points a,b,c,d are in convex position" as the sign of a
specific oriented determinant (the Radon/orientation sign pattern is a rank-3
Plücker/alternant condition). Then "X has no convex n-gon" means: for every
n-subset there is a 4-subset whose convexity determinant is zero in the "bad"
(triangle-containing) orientation — i.e. a degree-(const) polynomial P built
from the four-point convexity locality has NO n-subset where all its convexity
monomials are nonzero. By Combinatorial Nullstellensatz / Alon–Füredi (a
low-degree polynomial that does not vanish on all of a product grid A_1×…×A_m
has a normalized nonzero count; the degree-and-grid arithmetic forces |X| ≤
these-algebraic-bounds), the absence of a convex n-gon forces the point set to
index into at most an (n-2)-dimensional Boolean cube, hence |X| ≤ 2^{n-2}.
This is DIFFERENT from the closed routes: it is not a Sperner/LYM inequality on
an injection into B_{n-2} (boolean-lattice-injection, closed because Sperner
can't give 2^{n-2} and uniqueness is false — that objection is about INJECTION +
SPERNER, not about a polynomial rank bound); it does not count a 4^n grid
(etv-grid-simplex-compression, closed because its host is C(2n-4,n-2) ≈ 4^n —
MY host is the Boolean cube of size exactly 2^{n-2}, and the bound is algebraic
(rank/degree) rather than a count of order ideals); and it is not geometric
lifting to caps/cups (strict-convex-lifting, closed because its charge is the
4^n partition budget). The algebraic variable N ≤ 2^{n-2} is new to the run.

status: refuted
killed-by: The load-bearing step is exactly the injection that killed
boolean-lattice-injection-compression twice over: the mechanism needs an
injective index of ARBITRARY no-convex-n-gon sets into {0,1}^{n-2}, and the
α-injectivity whose natural host the closed route etv-grid-simplex-compression
established is the grid simplex C(2n-4,n-2) ≈ 4^n, NOT 2^{n-2}. The es_construct
alignment check (nonzero set = 2^{n-2} = |X|) only re-verifies the already-known
LOWER bound — it cannot give the required injection for general sets, and the
critical "4^n-collapse" risk the inventor flagged is unresolvable by the
literature (no published CN/Alon–Füredi application to the ES upper bound exists,
so nothing grounds the Boolean-cube host for arbitrary sets). Closed as a proof
route; this is the same obstruction that closed ETV and the boolean-lattice line,
re-stated in an algebraic register. Not re-derived.

precedent: The polynomial-grid machinery is REAL and standard: N. Alon,
"Combinatorial Nullstellensatz", Combin. Probab. Comput. 8 (1999) 7–29
(doi 10.1017/S0963548398003411); Alon–Füredi, "Covering the cube by affine
hyperplanes", European J. Combin. 14 (1993) 79–83 — the sharp bound on the number
of nonzeros/grid-misses of a low-degree polynomial over a product grid; A. Bishnoi,
P. L. Clark, A. Potukuchi, J. R. Schmitt, "On zeros of a polynomial in a finite
grid", Combin. Probab. Comput. 27 (2018), doi 10.1017/S0963548317000566, which
generalizes Alon–Füredi (per-variable degrees, rings with Condition (D)) and ties
it to Reed–Muller codes, blocking sets, and the Jamison–Brouwer–Schrijver bound —
the canonical modern development of the exact tool the mechanism invokes. The
4-point convexity criterion (a set is convex iff every 4-subset is) is already the
library claim es35-four-criterion (Erdős–Szekeres 1935) and is machine-verifiable
with lib/es_geom. Had the run searched the surveys (Morris–Soltan BAMS 2000,
doi 10.1090/S0273-0979-00-00877-6; Suk JAMS 2016, doi 10.1090/jams/869) and the
wider CN literature, NO published application of the Combinatorial Nullstellensatz
/ Alon–Füredi method to the Erdős–Szekeres convex-position upper bound
ES(n) ≤ 2^{n-2}+1 was found — the run is not re-deriving an existing result. The
precedent question the inventor flagged as open is answered: no one has posed ES
as a Boolean-cube CN grid bound. The tools are real but the alignment claim (the
convexity polynomial is nonzero on exactly {0,1}^{n-2}) is the run's own and is
NOT established anywhere.

caveat-on-collapse (must be read before adopting): The mechanism needs an
injective indexing of *arbitrary* no-convex-n-gon sets into {0,1}^{n-2} so the
polynomial lives on a fixed cube for all sets. That injection is EXACTLY the load
boolean-lattice-injection-compression carried and died on (Sperner cannot give
2^{n-2}), and it is also exactly the α-injectivity whose natural host the closed
route etv-grid-simplex-compression showed is C(2n-4,n-2) ≈ 4^n, not 2^{n-2}. The
alignment check on es_construct (nonzero set = 2^{n-2} = |X|) only verifies that
the CONSTRUCTION saturates the upper bound — which is already the known lower
bound — it does not by itself give an injection for general sets. The critical
risk the inventor states (the natural host recurs as a 4^n simplex) is real and
unresolved by the literature, which is exactly why this is grounded-as-reformulation
and NOT grounded-as-proof. A smallest-n first target is legitimate (n=5,6,7 on
es_construct) purely to test whether the nonzero set can be made to sit on a cube
of size 2^{n-2} rather than a 4^n host.

first-step: (tool_builder, today, exact, scoped to es_construct n=5,6,7) (1)
Build the convexity-determinant polynomial/certificate: for each 4-subset the
(exact) rank-3 orientation sign; confirm on es_construct that "no convex n-gon"
really is "every n-subset contains a bad 4-subset" (this is the verified
es35-four-criterion, machine-check it). (2) Assemble the single low-degree
polynomial P whose nonzero set is the convex n-subsets and whose gadget is the
Boolean cube: verify that on es_construct(5,6,7) the nonzero set has size
2^{n-2} = |X| = 8,16,32, i.e. the construction saturates the algebraic bound —
this is the critical alignment check that the 2^{n-2} constant really is the
*host size* (unlike ETV where the correct host is 4^n). (3) If (2) holds, state
the Alon–Füredi / Nullstellensatz bound and test whether it is tight at n=5,6,7
and whether any no-convex-n-gon set of size 2^{n-2} saturates it (i.e. the
polynomial is nonzero on exactly the Boolean cube = the extremal set IS the
cube). Speculative core to attack first: whether the convexity polynomial really
vanishes / is nonzero exactly on a {0,1}^{n-2} grid — if the host turns out to
be larger (a 4^n simplex again), record that as the refutation, exactly as ETV's
host was. Positive control: reproduce ES(4)=5, ES(5)=9 at the algebraic level
(no convex n-gon ⟹ N ≤ 2^{n-2} for n=4,5 with the same P).

falsified-by: an n-avoiding set of 2^{n-2} points on which the constructed
convexity polynomial is nonzero at MORE than 2^{n-2} positions of any
{0,1}^{n-2} grid structure, or a proof that the polynomial's natural host is a
4^n simplex (which would collapse this to the closed ETV route). Also falsified
if the run cannot produce a fixed Boolean-cube indexing for arbitrary sets, since
then the polynomial has no fixed host at all.
```
