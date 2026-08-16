# Ritt decomposition / indecomposable-polynomial classification

```approach
idea: Ritt's theory of polynomial decomposition — every monic f splits as a composition of
      indecomposable ("prime") polynomials, essentially uniquely (Ritt 1922 first theorem;
      Engstrom's theorem for the uniqueness), with the decomposition shapes controlled by the
      prime factorization of deg f. Reformulate CA: prove a CA polynomial over C is
      indecomposable, then attack the indecomposable polynomials of degree n, which are a
      classified finite family.
mechanism: CA's hypothesis is a tower of derivative-gcd conditions, and the derivative of a
      composition f = g∘h obeys f^(i) built from g^(j)(h) and h^(k). A common root of f and
      f^(i) forces either a common root of g and g^(j) at h(r), or a multiple root of h at r
      — a recursion that should transfer the CA property down a composition and, if it cannot
      propagate non-trivially, kills all decomposable f. That reduces CA_n to the indecomposable
      degree-n polynomials, which for n = 20 = 2^2·5 are a short explicit list (Ritt/Engstrom:
      decomposition is governed by the divisibility lattice of n). The target scheme shrinks
      from the full (n−1)-dimensional Z-scheme to a finite union of low-dimensional families.
status: refuted
killed-by: refuted on paper. The transfer lemma is false: the pure power x^4 = x^2 o x^2 (both factors non-linear) is CA, and x^n = x^d o x^{n/d} for every d | n, so "CA => indecomposable" is refuted by CA's own conclusion; any repaired statement ("the only CA compositions are pure powers") is CA in disguise and buys no reduction. Two further false premises: (i) for i >= 2, Faa di Bruno makes f^(i)(r) a linear combination of the g^(j)(h(r)), not a single common-root statement, so the claimed recursion does not exist; (ii) "indecomposable degree-20 polynomials are a finite classified family" is false — Ritt/Engstrom classify decomposition *shapes*, and the indecomposable locus is open dense of dimension 20 in coefficient space.
first-step: State and test the transfer lemma with the canonical oracle: for f = g∘h (deg h ≥ 2),
      a common root r of f and f^(i) forces (h(r) a common root of g and some g^(j)) or (r a
      multiple root of h). Exhaust all monic g, h of low degree over Q via lib.casas_alvero to
      find whether a CA composition with both g and h non-linear exists at all; if none in the
      tested range, the lemma survives its first attack and the classification becomes the path.
```

## What is established vs. what is speculation

- **Established (classical, name the sources to confirm):** Ritt's first theorem
  (polynomial decomposition into indecomposables, uniqueness up to linear factors),
  Engstrom's uniqueness theorem, and the theory controlling decompositions of degree
  `n` by the prime factorization of `n` (Ritt 1922, *Prime and composite polynomials*,
  Trans. AMS; the modern account is Zannier's *Lecture Notes on Diophantine Analysis*
  §"Ritt's theory", and the classification of prime polynomials of fixed degree is a
  standard application). This is named mathematics with a real object: the monoid of
  polynomials under composition, and its atoms.
- **Speculation (mine, to be attacked):** the transfer lemma above — that CA is
  incompatible with a non-trivial non-linear composition. This is *not* in the
  literature as far as the run's library knows and is the load-bearing claim.

## Char-`p` break (mandatory)

The chain rule and the transfer lemma must be re-examined in characteristic `p`:
`(g∘h)' = g'(h)·h'` still holds, but `h'` can vanish identically (inseparable `h`),
and the derivative tower collapses exactly as in the Hasse-vs-ordinary issue the run
already resolved. So the expected break is: in char `p`, `f = g(x^p)` has `f' = 0`,
and compositions such as the witnesses `x^{p+1} − x^p = (x^p)·(x − 1)… ` provide
decomposable CA polynomials — the transfer lemma is a char-0-only statement. Locating
*which* step uses `h' ≠ 0` / separability is part of the proposal and will be checked
against `x^{p+1} − x^p` before anything is trusted.

## Why it is not a restatement of a closed approach

This is a change of representation: from "coefficients `a_1,…,a_n` cut out by
resultants" to "atoms of the composition monoid". It does not touch resultants,
Gröbner bases, catalecticants, or tropical objects. The adopted approaches operate on
the *resultant ideal* and on *root differences*; Ritt theory operates on the
*compositional* structure of `f`, which none of them uses.

## Honest likely output

The transfer lemma, if it holds, is a real partial result: "every CA polynomial is
indecomposable" (a new structural constraint on a minimal counterexample, of the kind
GOAL.md point 3 asks for), and it reduces CA_20 to a classified finite family of
prime degree-20 polynomials. If the lemma fails, the failure mode (a decomposable CA
polynomial) is itself a new char-0 fact or a new counterexample, either of which is a
result.
