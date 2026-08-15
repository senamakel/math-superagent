# Grounding: the three candidates (majorization, Dirichlet energy, Nullstellensatz)

Research verdicts, per candidate. All three are refuted on evidence — each on
both a *structural* ground (a named theorem whose hypothesis fails here) and a
*concrete* ground (a real-row or class counterexample). None needs a prime
distribution beyond what Eppstein/Colonna already supply; each is refuted at
the general-class level, which is exactly where the inventor hoped they would
win.

---

## 1. `majorization-schur-flatness-lyapunov` — refuted

**What it is called.** The partial order is majorization / Hardy–Littlewood–
Pólya / Schur ordering; the machinery it invokes is Birkhoff's theorem (1946:
doubly stochastic = convex hull of permutation matrices), and Karamata's
theorem (majorization ⇔ Σφ(yᵢ) ≤ Σφ(xᵢ) for all convex φ).

**Precise statement of the theorem it relies on, and why the hypothesis fails.**
Karamata/Birkhoff require `x ≻ y` to imply `Σxᵢ = Σyᵢ`: majorization is
defined only between vectors of **equal sum** (Birkhoff's converse — `y = Dx`
for doubly stochastic D — forces sum preservation because D's rows sum to 1).
The run has *already established* (claim `chip-firing-path-collapse-refuted`,
evidence checked) that the absolute-difference row map **conserves no total
mass**: (2,0,3,1) has sums 6→7→2, (1,2,4,8) has 15→7. So `sorted(T(x))` and
`sorted(x)` have different totals, and the Karamata/Birkhoff equivalence — the
entire reason majorization is a vector Lyapunov — does not apply between the
two. One would have to pass to *weak* majorization (drop the equal-sum
condition), but then Karamata holds only for increasing convex φ, and the
monotonicity content collapses to the same max-dominated scalar that killed
the tropical approach.

**Concrete counterexample (off the flat stratum the claim must flatten).**
Halved x = (2,0,2,0) (not in the halved flat stratum {0,1}). T(x) = (2,2,2):
Σφ for φ(t)=t² is 8 → 12, i.e. the "flattening" (decreasing sum-of-squares)
*increases*. So even the weak "majorization makes the row flatter" thesis is
false of this map already on two-row data, and no λ<1 rescaling repairs a
quantity that goes the wrong way. This is the same rigid pair shape that killed
the contraction approach (ifs-attractor-contraction: the equal-mass
(a,a,c,c)-type pair).

**Class-level obstruction.** The flat stratum (halved {0,1} strings) is
*absorbing* (Rule-90 maps {0,1}↬{0,1}), so "once in, stays in" is free — but
the claim that majorization *forces everything in* is exactly the regeneration
statement. Eppstein 2011 (`anti-gilbreath-construction`, held claim) builds
2-then-odds sequences whose right edge leaves and re-enters 1 infinitely
often, so no monotone Schur-order convergence to a flat basin holds in the
class; the primes can only differ by unproved non-concentration, which this
approach supplies no mechanism for.

**Precedent.**
- Karamata/H-L-P definition and equal-sum requirement: Marshall–Olkin,
  *Inequalities: Theory of Majorization and its Applications* (1979); the
  Birkhoff-equivalence restated in Ljubenović 2015 (Filomat
  doi:10.2298/fil1509087l) and the Birkhoff-algorithm notes (Johnson et al.,
  Canad. Math. Bull. 2018, doi:10.4153/CMB-2017-030-9).
- No source applies majorization/Schur convexity to the iterated
  absolute-difference operator; the closest (Pečarić–Zwick 1989
  doi:10.1216/rmj-1989-19-1-303; Franjić 2015) use Schur convexity for
  divided-difference/quadrature inequalities, never as a Gilbreath Lyapunov.
- Run's own: `chip-firing-path-collapse-refuted` (sum not conserved),
  `ifs-attractor-contraction` (refuted contraction), `anti-gilbreath-construction`
  (class evasion).

**Verdict: refuted.** `killed-by`: the sum-preservation hypothesis of
Karamata/Birkhoff fails (row map is not sum-preserving), plus the SOS
counterexample (2,0,2,0)→(2,2,2): 8→12 off the flat stratum, plus Eppstein's
class-level escape. The partial-order wrapper adds no hypothesis that repairs
the equal-sum failure; this is the scalar-potential dead end in a vector
disguise.

---

## 2. `dirichlet-energy-electric-network-recurrence` — refuted

**What it is called.** Effective resistance / Dirichlet energy / Rayleigh
monotonicity / Pólya's theorem (recurrence of random walk ⇔ infinite effective
resistance to infinity): Doyle–Snell random-walk-and-electric-networks theory.

**Precise statements (all classical, transfer verbatim to paths).** Pólya: the
2D lattice is recurrent (effective resistance to infinity is infinite), the 3D
transient. Rayleigh monotonicity: adding/removing an edge of conductance c
changes effective resistance in a monotone, bounded way. These are theorems
about a *fixed* graph with *fixed* conductances.

