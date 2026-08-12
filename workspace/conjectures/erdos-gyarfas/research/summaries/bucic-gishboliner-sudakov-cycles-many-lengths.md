# Bucić–Gishboliner–Sudakov, "Cycles of many lengths in Hamiltonian graphs" (2021)

**Source:** Matija Bucić, Lior Gishboliner, Benny Sudakov, *Cycles of many lengths in Hamiltonian graphs*, J. London Math. Soc. (or Combinatorics in the 2022 arXiv version); arXiv:2104.07633. Full text on disk: `research/sources/bucic-gishboliner-sudakov-cycles-many-lengths.full.md`.

## What the source establishes

**Theorem.** Every $n$-vertex Hamiltonian graph with minimum degree at least 3
has at least $n^{1-o(1)}$ distinct cycle lengths.

This resolves asymptotically, in the minimum-degree-3 Hamiltonian setting:

- **Jacobson–Lehel conjecture (1999):** every $k$-regular ($k \ge 3$)
  Hamiltonian graph has at least linearly many distinct cycle lengths.
- **Verstraëte's strengthening (2016):** replace regularity by minimum degree
  at least 3 — the same linear-ish conclusion holds.

Previous best was $\Omega(\sqrt{n})$ cycle lengths; the paper pushes this to
$n^{1-o(1)}$ (essentially linear).

## Why it matters for this problem

This is the *count* of cycle lengths in the exact degree class the EG
conjecture targets ($\delta \ge 3$) — but with the extra Hamiltonian
hypothesis. It says: in a cubic-or-higher *Hamiltonian* graph, almost every
length up to $n$ occurs. That immediately implies the EG conclusion in the
Hamiltonian case (an interval of length $\gg 2^j$ contains a power of two).
So the conjecture is trivially true (and its degree-3 obstacle is entirely) in
Hamiltonian graphs; the difficulty is entirely for **non-Hamiltonian** graphs
with $\delta \ge 3$.

But note the careful statement: it is $n^{1-o(1)}$ distinct lengths *among an
interval*, i.e., the cycle spectrum is dense among possible lengths — and
dense near $n$ means a power of two in range. For a minimal counterexample
(which must be non-Hamiltonian and has no 2-power cycle), this theorem cannot
contradict minimality, because a Hamiltonian graph is never a counterexample;
the theorem shows any counterexample must be as far from Hamiltonian as
possible in the cycle-spectrum sense.

It also frames the obstruction sharply: the conjecture's target is not
"many lengths" but "a *specific* sparse length" — Bucić et al. deliver many
lengths under an extra (Hamiltonian) hypothesis that a counterexample lacks.

## Caveats

- The theorem needs *Hamiltonian*; a minimal EG counterexample is not
  Hamiltonian (if it were, the theorem would already give it a 2-power cycle,
  since $n^{1-o(1)}$ cycle lengths in an interval of length $n$ contains a
  power of two for $n$ large). So the theorem is evidence *against* a
  counterexample being Hamiltonian, not a counterexample obstruction.

```claim
id: EG-bucic-many-cycle-lengths-d3-ham
statement: Every n-vertex Hamiltonian graph with minimum degree at least 3 has at least n^{1−o(1)} distinct cycle lengths (asymptotically resolves Jacobson–Lehel and Verstraëte's δ≥3 strengthening).
hypotheses: Hamiltonian; δ≥3; n-vertex
holds-here: yes as a true theorem; but a minimal EG counterexample is NOT Hamiltonian (else it would already have a 2-power cycle: n^{1−o(1)} lengths in an interval of length n contains a power of two for large n), so the theorem applies to graphs other than counterexamples
status: proved
bearing: isolates the obstruction: the EG conjecture is easy under any hypothesis that yields an interval of cycle lengths of length exceeding the gaps between powers of two; a counterexample must evade every such interval result, so it must be very far from Hamiltonian
anchor: research/summaries/bucic-gishboliner-sudakov-cycles-many-lengths.md
```