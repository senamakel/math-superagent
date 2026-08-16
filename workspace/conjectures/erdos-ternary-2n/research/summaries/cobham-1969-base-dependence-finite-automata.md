# Cobham, "On the base-dependence of sets of numbers recognizable by finite automata"

Source: Mathematical Systems Theory 3 (1969) 186–192. Full text (abstract + paywall metadata): `research/sources/cobham-1969-base-dependence-finite-automata.full.md`.

## The decidability answer problem.md asked about

Cobham's theorem: the **only** sets of natural numbers recognizable by a finite automaton in *every* base are the **ultimately periodic** sets. The set `{2^n : n ≥ 0}` is recognizable in base `b` **iff `b` is a power of 2**, and is **not** recognizable in any other base — in particular not in base 3.

## Consequence for this run

The digit-avoidance hypothesis is recognized by a finite automaton in base 3 (the set `S` of 3-adic integers with digits in `{0,1}` is a regular/recognizable set). But the *sequence of values* `2^n` is **not 3-automatic**. Cobham's theorem says a set simultaneously recognizable in two multiplicatively independent bases is ultimately periodic; since `{2^n}` is not ultimately periodic, no "mechanical" Cobham/Walnut/Büchi-arithmetic decidability route applies directly to the statement "some n>8 has 2^n ∈ S". 

This is the honest negative answer to the run's question #4: **there is no applicable decidability machinery** (Cobham, Büchi arithmetic, Walnut) that decides Erdős's conjecture, because the inputs `2^n` are non-3-automatic. A Walnut query needs a 3-automatic input sequence; `2^n` is not one.

## Claims

```claim
id: COBHAM-DECIDABILITY-NEGATIVE
statement: The set {2^n : n >= 0} is recognizable by a finite automaton in base
  b iff b is a power of 2, and is NOT recognizable in base 3. A set recognizable
  in every base is ultimately periodic (Cobham 1969).
hypotheses: b a positive integer base.
holds-here: yes — {2^n} is not ultimately periodic, and 3 is not a power of 2,
  so {2^n} is not 3-automatic.
status: proved (Cobham 1969, peer-reviewed; statement from abstract + theorem)
bearing: no Cobham/Büchi/Walnut decidability machinery applies to "some n>8 has
  2^n digit-2-free", because the input sequence 2^n is not 3-automatic. This
  closes the automatic-sequences lead: it is a dead end, now with a source.
anchor: research/sources/cobham-1969-base-dependence-finite-automata.full.md
```

## Status

Sourced, peer-reviewed (Cobham 1969). The full text is paywalled at Springer; the abstract and theorem statement are captured.
