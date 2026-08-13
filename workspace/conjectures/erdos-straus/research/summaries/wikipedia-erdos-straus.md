# Wikipedia, "Erdős–Straus conjecture"

Source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture
Full text: `research/sources/wikipedia-erdos-straus.full.md`

## What it establishes (sourced, tertiary but uses primary refs)

- Statement: for every integer `n >= 2` there exist positive integers
  `x,y,z` with `4/n = 1/x+1/y+1/z`. Equivalent polynomial form:
  `4xyz = n(xy+xz+yz)`.
- Distinct-unit-fraction requirement is immaterial for `n >= 3` (two identical
  terms can be split).
- Negative-number relaxation is trivial for odd `n`
  (`4/n = 1/((n-1)/2)+1/((n+1)/2)-1/(n(n-1)(n+1)/4)`).
- **Composite reduction**: if `4/n` has a 3-term expansion then `4/(mn)` does
  (divide by `m`), so composite counterexamples would have a smaller prime
  one. Verification bound: `n <= 10^17` (Salez 2014).
- **Modular identities (Mordell 1967)**: polynomial identities give 3-term
  solutions when `n` is `2 mod 3`, `3 mod 4`, `2 or 3 mod 5`, `3/5/6 mod 7`,
  `5 mod 8`. Combinations cover all `n` except possibly `n ≡ 1,121,169,289,
  361,529 mod 840`. Smallest prime not covered is 1009.
- **Nonexistence of identities (Mordell 1967)**: a polynomial identity giving
  solutions for `n ≡ r mod p` can exist only when `r` is NOT a square mod `p`
  (quadratic non-residue). Since `1` is a square mod every `n`, no complete
  covering system of modular identities exists. (Hasse–Minkowski: every prime
  `p` is a non-residue mod some larger prime `q`, giving a possible approach.)
- **No Brauer–Manin obstruction** (Bright & Loughran 2020).
- Average number of solutions bounded polylogarithmically (Elsholtz–Tao 2013).

## Check values / examples

- `4/5 = 1/2+1/4+1/20 = 1/2+1/5+1/10`.
- Sequence of distinct-solution counts for `n=3,4,5,...`: 1,1,2,5,5,6,4,9,7,...
  (matches OEIS A073101).

```claim
id: mordell-covering-840
statement: Combinations of Mordell's polynomial identities (n ≡ 2 mod 3, 3 mod 4, 2 or 3 mod 5, 3/5/6 mod 7, 5 mod 8) give three-term Egyptian fractions for all n except possibly n ≡ 1,121,169,289,361,529 mod 840; the smallest prime not covered is 1009.
hypotheses: none (polynomial identities).
holds-here: true — this is the exact six-open-class statement this run works from.
status: sourced (Wikipedia, citing Mordell 1967).
bearing: identifies the target classes; any new family must cover one of these six, r=1 first.
anchor: research/sources/wikipedia-erdos-straus.full.md
```

```claim
id: mordell-nonsquare-necessary
statement: A polynomial identity giving solutions of 4/n for all n ≡ r mod p can exist only when r is NOT a quadratic residue mod p.
hypotheses: polynomial (modular) identity.
holds-here: true — all six open residues are squares mod 840, so no modular identity covers them.
status: sourced (Wikipedia, citing Mordell 1967; matches Elsholtz–Tao Prop 1.6).
bearing: the fundamental obstruction; a single modular identity cannot cover any open class.
anchor: research/sources/wikipedia-erdos-straus.full.md
```

## Implication

Confirms the six open classes and the fundamental obstruction (residue must be
a non-residue for a polynomial identity to exist). Any construction reaching
`n ≡ 1 (mod 840)` cannot be a single Mordell-type modular identity.
