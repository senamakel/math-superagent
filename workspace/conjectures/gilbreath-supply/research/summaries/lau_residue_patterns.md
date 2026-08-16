# Summary — Residue Class Patterns of Consecutive Primes

Source: Cheuk Fung Lau, arXiv:2409.12819 (2024).
Full text: `research/sources/lau_residue_patterns.full.md`
Source URL: https://arxiv.org/pdf/2409.12819

## What this source establishes

The most current strong statement about which residue-class *patterns* of
consecutive primes occur infinitely often. Define an m-tuple a ∈ ((Z/qZ)×)^m
"good" if infinitely many runs of m consecutive primes realize it. Dickson/HL
predict every pattern is good. Current unconditional knowledge:

- Shiu: the constant pattern (a,…,a) is good for any a.
- Dirichlet + Shiu: at least m·φ(q) patterns of length m are good.
- **Even a single non-constant pattern of length m is beyond reach** (the paper
  states this explicitly).
- New result: if q is squarefree and φ(q) ≫ (log m)^10, then ≥ m/(log m)^10 ·
  φ(q)^2 residue-class patterns of length m occur infinitely often (a
  higher-moment Maynard–Tao sieve).

## Why it matters for SUPPLY

This is the cleanest modern statement of how far we are from the mod-4 switch
density. For SUPPLY's reduction we would need the (1,3) and (3,1) patterns (q=4,
m=2) to have positive asymptotic frequency (or at least to occur with positive
density). The paper's own emphasis — that producing even *one* non-constant
2-term pattern (i.e. one consecutive pair p_n, p_{n+1} with p_n ≢ p_{n+1} mod 4
that occurs infinitely often) is beyond current methods — is the exact statement
of the parity barrier the problem describes. The constant patterns (1,1),(3,3)
are known good (Shiu); the non-constant patterns (1,3),(3,1) are not even known
to occur infinitely often.

## Evidence class

Proved theorem (conditional on standard sieve hypotheses as stated; the
non-constant-pattern difficulty is the paper's explicit statement of the current
state).

```claim
id: lau-nonconstant-pattern-open
statement: Even a single non-constant residue-class pattern of consecutive primes of length
  m — in particular a 2-term pattern like (1,3) or (3,1) mod 4 — is not known to occur
  infinitely often. Constant patterns (a,…,a) are good (Shiu); the non-constant ones are
  beyond current methods.
hypotheses: —
holds-here: true and directly relevant: the differing-residue consecutive-pair side that
  SUPPLY's switch-density reduction needs is precisely the non-constant 2-term pattern, which
  is open.
status: asserted-by-source (the paper says even one non-constant pattern is beyond reach).
bearing: the strongest available statement of the parity barrier. Motivates the run's
  central question: can the fold Φ prove SUPPLY from a weaker input than positive switch
  density, i.e. without needing the non-constant pair frequency?
anchor: Lau 2024, abstract and §1.
```

```claim
id: lau-pattern-count-bound
statement: For q squarefree with φ(q) ≫ (log m)^10, at least ≫ m/(log m)^10 · φ(q)^2
  residue-class m-tuples occur infinitely often among consecutive primes.
hypotheses: q squarefree, m large, higher-moment Maynard–Tao sieve.
holds-here: NO — the theorem's hypotheses fail exactly where SUPPLY needs them. The
  switch-density input requires the modulus 4 = 2^2, which is NOT squarefree, so the
  Lau count bound does not apply at q=4, m=2. It cannot supply the arithmetic input
  (it does not even bound the q=4 pair counts). This is the "true theorem whose
  hypotheses fail here" case: usable only as context, never as the switch input.
status: proved (Lau 2024).
bearing: context for how the set of good patterns grows; does NOT settle and does NOT
  apply to the (1,3)/(3,1) mod 4 switch — the modulus is not squarefree.
anchor: Lau 2024, Theorems 1.5, Corollaries 1.6–1.8.
```
