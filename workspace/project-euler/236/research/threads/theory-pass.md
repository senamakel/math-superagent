# Thread: External theory for Diophantine ratio feasibility

**Opened:** 2026-04-26, per steer directive 1.

**Question:** What does the standard mathematical literature establish about the
structure of rational solutions to simultaneous linear equations with
integrality bounds, and what (if anything) does it contribute beyond the
gcd-threshold + bounded-subset-sum reduction already derived in this run?

**Three topics to download and assess:**

1. **Rational solutions to linear systems with integrality constraints.**
   Classic integer linear programming / Diophantine linear systems — Knuth
   (Art of Computer Programming) on Diophantine equations, or standard
   treatments of solving a·x + b·y = c with bounds.

2. **Farey / Stern-Brocot mediant structure for bounding rational ratios.**
   The mediant property and how it constrains the set of rationals between two
   bounds; the Stern-Brocot tree as an enumeration of reduced fractions.

3. **Standard treatments of simultaneous linear Diophantine equations.**
   Systems of the form Σ k_i·w_i = 0 with each k_i in [1, K_i], and what is
   known about the structure of solution sets (subset-sum with bounded integer
   multipliers, not just 0/1).

**What it rests on:** The run already has a working structural reduction
(gcd-threshold + bounded subset-sum, verified on all 35 m) and an efficient
solution.py, but it has not connected this to the named theory. The directive
asks that we fetch and file the governing theory rather than treating the
reduction as a novel derivation.

**What to do with it:** Each source goes into `research/sources/<slug>.md`
with a `claim` block stating the theorem, its hypotheses, whether they hold
here, and the source URL. Sources that contribute nothing beyond what we
already derived are noted as confirmatory; sources that expose a better method
or a missing structural fact become the basis for improving solution.py.

**Falsifies:** If none of the three topics yields a theorem that applies to
this problem under its hypotheses, then the literature pass confirms that the
self-derived reduction was necessary. If a source does yield a stronger
classification (e.g. that all valid m must lie in a mediant subtree of
Stern-Brocot), that would falsify the current approach of enumerating
candidates from product 1.