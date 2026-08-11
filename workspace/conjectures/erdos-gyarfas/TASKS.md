# Tasks

Phase 1 — the library. Nothing below it starts until `research/ROOT.md` can
answer what is known.

- [ ] Find the conjecture stated in a primary source, not a secondary summary.
- [ ] Collect every partial result, each with its exact hypotheses and its exact
      conclusion. Restricted classes: planar, cubic, claw-free, bounded degree,
      girth conditions.
- [ ] Find the computational verification work: how far it has been checked, by
      what method, and what that leaves open.
- [ ] Collect the adjacent machinery on cycle lengths in graphs of given minimum
      degree — cycle spectra, prescribed lengths, lengths modulo $k$.
- [ ] Have the scholar turn each source into claim blocks, so a statement is
      retrievable one statement at a time rather than one paper at a time.

Phase 2 — what is known.

- [ ] `MEMORY.md`: every structural fact about a minimal counterexample the
      library establishes, each marked proved / verified-numerically /
      conjectured, each with what would falsify it.
- [ ] `MEMORY.md` failed approaches: every direction the literature closed, with
      the obstruction that closed it.
- [ ] State, in one sentence each, which obstruction defeated each previous
      attempt — because any new approach has to beat the same one.

Phase 3 — the oracle.

- [ ] `code/lib/`: an exact checker returning a graph's minimum degree and the
      full set of its cycle lengths. Verified by hand on $K_4$, $K_{3,3}$, the
      cube, and the Petersen graph.
- [ ] Reproduce the literature's verification bound with `nauty-geng -q -c -d3`
      before trusting anything computed past it.
- [ ] Report the count of connected minimum-degree-3 graphs at each order, so
      the point where exhaustive generation stops being the method is a number
      rather than a guess.

Phase 4 — the loop. One precise structural claim per attempt, attacked before
it is trusted.

- [ ] Lean: the formal statement of the conjecture, elaborating, with the
      conventions checked and written down.
- [ ] First structural claim about a minimal counterexample, stated exactly.
