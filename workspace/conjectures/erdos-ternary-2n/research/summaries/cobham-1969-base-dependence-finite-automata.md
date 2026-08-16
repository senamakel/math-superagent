# Cobham, "On the base-dependence of sets of numbers recognizable by finite automata"

Source: Mathematical Systems Theory 3 (1969) 186–192. Full text (abstract + paywall metadata): `research/sources/cobham-1969-base-dependence-finite-automata.full.md`.

## The decidability answer problem.md asked about

Cobham's theorem: the **only** sets of natural numbers recognizable by a finite automaton in *every* base are the **ultimately periodic** sets. The set `{2^n : n ≥ 0}` is recognizable in base `b` **iff `b` is a power of 2**, and is **not** recognizable in any other base — in particular not in base 3.

## Consequence for this run

The digit-avoidance hypothesis is recognized by a finite automaton in base 3 (the set `S` of 3-adic integers with digits in `{0,1}` is a regular/recognizable set). But the *sequence of values* `2^n` is **not 3-automatic**. Cobham's theorem says a set simultaneously recognizable in two multiplicatively independent bases is ultimately periodic; since `{2^n}` is not ultimately periodic, no "mechanical" Cobham/Walnut/Büchi-arithmetic decidability route applies directly to the statement "some n>8 has 2^n ∈ S". 

This is the honest negative answer to the run's question #4: **there is no applicable decidability machinery** (Cobham, Büchi arithmetic, Walnut) that decides Erdős's conjecture, because the inputs `2^n` are non-3-automatic. A Walnut query needs a 3-automatic input sequence; `2^n` is not one.

## Status

Sourced, peer-reviewed (Cobham 1969). The full text is paywalled at Springer; the abstract and statement above are captured. This suffices for the decidability-negative claim. If a precise statement is needed, Allouche–Shallut "Automatic Sequences" (Cambridge, 2003) is the standard book reference (not yet in library).
