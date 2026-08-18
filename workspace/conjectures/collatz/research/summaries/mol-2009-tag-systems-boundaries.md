# Mol 2009 — tag systems, Collatz reduction, solvability boundaries

<!-- src: De Mol, "On the boundaries of solvability and unsolvability in tag systems", EPTCS 1 (2009) 56–66, arXiv:0906.3329 -->

Full text: `research/sources/mol-2009-tag-systems-boundaries.full.md`

## What the source establishes

This is a survey of solvability/unsolvability boundaries for small tag
systems (Post's production systems with shift v and μ symbols), with an
experimental emphasis. Its relevance to the Collatz run is the reduction of
the Collatz problem to an extremely small tag system — evidence for why a
simple algebraic proof of the conjecture is unlikely (the problem can encode
unbounded computation in a 3-symbol, deletion-2 tag system).

**The reduction (Section 2.2, from De Mol's own [15]):** the Collatz problem
reduces to the tag system TS(3,2) with μ = 3 symbols, shift v = 2, and
production rules

- a₀ → a₁a₂
- a₁ → a₀
- a₂ → a₀a₀a₀

with l_max − v = v − l_min = 1. The Collatz orbit terminates in the loop
C(4)=2, C(2)=1, C(1)=4 iff the corresponding tag-system computation halts
or becomes periodic. The Collatz problem had previously been reduced to small
Turing machines (Baiocchi, Margenstern, Michel), but this tag system is
smaller than those descriptions.

**Solvability boundaries stated:**
- TS(2,2) has a solvable reachability problem; its words are incapable of
  producing "irregular" types 2 and 4.
- TS(2,3) and TS(3,2) are different — the Collatz reduction lands in TS(3,2),
  and proving TS(3,2) recursively solvable would be very hard precisely
  because of this encoding.

## What it implies for this run

The Collatz conjecture is equivalent to a halting/periodicity statement about
a specific 3-symbol, 2-shift tag system. This is the same shape of result as
Yolcu–Aaronson–Heule's rewriting-system equivalence and Kurtz–Simon's
Π⁰₂-completeness: it does not apply to the specific 3x+1 map's truth, but it
explains why generic proof machinery (uniform solvability of the class) is
unavailable.

## Claims

```claim
id: mol-collatz-tag-system
statement: The Collatz problem reduces to the halting/periodicity problem of the tag system TS(3,2) with rules a0 -> a1a2, a1 -> a0, a2 -> a0a0a0, deletion number v=2 and 3 symbols (De Mol 2009, §2.2, citing her own [15]).
hypotheses: none beyond the standard Collatz map on positive integers
holds-here: yes
status: asserted
bearing: why a generic proof method is unavailable; the conjecture is a halting question for a small tag system
anchor: research/summaries/mol-2009-tag-systems-boundaries.md
```

```claim
id: mol-ts22-solvable
statement: Tag systems in TS(2,2) have a solvable reachability problem, and cannot produce words of the irregular types 2 and 4; this is a fundamental difference from TS(2,3) and TS(3,2).
hypotheses: tag systems with 2 symbols, shift 2
holds-here: no — context about tag systems, not about the Collatz map itself
status: asserted
bearing: locates the Collatz-encoding class TS(3,2) beyond the solvable boundary
anchor: research/summaries/mol-2009-tag-systems-boundaries.md
```
