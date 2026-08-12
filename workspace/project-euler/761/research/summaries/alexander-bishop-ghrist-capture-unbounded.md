# Alexander, Bishop, Ghrist — "Capture pursuit games on unbounded domains"

Source: L'Enseignement Mathématique (2) 55 (2009) 103–125. Author preprint PDF:
`https://www2.math.upenn.edu/~ghrist/preprints/convexcapture.pdf`; EMS article page:
`https://ems.press/journals/lem/articles/12139`. Full text:
`research/sources/alexander-bishop-ghrist-capture-unbounded.full.md`.

## What it establishes

Develops elementary tools from geometric convexity to analyze **capture** ("Lion and Man")
pursuit games in *unbounded* convex Euclidean domains, in any dimension, in **discrete
time** with equal speeds.

**Main result.** A necessary-and-sufficient condition for eventual capture — the
**Boundedness Condition** (stated via *recession sets* in the unit tangent sphere) —
exactly characterizes when equal-speed capture is possible in a convex unbounded domain
(Theorem 17). It introduces the `Radius` and refined `RotatingRadius` pursuit algorithms,
treats the domain boundary as a stationary constraint that blocks the evader's escape
route, and extends the criteria to non-convex domains admitting a convex decomposition.

## Why it matters for this run

- This is one of the **canonical modern references in the frontier** of the 
  lion-and-man lineage (cited by the Abel et al. paper as [ABG09]).
- It shows how the *boundary of the domain* is used as a constraint on escape routes — the
  same structural role the pool's boundary plays in PE 761 (the swimmer must leave through
  the boundary, the runner patrols it). The "boundary as constraint" and "recession set"
  viewpoints are the geometric machinery behind explaining *why* the critical threshold is
  set by the boundary-time comparison.
- It is a **capture** (pursuer-centric) companion to the *escape*-centric Abel et al. model:
  together they pose the two sides of the same dichotomy PE 761 asks (escape iff v < V).

## What it does NOT settle
- Unbounded, discrete-time, equal-speed capture — a different regime from PE 761's
  bounded pool, continuous time, speed-ratio escape.
- No polygon critical speed ratios and no hexagon value.

## Notes
- Author-page preprint is a clean primary copy of the published L'Enseignement paper.
- Its own reference list is a useful bibliography of the classic pursuit literature
  (Besicovitch, Littlewood, Croft, Flynn, Sgall, Isaacs).

## Claims

```claim
id: abg-capture-unbounded-boundedness-condition
statement: In a convex unbounded Euclidean domain, discrete-time equal-speed capture of a single evader by pursuers is possible if and only if the initial configuration satisfies the Boundedness Condition (a recession-set condition in the unit tangent sphere); the boundary acts as a constraint blocking escape routes.
hypotheses: convex unbounded domain, arbitrary dimension; discrete-time; equal speeds; capture = pursuer reaches evader.
holds-here: partially — the domain-boundary-as-constraint idea is the structural principle behind the pool-boundary chase in PE 761, but the regime (unbounded, discrete, equal-speed) differs from the bounded pool / continuous / speed-ratio escape of the problem.
status: proved (published paper).
bearing: canonical modern reference for pursuit-evasion capture in domains with boundary; frames how the pool boundary constrains escape, the conceptual basis of the critical-speed dichotomy.
anchor: research/sources/alexander-bishop-ghrist-capture-unbounded.full.md
```
