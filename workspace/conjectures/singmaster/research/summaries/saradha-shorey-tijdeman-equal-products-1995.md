# Saradha–Shorey–Tijdeman, "On arithmetic progressions with equal products"

Source: https://bibliotekanauki.pl/articles/1391588.pdf — N. Saradha, T. N. Shorey,
R. Tijdeman, Acta Arithmetica LXVIII.1 (1994/1995) 89–100.
Full text: `research/sources/saradha-shorey-tijdeman-equal-products-1995.full.md`.

## What it establishes

The paper studies the equal-products Diophantine equation

```
(1)  x(x+d1)...(x+(L-1)d1) = y(y+d2)...(y+(M-1)d2)
```

in positive integers with d1, d2 fixed and L/M fixed. It sets k = gcd(L,M),
l = L/k, m = M/k (so gcd(l,m)=1, and l,m are fixed by the ratio L/M). The two
theorems cover all pairs (L,M) with L ≠ M in the literature up to 1994:

- **Theorem 1**: if L ∈ {2,4} and M is odd, then max(x,y) ≤ C1, an effectively
  computable constant depending only on d1, d2, M. (Proof: reduces to an elliptic
  equation z² = δy(y+d2)... + c² for M=3, and hyperelliptic for M≥5, using
  Brindza's lemma 2 — Baker's linear-forms-in-logarithms bound on z²=f(y).)
- **Theorem 2**: if gcd(L,M) > 1 and L ≠ M, then
  ```
  max(L, M, x, y) ≤ C2
  ```
  where C2 is effectively computable, depending only on d1, d2 and L/M, **unless**
  (d1,d2,L,M,x,y) or its mirror equals (d, 2d², 4, 2, z, z²+3dz) for positive
  integers d, z. (Proof: express each side as a shifted power via Lemma 6, show
  k ≪ 1 once m>2, then a resultant/factorization argument using Lemma 9 and a
  Chebyshev/rolle contradiction to exclude the exceptional structure.)

### Relevant surrounding results (same paper's introduction)

- Mordell 1963: (L,M)=(2,3) ⇒ (x,y)=(2,1) or (14,5)  [this is C(n,2)=C(n,3)-type].
- Boyd–Kisilevsky 1972: (3,4) ⇒ (x,y)=(2,1),(4,2),(55,19).
- Saradha–Shorey 1990: M=2L has only (L,M,x,y)=(3,6,8,1); M=3L,4L no solutions
  (1991); M=5L,6L (Mignotte–Shorey).
- Saradha–Shorey 1992: M=mL, d1=d2 ⇒ effective bound on max(L,x,y) depending only
  on m.
- Saradha–Shorey–Tijdeman [13]: L=M treated separately; the *only* infinite family
  is d1=1, d2=4, x=L+1, y=2, giving (L+1)(L+2)...(2L) = 2·6·...·(4L-2), i.e.
  C(n,k) dual-identity collisions.

## Implication for this problem (the C(x,k1)=C(y,k2) family)

With d1=d2=1, (1) is the shift of the binomial-collision equation:
`C(x+L-1, L)` and `C(y+M-1, M)` equal the products divided by L! and M!. So per
fixed (k1,k2) = (L,M), the SST-style effective method applies. **The key nuance
for the "finiteness is not a bound" obstruction:** SST 1995 gives an *effective*
bound — a computable constant — for the shared-factor unequal-degrees case
(gcd(L,M)>1, L≠M), and effectively computable bounds for L∈{2,4}, M odd. So not
every per-pair result is ineffective. What is still missing is uniformity: the
constant C2 depends on d1, d2, and the ratio L/M, so it does not yield a single
B uniform over all (k1,k2) — exactly the gap Singmaster needs closed. The honest
statement is: SST give effective-per-pair bounds but the dependence on L/M is
uncontrolled, which is why this does not settle the conjecture.

```claim
id: sst-effective-shared-factor
statement: Saradha-Shorey-Tijdeman 1995 (Acta Arith 68(1) 89-100, Thm 2): for the
  equal-products equation (1) with gcd(L,M)>1 and L≠M, max(L,M,x,y) ≤ C2 where
  C2 is effectively computable and depends only on d1, d2 and the ratio L/M,
  except a single explicitly-given family.
hypotheses: d1,d2 fixed; L/M fixed; gcd(L,M)>1; L≠M; exceptions as stated.
holds-here: yes for the binomial-collision equation C(x+L-1,L)=C(y+M-1,M) when
  the pair (L,M) shares a factor >1 and L≠M — the effective-per-pair regime of
  the C(x,k1)=C(y,k2) family.
status: asserted (primary source, read in full here)
bearing: effective but NOT uniform in (k1,k2): C2 grows with d1,d2,L/M, so the
  per-pair bound does not yield a constant B for all pairs. Names the obstruction:
  per-pair effectiveness exists (SST) but the ratio-dependence blocks uniformity.
anchor: research/sources/saradha-shorey-tijdeman-equal-products-1995.full.md
```

```claim
id: sst-equal-length-exception-family
statement: For the equal-length case (L=M) of (1), the only exceptional family is
  d1=1, d2=4, x=L+1, y=2, giving (L+1)(L+2)...(2L)=2·6·...·(4L-2) — the
  C(n,k) dual identity (2L choose L) = product relation that yields infinitely many
  repeated-product collisions.
hypotheses: d1=1, d2=4, x=L+1, y=2, L=2,3,...
holds-here: yes (§6 of the same thread — L=M is the golden-ratio 'a=b' case in
  Jenkins' reformulation, which is precisely the one he could not seal).
status: asserted
bearing: structural — the L=M case is where infinite families enter; this identifies
  the single infinite exception and its form.
anchor: research/sources/saradha-shorey-tijdeman-equal-products-1995.full.md
```
