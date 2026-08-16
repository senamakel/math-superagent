# Goal — first pass

Attack Frankl's union-closed sets conjecture (`problem.md`). This is the opening
pass on a cold workspace: nothing here is established, and the first job is to
make the problem *legible* to later passes rather than to solve it.

## What this pass is for

Four things, in this order. The run is a success if it delivers the first three
honestly even with nothing on the fourth.

1. **Pin down the frontier, from primary sources.** Every "known result" in
   `problem.md` is recalled from memory and marked as such. Confirm or strike
   each one with a citation and its exact hypothesis. In particular settle, with
   numbers and sources:
   - the **current best constant** `c` in "some element is in `≥ c|F|` sets",
     who proved it, and whether it is published or preprint;
   - what exactly `(3 − √5)/2` is a barrier *for* — which argument, stated
     precisely enough that one can ask whether a variant escapes it;
   - the **verified ranges**: largest `n` (ground set) and largest `|F|` for
     which UC is machine-verified, and by what method;
   - which lattice and graph classes are settled.

   Record each in `research/CLAIMS.md` with its evidence class. This section
   alone, done properly, is worth the run: the entropy literature moved in
   weeks in late 2022 and memory of it is unreliable.

2. **Build the oracle.** `code/` must contain an exact library over explicit
   finite families:
   - represent a family of subsets of `[n]` as bitmasks; decide union-closure
     exactly; compute every element's abundance vector exactly (integer counts,
     never floating point);
   - decide UC for a given family and return the abundant element or the
     witness that none exists;
   - **generate** union-closed families: the closure of a given generating
     family under union, and enumeration of union-closed families on small `n`
     up to isomorphism if feasible;
   - guard set at entry to every experiment: `2^[n]` must give every element
     density exactly `1/2`; a family containing a singleton must report that
     singleton abundant; a *non*-union-closed family with no abundant element
     must be constructible and must be rejected by the closure check — that is
     the negative control proving the oracle measures the right thing.

3. **Reproduce one published result computationally, end to end.** Pick the
   cheapest genuinely non-trivial one — a small verified range of `n`, or the
   certification of a known FC-family by its LP / weight argument — and
   reproduce it from scratch in `code/`. Record where the computation stops
   being feasible and why. That boundary is a fact about the problem worth
   writing down, and it tells later passes which computational routes are open.

4. **Attack one precise claim.** Choose it, state it before testing it, and hunt
   the counterexample as hard as the proof. Candidates, none endorsed:
   - **the barrier, made into a theorem.** Formalise "Gilmer-shape argument" as
     a concrete optimisation over distributions, then either prove it is capped
     at some `c₀ < 1/2` or find the escape. This is the highest-value target
     and it is a *self-contained analysis problem* — a one- or two-variable
     entropy inequality — which makes it unusually well suited to a run that can
     compute.
   - a structural constraint on a minimal counterexample: bounds on `|F|`
     relative to `n`, on the minimum set size, on the abundance profile.
   - the 3-set question: exactly which 3-element sets are FC, decided by the LP,
     with the boundary cases identified.
   - the bipartite graph formulation: is the reduction to bipartite graphs
     usable, i.e. does it make a class newly attackable?

## The tests every argument must pass

`problem.md` records three negative controls: **`1/2` is attained** (so nothing
proves more), **union-closure must be used**, **finiteness must be used**.

> **No argument in this workspace is admissible until it has been run against
> all three and, if it fails one, the failing step named.**

An argument that proves more than `1/2` proves a false statement, whatever it
looks like. Record the outcome for each candidate in `research/CLAIMS.md`
beside the claim. A candidate whose behaviour on the controls has not been
located is not "probably fine" — it is unfinished, and saying so is a result.

## Rules

- **One canonical oracle.** Everything that decides union-closure or abundance
  calls `code/lib`. No second implementation, and no script decides it inline.
  Every experiment asserts on the guard set at entry and asserts on the
  *produced* data, not on a fresh oracle call.
- **Exact arithmetic decides; numerics only search.** Abundances are integer
  counts. In the entropy work, floating-point evaluation of an inequality may
  *suggest* a bound; only an interval-arithmetic or symbolic argument may
  conclude one, and a claimed constant must come with the certificate that
  proves it, not the plot that suggests it.
- **A measurement is not a proof.** Label every statement proved /
  verified-computationally / conjectured / asserted-by-source, and name the
  ceiling of every computation.
- **`problem.md` is not authoritative.** It is written from memory and expects
  to be corrected. When a source disagrees with it, print both and say which
  won — especially for the post-Gilmer constants, where the order of events
  matters and memory compresses it.
- **Captures write to a temp file and move on exit 0**, and each states in its
  first three lines what it ran, which oracle function, and the exact range. An
  empty capture is a failed run, not a missing one.
- **Cite, do not re-derive**, once something is in `CLAIMS.md` with a source.
- **Do not claim UC.**

## Out of scope

Infinite and measure-theoretic analogues, the "union-closed sets conjecture for
multisets / matroids / other generalisations", and the history of the problem
beyond what is needed to read the sources. Read enough to know why the question
is asked in the form it is, then leave it. A generalisation is in scope only if
a source shows it is *easier* and implies a case of UC.
