# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly** — never a claim that
the general Toeplitz conjecture has been proved. It has stood since 1911 and
resists a proof technique (the Mobius-band parity argument) that is well
understood and has already been pushed to its natural boundary (locally
monotone curves, Stromquist 1989). The working assumption is that this run
will not close the general case. Claiming it on an argument that has not
survived attack is the one outright failure available here.

Read `problem.md` first — the exact statement, what it does and does not say,
the configuration-space technique worked out in full, the known results with
their real scope, and the three specific places the general argument breaks.

## The method this run is committed to

**Topology and configuration-space degree theory, backed by exact
computation and Lean formalization.** This is not a numerical-search problem
(see the trap in `problem.md`): there is no value to hunt for, only an
existence statement to prove or a class of curves to extend.

- **The formalized theorem to build from is Stromquist's (1989): every
  locally monotone Jordan curve inscribes a square.** Re-derive the
  configuration-space argument from `problem.md` in enough detail to state
  each step's hypothesis precisely, and identify exactly which step needs
  local monotonicity.
- **A genuine extension is a named subclass of curves, strictly larger than
  "locally monotone," with the corresponding step of the argument redone for
  it.** Candidates worth attempting first: curves that are locally monotone
  except at a controlled, finite set of points; curves with a Hölder
  condition weaker than `C^1` but strong enough to define a boundary winding
  number; curves with imposed symmetry beyond what is already published.
- **Computation** (`tool_builder`, `coder`) is for exact verification of the
  configuration-space map `F` on specific curves (polygons and piecewise-`C^1`
  curves with algebraic vertices), never floating-point root-finding
  presented as a witness. Every computed "square" must be checked against the
  exact class it belongs to and reported as an instance of Stromquist's
  theorem, not as new mathematics, unless the curve genuinely falls outside
  every known theorem's hypotheses.
- **Lean 4** (`lean_prover`) should carry: the exact statement of the
  conjecture; the statement of Stromquist's theorem for locally monotone
  curves; and, as they stabilize, the individual lemmas of the
  configuration-space argument (the Mobius-band identification, the map `F`,
  the boundary degenerate locus, the parity/degree step). A literature result
  used as a black box goes under `namespace Cited` as an `axiom`, never
  `formalised`.
- **The literature** (`librarian`, `scholar`, `research`) comes first. Fetch
  Matschke's 2014 survey immediately; use it to confirm or correct every item
  under "Known results" in `problem.md`, especially the unconfirmed
  Cantarella–Denne–McCleary 2020 claim — determine and record its actual
  current status (preprint / published / retracted / contested) rather than
  leaving it as a guess.

## Completion criteria

This run does not end by proving the general conjecture. It ends by having,
written down and defended:

1. `research/ROOT.md` stating what the literature actually establishes: the
   exact hypotheses and proof technique of Stromquist's theorem, the current
   status of the Cantarella–Denne–McCleary claim (checked, not assumed), the
   scope of the Greene–Lobb rectangle result and why it does not transfer, and
   every known failed or incomplete approach to the general case with the
   specific reason it failed.
2. `MEMORY.md` holding the structural facts this run has established, each
   marked proved / verified-by-computation / conjectured, and each with what
   would falsify it.
3. At least one statement that is genuinely this run's own: an extension of
   the locally-monotone class, a clean reduction, a verified instance
   exercising the configuration-space map on a curve outside prior published
   verification, or a precise impossibility statement — a step of the
   Mobius-band argument shown not to extend to a named broader class, with the
   exact obstruction identified. Stated exactly, attacked before it is
   trusted, and either proved, refuted, or left explicitly open with the gap
   named.
4. A Lean 4 file carrying the formal statement of the conjecture and of
   Stromquist's theorem (the latter either proved or filed as a `Cited`
   axiom, decided explicitly and not left ambiguous), plus every lemma proved
   along the way, with `#print axioms` output reported and every remaining
   `sorry` listed.
5. An honest final report: what was established, what was checked by machine
   (and under which exact-arithmetic guarantee), what remains conjectural
   folklore versus published theorem, and what the next attempt should try.

A run that ends with "the conjecture is proved" for the general continuous
case, or that reports an approximate/numerical square as a witness, has
failed however good the write-up reads. A run that ends with the
configuration-space argument correctly formalized for the locally monotone
case, an honestly-scoped extension attempt, and a precisely named obstruction
for the general case has succeeded.
