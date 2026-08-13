# Salez — "The Erdős–Straus conjecture: New modular equations and checking up to N=10^17"

Serge E. Salez, arXiv:1406.6307 (24 Jun 2014), 13 pp. + French version + C++ program.
Sources: `research/sources/salez-seven-modular-equations.full.md` (arXiv HTML v1,
50 KB) and `research/sources/salez-erdos-straus-new-modular-pdf.full.md` (arXiv PDF,
32 KB, complete text).

## What the paper establishes

**Purpose.** In 1999 Swett checked the conjecture to `N = 10^14` (150 h) with a
sieve from a single modular equation. This paper proves there is a *complete* set
of **seven** modular equations (three of them new), and gives an optimised sieve
based on them; runtime a few minutes at `10^14` and ≈16 h at `10^17` on a 2009
AMD Turion II.

**Reduction to `n ≡ 1 (mod 24)` (§1.1).** Identities solve `n ≡ −1 mod 3`,
`n ≡ −1 mod 4`, `n ≡ −3 mod 8` (respectively `4/(3t−1)`, `4/(4t−1)`,
`4/(8t−3)`), and if `4/n` is solvable so is `4/(kn)`. Hence it suffices to solve
**primes `p ≡ 1 mod 24`**. (This rests on the standard prime reduction.)

**Rosati parametrisation (Prop 1, attributed to Rosati 1954, not Mordell — Salez
explicitly warns against "Mordell's theorem/formulas").** For an odd prime `p`,
`4/p` is 3-Egyptian iff ∃ positive `A,B,C,D` with
- **(Type I / eq (1))** `4ABCD = A + B + pC`, `(ABD, p) = 1`, or
- **(Type II / eq (2))** `4ABCD = p(A+B) + C`, `(ABCD, p) = 1`.

The `E,F` shorthand (§1.3) gives `C | A+B`, `E=(A+B)/C`, `FE = 4B²D + p (or 1)`.

**The complete set of seven modular equations (Prop 3, Lemma 1, Cor 1).** For `p`
a degree-1 prime polynomial, `4/p` is 3-Egyptian iff one of exactly seven
constant-coefficient equations holds:
- case (1): **(14a)** `B + pC ≡ 0 mod 4BCD−1`; **(14b)** `p + E ≡ 0 mod 4AB` and
  `A+B ≡ 0 mod E`; **(14c)** `p + E + 4B²D ≡ 0 mod 4BDE`;
- case (2): **(15a)** `pE + 1 ≡ 0 mod 4AB` and `A+B ≡ 0 mod E`; **(15b)**
  `p + F ≡ 0 mod 4BC` and `pB + C ≡ 0 mod F`; **(15c)** `p + F ≡ 0 mod 4BD` and
  `4B²D + 1 ≡ 0 mod F`; **(15d)** `p + F ≡ 0 mod 4CD` and `p² + 4C²D ≡ 0 mod F`,
  with `(A,B)=(B,C)=(C,D)=(4ABD,E)=(4BCD,F)=1`.

History of the seven: Rosati (1954) gave (14a),(15a); Yamamoto (1965) gave
(14a),(14b),(15a),(15b); **the three new ones are (14c), (15c), (15d)**. The
"completeness" statement is for degree-1 prime polynomials: if a modular equation
`n ≡ b mod a` is not equivalent to one of the seven, then `4/(at+b)` cannot be
3-Egyptian. **For integers this completeness does NOT hold** — an integer `n` could
still be solved by a yet-unknown process (Salez's words: "a still unknown new
type"). This is the precise status of the modular-equation approach: exhaustive
for polynomial classes, open for ad hoc integer constructions.

**Schinzel's theorem (Prop 2), the square obstruction.** If `4/(at+b)` is
3-Egyptian for a polynomial family, then `b` is a quadratic **non-residue** mod
`a`. Proof is a Jacobi-symbol identity: `(p/(4BCD−1)) = −(D/(4BCD−1))… = −1`
contradicting `p` a perfect square (when `ak+b` is a square). This is the
polynomial-shape version of Mordell's nonexistence result, and it is why
`n ≡ r mod 840` with `r` a square mod 840 (the six residual classes) cannot be
covered by any single polynomial family. See `wikipedia-erdos-straus.md` claim
`mordell-nonsquare-necessary`.

**Sieve / filters (§3) and the verification bound (§4).**
- Filters: for `n ≡ 1 mod 24`, `S_m = {b mod m : 4/(mt+b) 3-Egyptian}`; `n` is
  *certified* if `n mod m ∈ S_m`. Computed: `S₅={0,2,3}`, `S₇={0,3,5,6}`, `S₁₁`,
  `S₁₃`, …; shortened composite filters `S*₅₅={24,39}`, `S*₆₅={54,59}`, …
- Progression hierarchy: start `n ≡ 1 mod 24`; with `S₅` keep
  `n mod 120 ∈ {1,49}`; with `S₇` keep `n mod 840 ∈ R₂ = {1,121,169,289,361,529}`
  — **exactly the six residual classes of the integer problem, and exactly the
  set Swett used.** Further `mᵢ ∈ {11,13,17,19,23}` give gaps
  `G₇ = 892 371 480` with `#R₇ = 147 348` residual classes and mean gap 6056
  (≈43× fewer checks than the mod-840 stage).
- **Main verification result (§4.3):** with `M` = all odd `m < 5000`,
  `N₇ \ ⋃_{m∈M} Ω_[m,24]` has **no element `n < N = 10^17` except squares**.
  The run checked `n = r + k·G₇`, `r ∈ R₇`, `0 ≤ k < 112 066 560`:
  **16 512 783 482 880 integers, of which 51 732 427 are squares**, each
  non-square certified by some `m ∈ MOD` (a 427-element sorted filter list, given
  in the paper). Non-prime composites are covered by the prime reduction; squares
  were verified by direct computation – hence the conjecture holds to `10^17`.

```claim
id: reduction-mod24
statement: By identifying n ≡ −1 mod 3, −1 mod 4, −3 mod 8, it suffices to prove the conjecture for primes p ≡ 1 mod 24; the six residual residues mod 840 {1,121,169,289,361,529} are exactly the intersection of this class with the mod-5 and mod-7 filters.
hypotheses: none (standard identities + prime reduction).
holds-here: true.
status: sourced (Salez §1.1, §4.1); residual-class facts hand-verified.
bearing: parameterise the hard class as n = 840k + r, r ∈ {1,121,169,289,361,529}; equivalently primes p ≡ 1 mod 24 after sieving.
anchor: research/summaries/salez-erdos-straus-new-modular-pdf.md
```

```claim
id: seven-equations-complete
statement: For p an odd prime, 4/p is 3-Egyptian if and only if one of seven constant-coefficient modular equations (14a,b,c; 15a,b,c,d) holds; this is a COMPLETE set for degree-1 prime polynomials (three new: 14c, 15c, 15d). For integers the seven are not exhaustive: a solution could come from an unknown new type.
hypotheses: p an odd prime (or degree-1 prime polynomial).
holds-here: true — no single one of the seven modular equations covers n ≡ 1 (mod 840); a covering family must be a new type outside the seven.
status: sourced (Salez Prop 3, Lemma 1, Cor 1, §2.4).
bearing: bounds the symbolic ansatz search — families collapsing to one of the seven shapes are rediscoveries; only genuinely new shapes can cover the six residual classes.
anchor: research/summaries/salez-erdos-straus-new-modular-pdf.md
```