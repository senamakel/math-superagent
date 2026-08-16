# The Casas-Alvero conjecture

Let `K` be a field of characteristic `0` and let

```
f ∈ K[x],   f monic,   deg f = n ≥ 1.
```

Write `f^(i)` for the `i`-th formal derivative.

> **(CA)** If `gcd(f, f^(i)) ≠ 1` for every `i = 1, …, n−1` — that is, `f`
> shares a root (in an algebraic closure) with each of its first `n−1`
> derivatives — then `f = (x − a)^n` for some `a ∈ K̄`.

The converse is trivial: `(x−a)^n` has `f^(i) = n(n−1)…(n−i+1)(x−a)^{n−i}`, so
every derivative vanishes at `a`. The content is that *nothing else* can do it.

Stated by Eduardo Casas-Alvero around 2001, arising from a question about
singularities of plane curves. Open in general.

## Normalisations that are free, and should be taken

1. **Scaling and translation.** `x ↦ λx + μ` preserves the hypothesis, so one
   may fix a normalisation — e.g. assume `f` is not `(x−a)^n`, translate so that
   the shared root of `f'` is `0`, or fix the sum of the roots to be `0`.
2. **Reduce to an algebraically closed field.** The hypothesis and conclusion
   are insensitive to base change, so one may work over `C` — or, better, over
   `Q̄`, since the conjecture for a given `n` is a statement about a
   `Q`-defined scheme (see 4).
3. **`n` may be assumed composite** for the standard reason: the prime-power
   cases are settled (see below), so a first open `n` is composite.
4. **It is a finite algebraic question for each fixed `n`.** Write
   `f = x^n + a_1 x^{n−1} + … + a_n`. For each choice function
   `σ : {1,…,n−1} → K̄` picking a common root `r_i` of `f` and `f^(i)`, the
   conditions `f(r_i) = f^(i)(r_i) = 0` cut out a variety in `(a, r)`-space. CA
   for degree `n` says: every point of that variety has all `r_i` equal and
   `f = (x−r)^n`. So each degree is, in principle, a Gröbner/elimination
   computation — and in practice the systems blow up fast.

## Known results — leads, not imports

**These are recalled from memory and must be re-established from primary
sources before anything is built on them. Print the source and the exact
hypothesis beside each one you confirm; strike any you cannot.**

- **Small degrees.** `n ≤ 4` is elementary; low degrees were done by hand
  early.
- **Prime powers.** CA holds for `n = p^k` (`p` prime). The standard proof is a
  reduction to characteristic `p` — in char `p` the operator identities
  degenerate in a way that forces the conclusion — and is the template every
  later result follows.
- **Graf von Bothmer, Labs, Schicho, van de Woestijne (2007).** CA holds for
  `n = 2p^k, 3p^k, 4p^k`. Same method: reduce mod a well-chosen prime and count.
- **Consequently the smallest degrees not covered are believed to be `n = 30`
  and up** (30 = 2·3·5 is the first integer that is not `p^k`, `2p^k`, `3p^k`
  or `4p^k`). **Verify this arithmetic and this claim of "smallest open" against
  a source — it is exactly the sort of fact that a later paper moves.**
- **Real-rooted case.** CA is known when all roots of `f` are real (and there
  are related results for roots in a half-plane / with positivity hypotheses).
- **Draisma–de Jong** wrote an expository account (EMS Newsletter) framing CA
  as a question about a specific system and its degenerations.
- **Claimed proofs.** CA attracts them. **Check whether a claimed complete
  proof exists in the literature as of now, and if one does, its status
  (published? refereed? withdrawn? gap found?) is the first thing this run must
  establish and record.** A claimed proof does not end this run — see `GOAL.md`.

## The hard constraint every proof must satisfy

**CA is false in positive characteristic.** The standard counterexample family:
over a field of characteristic `p`, polynomials such as `x^{p+1} − x^p` (and
relatives) satisfy the derivative-sharing hypothesis without being a pure power,
because `f^(p)` and higher derivatives vanish identically or degenerate.

*Consequence, and it is the sharpest structural fact in the problem:* **any
proof of CA must use characteristic `0` somewhere, and must break in char `p`.**
An argument that never mentions the characteristic — pure combinatorics of the
root multiset, pure degree counting, pure Newton-polygon bookkeeping — is
therefore wrong, and can be tested against the char-`p` counterexamples before
any effort is spent on it. Every candidate argument in this workspace must be
run against that test and the outcome recorded.

The same fact explains why the known results have the shape they do: reduction
mod `p` is used to *prove* CA for degrees where the char-`p` degeneration is
strong enough to force collapse, and the method stalls exactly where the
degeneration is too weak.

## What is genuinely unknown

- CA for any single degree not of the form `p^k, 2p^k, 3p^k, 4p^k` — `n = 30`
  first. A single new degree settled unconditionally is a real result.
- Any bound of the shape "CA holds for all `n` outside a sparse set", or "the
  variety of counterexamples has dimension 0 / is empty for `n` in a positive
  density set".
- A structural theorem about a counterexample: how many distinct roots it must
  have, bounds on multiplicities, whether the `r_i` can be forced to coincide
  in pairs, field of definition, height.
- Whether CA follows from, or implies, a statement about the Wronskian /
  Schur-like determinants in the coefficients.

## What counts as a result

In descending order of value.

1. CA for a new degree, unconditionally, with a verifiable certificate.
2. CA for an infinite family of degrees not covered by `p^k, 2p^k, 3p^k, 4p^k`.
3. A theorem constraining a minimal counterexample — number of distinct roots,
   multiplicity pattern, which `i` can share which root — proved, not measured.
4. A reduction of CA (for all `n`, or for a family) to a stated, strictly
   different problem, with the reduction proved in both the direction that is
   useful and the direction that is not.
5. A refutation of a published or folklore approach, with an explicit witness
   (for instance, a char-`p` object that kills a proposed char-free argument, or
   an explicit point on a degeneration that a paper claims is empty).
6. An exact computation extending the verified range — e.g. a complete Gröbner
   / elimination proof for a specific `n` — provided the computation is
   reproducible from a script in `code/` and its correctness argument is stated.

**Do not claim CA.** A proof of the full conjecture produced in a run of this
length is, on prior, an error; if you believe you have one, the deliverable is
the argument written out with every step's status labelled and the char-`p`
test applied to it explicitly, not an announcement.
