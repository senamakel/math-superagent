# Galois action on the shared-root partition

```approach
idea: Constrain a hypothetical counterexample through the Galois action on the set
    S_i = {j : H_i f(beta_j) = 0}, the roots of f shared with the i-th derivative
mechanism: Write f = prod_j (x - beta_j) over Q-bar. The hypothesis is: for each
    i = 1..n-1 the set S_i of roots beta_j at which H_i f vanishes is nonempty. Each S_i
    is Gal(Q-bar / K)-stable (f and its Hasse derivatives are defined over the
    coefficient field K), hence a union of G-orbits for G = Gal(splitting field / K).
    CA says: all S_i nonempty forces all beta_j equal. The new object is the combinatorial
    cover {S_1,...,S_{n-1}} of the root set together with its G-equivariance, i.e. the
    partition/covering structure forced by the permutation action. The bet: a transitive
    G (or a 2-transitive G, or a G with large minimal degree) is incompatible with a
    G-stable nonempty system {S_i} satisfying the root-difference identities
    H_i f(beta_j) = e_{n-i}(beta_j - beta_*), unless the beta_j coincide — giving an
    inductive descent on the Galois group (transitivity of a counterexample's factor,
    solvability, or a bound on G's orbit structure) instead of on the degree.
status: refuted
killed-by: ungrounded, and it cannot reach the degree that matters. Grounding
    found no theorem relating the Galois group of a counterexample to CA (the
    "transitive G incompatible with a G-stable cover" claim is a conjecture,
    not a named result). Worse, it is characteristic-free: the S_i are
    Galois-stable in every characteristic, so the char-0 ingredient that
    GOAL.md requires an argument to *name* cannot even be located (the
    candidate's own two guesses — the i!-invertibility convention, or
    distinctness of root differences — are statements about the root-difference
    identity the run already owns, not about Galois action). And its only
    first step, polgalois on small-n witnesses, scales to the splitting-field
    degree of a degree-20 polynomial (astronomical), so it cannot reach
    n = 20, the smallest open degree. The structural constraint it might
    produce (a bound on a counterexample's Galois group) is downstream of a
    hypothetical bridge that was never formed.
first-step: For small n and the char-p witnesses (x^{p+1}-x^p, and n=4,5,6 examples from
    the oracle), compute the sets S_i and the action of the Galois group of the splitting
    field (PARI/gp or Magma polgalois), then state the precise G-equivariance conjecture:
    which orbit structure of {S_i} is compatible with e_{n-i}(beta_j - beta_*) = 0, and
    test whether it forces G intransitive or the roots coincident. Record what survives.
```

## Char-p break (admissibility)

Galois theory is characteristic-free, so this argument does **not** by itself
distinguish char 0 from char p — the witness x^{p+1}-x^p has a genuine splitting field
and a genuine Galois action, and it must survive any purely Galois-theoretic statement.
The char-0 ingredient must be located: candidate locations are (a) the use of the
ordinary-derivative convention (f^{(i)} = i! H_i f, so i! is invertible exactly in char 0),
which changes S_i, or (b) a statement that the root differences beta_j - beta_k are
distinct/algebraically independent in char 0 in a way that fails mod p. The first step
explicitly runs the witnesses and reports which S_i differ under the two conventions;
a proposal that cannot name the break is unfinished.

## Honest status

Speculative. No known theorem links the Galois group of a counterexample to CA; the
"incompatibility of a transitive action with a G-stable cover" is a conjecture to be
formed and then attacked (hunt a transitive-G counterexample pattern as hard as the
proof). The concrete deliverable even in failure is a new structural constraint on a
minimal counterexample (its Galois group's orbit structure), which is a stated partial
result. No approach on the record (adopted or refuted) uses Galois theory.

## Decision (converging pass)

status: refuted
killed-by: ungrounded, and it cannot reach the degree that matters. Grounding
      found no theorem relating the Galois group of a counterexample to CA (the
      "transitive G incompatible with a G-stable cover" claim is a conjecture,
      not a named result). Worse, it is characteristic-free: the S_i are
      Galois-stable in every characteristic, so the char-0 ingredient that
      GOAL.md requires an argument to *name* cannot even be located (the
      candidate's own two guesses — the i!-invertibility convention, or
      distinctness of root differences — are statements about the root-difference
      identity the run already owns, not about Galois action). And its only
      first step, polgalois on small-n witnesses, scales to the splitting-field
      degree of a degree-20 polynomial (astronomical), so it cannot reach
      n = 20, the smallest open degree. The structural constraint it might
      produce (a bound on a counterexample's Galois group) is downstream of a
      hypothetical bridge that was never formed.
