# Ring structure and ramification of Z[zeta_p]: the factorisation machinery

## Source URLs

- Thaine, F., "On Fermat's last theorem and the arithmetic of Z[zeta_p + zeta_p^{-1}]",
  J. Number Theory 29 (1988), 297–299. https://doi.org/10.1016/0022-314X(88)90107-2
- Steidl, G., Tasche, M., "On a number-theoretic result of
  Sylvester–Kronecker–Zsigmondy", Math. Nachr. 140 (1989).
  https://doi.org/10.1002/mana.19891400116

Together with the standard treatment in Washington, *Introduction to Cyclotomic
Fields* (GTM 83), this records the exact arithmetic of the ring where the run's
open content lives. It is *machinery*: no exclusion or bound for
`x^p - y^q = 1` is derived here.

## The ring and its ramification (standard)

For `p` an odd prime and `zeta_p` a primitive `p`-th root of unity:

- The ring of integers of `Q(zeta_p)` is exactly `Z[zeta_p]`.
- The prime `p` is **totally ramified**: `(p) = (1 - zeta_p)^{p-1}` in
  `Z[zeta_p]`. The unique prime above `p` is `P = (1 - zeta_p)`; its residue
  degree is 1 and its ramification index is `e = p - 1`. Equivalently
  `(1 - zeta_p)` is a uniformiser of the (unique) p-adic valuation of
  `Q(zeta_p)`, with `v_P(p) = p - 1`.
- The ideals `(x - zeta_p^i)` for `i = 0, ..., p-1` (with `x in Z[zeta_p]`) are
  **pairwise coprime away from `(1 - zeta_p)`**: for `i != j`,
  `gcd(x - zeta_p^i, x - zeta_p^j)` is contained in `(1 - zeta_p)`.
- **Valuation identity** (the engine of Cassels-type divisibility arguments):
  for an integer `x` with `p ∤ x`,
  `v_p(x^p - 1) = 1 + v_p(x - 1)`, and the mirror form
  `v_q(y^q + 1) = 1 + v_q(y + 1)` for the `q`-side. This single extra unit of
  valuation is what forces `p | y` and `q | x` in the run's `G-odd-cassels`
  argument; the run's own note `research/backward/both-odd-primes.md` already
  names these two identities as the carry.

## Why the run's argument lives here

Writing `x^p - 1 = y^q` in `Z[zeta_p]`:

    y^q = x^p - 1 = prod_{i=0}^{p-1} (x - zeta_p^i)

The factors `(x - zeta_p^i)` are pairwise coprime off `(1 - zeta_p)`. Since their
product is a `q`-th **power** of an element, each is a `q`-th power of an ideal
off `(1 - zeta_p)`. For `p | y`, the `q`-th power valuation of `y^q` at the
ramified prime forces `q | v_P(y)` — and the congruence arithmetic in the ring
then yields `q | x`; the mirror in `Z[zeta_q]` yields `p | y`. This is the
classical Cassels divisibility, which the run's skeleton needs but the evidence
policy will not supply as a finished statement; the library records the
*machinery* (the ramification structure and valuation identity above) so the run
can re-derive it.

## Claims

```claim
id: zeta-p-ring-and-ramification
statement: >
  The ring of integers of Q(zeta_p) (p odd prime) is Z[zeta_p]; p is totally
  ramified with (p) = (1 - zeta_p)^{p-1}; the ideal (1-zeta_p) has residue degree 1
  and ramification index p-1.
hypotheses: p an odd prime.
holds-here: yes — the open content works in exactly this ring.
status: sourced (Thaine 1988; Steidl-Tasche 1989; standard, cf. Washington GTM 83).
anchor: research/sources/zetap-ring-ramification.md
bearing: fixes where the factorisation x^p-1 = prod(x-zeta_p^i) happens and how p ramifies.
```

```claim
id: faktor-pairwise-coprime-off-ramified
statement: >
  For x in Z[zeta_p] and i != j, the ideals (x - zeta_p^i) and (x - zeta_p^j) have
  gcd contained in (1 - zeta_p); they are pairwise coprime off the unique ramified
  prime. In particular, if x is an integer with x != 1 the gcd is 1 or a power of
  (1 - zeta_p).
hypotheses: p an odd prime, i != j in {0,...,p-1}.
holds-here: yes — this is what makes each factor a q-th power of an ideal.
status: sourced (Thaine 1988; Steidl-Tasche 1989).
anchor: research/sources/zetap-ring-ramification.md
bearing: the coprimality that turns the element equation into an ideal q-th power relation in Z[zeta_p].
```

```claim
id: valuation-identity-xp-1
statement: >
  For an integer x with p ∤ x, v_p(x^p - 1) = 1 + v_p(x - 1); mirror:
  for an integer y with q ∤ y, v_q(y^q + 1) = 1 + v_q(y + 1).
hypotheses: p, q odd primes; p ∤ x, q ∤ y.
holds-here: yes — this is the engine of the Cassels p|y, q|x step the run must re-derive; it produces a single extra unit of valuation per exponent, forcing the divisibility.
status: sourced (stated in the run's own note both-odd-primes.md; standard cyclotomic fact, cf. Thaine 1988 and Washington).
anchor: research/sources/zetap-ring-ramification.md
bearing: the load-bearing identity for the whole divisibility/Wieferich chain in the both-odd-primes case.
```

The three claims are mutually consistent and standard. The `v_p(x^p-1)=1+v_p(x-1)`
identity holds because `(x^p-1)/(x-1) = 1+x+...+x^{p-1} ≡ p mod (x-1)` and `p ∤ x`;
the run should verify this and the coprimality by exact computation in `code/`
before relying on the two heavier lemmas that build on them.
