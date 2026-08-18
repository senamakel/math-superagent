# Hilbert's 21st problem — the Riemann–Hilbert problem

## The question

> Given `n` points `a_1, …, a_n` on the Riemann sphere and a representation
> `ρ : π_1(CP¹ ∖ {a_1, …, a_n}) → GL_p(C)`, does there exist a **Fuchsian**
> linear system
>
> ```
> dY/dz = ( Σ_{i=1}^{n} A_i / (z − a_i) ) Y,   A_i ∈ Mat_p(C),
> ```
>
> with singularities exactly at the `a_i` and monodromy representation `ρ`?

Fuchsian means every singularity is a simple pole — a strictly stronger
requirement than *regular singular*, and the entire content of the problem sits
in that gap.

## The status

Recalled — **every item to be confirmed or struck against a primary source**:

- **Plemelj (1908)** claimed a positive answer. His argument in fact proves the
  statement with *regular singular* points, and gives Fuchsian only under an
  extra hypothesis (one monodromy matrix diagonalisable, in the usual telling).
  The gap went unnoticed for decades.
- **Bolibrukh (1989)** gave a **counterexample**: a representation of rank 3
  with 4 singular points that is not the monodromy of any Fuchsian system. So
  the answer as Hilbert asked it is **no**.
- **Bolibrukh and Kostov**, independently, proved the answer is **yes for
  irreducible** `ρ`. So every counterexample is reducible, and the problem
  reduces to the reducible case.
- The **reducible case is not classified.** Necessary and sufficient conditions
  on a reducible representation for realisability by a Fuchsian system are known
  only partially — in terms of the splitting type of the associated vector
  bundle on `CP¹` and the admissible sets of exponents.

> **(H21.red)** Characterise exactly which reducible representations
> `ρ : π_1(CP¹ ∖ {a_i}) → GL_p(C)` are monodromies of Fuchsian systems.

That is the target. Also in scope:

- **Higher genus**: the same question with `CP¹` replaced by a compact Riemann
  surface of genus `g ≥ 1`, where less is settled.
- **Explicit realisation**: given a realisable `ρ`, *construct* the residues
  `A_i`. This is an inverse problem, computationally hard, and even for small
  rank and few points the explicit answers are few.

## Where a machine has traction

Everything here is finite-dimensional linear algebra plus one analytic step.
A representation is a tuple of matrices `M_1, …, M_n` with `M_1 ⋯ M_n = I`, up
to simultaneous conjugation. A Fuchsian system is a tuple of residues `A_i` with
`Σ A_i = 0` (for a regular point at infinity). The monodromy of a given system
is computable to high precision by numerical continuation of the ODE — and to
*certified* precision by interval methods. So:

- Candidate counterexamples and candidate realisations are explicit matrix
  tuples over `Q` or a number field.
- The correspondence can be *tested* numerically at speed and then argued
  exactly.
- The obstruction theory — Fuchsian weights, the splitting of the associated
  bundle, the Fuchs relation `Σ (traces of exponents) = 0` — is arithmetic on
  integers and eigenvalues.

## The cheap tests every candidate must pass first

1. **The Fuchs relation test.** For a Fuchsian system the exponents at all
   singular points satisfy a linear relation summing to a non-positive integer
   determined by the bundle splitting. Any claimed realisation must satisfy it,
   and any claimed set of exponents violating it is refuted on integers, in
   seconds.
2. **The irreducibility test.** Bolibrukh–Kostov settles the irreducible case
   positively. So any claimed counterexample must be checked for irreducibility
   *first* — an irreducible counterexample contradicts a theorem and is an
   error. Compute the invariant subspaces exactly before anything else.
3. **The regular-vs-Fuchsian test.** Plemelj's theorem gives regular singular
   points. Any argument that never distinguishes a simple pole from a regular
   singularity has proved Plemelj's statement, not Hilbert's, and is refuted as
   progress. Name the step where the pole order is controlled.

## What is genuinely unknown

- H21.red: the exact characterisation of realisable reducible representations.
- Effective/explicit realisation: an algorithm producing the residues `A_i` for
  a realisable `ρ`, with complexity bounds.
- The minimal rank and minimal number of singular points for a counterexample —
  Bolibrukh's has rank 3 with 4 points; whether rank 3 with 3 points, or rank 2
  with any number, admits a counterexample is a sharp, finite question.
- The higher-genus problem in general.
- The analogue for other structure groups and for irregular singularities (the
  Riemann–Hilbert correspondence in the wild setting), where the dictionary is
  known but the realisation questions are not.

## What counts as a result

In descending order of value.

1. A characterisation, proved, of realisability for a stated class of reducible
   representations wider than the published results — the class stated before
   the proof and the obstruction to widening it named.
2. A **new counterexample** of smaller rank or fewer singular points than
   Bolibrukh's, with reducibility verified and the non-realisability proved by
   an obstruction — not by a failed search.
3. A settled answer to the minimal-rank / minimal-points question: e.g. a proof
   that every rank-2 representation is realisable, or a rank-2 counterexample.
4. An explicit algorithm realising a stated family, implemented, with residues
   produced over a number field and the monodromy certified to match.
5. A certified numerical verification of Bolibrukh's counterexample or of a
   published realisation — reproduced exactly, which nobody has published as a
   verified artifact.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not claim a counterexample from a failed search for residues.** Failing to
find `A_i` is a measurement of a search; non-realisability is an obstruction.
