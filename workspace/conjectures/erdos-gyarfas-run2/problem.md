# The Erdős–Gyárfás conjecture

## Statement

> Every graph with minimum degree at least 3 contains a cycle whose length is a
> power of two.

Formally: let $G$ be a finite simple graph with $\delta(G) \ge 3$. Then there
exists an integer $k \ge 2$ and a cycle $C \subseteq G$ with $|C| = 2^k$.

Posed by Paul Erdős and András Gyárfás in 1995. It is **open**. Nobody has
proved it and nobody has produced a counterexample, and it has resisted since
1995 — so the working assumption for this run is that a full proof is out of
reach, and the deliverable is a genuine partial result stated exactly, not a
claim of the conjecture.

## What the statement does and does not say

- $\delta(G) \ge 3$ is minimum degree, not average degree and not connectivity.
  The conjecture is false with $\delta(G) \ge 2$: a long odd cycle that is not
  a power of two is a counterexample, so degree 3 is doing real work.
- $2^k$ with $k \ge 2$: cycles of length 4, 8, 16, 32, …. A simple graph has no
  cycle of length 1 or 2, so those cases are vacuous, but state which
  convention any formal statement uses.
- The cycle need not be induced, chordless, or Hamiltonian. It is any cycle in
  $G$ whose length is a power of two.
- $G$ is finite and simple. Multigraphs and infinite graphs are a different
  question; if a result depends on finiteness, say so.

## Why it is hard, stated as the obstruction to beat

Extremal cycle-length results usually deliver an *interval* or an *arithmetic
progression* of achievable cycle lengths — "$G$ contains cycles of every length
in $[a, b]$", or "of every even length in some range", or "of some length
$\equiv r \pmod m$". The powers of two are sparse: the gap between $2^k$ and
$2^{k+1}$ is $2^k$, so an interval result must have length exceeding the
largest power of two below it to be forced to contain one, which is far more
than $\delta \ge 3$ buys. Any successful approach must produce a cycle at a
*prescribed* length rather than somewhere in a range.

That is the single sentence to keep in view. An approach that ends in "and
therefore $G$ has cycles of all lengths in $[a,b]$" has not made progress
unless $b > 2a$, and one that ends in a congruence class has not made progress
at all.

## Where the literature is known to have got to

**These are leads to verify, not established facts.** Every one must be checked
against a primary source before anything is built on it, and any that cannot be
found must be recorded as unfound rather than assumed. Names and years here are
starting queries and may be wrong.

- The conjecture is stated in Erdős's problem papers of the mid-1990s and
  appears in his published problem collections.
- Partial results are known for restricted classes: planar graphs under
  connectivity or cubic hypotheses, claw-free graphs, and graphs of bounded
  degree or given girth. Find the exact hypotheses and the exact conclusions.
- Computational verification exists for small graphs — find the bound and the
  method, because it is both the oracle for this run and the evidence about
  where a counterexample could still live.
- There is adjacent literature on cycle lengths in graphs of given minimum
  degree, on cycle spectra, and on cycles of prescribed length modulo $k$.
  Bondy–Vince, Verstraëte, Sudakov–Verstraëte, Liu–Ma and Gao–Huo–Liu–Ma are
  plausible places to look; verify each before citing it.
- Erdős offered a prize for it. The amount, if stated in a source, is a fact
  about the problem's standing and not about its mathematics.

## What counts as a result here

In descending order of value, and every one of these is a real contribution:

1. A proof for a natural class of graphs, with the hypotheses stated exactly.
2. A structural theorem: a minimal counterexample must have properties
   $P_1, \dots, P_n$ — high girth, no small separators, near-regularity,
   forbidden subgraphs. This is the standard route on a problem like this, and
   a strong enough list is what a proof is eventually assembled from.
3. A computational verification pushed past whatever the literature reached,
   with the search space and the method stated so the bound is checkable.
4. A precise reduction: statement $S$ implies the conjecture, and $S$ is a
   cleaner problem.
5. A counterexample. Extremely unlikely, and the bar for reporting one is a
   machine-checked verification of its degree sequence and cycle spectrum.
6. A formalisation in Lean 4 of the statement, and of whichever lemmas are
   proved along the way, with no `sorry`.

Reporting the conjecture as proved, on anything short of a complete argument
that survives adversarial attack, is the one outright failure available on this
run.
