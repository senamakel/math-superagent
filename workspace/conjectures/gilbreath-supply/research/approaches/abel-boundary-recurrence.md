# Abel summation in the depth index: a boundary-only recurrence for S(n)

```approach
idea: Attack the excess S(n)=Σ_{d=2}^{n−1} (−1)^{T(n,d)} by discrete Abel
summation (summation by parts) over the DEPTH index d, using the exact first-order
recurrence of the fold cells coming from Pascal's rule C(d,i)=C(d−1,i)+C(d−1,i−1).
The sum over d telescopes, leaving an inhomogeneous (boundary) term that is a
*local* statistic of h at O(log n) positions — the one-point/two-point residue
statistics that PNT in AP mod 4 controls — while the bulk is a pure recurrence.
This is a change of *variable ordering* (sum in d, recur in n), not a claim about
polynomial degree (distinct from `newton-series-degree-dichotomy`) and not a
2×2 weight-block recursion (distinct from the refuted `pascal-cascade`).
mechanism: T(n,d)=⊕_{o⊆d} h[n−1−d+o] obeys, from Pascal's rule mod 2 applied to the
d index, an exact neighbour relation T(n,d)=T(n−1,d)⊕T(n−1,d−1) (up to the window
reversal), because the submask set of d splits by the lowest set bit. Summation by
parts: S(n)=Σ_d (−1)^{T(n,d)} is then a first-order linear difference equation in n,
S(n)=S(n−1) + (boundary terms at d=2 and d=n−1) + (telescoped body). The boundary
terms are sums of (−1)^{h[j]} over a single index or a pair — a *one-point* or
*adjacent-pair* statistic of the prime gap parity — and the body telescopes to
zero or to a shift. The load-bearing, checkable claim is that the inhomogeneity is
LOCAL: if true, SUPPLY reduces to bounding a short, explicit sum over the prime
residue string, which is in the territory of PNT in AP (one-point, provable) or
at worst the adjacent switch density (the known barrier), with the depth-average
doing the rest of the work.
status: refuted
killed-by: The literal first-order neighbour relation this approach mounts its
whole mechanism on, T(n,d)=T(n−1,d)⊕T(n−1,d−1), is FALSE for the actual fold-cell
definition T(n,d)=⊕_{o⊆d}h[n−1−d+o]. Counterexample (hand-verified, and recorded as
claim `abel-boundary-recurrence-relation-false`): h=(0,0,0,1), n=4, d=2 gives
T(4,2)=h[1]⊕h[3]=1 while T(3,2)⊕T(3,1)=h[0]⊕h[2]⊕h[1]⊕h[2]=0; generally
T(n,d)⊕T(n−1,d)⊕T(n−1,d−1)=h[n−1]⊕h[?], not identically 0, because the three cells
read different contiguous windows of the same h and the window-start shifts prevent
the far-end boundary from cancelling. Since the Abel-summation-in-d body was to be
built on that exact relation, the approach's own first-step falsifier fires before
any number theory. The deeper "the d-sum telescopes into a LOCAL boundary term" is
untouched by this counterexample but must be restated with a correct indexing
relation before it can support anything; as a distinct speculation it was not priced.
Changes of ground: this is NOT the refuted pascal-cascade (block recursion) nor
newton-series-degree-dichotomy (degree); it is a distinct summation-in-d /
recurrence-in-n move, killed on its own literal relation.
precedent: (the algebraic/analytic toolkit is real and citable — Abel summation by
parts, Abel–Zeilberger algorithm, binomial-transform recurrences; but the advertised
"boundary is LOCAL" is an in-workspace falsifiable claim, and the literal relation it
needs has been refuted — see "Grounded, and what is not" below)
- Chen, Hou, Jin, "The Abel–Zeilberger algorithm", Electron. J. Combin. 18 (2011), https://doi.org/10.48550/arxiv.1105.0178 (Abel's lemma on summation by parts + Zeilberger's creative telescoping to derive recurrences for definite sums — the named home of "sum in one index, recur in another").
- Koepf, "Algorithms for the indefinite and definite summation", arXiv:math/9412227 (extended Zeilberger/Gosper for non-hypergeometric terms; certification of recurrences).
- Bostan–Lairez–Salvy, "Multiple binomial sums", J. Symbolic Comput. 2016, https://doi.org/10.1016/j.jsc.2016.04.002 (creative telescoping and diagonal/generating-function methods for definite sums; binomial transforms).
- In-workspace (established): claim `excess-is-negative-character-sum` (ν₂(n)=(n−2−S(n))/2); claim `endpoint-sign-corrected-identity` (−1)^{T(n,d)}=∏_R χ(r_{a_R})χ(r_{b_R}); claim `abel-boundary-recurrence-relation-false` (the killed relation).
- Pascal/binomial-transform recurrences and summation by parts: Chen–Hou–Jin,
  "The Abel–Zeilberger algorithm", Electron. J. Combin. 2011, https://doi.org/10.37236/2013
  (Abel's lemma on summation by parts combined with Zeilberger's algorithm to produce
  recurrences for definite sums — the named home of "sum in one index, recur in
  another"); "Combinatorial sums and finite differences", Discrete Math. 2007,
  https://doi.org/10.1016/j.disc.2007.06.002 (binomial transform g_n = Σ C(n,k)a_k
  evaluated through the finite-difference companion; the exact transform/recurrence
  machinery); "Identities from the binomial transform", J. Number Theory 2006,
  https://doi.org/10.1016/j.jnt.2006.04.009 (binomial pairs and their recurrences).
- Pascal's matrix as one discrete transform (binomial/Seidel): "Unification of
  Legendre, Laguerre, Hermite, and binomial discrete transforms using Pascal's
  matrix", J. Math. Anal. Appl., https://doi.org/10.1007/BF00980712 .
- In-workspace (established): claim `excess-is-negative-character-sum`
  (ν₂(n)=(n−2−S(n))/2 — the sign-forced recurrence SUPPLY needs an upper bound on S);
  claim `endpoint-sign-corrected-identity` (−1)^{T(n,d)}=∏_R χ(r_{a_R})χ(r_{b_R}),
  the character form on which any local-boundary reading must land);
  claim `g-run-telescope-verified` (run decomposition of ↓d); adopted route
  `fold-second-moment-krawtchouk` and refuted `newton-series-degree-dichotomy`
  (which this route is explicitly not); refuted `pascal-cascade-block-recursion`
  (which this route is explicitly not).
first-step: Derive the exact neighbour relation T(n,d) in the folded (reversed)
indexing and machine-verify it against the brute submask-XOR oracle for all
(n,d), n ≤ 200, d ∈ [2,n−1]. Then Abel-sum S(n) in d to produce the explicit
boundary recurrence S(n)=F(S(n−1), boundary(n)), verify it against the oracle
(and against the known S(4000)=48, ν₂(4000)=1975), and print the boundary term's
explicit arithmetic content. Falsifier: if the boundary term is NOT local (if it
re-accumulates a full n-length sum), the route is dead before any number theory.
```

