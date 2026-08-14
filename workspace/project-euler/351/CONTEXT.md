# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

## Established

**The answer.** H(10⁸) = **11762187201804552** (17 digits). Computed and
checked, from Φ(10⁸) = 3039635516365908 via the identity below. Backed by
`code/out/pe351_values.md`, `code/brute.py`, `code/solution.py`,
`code/verify_mobius.py`, `code/out/patterns.py`.

**The identity.** For every n ≥ 1, a point (a,b) of the order-n hexagon
{(a,b) ∈ Z² : |a|,|b|,|a+b| ≤ n} is hidden from the centre iff
gcd(|a|,|b|) > 1 (origin excluded). Six sectors each contribute
C(n+1,2) − Φ(n) hidden points, so

    H(n) = 6·(C(n+1,2) − Φ(n)) = 3n² + 3n − 6·Φ(n),
    Φ(n) = Σ_{k=1..n} φ(k).

Verified against the brute-force oracle at n = 5, 10, 1000 (30, 138,
1177848 — the statement's values) and against OEIS A216453 for n ≤ 20
(computed terms match the catalogue entry via oeis_lookup). The closed form
is the OEIS A216453 formula (Kumar–Israel 2014) = 6·A063985(n).

**Governing theory** (see `research/notes/pe351-governing-theory.md`):
- coprime iff visible: lattice point visible from origin iff gcd = 1
  (MathWorld VisiblePoint; Baake–Grimm–Warrington 1994) — checked against
  a literal no-number-theory scan for n ≤ 8.
- φ = μ ∗ id (ProofWiki; MathWorld TotientFunction eq. 16), so
  Φ(n) = (1/2)Σ_{d≤n} μ(d)⌊n/d⌋(1+⌊n/d⌋) — the Möbius-inversion verification
  route (MathWorld/Wikipedia Totient summatory function).
- Gauss: Σ_{d|n} φ(d) = n, hence Σ_{d≤n} Φ(⌊n/d⌋) = n(n+1)/2 and the
  floor-grouped recursion Φ(n) = n(n+1)/2 − Σ_{d=2..n} Φ(⌊n/d⌋) — the
  sublinear (O(n^{2/3})) route (MathWorld TotientFunction eq. 15; Wikipedia).
- Chai Wah Wu's A063985 recursion (OEIS A063985, Mar 24 2021) — the third,
  sieve-free route; A063985(10⁸) = 1960364533634092, H = 6·A063985.
- Asymptotic anchors: Φ(n) ~ (3/π²)n²; computed ratio Φ(10⁸)/10¹⁶ =
  0.303964 ≈ 3/π²; H(n)/10¹⁶ = 1.17622 ≈ 3(1 − 6/π²).

**Method tier.** `code/solution.py` computes Φ(10⁸) by an exact incremental
totient sieve over int32 (O(n log log n) time, ~400 MB), then H = 3n²+3n−6Φ.
`code/verify_mobius.py` recomputes Φ(10⁸) by Möbius inversion with a separate
int8 μ sieve (shares only the prime list): exact agreement. `code/out/
patterns.py` reaches the same value via the A063985 recursion. Three
independent routes, one integer.

## Ruled out

- **Counting the origin as hidden**: off by exactly 1 (brute force first
  printed 31/139/1177849 before the fix). The origin is visible.
- **Möbius sieve with step p instead of p²** (`mu[p*p::p]=0`): zeroes
  squarefree numbers, broke the Möbius verification at small N; fixed to
  `mu[p*p::p*p]=0`. Recorded in `code/out/fix_mobius_verify.py`.
- **Φ(10⁸) = 303963552391 / 303963552392**: recurring typo in early notes —
  that is Φ(10⁶); the correct value a(8) = 3039635516365908 (A064018,
  two sieves).
- **arXiv:1801.07931 as "Helfgott–Thompson"**: wrong paper (Galton–Watson
  processes); the correct reference is Research in Number Theory 9(1):6
  (2023), stored as `springer-helfgott-thompson-summing-mu.full.md`. The
  corrupted files are marked DO NOT CITE.
- **Spurious order-4 recurrence** for H/A063985: falsified by patterns.py at
  n = 9 over a 200000-term prefix; the mod-4 residue law (A063985(n) odd iff
  n mod 4 ∈ {1,2}) survives and is verified independently.

## Numbers

- H(5)=30, H(10)=138, H(1000)=1177848 — brute force and identity agree at
  every n the oracle reaches (brute.py); H(1..20) matches A216453.
- Φ(10^k) for k = 0..8: 1, 32, 3044, 304192, 30397486, 3039650754,
  303963552392, 30396356427242, **3039635516365908** — reproduced by a naive
  sieve (`code/out/check_library_values.py`) against OEIS A064018, and by
  both big sieves at k = 8.
- Φ(10¹⁹) = 30396355092701331435065976498046398788 (Brown 2025, b-file term
  19) — catalogue, not computed here.
- A063985(10⁸) = 1960364533634092; H(10⁸) = 6·A063985(10⁸) =
  11762187201804552; H(10⁸) mod 12 = 0.
- H(10⁸) = 3·10⁸·(10⁸+1) − 6·3039635516365908 = 30000000300000000 −
  18237813098195448 = 11762187201804552 (check anchor).

## Recalled

Durable memory holds the identity, the oracle values, the two-sieve Φ
agreement, the origin-not-hidden and step-p² lessons (all consistent with
this run's findings), and the librarian's download-overwrite lesson. **One
recalled chunk contains a stale check anchor "11762189901804552"** — a typo
for 11762187201804552; the computed and independently verified value is the
latter (see Contradictions).

## Contradictions

- **Recalled memory vs computation**: a durable-memory chunk from the library
  build report states the check anchor H(10⁸) = "11762189901804552"; the
  correct value is **11762187201804552** (the recalled string would require
  Φ(10⁸) = 3039635496…, contradicting A064018 and both sieves). The recalled
  value is a transcription typo; every program output, the catalogue, and the
  independent recursion agree on 11762187201804552.
- The OEIS A063985 comment says a(n) counts pairs with "1 = gcd(x,y)" — a
  typo in the source for "1 ≠ gcd(x,y)" (the Haskell program `gcd x y > 1`
  and the formula A000217(n) − A002088(n) confirm the intended reading);
  summarized accordingly.

## Gaps

- None blocking: the final answer is computed and cross-checked three ways.
- Optional: an O(n^{2/3}) reimplementation of Φ(10⁸) (Dirichlet hyperbola /
  Gauss recursion, Brown Algorithm 1) would be a fourth, sublinear route;
  approach recorded in `research/approaches/dirichlet-hyperbola-gauss-2-3.md`.
