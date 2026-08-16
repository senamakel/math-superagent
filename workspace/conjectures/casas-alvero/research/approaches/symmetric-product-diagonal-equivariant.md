# Symmetric-product diagonal and S_n-equivariant intersection theory

```approach
idea: CA as a statement about the diagonal section of Sym^n(A^1)
mechanism: The coefficient space A^n with coordinates (a_1,...,a_n) is the symmetric product
    Sym^n(A^1) (the elementary symmetric functions are its coordinates). The pure-power
    locus {(x-a)^n} is exactly the image of the diagonal section t |-> (t,...,t) under the
    quotient A^n -> Sym^n(A^1), i.e. the moment/Veronese curve a_j = C(n,j) t^j. The
    resultants R_i = Res(f, H_i f) are S_n-symmetric in the roots, hence divisors on
    Sym^n(A^1), and CA is the statement that the intersection of these n-1 divisors equals
    the diagonal section. Since Sym^n(A^1) = A^n//S_n is the affine GIT quotient and the
    S_n-action (Springer theory, equivariant cohomology of the flag variety, the
    coinvariant algebra) is exactly the machine that describes Sym^n and its diagonal,
    the bet is that (R_1,...,R_{n-1}) carries S_n-stable structure (a specific Schur
    / plethysm decomposition) that forces the radical to be the moment-curve ideal.
status: refuted
killed-by: no load-bearing inference survives grounding. Springer theory /
      equivariant cohomology of the flag variety describes Sym^n(A¹) and its
      diagonal (a true, sourced description of the *space*), but no theorem of
      that theory says anything about the radical of the particular ideal
      (R_1,…,R_{n−1}): the "S_n-module structure forces the radical" bridge has
      no statement behind it, and its only concrete content — rad(R_1,…,R_{n−1})
      = moment-curve ideal — is CA_n restated, not reduced. The first step
      (Schur expansion + primary decomposition at n = 4,5,6) re-derives the
      Gröbner wall the run already owns without adding a new handle. The
      S_n-equivariant geometry of the diagonal is a description of the answer,
      not a proof of it.
first-step: For n = 4,5,6 compute over Q: (1) the Schur-function (or monomial-symmetric)
    expansion of each R_i viewed in root space, confirming each is S_n-invariant; (2) the
    ideal I = (R_1,...,R_{n-1}) in Q[a_1,...,a_n], its radical-membership test against
    the moment-curve ideal (a_j - C(n,j) t^j), and its primary decomposition — establish
    rad(I) = (a_j - C(n,j) t^j) in these degrees as the concrete form of the reformulation.
```

## Char-p break (admissibility)

The symmetric product Sym^n(A^1) and its diagonal are characteristic-free, so this
framing alone cannot separate char 0 from char p. The step that must break: the claim
`rad(R_1,...,R_{n-1}) = moment-curve ideal` is **false** over F_p (the witness x^{p+1}-x^p
is an extra point of the variety off the moment curve), so the reduction
Sym^n(F_p) must have the resultants acquiring a *different* radical mod p. The char-0
ingredient the argument would need is a flatness/regularity statement (the sequence R_i
being a regular sequence over Z, or the moment-curve ideal being the saturation of (R_i)
only after inverting the bad primes) — i.e. the argument must be carried over Z and the
bad primes must appear as the primes where the radical grows. That is the claim to check,
not assume.

## Honest status

Speculative. The "Schur/plethysm structure forces the radical" bridge has no known
theorem behind it yet; the concrete, checkable content in the first step is the
reformulation `rad(I) = moment-curve ideal` at small n, which is a *restatement* of CA_n
until a representation-theoretic reason for it is produced. Distinct from
`root-difference-coloring` (which works per root, H_i f(β_j) = e_{n-i}(β_j - β_*)):
this works on the *global* symmetric-function ideal and its S_n-module structure, and
distinct from `milnor-local-multiplicity` / Ghosh's complete intersection (which is
regularity of a sequence, not the S_n-equivariant geometry of the diagonal).

## Decision (converging pass)

status: refuted
killed-by: no load-bearing inference survives grounding. Springer theory /
      equivariant cohomology of the flag variety describes Sym^n(A¹) and its
      diagonal (a true, sourced description of the *space*), but no theorem of
      that theory says anything about the radical of the particular ideal
      (R_1,…,R_{n−1}): the "S_n-module structure forces the radical" bridge has
      no statement behind it, and its only concrete content — rad(R_1,…,R_{n−1})
      = moment-curve ideal — is CA_n restated, not reduced. The first step
      (Schur expansion + primary decomposition at n = 4,5,6) re-derives the
      Gröbner wall the run already owns without adding a new handle. The
      S_n-equivariant geometry of the diagonal is a description of the answer,
      not a proof of it.
