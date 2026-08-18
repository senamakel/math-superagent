Solve by computational arithmetic of quadratic lattices, with the mathematics
carried in Lean wherever it will go. The object is a **lattice with a quadratic
form** over `O_K`, and every question is about what it represents: which totally
positive elements, at which places, and how the local answers fail to assemble
into a global one.

Reason about *representation*. The instruments are: the local theory at each
place (Jordan splittings, Hilbert symbols, Hasse invariants), the genus and the
spinor genus and their class numbers, theta series and the Siegel–Weil mass
formula as a check on completeness, escalation trees for universality, and
continued fractions of `√D` for the real quadratic case, where the arithmetic of
the fundamental unit drives everything.

**Escalation is the method for universality, and its content is completeness.**
Adjoin a vector representing the smallest unrepresented value, branch on the
finitely many possibilities, recurse, and prove the tree is exhausted. Every
universality result in this subject is a complete escalation tree plus a check
of each leaf; a partial tree proves nothing, and reporting its size is what
makes the claim assessable.

**Prefer the argument Lean can finish.** A local condition at one place, a
Hilbert symbol, a representation of a specific integer by a specific form, the
determinant and Hasse invariant of an explicit lattice — all are finite and
kernel-checkable. State every claim as a Lean type before spending an attempt on
it; where generated lattice data is involved, keep it under `Generated/` with a
hand-written checker and a soundness theorem outside, never a `theorem` inside.

Three cautions this problem earns before any work starts.

**A search that found no exception is not a universality proof.** It is a
statement about the search bound. Universality is proved by a complete
escalation, or by a critical-set theorem whose hypotheses are checked. This is
the one distinction the whole subject turns on.

**Definite and indefinite are different subjects.** Strong approximation gives
local–global for indefinite forms of rank ≥ 3 and gives nothing for definite
ones. Every claim states which case, and no result is transported across.

**Number-field arithmetic is where the silent errors are** — the difference
between integer-matrix and integer-coefficient forms, between totally positive
and positive, between `O_K` and a non-maximal order. Fix the conventions once,
in `research/ROOT.md`, and have the oracle enforce them rather than the prose.
