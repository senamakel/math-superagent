# Summary — Strings of Congruent Primes

Source: D. K. L. Shiu, *J. London Math. Soc.* 61 (2000) 359–373.
Expository companion: `research/sources/shiu_strings_expository.full.md`.
Source URL: https://doi.org/10.1112/s0024610799007863

## What this source establishes

Proves Chowla's conjecture in full: for any modulus q ≥ 3 and residue a with
(q,a)=1, there are infinitely many pairs of consecutive primes p_n, p_{n+1}
with both ≡ a (mod q). More: for any k there are arbitrarily long *strings* of
k consecutive primes all ≡ a (mod q). For the "special" residue classes
A+ = {a : ∀p|q, a ≡ 1 mod p} and A− = {a : ∀p|q, a ≡ −1 mod p} the string can be
chosen with the largest prime < x and length k ≥ (log log x / log log log x)^{1/φ(q)}.
For general (q,a)=1 slightly weaker.

**For q=4, a=1 or a=3:** both are in A±. So there are arbitrarily long runs of
consecutive primes all ≡ 1 (mod 4), and arbitrarily long runs all ≡ 3 (mod 4).
In the bit string h[j] = ((q_{j+1}−q_j)/2) mod 2 used by this run, a run of
consecutive primes all ≡ 1 (mod 4) is a run of 0s and a run all ≡ 3 (mod 4) is a
run of 2s-reduced (h=0). Directly: **arbitrarily long all-zero runs in h**.

## Why it matters for SUPPLY — door 5

This is the source for the "no long constant runs" hypothesis being false for
the primes. Door 3 (no long constant runs) is refuted by exactly this: Shiu
gives arbitrarily long runs of consecutive primes in one residue class mod 4,
hence arbitrarily long constant runs in h. So SUPPLY cannot rest on h having no
long runs.

Also the equal-residue (a,a) consecutive-pair frequency is bounded below by this
result (infinitely many, indeed strings of arbitrary length). But the bound is a
lower bound on the *equal* side — the wrong direction for the switch density
(non-equal side) that the reduction needs.

## Evidence class

Proved theorem.

```claim
id: shiu-string-theorem
statement: For every modulus q ≥ 3 and (q,a)=1, there exist arbitrarily long strings of
  consecutive primes all congruent to a mod q. For a ∈ A± the length can be taken
  ≥ (log log x / log log log x)^{1/φ(q)} with largest prime < x.
hypotheses: q ≥ 3, (q,a)=1.
holds-here: true; for q=4, a=1,3 both in A±. Hence arbitrarily long all-zero runs (and
  arbitrarily long all-2 runs) in the prime gap-parity string.
status: proved (Shiu 2000).
bearing: refutes door 3 (no long constant runs) — a hypothesis SUPPLY cannot use. Also gives
  the lower bound on the equal-residue pair frequency, the wrong direction for switch
  density.
anchor: Shiu 2000, Theorems 1–2; expository note Thm 1.1.
```
