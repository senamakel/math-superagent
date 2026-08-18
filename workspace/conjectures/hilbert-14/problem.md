# Hilbert's 14th problem — finite generation of invariant rings

## The original question, and its answer

> Let `k` be a field, `k[x_1, …, x_n]` a polynomial ring, and `K` a subfield of
> the fraction field with `k ⊆ K ⊆ k(x_1, …, x_n)`. Is
> `K ∩ k[x_1, …, x_n]` a finitely generated `k`-algebra?

Hilbert asked it because the invariant ring `k[x]^G` of a linear group action
is of this shape. **Nagata (1959) answered no**, with a counterexample built
from an action of a product of additive groups `G_a` on a polynomial ring in
32 variables. So the target of this workspace is not the original question. It
is the **boundary**: for which classes is the answer yes, and where exactly is
the frontier between the finitely generated and the counterexamples.

That boundary has a single crisp open case, and it is the run's target.

## The target: the dimension-4 case

For `k` of characteristic zero, an action of the additive group `G_a` on affine
`n`-space corresponds to a **locally nilpotent derivation** `D` on
`k[x_1, …, x_n]`, and the invariant ring is `ker D`. The recalled state of the
frontier — **every item to be confirmed or struck against a primary source**:

- `n ≤ 2`: `ker D` is finitely generated; classical.
- `n = 3`: finitely generated (Miyanishi; Zariski's finiteness in dimension
  ≤ 3 is the other standard route).
- `n = 5`: **not** always finitely generated — Daigle–Freudenburg produced a
  locally nilpotent derivation on a five-variable polynomial ring with
  non-finitely-generated kernel.
- `n = 6`: Freudenburg, and `n = 7`: Paul Roberts, both counterexamples,
  historically earlier and larger.
- **`n = 4`: open.** Whether the kernel of every locally nilpotent derivation
  on `k[x_1, x_2, x_3, x_4]` is finitely generated is not known.

> **(H14.4)** Is `ker D` a finitely generated `k`-algebra for every locally
> nilpotent derivation `D` on a polynomial ring in four variables over a field
> of characteristic zero?

This is the statement to attack. It is entirely polynomial, and every object in
it — the derivation, its kernel, a candidate generating set, a Gröbner basis, a
slice — is something a program can construct exactly over `Q`.

## Related open ground

- **Weitzenböck / linear actions.** For a *linear* `G_a`-action the invariant
  ring is finitely generated in every dimension (Weitzenböck; Seshadri's
  proof). So a dimension-4 counterexample must be non-linear, and any argument
  that would apply to linear derivations proves nothing new.
- **Nagata's problem in low dimension.** How few variables can a
  non-finitely-generated invariant ring of a *unipotent* group action need?
  Nagata used 32; the current record is lower and is worth pinning down exactly.
- **Positive characteristic.** The picture changes completely — the correct
  object is a `G_a`-action / exponential automorphism, not a locally nilpotent
  derivation. Records here are separate and must not be quoted across.
- **Zariski's problem** in dimension 2, and finite generation for kernels of
  *ordinary* (not locally nilpotent) derivations, where far less is known.

## The cheap tests every candidate must pass first

1. **The Weitzenböck test.** An argument for finite generation in dimension 4
   that does not use non-linearity somewhere proves only the linear case, which
   is a theorem. Say which step uses that `D` may be non-linear.
2. **The slice test.** If `D` has a *slice* — an `s` with `Ds = 1` — then
   `k[x] = (ker D)[s]` and `ker D` is a polynomial ring in `n − 1` variables,
   hence finitely generated. Every candidate counterexample must be checked for
   a slice, and every finite-generation argument must say what it does when
   there is none: that is the whole difficulty.
3. **The dimension test.** A strategy for dimension 4 must **fail** at
   dimension 5, where a counterexample exists. Locate the step that breaks at
   `n = 5` before spending an attempt. An argument uniform in `n` is refuted,
   not promising.

## What is genuinely unknown

- H14.4 itself, in either direction.
- The minimal `n` for which a `G_a`-action on `A^n` has a non-finitely-generated
  invariant ring — currently pinned between 4 and 5 by the above.
- Whether the dimension-5 counterexample's kernel has an explicit infinite
  minimal generating set with a degree pattern that could be transported down.
- Finite generation for kernels of non-locally-nilpotent derivations in
  dimensions 3 and 4.
- Explicit generators for kernels of named dimension-4 derivations where the
  computation has not been carried out.

## What counts as a result

In descending order of value.

1. A resolution of H14.4 in either direction. A counterexample is a derivation
   plus a *proof* its kernel is not finitely generated — never a computation
   that failed to terminate.
2. Finite generation for a stated subclass of dimension-4 locally nilpotent
   derivations (triangular, of a given rank, with a prescribed degree
   function), with the obstruction to removing the hypothesis named.
3. An explicit generating set for the kernel of a named dimension-4 derivation
   the literature has not computed, reproducible, with its cost recorded.
4. A structural invariant of the dimension-5 counterexample that a dimension-4
   derivation provably cannot carry — evidence for finite generation, and a
   theorem in its own right.
5. A lowering of the variable count in Nagata-type counterexamples for
   non-`G_a` unipotent groups.
6. A refutation, with a witness, of a published claim or a folklore expectation
   about where the boundary sits.

**Do not claim H14.4 in either direction on a computation alone.** A Gröbner
basis that did not terminate measures a program's ceiling; it does not prove a
ring is infinitely generated.