**Why the hypotheses fail here.**
(a) **The network is not fixed — it is rebuilt every row.** The candidate's
conductance rule cᵢ = 1_{|hᵢ−hᵢ₊₁|≤1} makes the vertex/edge set a function of
the current halved row. Pólya and Rayleigh are static-network theorems; there
is no theorem that "effective resistance to infinity is infinite" across a
*sequence of changing networks* is equivalent to "the (2,4)-events keep
coming." That biconditional is asserted, not proved, and is precisely the
unproved regeneration rate restated in electrical language (the same
re-description that killed the chip-firing and zero-sum-flow approaches).
(b) **The left component is disconnected from the tail by the boundary.** With
this conductance rule the leading block is a finite conducting path; the
"break" (a c=0 edge, a difference ≥2 in halved units) separates it from the
tail. Effective resistance of a *disconnected* left component to infinity is
trivially infinite, so "recurrent iff R→∞" is either ill-posed or has no
content — it cannot distinguish regeneration from death.
(c) **The energy is not monotone on the real rows** (hand oracle from
witnesses.json first-12 of each row, halved):
- E(h₁)=7, E(h₂)=3, E(h₃)=5. **E increases at step 2→3** (3→5). So the
  claimed Lyapunov monotonicity E(h_{k+1}) ≤ E(h_k) + boundary is false in its
  raw form on the actual prime rows. A boundary term rescuing a 3→5 increase
  "bounded by the drain law" is not supplied and is the open content.

**Verdict: refuted.** `killed-by`: oracle E monotonicity fails 3→5 on real
rows; the "R to infinity" criterion is trivial/ill-posed once the break
disconnects the left block from the tail; the recurrence/regeneration
biconditional is the unproved rate restated. The classical electric-network
theory is real but supplies no theorem for a *changing* network, which is what
a Gilbreath row sequence is.

---

## 3. `combinatorial-nullstellensatz-failure-polytope` — refuted

**What it is called.** Alon's Combinatorial Nullstellensatz (1999,
doi:10.1017/S0963548398003411) — a nonvanishing criterion for a polynomial on
a *box* (full grid) S₁×…×Sₙ; its modern form (Mészáros–Rónyai 2014,
doi:10.71352/ac.42.249): the CNS holds exactly when the vanishing ideal I(X)
of the point set X has a universal Gröbner basis of the box-like form
{xᵢ^dᵢ}. The UNSAT tool the candidate actually wants is *Hilbert's*
Nullstellensatz (certificate Σβᵢfᵢ = 1), which is a different theorem.

**Why the hypotheses fail.**
(a) **Theorem misapplication.** CNS is an *existence* statement: a low-degree
polynomial with a nonzero top coefficient does NOT vanish on a box. The
failure set {A_k(1) ≥ 4 first time} is a union of rational polytopes
(half-spaces and integer-coefficient branches), which is not a box S₁×…×Sₙ,
and by Mészáros–Rónyai the CNS box argument applies only to point sets whose
vanishing ideal is box-like — a generic polytope intersection is far from
that. The claim "UNSAT over a polynomial ideal is a theorem" belongs to
Hilbert's Nullstellensatz, whose certificate degree is in general uncontrolled
(double-exponential); there is no known small-certificate bound for GC.
(b) **No finite bound.** The SAT+Nullstellensatz certificate method works when
the conjecture has a finite extremal bound (EDP: no discrepancy-2 sequence of
length 1161; MATHCHECK: finite Ramsey-type numbers). GC is about an *infinite*
array with a *global* extension criterion (claim
`valid-extension-backward-nonlocal-refuted`, `gatti-2020-valid-extension-global-formula`:
whole-prefix factorial weights). The run has already recorded that no published
SAT/SAT+CAS attack reaches GC *because* the successful targets are finite-state
(`minimal-counterexample-geometry` ground). A certificate at finite k proves
nothing about k→∞.
(c) **Class-level impossibility of a gap-only certificate.** The input
properties the candidate names (g₁=2, all later gaps even, mod-4 switch) are
exactly what holds for 2-then-odds sequences that FAIL: Colonna's delete-5
sequence (claim `colonna-deletion-left-edge-failure`, held) is a 2-then-odds
bounded-gap sequence with A₁(1) = 4 — a first failure already at k=1 inside
the class. So any polynomial that nonvanishes on "the primes" and vanishes on
"the failure set" must use a distinguishing property that holds for the primes
and not for Colonna's sequence; the only candidate is CHT non-concentration,
which is *unproved for primes* (that is literally the open problem). A
degree/box certificate that separates the primes from the failure polytope is
equivalent to the conjecture, not a route to it.

**Verdict: refuted.** `killed-by`: CNS requires a box, not a polytope union
(and the intended UNSAT theorem is Hilbert's Nullstellensatz, with uncontrolled
certificate degree); there is no finite bound where a certificate terminates for
an infinite-array conjecture; and any even-gap bounded class already contains a
first-failure example (Colonna delete-5: A₁(1)=4), so no gap/mod-4-only
certificate can separate the primes from the failure set. This is the refuted
minimal-counterexample/Farkas line at higher degree, and the degree higher does
not escape the global-extension obstruction.

---

## What survives

- The equal-sum obstruction (candidate 1) and the change-of-network obstruction
  (candidate 2) are the same shape as the refuted contraction and flow
  approaches: any monotone or variational certificate on the *whole row*
  reduces to the unproved regeneration rate. This is pattern-matching the run
  already sees; it is recorded so the next round does not re-propose a vector
  Lyapunov or an energy, which is the same class.
- The flat-stratum-absorption fact (halved {0,1} is closed under the map) is
  real and already held (rule90-interior-xor, closure-0d-double-edge). The
  candidates add no new mechanism for how a row *enters* the flat stratum —
  which is the only open content.
