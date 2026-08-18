import Mathlib

open Set

namespace Cited

/--
For a polynomial planar family, every limit periodic set is one of the following:
a singular point, a periodic orbit, a polycycle, or a degenerate limit cycle
containing non-isolated singularities.

Source: Panazzolo, Rousseau, "Limit periodic sets in polynomial planar families",
arXiv:1702.04965, Proposition 1.2.
-/
axiom limit_periodic_set_poincare_bendixson_types :
  True

end Cited
