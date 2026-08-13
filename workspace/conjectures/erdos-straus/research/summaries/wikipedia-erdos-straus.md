# Wikipedia — Erdős–Straus conjecture (encyclopedic reference)

Source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture
(snapshot oldid 1367560126; "good article").
Full text: `research/sources/wikipedia-erdos-straus.full.md` (62 KB, complete).

## The classical worked-identity list (this is the reference for the identity tier)

**Simple identities (Salez §1.1 calls these "basic formulas"; Wikipedia states the
first explicitly):**
- `4/n = 1/n + 1/((n+1)/3) + 1/(n(n+1)/3)` for `n ≡ 2 (mod 3)`. ["Mordell-type":
  for prime `p = n`, denominators divisible by `p` twice → **Type II** shape.]
- Greedy algorithm gives ≤ 3 terms whenever `n ≢ 1, 17 (mod 24)`; the `17 mod 24`
  case is covered by `2 mod 3` (17 ≡ 2 mod 3). **So only `n ≡ 1 (mod 24)` needs a
  new method** (matches Salez's reduction).
- Other elementary identities: `4/(3t−1)`, `4/(4t−1)`, `4/(8t−3)` solved in Salez.

**Mordell's five polynomial identities (Mordell 1967, *Diophantine Equations*,
pp. 287–290; Wikipedia's list):** solved for `n`
- `≡ 2 (mod 3)` (five families: 280, 210, 336, 360, 105 residue classes mod 840
  respectively — counts are 840/m for the single-residue mod-m classes and
  (#residues)·840/m otherwise),
- `≡ 3 (mod 4)`,
- `≡ 2 or 3 (mod 5)`,
- `≡ 3, 5 or 6 (mod 7)`,
- `≡ 5 (mod 8)`.

**Coverage mod 840 (the key settled-class fact).** The union of these five
families covers all 840 residue classes **except the six squares
`{1, 121, 169, 289, 361, 529} mod 840`** (= `1², 11², 13², 17², 19², 23² mod
840`). The smallest prime not covered is **1009** (1009 ≡ 169 mod 840; prime —
checked). Facts hand-verified this run: all six classes are `≡ 1 (mod 24)`
(hence inside the hard `1 mod 24` slice), all six are quadratic residues mod
840, and they coincide exactly with Salez's sieve residual set `R₂ =
{1,121,169,289,361,529}` (n ≡ 1 or 49 mod 120 and n mod 7 ∈ {1,2,4}).

**Nonexistence of identities (Mordell 1967; Wikipedia "Nonexistence of
identities").** A polynomial identity solving `4/n` for *all* `n ≡ r (mod p)`
can exist **only when `r` is a quadratic non-residue mod `p`**. Since `1` is a
square mod every `m`, no complete covering system of modular identities can
exist — the class `n ≡ 1` is always uncovered by any single congruence.

## Other facts recorded

- **Computational verification: `n ≤ 10^17`** (Salez 2014). (Note: the Erdős
  problems database, also in this library, now states `n ≤ 10^18`, 2025 —
  see Contradictions.)
- Prime reduction: a composite counterexample would imply a smaller prime
  counterexample, so it suffices to check primes.
- Sequence of solution counts (distinct denominators): 1, 1, 2, 5, 5, 6, 4, 9,
  7, 15, 4, 14, 33, 22, 4, 21, 9, … (OEIS A073101).
- Elsholtz–Tao (2013): average number of solutions is polylogarithmic;
  classification by how many of x,y,z are divisible by n (see
  `elsholtz-tao-counting.md`).

```claim
id: mordell-covering-840
statement: Combinations of Mordell's polynomial identities (n ≡ 2 mod 3, 3 mod 4, 2 or 3 mod 5, 3/5/6 mod 7, 5 mod 8) give three-term Egyptian fractions for all n except possibly n ≡ 1,121,169,289,361,529 mod 840; the smallest prime not covered is 1009.
hypotheses: n positive integer (families are polynomial in n; denominators integral on the stated residue class).
holds-here: true.
status: asserted — Wikipedia citing Mordell (1967), independently erdosproblems/242 ([Mo69]); structural checks (≡1 mod 24, squares, R₂ coincidence) hand-verified this run.
bearing: defines the six open classes every new family must engage; the residual classes are all squares mod 840, below a Type-I/II family vanishes (Elsholtz–Tao Prop 1.6).
anchor: research/summaries/wikipedia-erdos-straus.md
```

```claim
id: mordell-nonsquare-necessary
statement: A polynomial identity giving solutions of 4/n for all n ≡ r mod p can exist only when r is NOT a quadratic residue mod p; hence no complete covering system of single-congruence identities can exist (1 is a square mod every m).
hypotheses: p prime; identity of the classical shape (see source).
holds-here: true.
status: asserted — Wikipedia citing Mordell (1967); Salez Prop 2 proves the same via Schinzel's theorem (Jacobi-symbol argument).
bearing: rules out the naive covering-system completion; a proof must step outside single modular identities.
anchor: research/summaries/wikipedia-erdos-straus.md
```