# Goal

Attack the **Erdős–Szekeres conjecture**: $\mathrm{ES}(n) = 2^{n-2}+1$, where
$\mathrm{ES}(n)$ is the least $N$ forcing $n$ points in convex position among
any $N$ points in general position in the plane.

The full statement, the conventions, the obstruction that makes it hard, and the
leads into the literature are in `problem.md`. Read that before deciding
anything. The lower bound is settled; only the upper bound
$\mathrm{ES}(n) \le 2^{n-2}+1$ is open.

## What this run is not allowed to drift into

Three drifts are predictable on this problem and each one ends the run's value:

- **Asymptotics.** Improving the $o(n)$ or $O(\sqrt{n\log n})$ term in the known
  $2^{n+o(n)}$ bound is a different problem. If an attempt is producing an
  estimate rather than an exact statement, say so and redirect.
- **The wrong Erdős–Szekeres theorem.** The monotone-subsequence result
  ($(r-1)(s-1)+1$) shares the name and is in Mathlib. It is not this.
- **Adjacent problems.** Empty hexagons, higher dimensions, and the
  cups-and-caps function in isolation are all easier and all publishable-looking.
  Working one of them is fine only if a stated reduction connects it back.

## Completion criteria

This run does not end by proving the conjecture. It ends by having, written
down and defended:

1. `research/ROOT.md` describing what the literature actually establishes: the
   exact statement and error term of every published upper bound with its
   source, the Erdős–Szekeres lower-bound construction written out concretely,
   the exact values $\mathrm{ES}(3..6)$ with the method that settled each, the
   Peters–Szekeres $n=6$ computation with its encoding and cost, and at least
   three restricted classes or partial results with their exact hypotheses. Each
   entry marked proved / verified-numerically / conjectured / asserted-by-source.
2. `MEMORY.md` holding the structural facts this run has *established* about a
   hypothetical extremal set (a set of $2^{n-2}$ points with no convex $n$-gon),
   each marked with its evidence class and with what would falsify it.
3. **A working oracle, verified before it is trusted.** An exact-arithmetic
   checker that, given a point set (rational or integer coordinates), decides
   general position and reports the largest subset in convex position, plus the
   cup/cap spectrum. It must reproduce, before anything is built on it:
   $\mathrm{ES}(4)=5$, $\mathrm{ES}(5)=9$, and the Erdős–Szekeres construction's
   emptiness of a convex $n$-gon at $n=5,6$. A convex-position test built on
   floating-point orientation is a bug; use exact integer/rational determinants.
   State the search space and the isomorph-rejection method for any enumeration,
   and say what an empty result rules out.
4. At least one new statement that is genuinely this run's: a lemma, a proof for
   a restricted class, a structural constraint on an extremal set, a reproduced
   or extended computation, or a reduction. Stated exactly, attacked before it is
   trusted — hunt the counterexample as seriously as the proof — and either
   established, refuted, or left explicitly open with the gap named.
5. A Lean 4 file carrying the formal statement of $\mathrm{ES}(n)$ and the
   conjecture, plus every lemma proved along the way, with `#print axioms`
   output reported and every remaining `sorry` listed. Getting the formal
   statement right — general position, convex position, the worst-case
   quantifier order — is itself work worth doing.
6. An honest final report: what was established, what was checked by machine,
   what remains conjecture, and what the next attempt should do.

A run that ends with "the conjecture is proved" and an argument that has not
survived attack has failed, however good the argument reads. A run that ends
with a verified oracle, a reproduced $\mathrm{ES}(5)$, and two exactly stated
structural lemmas about extremal sets has succeeded.
