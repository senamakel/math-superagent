# Hilbert's 16th problem

Hilbert's sixteenth problem, *"The problem of the topology of real algebraic
curves and surfaces"*, has two parts. They are different subjects with a common
ancestor, and only one of them is this workspace's target.

## Part I — real schemes (background here, not the target)

For a nonsingular real plane algebraic curve of degree `n`, its real point set in
`RP²` is a disjoint union of circles ("ovals", plus a one-sided component when
`n` is odd). Determine which *real schemes* — which nestings and mutual
positions of those ovals — are realised by a curve of degree `n`, and the same
for surfaces in `RP³`.

Recalled status, **to be confirmed or struck against sources, not built on**:
Harnack's bound `(n−1)(n−2)/2 + 1` on the number of components is sharp;
degree 6 was classified by Gudkov (1969); the Gudkov–Rokhlin congruence
`p − m ≡ k² (mod 8)` holds for M-curves of even degree `n = 2k`; Petrovskii,
Arnold and Rokhlin supply further inequalities and congruences; Viro's
patchworking classified degree 7; degree 8 is *not* fully classified, and the
undecided real schemes there are a finite, explicit list — Orevkov's braid /
complex-orientation obstructions and patchworking constructions are what has
been closing them one at a time.

That finite undecided list makes Part I an unusually well-shaped target for this
harness, and it is deliberately **out of scope for this pass**: it needs a
different oracle (patchworking, Viro diagrams, braid monodromy) and a different
literature. Spin a sibling workspace for it rather than folding it in here.

## Part II — limit cycles (the target)

For a planar polynomial vector field

```
ẋ = P(x, y),   ẏ = Q(x, y),   P, Q ∈ R[x, y],   max(deg P, deg Q) ≤ n,
```

a **limit cycle** is a periodic orbit that is isolated in the set of periodic
orbits. Set

```
H(n) = sup { number of limit cycles of X : X polynomial planar, deg X ≤ n }.
```

> **(H16.2)** Is `H(n) < ∞` for every `n ≥ 2`? And what are the possible
> configurations (mutual positions, nesting) of the limit cycles?

`H(1) = 0` — a linear field has no limit cycle. **Everything from `n = 2`
onward is open, including whether `H(2)` is finite at all.** This is the
statement meant when a paper says "Hilbert's 16th problem" today.

Two things about the formulation matter and are easy to lose:

1. **Uniformity is the whole content.** For a *fixed* polynomial field,
   finiteness is a theorem (below). H16.2 asks for a bound depending only on
   `n` — a statement about the family, and the gap between the two is exactly
   where a century of work sits.
2. **It is not merely a counting question.** The second half — which
   configurations occur — is asked, is almost untouched for `n ≥ 3`, and admits
   partial answers (a realisable configuration is a construction, hence
   certifiable) even while the bound stays unknown.

## Known results — leads, not imports

**Every item below is recalled from memory. Re-establish each from a primary
source before anything rests on it; print the source and the exact hypothesis
beside the ones you confirm, and strike the ones you cannot.**

