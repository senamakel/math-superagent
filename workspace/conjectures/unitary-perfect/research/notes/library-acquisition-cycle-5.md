# Library acquisition cycle 5 — frontier-cited primary tier (Higgs origin, explicit Stewart, friable-index)

## What was added this cycle

| Path | What it is | Verdict |
| --- | --- | --- |
| `research/sources/ligh-wall-1987-functions-nonunitary-divisors.full.md` (+ summary) | Ligh & Wall, *Functions of Non-Unitary Divisors*, Fib. Quart. 25(4):333–338 (1987) | **PRIMARY** — the last "cited by 2 sources" frontier item; non-unitary divisor class, `n = n*·n#` squarefree/powerful split (the lens behind Graham 1989), Thm 7: `n#` needs ≥ 2 distinct primes |
| `research/sources/burris-yeats-saga-high-school-identities.full.md` (+ summary) | Burris & Yeats, *The Saga of the High School Identities*, Algebra Universalis 52:325–342 (2004) | **PRIMARY + origin text** — defines the Higgs prime sequences `Σ_a`; `Σ_1 = (2,3,7,43)` finite, `Σ_a` conjecturally infinite for a > 1; the run's `P_3` is exactly `Σ_3` |
| `research/sources/bilu-gun-hong-uniform-explicit-stewart.full.md` (+ summary) | Bilu, Gun & Hong, *Uniform explicit Stewart's theorem on prime factors of linear recurrences*, arXiv:2108.09857v5 (2022) | **PRIMARY (modern explicit Stewart)** — Thm 1.2 rational `n₀=exp(10⁶)`; Thm 1.3 quadratic norm ±1; Prop 8.2 primitive-divisor facts. **Confirms (H2) of the paper is NOT a Stewart consequence** |
| `research/sources/wu-elliott-halberstam-shifted-primes.full.md` (+ summary) | Jie Wu, *Elliott–Halberstam conjecture and values taken by the largest prime factor of shifted primes*, J. Number Theory 206:282–295 (2020), from HAL | **PRIMARY (friable-index family)** — Bombieri–Vinogradov / Brun–Titchmarsh-type estimates for `π(x, y; q, a)` under EH variants; pins the paper's "existing literature does not apply" claim to a held text |

All summaries carry fenced claim blocks (`ligh-wall1987-nonunitary-perfect-construction`,
`burris-yeats-higgs-prime-origin`, `bgh2022-explicit-stewart-prime-factor`,
`wu2020-friable-index-shifted-primes`); all four full texts and summaries indexed.

## Key findings

1. **The origin of the 3-Higgs primes is now primary-sourced.** Burris–Yeats
   define `Σ_a` (with `p₁ = 2`, `(p_{i+1}−1) | (p₁⋯p_i)^a`) as the classification
   invariant of finite quotients of the exponentiation algebra. `Σ_1 = (2,3,7,43)`
   is **finite** — the exponent cap matters: the greedy exponent-1 sequence dies
   at 43, while a ≥ 2 is conjecturally infinite. The run's `P_3 = Σ_3`. This
   upgrades `hb-defs-3higgs-heven` from OEIS-digest-only to origin-text.

2. **Stewart's theorem is a largest-prime-factor theorem, not an ω bound.**
   BGH Thm 1.2/1.3 give, for `γ^n − 1`, a prime divisor `p ≥ n·exp(c log n/log log n)`.
   For `γ = 2, n = 4p` this bounds the largest prime factor of `2^{4p}−1`, i.e.
   of `Φ_{4p}(2)`, but says nothing about the *number* `ω(Φ_{4p}(2))` of distinct
   prime divisors. This is exactly why the paper's hypothesis (H2)
   (`ω(Φ_{4p}(2)) ≥ C log p`) is "not a current theorem" — the Stewart tradition
   cannot supply it. The run's `hong-stewart-nonprimitive-bound` claim now has
   its explicit quantitative anchor.

3. **The "existing literature does not apply" demarcation is primary-verified.**
   Wu 2020 (and the Liu–Wu–Xi family it represents) bounds the *ambient* count
   of primes in friable-index progressions. Friable = size-cutoff smoothness;
   the run's semigroup `S_3^(≤3)` is defined by recursive prime chains + exponent
   caps. No held source transfers counts of ambient primes to the prime-divisor
   set of a fixed `Φ_{4p}(2)` — the "divisor-transference" gap is real and unmet,
   confirming the paper's central analytic claim.

4. **The dangling MathWorld anchor is fixed.** `qr-2-quartic-criterion` and the
   MathWorld biquadratic summary previously anchored to
   `research/sources/mathworld-*.full.md` which never existed; both now anchor to
   the summary files (the download manager keys the URL to them and refuses a
   second fetch). No claim references a non-existent file.

## Not obtained (recorded, not repeated)

- **Frei 1978** — captcha wall at e-periodica (`pid=edm-001:1978:33::216`,
  Heft-4 Kleine Mitteilungen pp. 90–96). OEIS A002827 still the only record of
  the theorem (m ≥ 144, ω ≥ 144, n > 10^440). REQUESTS row 1 stays OPEN.
- **Goto 2007** — paywalled at Project Euclid (RMJM 37(5):1557–1576). MaRDI
  item Q2478044 records `N < 2^(2^k)` (UPN) and `N < (2^(2^k))^k` (UHN).
  REQUESTS row 2 stays OPEN.
- **Liu–Wu–Xi 2017/2020 arXiv preprint** — no arXiv ID surfaced; the published
  Sci. China Math. (2020) version is paywalled, but the run now holds Wu 2020
  from HAL, the directly adjacent primary.

## Library shape after this cycle

The frontier's multi-cited rows are now all held. Held tiers: origin/definition
(Burris–Yeats, OEIS A057447), canonical head (Subbarao–Warren 1966, Wall 1975,
Graham 1989, Wall 1987/1988), branch target (Maciejewski 2026 full text),
analytic machinery (BGH 2022 explicit Stewart, Hong 2022, Ford 2014, FKL 2010,
BHV 2001), divisor-class neighbours (Wall 1972, Cohen 1990, Ligh–Wall 1987,
Hagis 1984/1985/1987), reciprocity (Williams 1976, Dummit, Wikipedia,
MathWorld), lookups (Cunningham 2± tables + Appendix C + 1-side, OEIS
A002827/A057447), context (Guy 2nd/3rd ed., Handbook of Number Theory II,
Encyclopedia of Math).

Frei 1978 remains the single RN open row with real content value; it is
captcha-walled at the only known free host and cannot be fetched with the
current tooling.