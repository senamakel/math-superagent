# C. L. Stewart 2013, *On divisors of Lucas and Lehmer numbers* (Acta Math. preprint)

Source: arXiv:1008.1274 (2010 preprint of Acta Math. 211 (2013) 291–314).
Full text: `research/sources/stewart-2013-divisors-lucas-lehmer-arxiv.full.md`.
Peer version: Acta Math. 211 (2013), DOI 10.1007/s11511-013-0105-y (Project
Euclid, paywalled).

## What it establishes

**Theorem 1.** Let α, β be complex numbers with (α+β)² and αβ non-zero
integers and α/β not a root of unity. There is an effective constant C (in
terms of ω(αβ) and the discriminant of Q(α/β)) such that for n > C,

```
P(Φ_n(α,β)) > n · exp( log n / (104 log log n) )
```

where P(·) is the greatest prime divisor and Φ_n(X) the n-th cyclotomic
polynomial. This is a **largest-prime-factor** lower bound, not a bound on the
*number* ω(Φ_n(α,β)) of distinct prime divisors.

Applied to the problem's `Φ_{4p}(2)` (Lucas/Lehmer term with n = 4p), it bounds
how large the *largest* primitive divisor must be — it says nothing about how
many distinct prime divisors `Φ_{4p}(2)` has.

## Why it matters for this run

This is **reference [13] of Maciejewski arXiv:2605.20475** and the entire
Stewart-tradition anchor for the paper's hypothesis **(H2)** —

`ω(Φ_{4p}(2)) ≥ C log p` — is *not* a current theorem. Stewart's program
(T1977, T2013) gives `P(Φ_n(2)) ≫ n · exp(log n/log log n)` bounds and
`log |Φ_n| ≥ (φ(n)/2) log |α|` (Lemma 7), but "a primary-source effective
lower bound of the form ω(Φ_n(2)) ≫ log n is, to our knowledge, not in the
literature" — exactly as the paper says. Actually a *trivial* upper bound
`ω(Φ_{4p}(2)) ≤ 2p log 2` always holds; the hard direction is the lower bound,
which this paper does not supply. This confirms the claimed gap is real:
(largest-prime-factor) ≠ (number of prime factors).

```claim
id: stewart2013-largest-prime-factor-not-omega
statement: Stewart (2013) Theorem 1 gives P(Phi_n(alpha,beta)) > n exp(log n / (104 log log n))
  for n > C effective, a LARGEST PRIME FACTOR lower bound on the primitive part of
  Lucas/Lehmer terms; it does not give any lower bound on omega(Phi_n(alpha,beta)),
  the number of distinct prime divisors.
hypotheses: (alpha+beta)^2, alpha*beta nonzero integers; alpha/beta not a root of unity;
  n > C effective.
holds-here: yes -- Phi_{4p}(2) is a cyclotomic/Lucas-type value with these hypotheses
  (alpha/2 or the Aurifeuillean halves are in the right class).
status: asserted by source; not re-derived here
bearing: confirms the paper's (H2) -- omega(Phi_{4p}(2)) >= C log p -- is NOT a
  consequence of the Stewart tradition; (H2) is a conjectural target, not a theorem.
anchor: research/sources/stewart-2013-divisors-lucas-lehmer-arxiv.full.md
answers: why-h2-omega-growth-is-open
```

## Notes

- Lemma 7: `log|Φ_n(α,β)| ≥ (φ(n)/2) log|α|` — the log-mass of the primitive
  part is ≳ n, consistent with the paper's cyclotomic mass identity
  `log Φ_{4p}(2) ~ 2p log 2`.
- Lemma 1: for n > 4, n ∉ {6,12}, Φ_n(α,β) has all prime divisors ≡ ±1
  (mod n) except possibly one small prime dividing n/3 to the first power —
  the structural reason the primitively divisible primes of `2^{2p}+1` are
  ≡ 1 (mod 4p).
- T1977 (Proc. LMS 35 (1977) 425–447) is the sibling paper reference [12];
  not on arXiv, not yet held.
