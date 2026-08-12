# Zimmermann, Pierrat & Thiriet, "Magic squares of squares", LORIA, 2015

[[zimmermann-loria-magic-squares-of-squares-2015]]

A short refereed-style note giving the modular necessary conditions, a clean theorem on all
3-square APs, and new "magic hourglass" computational results beyond Buell.

## Established statements

**Lemma 1 (modular conditions).** For any *primitive* 3×3 MSS, the magic sum `s ≡ 3 mod 72`
and every (square) element is `≡ 1 mod 24`. Proof: mod 4 only two forms (all 0 or all 1, SUM 3);
mod 8 the only primitive form is all entries 1; mod 9 gives `s ≡ 3 mod 9`; CRT ⇒ `s≡3 mod 72`.
Remark 1: mod 7 and mod 11 say `s` not divisible by 7 or 11. Remark 2: the same conditions
hold for the *hourglass* and Enigma-1 problems, and **for all problems 7.I–7.VIII all square
elements must be ≡1 mod 24**.

**Theorem 1 (all 3-square APs, unique parametrisation).** For any positive odd `A`, every
non-trivial AP `x², A², y²` is obtained, **uniquely**, as: pick a square-free `p | A`, `p ≡ 1
mod 4`; write `A = pA′`, decompose `A′ = m²+n²` with `m` even, `n` odd, `m,n>0`; set
`b = 4mn(m²−n²)`, `x = √(A²−p²b)`, `y = √(A²+p²b)`. So an AP of squares is pinned by the
single parameter `A` and its decomposition, exactly the data that indexes three-AP families.
Lemma 2, Lemma 3: auxiliaries (primes dividing `m²+n²`), and for `A ≡ 3 mod 4` there is a
`g>1` dividing `p` for *every* decomposition `A=p(m²+n²)`.

**Magic hourglass / 7-square results.** For the hourglass config, decomposing `A` in three
different ways with coprime `p` can give a solution. They found hourglasses with all 5 relevant
sums equal mod `2⁴⁷` etc. (central element ~10 digits), whereas Buell's search found none mod
`2⁴⁷` up to `A=5·10¹²` under the coprime assumption; similarly beyond Pech's mod-`2⁵³` bound.
So **relaxing Buell's coprimality assumption yields much smaller hourglass near-solutions**.
For problems 7.II, 7.III, 7.V: no solutions up to the stated bounds (partial).

## Implications for this run

- Confirms and sharpens the modular sieve (entries `1 mod 24`, sum `3 mod 72`) — the run's
  "locally solvable mod every prime power" claim is *consistent* with these, which are
  necessary-not-sufficient.
- Theorem 1 is the clean characterisation of an AP of squares that the run's four-AP
  obstruction needs: each centre line `x², c, y²` is indexed by `A=√c` and a
  `(p, m, n)` decomposition. The additive relations among `u, v, u+v, u−v` become relations
  among these AP data.
- The hourglass result is a **direct counterexample-shaped caution**: Buell's coprime
  assumption is not automatic (it was criticised by Zimmermann–Loria), so any run lemma that
  assumes the three APs' data are coprime is unsound.

## Contradictions / cautions

- The "centre > 25×10²⁴" bound as usually quoted is *Buell's* for the hourglass configuration
  specifically, not the full 3×3 MSS; Michaud-Rodgers cites it loosely for the full problem.
  Both Bremner II and Zimmermann attribute it to Buell's hourglass search.

```claim
id: ap-three-squares-unique-param
statement: Every non-trivial 3-square AP x²,A²,y² (A odd positive) is given uniquely by a
  square-free p|A with p≡1 mod 4, A=pA′=(m²+n²) (m even, n odd), b=4mn(m²−n²),
  x²=A²−p²b, y²=A²+p²b.
hypotheses: A>0 odd, x²,A²,y² an AP of squares, primitive after removing common factors
holds-here: yes (every centre line of a MSS is such an AP)
status: proved
bearing: indexes each centre AP by (p,m,n); basis for expressing the four-AP additive relations
anchor: research/sources/zimmermann-loria-magic-squares-of-squares-2015.full.md
```

```claim
id: primitive-mss-modular-124-72
statement: A primitive 3x3 MSS has all nine entries ≡1 mod 24 and magic sum ≡3 mod 72.
hypotheses: primitive
holds-here: yes
status: proved
bearing: necessary sieve conditions; consistent with local solvability, so no sieve alone decides
anchor: research/sources/zimmermann-loria-magic-squares-of-squares-2015.full.md
```
