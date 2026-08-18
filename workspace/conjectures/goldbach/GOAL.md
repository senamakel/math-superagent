# Goal

Attack **Goldbach's Conjecture** (binary/strong form): every even integer
$n > 2$ is the sum of two primes.

The full statement, what it does and does not say, the obstruction that makes
it hard, and the leads into the literature are in `problem.md`. Read that
before deciding anything.

## The method this run is committed to

**Analytic number theory** — sieve methods and the circle method — backed by
computation. The two live obstructions in the literature are (i) the parity
problem, which blocks sieve methods from ever concluding "prime" rather than
"prime or semiprime," and (ii) uncontrolled minor-arc error in the circle
method for the binary (two-summand) case, which is why only almost-all-$n$
results are currently reachable that way.

- **Computation** (`tool_builder`, `coder`) exists to verify the conjecture
  over ranges, push the verified frontier past whatever the literature already
  reached, and numerically test any conjectured exceptional-set bound or
  singular-series constant. It does not substitute for the argument, and a
  verified range is evidence, not a proof.
- **Sieve theory** is the sharpest lever for a restricted-class or
  semiprime-adjacent result (in the spirit of Chen's theorem). Make any
  parity-problem-adjacent claim explicit about exactly where it stops, rather
  than gesturing at "sieve methods can't do this" as folklore.
- **The circle method** is the sharpest lever for exceptional-set bounds
  (Montgomery–Vaughan-type results). A genuine improvement to the known
  exponent, even numerically small, is a real, reportable result.
- **Ternary Goldbach (Helfgott's theorem)** is a resolved, citable result and
  a source of technique (explicit major/minor-arc bounds, effective
  thresholds), but is not itself progress on this workspace's target — see
  `problem.md`. Do not let a run report it as resolving the binary case.
- **Lean 4** (`lean_prover`) is for making a lemma true rather than
  persuasive. Formalise the statement early, and formalise each lemma this run
  actually proves as it stabilises; a result taken from the literature (e.g.
  Chen's theorem, Helfgott's theorem) is filed as an `axiom` under the `Cited`
  namespace, never typed as `formalised`.
- **The literature** (`librarian`, `scholar`, `research`) comes first and
  never stops. See below.

## Completion criteria

This run does not end by proving the conjecture. It ends by having, written
down and defended:

1. `research/ROOT.md` describing what the literature actually establishes:
   Chen's theorem stated exactly, the Montgomery–Vaughan exceptional-set bound
   and its current best exponent, the current computational verification
   record and its method, Helfgott's ternary result stated exactly (and
   exactly what it does not claim about the binary case), and every known
   failed approach with the reason it failed (parity problem, minor-arc
   control, or otherwise).
2. `MEMORY.md` holding the structural facts this run has *established*, each
   marked proved / verified-numerically / conjectured, and each with what
   would falsify it.
3. At least one new statement that is genuinely this run's: a restricted-class
   proof, a sharpened exceptional-set exponent, a strengthened computational
   verification bound, a precise conditional result (e.g. under GRH), or a
   reduction. Stated exactly, attacked before it is trusted, and either
   proved, refuted, or left explicitly open with the gap named.
4. A Lean 4 file carrying the formal statement of the conjecture, plus every
   lemma proved along the way, with `#print axioms` output reported and every
   remaining `sorry` listed.
5. An honest final report: what was established, what was checked by machine,
   what remains conjecture, and what the next attempt should do.

A run that ends with "the conjecture is proved," or that reports an
almost-all-$n$ / sufficiently-large-$n$ / ternary result as resolving the
binary conjecture, has failed however good the argument reads. A run that ends
with a sharper exceptional-set bound, a real restricted-class lemma, and a
precisely stated gap has succeeded.