**Finiteness for one field (Dulac's problem).** Dulac (1923) claimed that an
individual analytic planar vector field has finitely many limit cycles.
Ilyashenko found the gap (early 1980s). The theorem was then proved
independently by Ilyashenko (1991) and Écalle (1992), by very different routes
(resurgent functions / almost-regular germs). **It gives no bound uniform in the
coefficients**, and the reason it does not is the single most important
structural fact about the problem.

**Reduction to finite cyclicity (Roussarie's program).** For a fixed `n` the
family, compactified in coefficients and in the phase plane, has a compact
parameter/limit space; limit cycles can only accumulate on *limit periodic
sets* (singular points, closed orbits, polycycles at finite distance and at
infinity). `H(n) < ∞` follows if every limit periodic set in the closure has
**finite cyclicity** — finitely many limit cycles bifurcating from it under
perturbation within the family. Roussarie (1998) is the standard reference.

**The `n = 2` list.** Dumortier, Roussarie and Rousseau (1994) reduced
`H(2) < ∞` to the finite cyclicity of **121 graphics**. Most have since been
settled; a small number are reported still open, and *which* ones and how many
is the first fact this run must pin down. **A single unsettled graphic proved
finitely cyclic is a real, publishable result, and is the most concrete route to
progress that exists here.**

**Hilbert–Arnold problem.** For generic finite-parameter families of *smooth*
fields, the number of limit cycles bifurcating from a nondegenerate polycycle is
bounded. Ilyashenko–Yakovenko proved this for elementary polycycles; Kaloshin
gave an explicit bound of shape `2^{c n²}` for `n` parameters. Elementary is the
hypothesis carrying the weight — nilpotent and degenerate polycycles are where
it stops.

**Infinitesimal (weakened / tangential) H16.** For `H` a polynomial of degree
`n + 1` and `ω` a 1-form with polynomial coefficients of degree `≤ n`, bound the
number of isolated zeros of the Abelian integral `I(h) = ∮_{γ(h) ⊂ {H = h}} ω`
over continuous families of ovals. Varchenko and Khovanskii proved a uniform
bound `V(n) < ∞` non-constructively; Binyamini, Novikov and Yakovenko (2010)
gave an *explicit* bound, doubly exponential in `n`. This is the linearised
problem: it bounds limit cycles born in a first-order perturbation of a
Hamiltonian field, and not H16.2 itself.

**Lower bounds.** `H(2) ≥ 4` (Shi Songling; Chen–Wang, around 1979–80), with a
`(3,1)` configuration; `H(2) = 4` is the standing conjecture. `H(3) ≥ 13` is
claimed. Christopher–Lloyd (1995) showed `H(n)` grows at least like
`n² log n` — so any candidate bound of order `n²` or below is refuted before it
is examined. Locally, the number `M(n)` of small-amplitude limit cycles around a
single singular point satisfies `M(2) = 3` (Bautin, 1954, via what is now the
Bautin ideal) and `M(3) ≥ 11` (Żołądek), with later claims of more.

**Liénard and Smale's 13th.** For `ẋ = y − F(x)`, `ẏ = −x`, Smale asked for a
bound in `deg F`. The Lins–de Melo–Pugh conjecture (`k` cycles for
`deg F = 2k + 1`) was **disproved** by slow–fast constructions
(Dumortier–Panazzolo–Roussarie; De Maesschalck–Dumortier). Take this as a
warning about the plausibility of sharp conjectures in this field, not as
folklore.

**Surveys.** Ilyashenko's *Centennial history of Hilbert's 16th problem*
(Bull. AMS, 2002) and Ilyashenko–Yakovenko's *Lectures on Analytic Differential
Equations* are the two places to start; Roussarie's book has the bifurcation
machinery.

## The three tests every argument in this workspace must pass

These are the analogue of a characteristic-`p` counterexample: cheap, decisive,
and applied *before* effort is spent.

1. **The smooth test — where does analyticity enter?**
   A `C^∞` planar vector field can have infinitely many limit cycles, and a
   `C^∞` family can have unbounded numbers of them. So **any argument for
   finiteness must have a step that fails for smooth fields**, and naming that
   step is part of stating the argument. An argument built from topology,
   index theory, phase-plane geometry or transversality alone — never touching
   analyticity, quasianalyticity, or algebraicity of the coefficients — proves a
   false statement and is refuted, whatever it looks like. This is precisely
   Dulac's error: an asymptotic expansion of the return map manipulated as if it
   determined the map.

2. **The lower-bound test.** Any claimed bound must be checked against
   `H(2) ≥ 4`, `H(3) ≥ 13` and `H(n) ≳ n² log n`. A bound below a confirmed
   lower bound is an error in the argument, located immediately.

3. **The slow–fast test.** Sharp-looking conjectures here die to canard and
   relaxation-oscillation constructions in a singular limit (Liénard, above).
   Any conjectured *sharp* count must be examined in the slow–fast regime — put
   a small parameter where the argument assumes the field is generic — before it
   is believed.

Record, for each candidate argument, which test it was run against and the
step that failed. A candidate whose failure point under test 1 cannot be located
is not "probably fine"; it is unfinished, and saying so is a result.

## What is genuinely unknown

- `H(2) < ∞`. Equivalently, by the reduction: finite cyclicity of every one of
  the 121 graphics. **One unsettled graphic is a self-contained target.**
- Finite cyclicity of any degenerate (non-elementary, nilpotent) polycycle class
  not already covered.
- `H(2) = 4`, or any finite upper bound whatsoever for `n = 2`.
- Sharp counts for Abelian integrals in specific families where only the
  doubly-exponential general bound is known — an exact count for a named
  Hamiltonian family, proved by an argument-principle / Picard–Fuchs route.
- Improved lower bounds: `H(3) ≥ 14`, `M(3) ≥ 12`, or a better growth rate than
  `n² log n`.
- Configurations: which nestings of `k` limit cycles are realisable in degree
  `n`. Almost nothing is known for `n ≥ 3` and each realisation is a
  construction that can be certified.

## What counts as a result

In descending order of value.

1. Finite cyclicity of a limit periodic set that the literature records as open
   — a graphic from the DRR list above all.
2. A finite bound on `H(n)` for some `n ≥ 2` under an explicitly stated
   restriction (a subfamily, a normal form, a sign condition), with the
   restriction stated before the proof and the obstruction to removing it named.
3. A sharp or improved zero-count for Abelian integrals in a named family,
   with the Picard–Fuchs system written down and the argument-principle count
   carried out.
4. A new lower bound — a certified configuration with more limit cycles than the
   published count for its degree, or more small-amplitude cycles at a focus.
   Certified means an interval-arithmetic trapping-region proof or an exact
   Bautin-ideal computation, never a phase portrait.
5. A realisability or non-realisability theorem for a configuration of limit
   cycles in degree `n`.
6. A refutation, with an explicit witness, of a published approach or a folklore
   sharp conjecture — for instance a slow–fast family beating a conjectured
   count.
7. An exact, reproducible computation extending a known boundary: Lyapunov
   quantities / Bautin ideal for a family further than published, or the
   feasibility wall of that computation stated with its measurements.

**Do not claim `H(n) < ∞`, and do not claim `H(2) = 4`.** A proof of either
produced in a run of this length is, on prior, an error. If you believe you have
one, the deliverable is the argument written out with every step's status
labelled and all three tests above applied to it explicitly — not an
announcement.
