# Tasks

Order of work, from the run directive; work the earliest incomplete item.

## 1. Build the library — stop when it is enough

- [ ] Spawn librarian + research; scholar digests each source into claim blocks
      as it lands (hypotheses, holds-here, status).
- [ ] Fetch via `read_sources` / `deep_research` (server-side). Do **not** call
      `download_document` for arxiv.org, doi.org, sciencedirect.com, or
      springer.com — the run's network boundary drops those hosts every time,
      regardless of the URL. This is the environment, not the sources; do not
      file it as a finding about the mathematics.
- [ ] Exit when research/ROOT.md states: the structure of a minimal
      counterexample, the current verification bound, and at least three settled
      restricted classes with their hypotheses. After that, gather only against
      a gap named in research/REQUESTS.md.

## 2. Extract as you go

- [ ] Every source that lands: a fenced claim block in its note (hypotheses,
      holds-here, status) plus a line under Established in CONTEXT.md, each
      with its evidence class and what would falsify it.
- [ ] Record closed directions under Ruled out with the obstruction that closed
      them.

## 3. Build the oracle

- [ ] tool_builder: exact edge certifier (`|x - y|^2 = 1` symbolically) and a
      complete k-colouring test that returns a witness colouring when one exists.
- [ ] Calibrate both on the 7-vertex graph: certify every edge exactly, and
      report 4-colourable and not 3-colourable. Record the actual output.

## 4. Loop

- [ ] Each attempt states one precise structural claim about a minimal
      counterexample, attacks it before trusting it (hunt the counterexample as
      seriously as the proof), and establishes, refutes, or leaves it open with
      the gap named exactly.
- [ ] Use sat_solver for finite SAT questions (UNSAT is a theorem), lean_prover
      for the statement and stabilised lemmas, symbolic_math for closed forms.
- [ ] Verify any result by a second, independent route.
