Solve by explicit computational class field theory, with the mathematics carried
in Lean wherever it will go. The object is a **special value** — a Stark unit,
a singular modulus, a `p`-adic invariant — and the question is always the same:
does the field it generates equal the abelian extension the ray class group
predicts?

Reason about *that equality*. It has two halves with different evidential
status, and keeping them apart is the whole discipline of the subject. The
analytic half — computing partial zeta values, `L`-function leading terms, or
`p`-adic integrals to high precision — is numerical and concludes nothing. The
algebraic half — forming the minimal polynomial, factoring it, computing the
degree, discriminant, conductor, Galois group and ramification of the field it
cuts out — is exact and is where a claim becomes a claim.

The instruments: ray class groups and conductors, Artin `L`-functions and
partial zeta functions, Shintani domains and cone decompositions, continued
fractions of `√D` and the fundamental unit, `p`-adic integration and
Darmon-style cycles, lattice reduction (LLL/PSLQ) for recognising an algebraic
number from its numerical approximation, and exact number-field arithmetic for
the verification.

**Prefer the argument Lean can finish.** Once a minimal polynomial is in hand,
its irreducibility, its degree, its discriminant and the ramification of the
field it defines are finite algebraic facts a kernel can check. State claims as
Lean types before spending an attempt on them, and record what today's Mathlib
carries of class field theory — probably little, and saying exactly how little
is a reportable finding.

Three cautions this problem earns before any work starts.

**A `p`-adic theorem is not an archimedean one.** The recent progress on
totally real fields is `p`-adic, and summaries drop that word. Every statement
in this workspace says which. An argument that quietly transports one to the
other has proved nothing.

**Recognition is where the wrong claims come from.** LLL will return *some*
polynomial for any input; the question is whether the precision justifies it.
Report the working precision, the polynomial's coefficient height, and the
margin between them — and then verify the field exactly, which is what settles
it independently of the recognition.

**Compute the ray class group first, always.** It predicts the degree, the
conductor and the ramification. Everything else is checked against it, and that
check is cheap enough to run before any analytic work begins.
