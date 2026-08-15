# Liu, Zhou, "Eigenvalues of Cayley Graphs" (Electronic J. Combinatorics — Dynamic Surveys, 2022)

Source URL: https://doi.org/10.37236/8569
(Retrieved via `read_sources`; direct PDF download blocked by network boundary.)

## What this source establishes

The n-dimensional hypercube H(d,2) is the Cayley graph Cay(Z_2^d, S) with
S = {e_1, ..., e_d} the standard basis. The characters of the abelian group
Z_2^d are `chi_a(x) = (-1)^{<a,x>}`, `a in Z_2^d`. For a Cayley graph the
eigenvalues are the character sums

```
lambda(a) = sum_{s in S} chi_a(s) = sum_{i=1}^d (-1)^{a_i} = (d - w(a)) - w(a)
          = d - 2 w(a)
```

where `w(a)` is the Hamming weight of `a`. Concretely:

- **Adjacency spectrum of Q_d:** eigenvalues `d, d-2, d-4, ..., -d`, with
  `d - 2i` having multiplicity `C(d, i)` for `i = 0..d`.

So the eigenvalues are exactly the values `d - 2i` with binomial multiplicities
— the symmetric ± spectrum, largest eigenvalue d (multiplicity 1), smallest -d,
and (when d is even) a multiplicity-`C(d,d/2)` eigenvalue at 0.

This is the standard reference for the method: characters of the abelian group
(= Fourier transform on the Boolean cube), or equivalently the tensor/NEPS
product structure `Q_d = K_2 □ ... □ K_2`.

## Why it is here

This is the primary spectral fact the run's sqrt(n) re-derivation rests on once
its edge signs are laid over the cube. The unsquared adjacency has eigenvalues
`d - 2i`; the *signed* adjacency used in the max-degree argument (A_n with
A_n^2 = nI) is a Hadamard-style sign choice that collapses this to ±sqrt(d),
each with multiplicity 2^{d-1}. Having the base spectrum (with its provenance
via characters) in the library lets that sign-construction be checked against a
known primary statement instead of taken on trust.

## Claim block

```claim
id: hypercube-adjacency-spectrum-cayley
statement: The adjacency matrix of Q_d has eigenvalues d - 2i (i = 0..d),
  each with multiplicity C(d,i). Equivalently lam(a) = d - 2 w(a) over
  a in Z_2^d via the character evaluation chi_a(s) = (-1)^{<a,s>}.
hypotheses: Q_d as Cay(Z_2^d, {e_1,..,e_d}); group characters of Z_2^d.
holds-here: yes. This is the un-signed adjacency spectrum; the run's signed
  adjacency A_n (with A_n^2 = nI) is a ± sign assignment over these edges and
  its spectrum ±sqrt(n) is consistent with this binomial base spectrum.
status: asserted-by-source (Liu–Zhou 2022, standard character method for
  Cayley graphs; also matches Wang 2007 Laplacian result and Balasubramanian's
  binomial-pattern computations).
bearing: fixes the exact spectrum and multiplicities of Q_d; the largest
  eigenvalue is d (not sqrt(d)); the sqrt(d) of the max-degree argument comes
  only from the signed Hadamard matrix, not from the plain adjacency. This
  distinguishes the two spectral objects cleanly for the run.
falsifies: any claim that the plain (unsigned) adjacency of Q_d has an
  eigenvalue larger than d for d >= 1, or that the multiplicity of d-2i is
  not C(d,i).
anchor: doi:10.37236/8569
```
