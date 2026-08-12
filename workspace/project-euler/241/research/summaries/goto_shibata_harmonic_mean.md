# Goto & Shibata — All numbers with integral harmonic mean up to 300 (Math. Comp. 2004)

Source: https://www.ams.org/journals/mcom/2004-73-245/S0025-5718-03-01554-0/S0025-5718-03-01554-0.pdf
— `[[goto_shibata_harmonic_mean.full]]` (Math. Comp. 73(245) (2004), 475–491; peer-reviewed,
AMS-hosted.)

## What it is

The definitive computation of **harmonic numbers** — n whose divisor harmonic mean
H(n) = n·τ(n)/σ(n) is an integer. All 280 such n with H(n) ≤ 300 are listed; all are even
except n=1; three months of computer search (Mathematica) was needed.

## Why it belongs in this library (adjacent theory, method confirmation)

- H(n) and the abundancy index I(n)=σ(n)/n are multiplicative siblings. The paper's
  Lemma 2.1 derives the *same* multiplicative + monotone structure the run's DFS uses:
  H(nm)=H(n)H(m) for coprime n,m; H(p^e) < H(p^f) < H(q^f) for e<f, p<q. This
  monotonicity is precisely why the denominator-cancellation DFS can prune (adding a
  prime power moves the index monotonically).
- **Theorem 1.2 (Cohen):** for any fixed integer c there are *only finitely many* n with
  H(n)=c — the finiteness theorem for fixed integer divisor-mean, the multiply-perfect
  analogue of the (conjectural) finiteness of fixed half-integer abundancy sets. Supports
  the run's expectation that each target r/2 contributes finitely many n below 10^18.
- Documents the standard *computational attack shape* for this whole family of
  divisibility-of-σ equations: bound the prime-power shape, prune monotonically, enumerate
  the survivors. Same shape as Flammenkamp's tree-search and the run's DFS.
- All harmonic numbers ≤ 300 are even (except 1) — the same parity phenomenon the run
  relies on for hemiperfects (Lemma 4.1: if H(n) is even then n is even).

## What it lets this run do

Confirms from the peer-reviewed computational literature that the multiplicative monotone
pruning DFS is the correct standard technique for σ-ratio enumeration to huge bounds, and
that fixed-ratio sets are expected finite. No numeric value below 1e18 for the half-integer
problem is affected; the harmonic/hemiperfect sets are distinct.

## Does not settle

Harmonic numbers ≠ hemiperfect numbers (different ratio integrality: nτ/σ vs σ/n). The
specific n ≤ 10^18 half-integer solutions and their sum remain the run's computation.

```claim
id: goto-shibata-multiplicative-monotone-method
statement: H(n)=n*tau(n)/sigma(n) is multiplicative and monotone (Lemma 2.1: H(nm)=H(n)H(m) for coprime factors; H(p^e)<H(p^f)<H(q^f) for e<f and p<q; H(p^a q^b) ordered by exponent sorting), and for fixed c only finitely many n have H(n)=c (Cohen), while all harmonic n with H(n)<=300 are even except 1 — the same multiplicative-monotone parity structure the run's denominator-cancellation DFS uses.
hypotheses: standard divisor-function identities
holds-here: yes
status: sourced (peer-reviewed Math. Comp. 2004)
bearing: peer-reviewed confirmation that multiplicative/monotone pruning DFS is the standard complete method for sigma-ratio enumeration, and that fixed-ratio solution sets are finite
anchor: research/sources/goto_shibata_harmonic_mean.full.md
```