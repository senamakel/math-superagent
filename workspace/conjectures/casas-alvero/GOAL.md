# Goal — first pass

Attack the Casas-Alvero conjecture (`problem.md`). This is the opening pass on a
cold workspace: nothing here is established yet, and the first job is to make
the problem *legible* to later passes rather than to solve it.

## What this pass is for

Three things, in this order, and the run is a success if it delivers the first
two honestly even with nothing on the third.

1. **Establish the status of the problem, from primary sources.** Every "known
   result" in `problem.md` is recalled from memory and is marked as such. Confirm
   or strike each one with a citation and its exact hypothesis. In particular
   settle: which degrees are proved, what the smallest open degree actually is,
   and **whether a complete proof has been claimed** — and if so whether it
   stands, is under review, or has a known gap. Record the answer in
   `research/CLAIMS.md` with its evidence class.

   If a proof does stand: this run's target changes to *understanding and
   stress-testing it* — restate its key step, apply the char-`p` test to it,
   and identify what it does not give (effectivity, other characteristics,
   the geometric question behind CA). Do not simply summarise it.

2. **Build the oracle and reproduce the boundary.** `code/` must contain an
   exact checker: given `f` over `Q` or a number field, decide `gcd(f, f^(i)) ≠ 1`
   for all `i`, exactly (resultants or exact gcd over the coefficient field — no
   floating point root-finding as the decision procedure; approximate roots may
   *search*, never *decide*). Then:
   - verify it against `(x−a)^n` and against small hand cases;
   - verify it against the **characteristic-`p` counterexamples** — it must
     report them as satisfying the hypothesis and not being pure powers, which
     is the negative control that proves the checker is measuring the right
     thing;
   - reproduce, by elimination/Gröbner over `Q`, CA for the smallest degrees
     where the literature says it holds (`n = 4, 5, 6, 8, 9, …` as far as the
     computation goes), and record where the computation stops being feasible
     and why. That boundary is a fact about the problem worth writing down.

3. **Attack one precise structural claim about a minimal counterexample.**
   Choose it, state it before testing it, and hunt the counterexample as hard as
   the proof. Candidates, none endorsed:
   - a bound on the number of distinct roots of a counterexample of degree `n`;
   - forcing coincidences among the shared roots `r_i` (can `r_i = r_j` be
     forced for `i ≠ j`? can they be forced *apart*?);
   - the dimension of the counterexample variety for fixed `n`, or that its
     `n`-th component is a complete intersection / has an expected dimension
     that a degeneration argument makes precise;
   - the multiplicity structure: what multiplicity patterns are compatible with
     sharing a root with every derivative.

## The test every argument must pass

`problem.md` records that CA is **false in characteristic `p`**. So:

> **No argument in this workspace is admissible until it has been run against
> the char-`p` counterexamples and the step that fails there has been named.**

An argument that survives in char `p` proves a false statement and is therefore
wrong, whatever it looks like. Record the failing step for each candidate in
`research/CLAIMS.md` beside the claim. A candidate whose char-`p` failure point
cannot be located is not "probably fine" — it is unfinished, and saying so is a
result of this pass.

## Rules

- **One canonical oracle.** Everything that decides the derivative-sharing
  hypothesis calls `code/lib`. No second implementation, and no script decides
  it inline. Every experiment asserts on a small guard set at entry —
  `(x−1)^n` for a few `n` must pass, a generic random `f` must fail, and the
  char-`p` witness must pass with `f` not a pure power — and asserts on the
  *produced* data, not on a fresh oracle call.
- **Exact arithmetic decides; numerics only search.** A root computed in
  floating point may suggest a near-coincidence; only an exact gcd, resultant,
  or ideal membership may conclude one.
- **A measurement is not a proof.** Label every statement proved /
  verified-computationally / conjectured / asserted-by-source, and name the
  ceiling of every computation.
- **`problem.md` is not authoritative.** It is written from memory and expects
  to be corrected. When a source disagrees with it, print both and say which
  won.
- **Captures write to a temp file and move on exit 0**, and each states in its
  first three lines what it ran, which oracle function, and the exact range. An
  empty capture is a failed run, not a missing one.
- **Cite, do not re-derive**, once something is in `CLAIMS.md` with a source.
- **Do not claim the conjecture.**

## Progress of this pass (2026)

Two executable verifications are complete, each closing a load-bearing claim:

1. **`bad-prime-minors-criterion` (Thm 3.1, arXiv:2411.13967) verified at n=4.**
   lcm over all 64 tuples T∈{1,2,3,4}³ of J_T (gcd of all 15×15 minors of the
   19×15 matrix M_T, exact via Smith normal form) = 1575 = 3²·5²·7, prime
   divisors exactly {3,5,7} = the known bad primes of degree 4. Second route
   (rank_{F_p}(M_T)<15) agrees. The sufficient binomial criterion gives {3,5},
   a strict subset — confirming sufficiency-not-exhaustion exactly as the
   source states. The adopted `arithmetic-jet-lift` approach's central tool is
   thereby validated at its smallest non-trivial degree. (capture:
   code/out/badprimes_n4.captured.txt)

