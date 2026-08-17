# Berger, "The Casas-Alvero Conjecture" (ENS Lyon course handout, CApromys.pdf)

Source: https://perso.ens-lyon.fr/laurent.berger/autrestextes/CApromys.pdf · Full text:
`research/sources/berger_ens-lyon_casas-alvero-cours.full.md` ([[berger_ens-lyon_casas-alvero-cours.full]])

## What this source is

A pedagogical course-project handout (Laurent Berger, UMPA/ENS de Lyon), not a
research paper. It states the conjecture, walks through the resultant and
Hasse-derivative machinery, and restates the known settled classes. Its value to
this run is as an **independent corroboration** of results the run already holds,
not as a source of new theorems.

## Statements it actually establishes

- **Conjecture 1** = the classical CA statement (monic, char 0, ℂ), phrased over ℂ.
- **"It is known for d ≤ 19 as well as any d a prime power or twice a prime
  power."** The librarian has checked (librarian-cycle-2, lines 9–17) that every
  degree ≤ 19 is settled by the union of held families (p^k, 2p^k, and the
  small-degree verifications). So Berger independently asserts `smallest-open-
  degree = 20`; it does not extend the boundary, and it agrees with the run's
  sourced claim `smallest-open-degree` (Castryck–Laterveer–Ounaïes 2012,
  Schaub–Spivakovsky 2024, Wikipedia).
- **Section 4, char p**: defines the i-th Hasse derivative
  H_k P = Σ_j (j choose k) a_j x^{j−k}, notes P^{(k)} = k!·H_k P, and formulates
  the char-p CA hypothesis **in the Hasse formulation** — an independent restatement
  of the run's `hasse-vs-ordinary` resolution (the published lists and this
  course both use Hasse derivatives; the ordinary convention degenerates for
  p < n).
- **Theorem 2** (restated from [BLSW] = Graf-von-Bothmer et al. 2007): if K is
  algebraically closed, p ∤ n, and Question 1 (char-p CA) has a positive answer
  in degree n, then it has a positive answer in degree d = n·p^e for all e ≥ 1.
  This is the Graf-von-Bothmer lift theorem, already held (`settled-classes`).
- **Section 5**: the reduction-mod-p / p-adic-valuation route for degrees p^k,
  2p^k, and (citing [DdJ11], [CS12]) 3p^e, 4p^e, 5p^e with prime exclusions —
  again already held.
- **Exercise 9**: CA equivalent to: for P = X(X−1)(X^{d−2}+…+a_0), some
  A-linear combination of {res(P,P^{(i)})}_{1≤i≤d−1} equals 1 in
  A = ℂ[a_0,…,a_{d−3}] — the resultant/Nullstellensatz formulation, consistent
  with the run's `resultant-reformulation`.

## Hypotheses and whether they hold for this problem

All hypotheses are char 0 (ℂ) for the Conjecture statement; char-p section is the
Hasse formulation. Both match what the run already holds. holds-here: yes.

## Bearing

No new claim. This is a clean, citable, independent source that (a) corroborates
`smallest-open-degree = 20` and (b) independently restates the Hasse char-p
convention. The one phrasing that looked like it might extend the boundary
("d ≤ 19") is exactly the union of held settled families, verified by hand by the
librarian. Do not re-read this source for new content.

```claim
id: berger-smallest-open-degree-20-corroboration
statement: Berger's ENS course handout states CA is known for d <= 19 and any d a prime power or twice a prime power, independently corroborating the run's sourced smallest-open-degree = 20; every d <= 19 is settled by the union of held families (no boundary extension).
hypotheses: char 0 (C for the Conjecture); char-p section uses the Hasse formulation
holds-here: yes
status: asserted
bearing: independent corroboration of smallest-open-degree=20 and of the Hasse char-p convention; no new theorem
anchor: research/sources/berger_ens-lyon_casas-alvero-cours.full.md
answers: smallest-open-degree
```
