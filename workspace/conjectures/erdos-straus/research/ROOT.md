# ROOT — what a minimal counterexample looks like, and what is settled

## Structure of a minimal counterexample

Work from the prime reduction (Elsholtz–Tao intro; Wikipedia): it suffices to
consider `n = p` prime, because `f(nm) >= f(n)`, so the smallest
counterexample is prime. A minimal counterexample is therefore a **prime
`p ≡ 1 (mod 24)`**, and more specifically a prime in one of the six open
classes:

```
p ≡ 1, 121, 169, 289, 361, 529   (mod 840)
```

These six are exactly the primitive perfect-square residues mod 840
(`1^2, 11^2, 13^2, 17^2, 19^2, 23^2`). The run's target is `p ≡ 1 (mod 840)`,
i.e. `p = 840k+1` prime.

A minimal counterexample p must have **no** Type-I and **no** Type-II solution
and no neither-type solution. The literature guarantees:

- For **any** odd square (which `p` is not — p is prime), `f_I = f_II = 0`
  (Elsholtz–Tao Prop 1.6). This is why the *squares* are hard — but p is not a
  square, so it is a *possible* positive case.
- No single Mordell-style modular identity can cover `p ≡ 1 (mod 840)` because
  1 is a quadratic residue mod every modulus (Mordell 1967; Wikipedia
  "Nonexistence of identities").
- **The precise polynomial obstruction (Schinzel 2000, Theorem 1)**: if
  `(a,b)=1` and `b` is a quadratic residue mod `a`, then there are **no**
  polynomials `F1,F2,F3 ∈ Z[x]` with positive leading coefficients satisfying
  `4/(ax+b) = 1/F1(x) + 1/F2(x) + 1/F3(x)`. With `a = 840`, `b` one of the six
  open residues — each a square mod 840 — this rules out **any single
  polynomial identity of the standard shape** covering an open class. (Full
  text: `research/sources/schinzel-three-unit-fractions.full.md`.)
- The seven constant-coefficient modular equations are **exhaustive** for
  degree-1 prime polynomials (Salez 2014), so any new family must be a
  genuinely new type, not one of the seven shapes.

## Current verification bound

- `n <= 10^18` (Mihnea & Dumitru, arXiv:2509.00128, 2025 — the [MiDu25]
  citation from erdosproblems #242, now verified from the primary source).
  They extend Salez's modular-filter sieve with the S_29 filter, checking a
  residual set R_8 (2,101,514 classes) modulo G_8 = 25,878,772,920.
- Historical chain (all in library): Straus ≤5000 (1950) → ... → Swett 10^14
  (1999, now on disk via Wayback) → 2×10^14 (2012) → Salez 10^17 (2014) →
  Mihnea–Dumitru 10^18 (2025).
- Oracle should reproduce the Type-I/II + existence logic on small `n` before
  any computation beyond that bound is trusted (see
  `code/verify_library_claims.py`).

## Restricted classes already settled, with hypotheses

1. **even n**: `4/(2m) = 1/m + 1/(2m) + 1/(2m)`. Hyp: `n=2m` even. ALL even n.
   (trivial; verified in `verify_library_claims.py` Claim1a).
2. **n ≡ 3 (mod 4)**: Mordell identity. Hyp: `n ≡ 3 mod 4`. Sourced
   (Wikipedia, Salez Ex 0 eq 14b with A=B=E=1, `D=(n+1)/4`).
3. **n ≡ 2 (mod 3)**: identity `4/n = 1/n + 1/((n+1)/3) + 1/(n(n+1)/3)`.
   Hyp: `n ≡ 2 mod 3`. Sourced (Wikipedia "Modular identities").
4. **n ≡ 2 or 3 (mod 5)**, **n ≡ 3,5,6 (mod 7)**, **n ≡ 5 (mod 8)**: Mordell
   identities. Hyp as stated. Sourced (Wikipedia).
5. Together these five families cover every residue mod 840 except the six
   squares. **All other 834 primitive classes are settled by polynomial
   identities.** (Sourced: Wikipedia, Mordell 1967; to be re-derived by the
   oracle — see `verify_library_claims.py` Claim2.)

## What is NOT settled

The six classes above. The deliverable is a new identity family for one of
them (`r=1` first), or a proof one shape cannot cover `r=1`.

## Bookkeeping / warnings

- `research/sources/pomerance-erdos-straus.full.md` is misnamed: it is the
  ar5iv HTML of the Elsholtz–Tao paper (1107.1010), not Pomerance's survey.
  The real Pomerance survey `esconj.pdf` (math.dartmouth.edu/~carlp) was too
  large to download. Do NOT cite it as Pomerance.
- `research/sources/salez-erdos-straus-new-modular.full.md` is the abstract
  landing page; the full paper is `salez-seven-modular-equations.full.md`.