## Grounded, and what is not

**The toolkit is real.** Abel summation by parts (Abel's lemma), the binomial
transform, finite-difference evaluation, and Pascal-matrix recurrences are named,
citable, and apply to sums of the shape Σ_d a_d with a_d governed by a Pascal/binomial
recurrence. The "recur in the outer index, telescope in the inner index" move is the
Abel–Zeilberger / binomial-transform pattern: a definite sum over d satisfying a
first-order difference recurrence in d yields an evaluation through a boundary term.
This is exactly the shape S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} is claimed to have, and
the mechanism is internally consistent with the in-workspace-established identity
ν₂(n)=(n−2−S(n))/2 (claim `excess-is-negative-character-sum`), whose sign structure is
the operative constraint (SUPPLY needs an *upper* bound on S).

**But the crux — "the boundary term is LOCAL" — is a falsifiable in-workspace claim,
NOT a literature fact.** Abel summation converts a sum into a boundary term only when
you can sum the *partial* finite differences of the summed quantity; here the summed
objects are (−1)^{T(n,d)}, and T(n,d) is itself an XOR over submasks of d. The literal
neighbour relation T(n,d)=T(n−1,d)⊕T(n−1,d−1) exists (Pascal mod 2), but whether
telescoping S(n) in d leaves an inhomogeneity supported on O(log n) (or O(1))
positions — a one/two-point residue statistic — rather than re-accumulating a full
n-length sum, is precisely what the first-step's oracle check must decide, and the
file's own speculation already names the two possible outcomes: a one-point statistic
(PNT-in-AP territory, provable) versus the adjacent-switch sum Σ_j (−1)^{[q_j≢q_{j+1}]}
(the named parity barrier, open). No published source evaluates S(n) by Abel summation
in d; this is the route's own construction, and its hypothesis folds back onto known
ground either way but the sign-forced recurrence it would give is new.

**What the literature does NOT supply.** No source applies Abel/by-parts summation to
the submask-XOR fold weight wt(Φ_n h) or to the excess S(n). The route is distinct from
the refuted `newton-series-degree-dichotomy` (no degree claim) and from the refuted
`pascal-cascade` (no 2×2 block recursion) — the mechanism here is a summation-in-d /
recurrence-in-n, which is a different operation — and the refutation record does not
already cover it. So this is a genuinely open reformulation of the parity barrier's
sign structure, grounded in a real toolkit but with its single load-bearing property
(unproven locality of the boundary) left to the first-step's falsifier.

**Verdict.** Grounded as machinery: Abel summation / binomial-transform recurrence is
real, citable, and internally consistent with the in-workspace sign identity. Not
grounded as a theorem: the locality of the boundary term is unproven and is exactly
what the first-step checks against the brute oracle; the named risk (landing on the
adjacent-switch parity barrier) is a real possibility the file correctly flags. Run the
first-step — derive the neighbour relation, Abel-sum in d, and print the explicit
boundary term — before spending number theory. If the boundary is O(log n) as hoped,
the reduction is to PNT-in-AP territory; if it is the full switch sum, the route has
merely re-encountered the known barrier in a new sign-forced form.
