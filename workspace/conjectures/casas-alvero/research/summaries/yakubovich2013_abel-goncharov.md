# Yakubovich, *Abel-Goncharov's polynomials and the Casas-Alvero conjecture* (2013, arXiv:1308.5320)

<!-- source: https://arxiv.org/pdf/1308.5320 | PDF held in full -->

## What this source is

The primary statement of the Abel–Goncharov / interpolation machinery that this
run's **adopted** root-difference-coloring approach explicitly rests on. Earlier
in the chronology than the held Yakubovich 2015 validity preprint (1504.00274);
this 2013 paper is where the Abel–Goncharov reformulation of CA is set out, with
bounds, integral and "genetic sum" representations, Sz.-Nagy identities, and
Laguerre/Obreshkov–Chebotarev inequalities for the roots of a polynomial and its
derivatives.

## The load-bearing identification (the link to root-difference-coloring)

Let f be monic degree n, with common-root sequence z_0,…,z_{n−1}, where
z_m is a common root of f and its m-th derivative, f^{(m)}(z_m)=0, and
z_0 ∈ {distinct roots}. Write f(z) = z^n + P_{n−1}(z). Differentiating m times
and evaluating at z_m gives the **Abel–Goncharov interpolation problem**

    P^{(m)}_{n−1}(z_m) = − (n!/(n−m)!) z_m^{n−m},  m = 0,…,n−1,

a triangular linear system with unique solution. Its solution is expressed via
the system of Abel–Goncharov polynomials G_k(z):

    P_{n−1}(z) = − Σ_{k=0}^{n−1} (n!/(n−k)!) z_k^{n−k} G_k(z)

and the Abel–Goncharov interpolation polynomial is

    G_n(z,z_0,…,z_{n−1}) = z^n + P_{n−1}(z) = f(z).

**So a CA-polynomial f is exactly an Abel–Goncharov interpolation polynomial
G_n at the nodes z_m = (a common root shared by f and f^{(m)}).** This is the
precise statement the root-difference-coloring approach uses when it evaluates
H_i(f) = e_{n−i}(x−β_*) at root differences.

## Properties of G_n used downstream

- **Multiple-integral representation**: G_n(z) = n! ∫_z0^z ∫_{z1}^{s1} … ∫_{z_{n−1}}^{s_{n−1}} ds_n…ds_1.
- **Homogeneity**: G_n is a homogeneous function of degree n:
  G_n(αz, αz_0,…,αz_{n−1}) = α^n G_n(z,z_0,…,z_{n−1}). This is exactly the
  weighted-scaling invariance the run's scheme formulation exploits.
- **Goncharov bound**: |G_n(z)| ≤ (|z−z_0| + Σ_{s=0}^{n−2} |z_{s+1}−z_s|)^n.
  This bound is the engine behind the real-rooted / span arguments (Lemma 8's
  lower bound on span, Proposition 2 real-rooted case).

## Statements bearing on CA (real-rooted / span results)

- Cor 2: f degree n≥3 with ≥2 distinct roots whose (n−2)-nd derivative has a
  double root has ≥1 complex root.
- Lemma 8: with common roots λ_1 (of f^{(n−1)}), λ_2 (of f^{(n−2)}),
  multiplicities r_1, r_2 with r_1+r_2<n, a lower bound on span(f).
- Proposition 2: CA holds for polynomials with only real roots (under the
  listed conditions).
- Cor 9: no real-rooted CA-polynomial with a non-increasing common-root
  sequence {x_ν}; Cor 10: no real-rooted CA-polynomial with each x_ν a maximal
  root of f^{(ν)}.

## Status

Preprint (2013). Not peer-reviewed as its own publication; the results feed the
2014 J. Classical Analysis paper "Polynomial problems of the Casas-Alvero type"
(10.7153/jca-04-07) and the 2015 validity preprint. The full-CA claim in 2015
did not become an accepted resolution; the machinery here (Abel–Goncharov
identification, integral representation, homogeneity, span bounds) is the
durable contribution and is what this run relies on, not the full-CA claim.

## Bearing on this run

Fills the library's thinnest spot: the **primary statement** of the
Abel–Goncharov theory that the adopted root-difference-coloring approach names
as its engine. In particular it supplies:
1. The exact node-identification f = G_n(z, z_0,…,z_{n−1}) (the "shared
   root" sequence IS the interpolation node sequence).
2. The multiple-integral representation, which gives a second independent
   route to the root-difference/results.
3. The homogeneity G_n(αz,…)=α^n G_n — grounds the scaling-weight
   degeneration the scheme argument uses.
4. The Goncharov bound — the analytic content that mirrors (and in real-
   rooted cases substitutes for) the Gauss–Lucas convex-hull step the char-p
   break analysis says is missing.
