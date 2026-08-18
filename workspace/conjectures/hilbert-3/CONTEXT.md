# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call.

**This workspace is a fresh scaffold. Everything about the mathematics below is
unverified recall; nothing has been established, tried, or computed yet.**

## Established

Nothing. Every ledger is empty (`tasks`, `attempts`, `reductions`, `thesis`,
`goals`, `requests`, `frontier`, `entailment` all 0 entries;
`claims`/`threads`/`approaches` never rendered). No source has been downloaded —
`research/sources/`, `research/summaries/` and `research/notes/` do not exist.
`code/` holds no programs and no Lean (`code/lean/Lib/Statement.lean` is the
first file to write). `code/out/` holds no captured output. Cognee memory and
scratch are empty for this problem and its shape.

## Asserted but unverified

Everything in `problem.md`. It is recalled status, explicitly flagged as such:
"problem.md is written from memory and expects correction" (GOAL.md). The
load-bearing items, none with a citation in the workspace:

- Sydler 1965: `R³` completeness; Jessen: `R⁴` completeness by reduction. The
  run's whole target depends on `n ≥ 5` open and `n = 4` closed being true.
- `H³` and `S³` Dehn sufficiency conjecture open — the "most attention" form of
  the question.
- `D(P) = Σ ℓ_i ⊗ θ_i ∈ R ⊗_Z R/πQ`; vanishing is a `Q`-linear-independence
  statement about the `θ_i/π`, to be proved, not observed.
- Zakharevich `K`-theory reframing exists; no detail in the workspace.

GOAL.md phase 1 is: confirm or strike each with a primary source, exact
hypotheses, and a falsifier. Nothing below may be built on until it is.

## Ruled out

Nothing has been tried. No approaches, no attempts, no closed threads, no
scratch. The only constraints are GOAL.md's out-of-scope list: Dehn's and
Sydler's theorems as *targets* (fine as background and controls),
Banach–Tarski, and `K`-theory beyond what bears on the two target statements.

## Numbers

None. No computation has been run. GOAL.md's oracle guardrails — cube returns
Dehn `0`; regular tetrahedron *provably* nonzero (the arccos(1/3)/π
irrationality must be proved, not observed); a published prism dissection
verifies — are requirements on the first library, not results.

## Recalled

Cognee returns nothing (queried: Hilbert third problem, scissors congruence,
Dehn invariant, Dupont–Sah, hyperbolic/spherical sufficiency). No earlier run
left anything for this problem.

## Contradictions

None — nothing to contradict yet. The first checks against sources (Sydler,
Jessen, `H³`/`S³` status) are where the first contradictions will appear;
record them here rather than silently picking a side.

## Gaps

The immediate unresolved thing: GOAL.md phase 1 — settle the exact statements
and which dimensions are settled, from primary sources, before any strategy is
chosen. Precisely: (a) Sydler's theorem and Jessen's `R⁴` reduction, exact
hypotheses; (b) what is proved vs conjectured for `H³`/`S³` sufficiency, and by
whom; (c) one fixed definition of `P(X)` per geometry, used unchanged; (d) any
dimension-5 invariant beyond volume and Dehn, and its fate; (e) what the
`K`-theory reframing gives — a new theorem or a new language. Each becomes a
research request with a falsifier when it is attacked.