2. **Hasse-vs-ordinary resolution for char-p CA (steering directive).** The
   published bad-prime lists use Hasse derivatives H_i(f); in char p the
   ordinary derivative f^(i)=i!·H_i(f) vanishes for i≥p, so the ordinary
   hypothesis degenerates and wrongly marks p=2 bad for n=4. Using the Hasse
   formulation, the S_n-scheme radical-equality route reproduces {2} (n=3)
   and {3,5,7} (n=4) EXACTLY over all 17 primes p<60, plus a bounded F_p
   enumeration through lib.casas_alvero.is_ca_hasse. Three independent routes
   agree. `is_ca_hasse` added beside `is_ca` (both kept; agree in char 0 and
   p≥n). (capture: code/out/badprimes_sn.captured.txt)

3. **Degree-20 certified-bad frontier** (for when the lift route resumes):
   the 18 certified-bad primes p|C(20,i)−1 are
   {2,3,5,7,11,13,17,19,37,67,89,103,109,113,173,419,1223,15269}; the 20
   smallest non-certified candidate-good primes are
   {23,29,31,41,43,47,53,59,61,71,73,79,83,97,101,107,127,131,137,139}.
   Caveat recorded: binomial criterion is sufficient only (n=4 calibration
   misses 7), and the full minor criterion for n=20 is infeasible
   (C=binomial(190,18)≈10²⁰). (capture: code/out/badprimes_n20_frontier.captured.txt)

4. **Hasse recheck of the char-p witness clause** (directive 4 loose end).
   The clause "f(X^p) without constant term also works since all derivatives
   vanish" in `charp-witness-xpp1-xp` is ordinary-derivative vacuity and does
   NOT survive the Hasse convention: x^p+x^{2p} fails Hasse-CA at i=p
   (H_p(x^{2p})=2x^p≠0); only the monomial x^{mp} passes, and only via the
   monomial-root accident gcd(x^{mp},H_i)∋x. The substantive witness
   x^{p+1}−x^p is Hasse-CA under both conventions. Verified by two
   independent exact routes (canonical oracle + hand-rolled F_p Euclid),
   56/56 agree. (capture: code/out/ordinary-vs-hasse-charp-witness.captured.txt)

5. **Bad-prime-minors criterion verified at n=5, and its feasibility
   boundary mapped to n=8** (directive 5). The n=5 bad-prime verification
   switched from the (measured-infeasible) SNF route to rank over F_p: the
   exact rank_{F_p}(M_T)<120 criterion reproduces exactly the published
   degree-5 bad-prime list {2,3,7,11,131,193,599,3541,8009} over all 625
   tuples T∈{1..5}⁴ × 170 primes (106,250 ranks, 28 workers, 384 s,
   independently re-confirmed this attempt, ALL CHECKS PASSED). The
   feasibility boundary of the minors criterion: n≤4 SNF-feasible (n=4:
   19×15, 64 tuples, ms, lcm J_T=1575→{3,5,7}); n=5 SNF-infeasible (one
   195×120 SNF >90 s cap) but rank-only feasible; **n=6 rank-infeasible**
   (C=1365, D=2751, ~185 core-s/rank, full sweep ~2.2e5 core-hours); n=7,8
   neither a fortiori. So the minors criterion tops out at n=5.
   (captures: code/out/badprimes_n5.captured.txt,
   code/out/feasibility_boundary.captured.txt; claim
   minors-criterion-feasibility-boundary)

6. **Binomial bad-prime criterion calibrated; n=20 goodness unreachable by
   the minors route.** The sufficient binomial criterion p|C(n,i)−1 is
   never exhaustive: n=3 catches {2} of {2}; n=4 {3,5} of {3,5,7} (missing
   7); n=5 {2,3} of the 9 true bad primes (missing 7 of 9, 22%). Negative
   control: it never falsely condemns a good prime (30 checks). Direct
   consequence for the adopted `arithmetic-jet-lift` approach: its
   first-step — test candidate primes for goodness at n=20 by the minors
   criterion — is infeasible (C≈1e20, far past the n=6 wall). At n=20 the
   certified-bad list is a LOWER BOUND on the true bad set and the
   candidate-good primes {23,…} are NOT proven good. Any route to a good
   prime at n=20 must use a method that beats the C≈1e20 minor-criterion
   wall (scenario-type reduction, or an analytic bound) — an open
   sub-problem. (capture: code/out/binomial_calibration.captured.txt; claim
   binomial-criterion-calibration)

None of this settles CA_20; it validates the bad-prime framework the run's
lift route rests on, resolves the derivative-convention that had two parts of
the run disagreeing about char-p facts, and maps the n=20 good-prime frontier
with its exact infeasibility boundary. See TASKS.md and
research/notes/badprimes-criterion-n4-n20.md.

## Out of scope

The original singularity-theory motivation (plane curve germs, Puiseux
expansions) is background, not the target — read enough to know why the question
was asked, then leave it. Generalisations of CA to several variables, to
non-monic or non-polynomial settings, and to systems of higher-order operators
are out of scope for this pass unless a source shows the generalisation is
*easier* and implies a case of CA.
