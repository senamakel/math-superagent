# Research pass on three proposed candidates — final report

Grounding conducted for the inventor's three proposed approaches, taking each
to the literature, checking the precise statement of the theorems each rests on
and whether their hypotheses hold here, and correcting each file under
`research/approaches/`.

## 1. circular-chromatic-sharpened-bound — GROUNDED

**Theorem.** (Vince 1988, "Star chromatic number", J. Graph Theory 12:551–559;
surveyed by Zhu 2001.) For every finite graph G, with chi_c(G) the circular
chromatic number, `chi(G) - 1 < chi_c(G) <= chi(G)`, hence `chi(G) = ceil(chi_c(G))`.
A (k,d)-circular colouring is f: V -> {0,...,k-1} with `d <= |f(u)-f(v)| <= k-d`
on each edge; `chi_c = min{ k/d }`.

**Holds here:** yes. The central equivalence is exactly right and verified by
several independent sources (Pêcher–Wagler EJC 2020 survey; circular game
chromatic paper; algebraic no-homomorphism paper): `chi_c(G) > 4` **iff** G is
not 4-colourable. Chi_c is strictly finer than chi (takes non-integer values).

**Correction (caveat, not refutation):** deciding `chi_c(G) > 4` is equivalent
in difficulty to deciding 4-colourability (the threshold IS the chromatic
threshold), and computing chi_c is NP-hard — so "certifies non-4-colourability
without the exponential 4-SAT search" overclaims for arbitrary graphs. The real
value: (a) vertex-transitive Eisenstein-lattice distance graphs, where
`chi_c = chi_f` is a closed-form exact LP with no SAT; (b) a tightness grader —
a 4-colourable UDG with chi_c close to 4 is the most promising spindling seed.

## 2. discharging-minimal-counterexample — GROUNDED (method), mechanism corrected

**The mechanism as written is wrong**, and corrected:
- A 5-chromatic graph is **necessarily non-planar** (four-colour theorem: every
  planar graph is 4-colourable; a 5-critical graph is not 4-colourable).
- Therefore "charge each *face* by *angle sums*, discharge via **Euler's
  formula**" does not apply — no planar embedding, no Euler identity.

**The method is fully viable via the non-planar k-critical discharging
literature**, which does NOT use Euler's formula:
- Dirac 1957: `2|E| >= (k-1)n + k-3` for k-critical graphs.
- Krivelevich 1997; Kostochka–Yancey 2014: `f_5(n) >= (9n-5)/4` (avg degree
  > 4.25).
- Cranston–Rabern 2016 state their discharging proof explicitly "does not rely
  on planarity or the four-colour theorem."

**What it buys the size-bound rung:** edge-lower-bound `c·n` combined with the
unit-distance edge ceiling `u_2(n) = O(n^{4/3})` (claim `unit-distance-upper-bound`)
gives `c·n <= C·n^{4/3}`, i.e. a **constant analytical lower bound** on the size
of any 5-chromatic UDG — exactly the analytic route past the nauty census's n=12
stall, with the geometric 60°-neighbourhood structure (`sharp-nbhd-local`) only
sharpening the constant.

## 3. rigidity-matroid-henneberg-construction — GROUNDED, with two overclaims corrected

**Theorem.** (Pollaczek-Geiringer 1927 / Laman 1970; Henneberg 1911; confirmed by
Capco–Gallet–Grasegger–Koutschan–Lubbes–Schicho 2018, doi:10.1137/17m1118312.) A
graph is *generically rigid* in the plane iff it is Laman ((2,3)-sparse, |E|=2|V|-3)
iff it is built from an edge by H1 (add vertex on 2) and H2 (add vertex on 3,
delete one edge). This is the complete grammar for the rigid-framework class.

**Two overclaims corrected:**
- **Henneberg completeness is a GENERIC-length theorem, not an all-unit-edges
  theorem.** Unit-distance graphs are the non-generic case with every edge = 1;
  there is no completeness result for the all-unit subclass. Owen–Power
  (Trans. AMS 2006) show generic Laman realizations are not solvable by radicals
  — successive H-moves don't stay in a tame field (H1-only type-1 graphs are,
  solvable 2-groups; H2-steps aren't).
- **H2 at all-unit length is NOT a free move.** A point at distance 1 from three
  specified vertices exists iff they are concyclic with circumradius exactly 1
  (the new vertex is the centre) — a measure-zero coincidence, itself a
  realizability query. H1 (two unit circles) is genuinely free; H2 is not.

**What genuinely buys value:** the exact H1 construction tree (safe, free,
quadratic) plus H2 deliberately sought as a rigidity coincidence, every node
machine-certified, feeding the forced-pair harness with richer base graphs than
Moser and Moser+Moser — the concrete way to attack the `G-forced-pair-exists`
crux.

## Status summary

All three files updated under `research/approaches/`; `APPROACHES.md` re-derived.
None is refuted; all three are `grounded` with their advertised mechanisms
scoped precisely against the literature. Durable findings recorded in Cognee.
