# Bloom & Elsholtz, "Egyptian Fractions" (survey) — the modern reference

Source: https://arxiv.org/abs/2210.04496 (arXiv:2210.04496v1, 10 Oct 2022);
published as T. F. Bloom and C. Elsholtz, "Egyptian fractions", Nieuw Archief
voor Wiskunde (5) 23 (2022), 237–245.
Full text: `research/sources/bloom-elsholtz-egyptian-fractions-survey.full.md`

## What it establishes (sourced, primary survey)

**Theorem 1 (ESC ⇔ covering by two congruence-class families).** The
Erdős–Straus conjecture is equivalent to: every prime p lies in at least one of
the congruence classes

```
p ≡ −a/c  (mod 4acd − 1)      for some a, c, d ≥ 1,        or
p ≡ −(4c²d + 1)/k  (mod 4cd)  for some c, d, k ≥ 1 with k | 4c²d + 1.
```

Proof (in full text, two directions):
- If `p ≡ −a/c (mod 4acd−1)`: `cn + a = (4acd−1)b`, then
  `4/n = 1/(abd) + 1/(acdn) + 1/(bcdn)`.
- Necessity: from a solution `4/p = 1/x+1/y+1/z`, `x ≤ y ≤ z`, one shows
  (greatest-common-divisor argument) that either (1) `x=abd, y=acdp, z=bcdp`
  giving `4abcd = a + b + cp` so `p ≡ −a/c (mod 4acd−1)`, or
  (2) `x=abd, y=acd, z=bcdp` giving `4abcd = a + (b+c)p`, and with
  `b+c = ak`: `kp + 1 = 4cd(ak − c)`, so `k | 4c²d+1` and
  `p ≡ −(4c²d+1)/k (mod 4cd)`.
- The proof gives, in case (2), the explicit solution
  `4/p = 1/(ad(ak−c)) + 1/(acd) + 1/((ak−c)cdp)`.
- Similar statements in Nakayama (1939), Rosati (1954), Mordell (1969).

**Other established facts in the survey.**

- **Stewart's two-term criterion**: reduced `m/n` is a sum of two unit
  fractions iff there are coprime divisors n₁, n₂ of n with m | n₁ + n₂. For
  m = 4 this implies 4/n is a sum of two unit fractions for almost all n (all
  but those n whose prime factors are all ≡ 1 mod 4).
- **Vaughan (1970)**: at most `N exp(−c (log N)^{2/3})` exceptions n ∈ [1,N],
  some absolute c > 0 (the 2/3 exponent confirmed from primary survey; uses
  Bruno–Titchmarsh, Bombieri–Vinogradov, and that the number of soluble
  classes mod `4t−1` is `d₃(t)`).
- **Schinzel (2000)**: no polynomial identity `4/(ax+b) = 1/F₁+1/F₂+1/F₃`
  (Fᵢ ∈ Z[x], positive leading coefficients, m ≡ 0 mod 4) exists when b is a
  quadratic residue mod a. Quote: "there is no such formula for n = 4t + 1."
- **Modulo-840 statement**: "modulo 840 only the congruence classes
  1, 49, 121, 169, 289, 361 are not generally solved" — see Contradictions
  in CONTEXT.md: this list has 49 (non-primitive: 7 | 49) and omits 529;
  this run's verified list is {1,121,169,289,361,529}.
- **Counting**: `Σ_{p≤N} f(p) = N (log N)^{2+o(1)}` (Elsholtz–Tao),
  `f(n) ≥ (log n)^{log 6 + o(1)}` for almost all n (Elsholtz–Planitzer,
  Proc. R. Soc. Edinb. A 150 (2020) 1401–1427), `f(n) ≤ n^{3/5+o(1)}`.
- **Parametric structure**: for prime n = p, a solution
  `m/n = 1/x₁+1/x₂+1/x₃` has each tᵢ ∈ {1, p} (gcd bookkeeping), leaving
  4 free parameters; general k-term solutions of `m/n` have 2ᵏ−k−1 free
  parameters (Dedekind's idea).
- Elsholtz (2001): `E_{m,k}(N) ≤ N exp(−c_{m,k} (log N)^{1 − 1/(2^{k−1}−1)})`.

## Consequence for this run

Theorem 1 is the *parametrisation in congruence-class form*: it turns a
3-term solution for 4/p into one of two finite-parameter families of classes.
The first family (p ≡ −a/c mod 4acd−1) is the "Mordell/Rosati" shape; the
second (k | 4c²d+1) is the Type II shape Chamberland (Integers 2026, in
library) re-derives as `p = qr − 4s₁s₂`. An ansatz search should test shapes
directly in these two forms — the survey's proof shows *any* prime solution
must fall into one of them, and which one is decidable from the gcd bookkeeping.

```claim
id: bell-esc-equivalence-congruence-classes
statement: The Erdős–Straus conjecture holds iff every prime p lies in a class p ≡ −a/c (mod 4acd−1) for some a,c,d ≥ 1, or p ≡ −(4c²d+1)/k (mod 4cd) for some c,d,k ≥ 1 with k | 4c²d+1. Necessity: from any solution 4/p = 1/x+1/y+1/z with x≤y≤z, either (x,y,z) = (abd, acdp, bcdp) giving the first class, or (abd, acd, bcdp) giving the second; sufficiency gives explicit unit-fraction representations in both cases.
hypotheses: p prime; x ≤ y ≤ z ordering.
holds-here: true — this is the parametrisation in the form the ansatz search should use; it is a complete characterisation for prime n, and primes suffice.
status: asserted (survey Theorem 1 with full proof reproduced in the full text; attributed to Nakayama 1939, Rosati 1954, Mordell 1969).
bearing: THE structural route from solutions to congruence classes; both families are finite-parameter and polynomial, so any family covering n ≡ 1 (mod 840) must specialise into these forms or use non-prime n machinery.
anchor: research/sources/bloom-elsholtz-egyptian-fractions-survey.full.md
```

```claim
id: bell-mod840-list-discrepancy
statement: The Bloom–Elsholtz survey lists the unsolved classes mod 840 as {1, 49, 121, 169, 289, 361}, whereas this run's verified list (code/verify_library_claims.py, Mordell/classical identities) is {1, 121, 169, 289, 361, 529}.
hypotheses: none.
holds-here: n/a — a bibliographic contradiction to record.
status: asserted (survey text vs this run's computation); 49 is non-primitive (gcd(49,840)=7) and 529 = 23² is a primitive square, so the survey list reads as a typo for {1,121,169,289,361,529}.
bearing: never cite the survey's 49 as an open class; cite the verified list.
anchor: research/sources/bloom-elsholtz-egyptian-fractions-survey.full.md
```