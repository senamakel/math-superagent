# Liu, Zhou, "Eigenvalues of Cayley graphs" (Electronic J. Combinatorics, Dynamic Survey, 2022)

URL: https://doi.org/10.37236/8569

## What it establishes

The n-cube Q_d = Cay(Z_2^d, {e_1,…,e_d}). The characters of Z_2^d are
chi_a(x) = (−1)^{⟨a,x⟩}, a ∈ Z_2^d. For a Cayley graph the eigenvalue at
character a is the character sum, giving the **adjacency spectrum of Q_d**:

    lambda(a) = Σ_{s∈S} chi_a(s) = Σ_{i=1}^d (−1)^{a_i} = d − 2w(a),

so the eigenvalues are d, d−2, d−4, …, −d, with eigenvalue d−2i of
multiplicity C(d,i) for i = 0..d.

## Why it is here / relevance

This is the primary spectral fact the run's √n re-derivation rests on, laid over
the cube. The **unsigned** adjacency has spectrum d − 2i (largest eigenvalue d);
the **signed** adjacency A_n with A_n² = nI (used in the max-degree argument) is
a Hadamard-style ± sign assignment over the same edges, and its spectrum
collapses to ±√n, each of multiplicity 2^{n-1}. Having the base binomial
spectrum with provenance (via characters) lets the signed construction be
checked against a known primary statement instead of taken on trust. Also
matches the tensor/NEPS structure Q_d = K_2 □ … □ K_2.

## claim block

```claim
id: hypercube-adjacency-spectrum-cayley
statement: The adjacency matrix of Q_d has eigenvalues d − 2i (i = 0..d), each
  of multiplicity C(d,i); equivalently lambda(a) = d − 2w(a) over a in Z_2^d
  via chi_a(s) = (−1)^{⟨a,s⟩}.
hypotheses: Q_d as Cay(Z_2^d, {e_1..e_d}); group characters of Z_2^d.
holds-here: yes. The run's signed A_n (A_n^2 = nI) has spectrum +-sqrt(n) for
  every n (exactly verified n=1..8, huang_spectral.captured.txt), consistent
  with — and a sign-colouring of — this binomial base spectrum.
status: asserted-by-source (standard character method; also matches the tensor
  product structure and the run's own spectral computation)
bearing: fixes the unsigned spectrum and multiplicities; clarifies that the
  sqrt(n) of the max-degree argument comes only from the sign/Hadamard choice,
  not from the plain adjacency (whose largest eigenvalue is d).
falsifies: any claim that the plain unsigned adjacency of Q_d has an eigenvalue
  larger than d, or that d−2i has multiplicity other than C(d,i).
anchor: research/sources/liu-zhou-eigenvalues-cayley-2022.md
```

Confirms, at the primary-spectral level, the base spectrum the run's signed
interlacing argument colourings.
