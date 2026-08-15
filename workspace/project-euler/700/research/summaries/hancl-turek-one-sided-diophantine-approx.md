<!-- source: https://arxiv.org/pdf/1809.01013 | full text at research/sources/hancl-turek-one-sided-diophantine-approx.full.md -->

# Hančl–Turek: One-sided Diophantine approximations (arXiv 1809.01013, J. Phys. A 52 (2019) 045205)

The authoritative primary treatment of **best lower/upper Diophantine
approximations** of the ℓ-th kind — the exact notion that the Eulercoin record
lows of Project Euler 700 are. This is the classical theorem that ties the
record-low sequence to the continued fraction of α = A/M, replacing the
blog-sourced hand-wave with a proved, citable statement.

## The relevant theorem (Section 4)

Let α = [a₀; a₁, a₂, …] with convergents pₙ/qₙ (recurrences (8), p₋₁=1, p₀=a₀,
q₋₁=0, q₀=1) and semiconvergents (intermediate fractions)

    (pₙ r + pₙ₋₁) / (qₙ r + qₙ₋₁),   0 ≤ r < a_{n+1}.

A fraction p/q < α is a *best lower Diophantine approximation of the second
kind* (BLDA(2)) if among all fractions p′/q′ ≤ α with q′ ≤ q it minimises the
vertical gap q(α − p/q) — equivalently (Remark 4.7) the grid point [q, p] lying
on/below the line y = αx has the smallest vertical distance to the line among
all such points with 0 < q′ ≤ q.

**Theorem 4.5.** (i) The set of best lower approximations of the 1st kind equals
the set of best lower approximations of the 2nd kind; both consist exactly of
the fractions (pₙ r + pₙ₋₁)/(qₙ r + qₙ₋₁) for **odd n**, 0 ≤ r < a_{n+1}.
(ii) The best upper approximations (1st = 2nd kind) are the same fractions for
**even n** except (n,r)=(0,0).

So: **best lower approximations (2nd kind) = convergents + semiconvergents at
which pₙ/qₙ is odd-indexed.** Corollary 4.2 (every BLDA/BUDA of any kind is a
convergent or semiconvergent), Theorem 4.1 (first-kind case), Theorem 4.3 (the
converses). The count of such fractions is finite and small, since there are
a_{n+1} semiconvergents per stage.

## Why it is exactly this run's structure

The Eulercoins are the record lows of c_n = A n mod M (A = 1504170715041707,
M = 4503599627370517, gcd = 1). Writing c_n = A n − M·⌊A n/M⌋, the vertical gap
of grid point [n, ⌊An/M⌋] from the line y = (A/M)x is c_n/M. A record low at n
means c_n is a new minimum — i.e. [n, ⌊An/M⌋] has the smallest vertical distance
to the line among all grid points with x-index < n. These are precisely the
BLDA(2) to α = A/M, which by Theorem 4.5 are exactly the odd-stage convergents
and semiconvergents of A/M. Hence:

- The number of Eulercoins is bounded by (indeed equals) the number of
  convergents + semiconvergents of A/M — a small, finite count (here 102), NOT
  O(M). This is the structural reason a scan to n ≈ 4.5e15 is the wrong method.
- The record-low index recurrence n_{k+2} = ⌈c_{n_k}/c_{n_{k+1}}⌉·n_{k+1} − n_k
  (smsxgz / brob26, claim `eu700-record-low-recurrence`) is the index-level walk
  through this convergent/semiconvergent list; this theorem is the reason that
  list is short and that the recurrence terminates in O(log M) Euclidean steps.

Note the caveat that also applies to the Three Gap source: α = A/M is
**rational**, so formally the theory here (which treats irrational α and is most
nontrivial there) transfers to the rational finite orbit by the same
identification — the grid-point/vertical-distance characterisation (Remark 4.7)
does not depend on irrationality, and the rational claim is the finite analogue.
The record lows are still exactly the BLDA(2), and Theorem 4.5's classification
still lists them among convergents/semiconvergents. This is corroboration and
structure, not an alternative computation: the answer still comes from the
verified recurrence.

```claim
id: eu700-record-lows-are-best-lower-approximations
statement: The record lows (Eulercoins) of c_n = A n mod M, gcd(A,M)=1, are exactly the best lower Diophantine approximations of the second kind to α = A/M (grid points below y=αx with minimal vertical distance to the line). By Hančl–Turek Theorem 4.5 these are exactly the convergents and semiconvergents (p_n r + p_{n-1})/(q_n r + q_{n-1}) of A/M for odd n, 0 ≤ r < a_{n+1}. Hence the number of Eulercoins is the (small, finite) number of such convergents and semiconvergents, not O(M).
hypotheses: A, M positive integers, gcd(A,M)=1, A < M; residues in [0, M). The grid/vertical-distance identification is illustration-free and holds verbatim; the one-sided-approximation classification of Theorem 4.5 holds for the rational α = A/M as the finite analogue of the irrational statement (the vertical-distance definition, Remark 4.7, does not need irrationality).
holds-here: true. A = 1504170715041707, M = 4503599627370517, gcd = 1. There are 102 Eulercoins, matching this structure (the odd-stage convergents/semiconvergents of A/M).
status: sourced — Hančl & Turek, One-sided Diophantine approximations, J. Phys. A 52 (2019) 045205 (arXiv 1809.01013), Theorem 4.5 and Remark 4.7, proved in the source; the identification of Eulercoins with these best lower approximations is this run's inference, corroborated by the verified recurrence and brute-force agreement (102 coins, code/out/solution.txt).
bearing: Structural grounding (now primary-sourced) for the small Eulercoin count and the O(log M) record-low recurrence; classical explanation of why scanning to M is the prohibited method. Not needed to compute the answer (that is eu700-record-low-recurrence), but it is the theorem behind it.
anchor: research/summaries/hancl-turek-one-sided-diophantine-approx.md
```
