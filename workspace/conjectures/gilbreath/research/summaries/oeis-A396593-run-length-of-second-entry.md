# OEIS A396593 — Run length transform of A089582

**Source URL:** https://oeis.org/A396593 (C. Owen Prestwood, May 29 2026, approved). OEIS record is short; **this summary IS the complete captured page — there is no separate `sources/oeis-A396593-*.full.md`; do not search for one.**

## What this is and why the run needs it

A fresh (2026) OEIS catalogue record computing the **run lengths of the second-
entry sequence** `d_k(2)` of the Gilbreath triangle — i.e. the run structure of
exactly the sequence whose membership in {0,2} is the whole conjecture. It is
consecutive-identical-run-lengths in `d_k(2)`, the second column of the prime
difference triangle, and it cites **Miller 1970 and Odlyzko 1993** — the two
primary sources of the run's proved {0,2}/Rule-90 interior mechanism.

## What it establishes

- Definitions: `d_0(n)` = n-th prime; `d_{k+1}(n) = |d_k(n) − d_k(n+1)|`
  (the absolute-difference Gilbreath operator). `a(n)` = length of the n-th
  consecutive identical run in `d_k(2)` for k ≥ 1 (the run-length transform).
- Terms (n=1..88): `1, 1, 6, 6, 2, 1, 2, 2, 3, 3, 2, 1, ...`
- **Comment (the connection to the run's proved result):** "If Gilbreath's
  conjecture holds, then d_k(2) consists entirely of 0s and 2s. For n > 2,
  certain values of d_k(n) can be determined using d_k(2) through an XOR process
  related to a cellular automaton. Specifically, for a uniformly 0-and-2 sequence
  in d_k, Rule 90 expands to the analogous sequence in d_{k+1}." This is exactly
  the run's proved `rule90-interior-xor`: inside the {0,2} regime the halved
  entries evolve by XOR/Rule 90.
- Author provides a Mathematica implementation of the run-length computation and
  cross-references A089582 (second-entry sequence) and A036262 (iterated prime
  differences) — both already in the library (`oeis-A089582-second-entry-sequence`,
  `oeis-A036262-iterated-prime-differences`).

## Bearing on this problem

This is a **catalogue item**, not a derivation: it confirms the run's reduction
(`A_k(1) ∈ {0,2}` ⟺ Gilbreath, per the {0,2}-second-entry equivalence already in
the library) and again records the Rule-90-interior structure in an independent
catalogue. It independently cites the two primary sources (Miller 1970, Odlyzko
1993) that anchor the run's proved interior claim. Under the run's "taken from a
catalogue" rule, this confirms (never causes) claims already established by the
run's own derivation.

```claim
id: oeis-A396593-run-length-second-entry
statement: A396593 gives the lengths of consecutive identical runs in the second-entry sequence d_k(2) of the prime Gilbreath difference triangle; its comment states that if Gilbreath holds then d_k(2) is all 0s and 2s, and that within a uniformly-0-and-2 sequence Rule 90 (XOR) determines the analogous values in the next row.
hypotheses: A_0 = primes, absolute-difference operator.
holds-here: yes — consistent with the proved reduction and rule90-interior-xor.
status: catalogued (read from OEIS, not derived here).
bearing: independent catalogue confirmation of the {0,2}-second-entry reduction and the Rule-90 interior structure; independently cites Miller 1970 and Odlyzko 1993.
anchor: research/summaries/oeis-A396593-run-length-of-second-entry.md (small catalogue record; the summary file is the complete captured page — no .full.md companion exists)
```
