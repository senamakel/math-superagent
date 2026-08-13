# L. Hajdu, Á. Pintér, Sz. Tengely, N. Varga, "Equal values of figurate numbers" (J. Number Theory 137 (2014) 130-141)

Source: https://doi.org/10.1016/j.jnt.2013.10.017 ; author's accepted version:
https://shrek.unideb.hu/~tengely/hptvrevised.pdf
Full text: `research/sources/hajdu-pinter-tengely-varga-equal-figurate-2014.full.md`

## What the paper is

The X-th figurate number with parameters k, m is

    f_{k,m}(X) = X(X+1)...(X+k-2)((m-2)X + k+2-m) / k!,   k≥3, m≥3.

Special cases: **m=3 gives the binomial coefficient** `f_{k,3}(X) = C(X+k-1, k)`
(one column of Pascal's triangle, up to a shift); k=2 gives the polygonal
numbers `f_{2,n}(X)`; k=3 gives pyramidal numbers.

The paper studies the equal-values equation

    f_{k,m}(x) = f_{2,n}(y)   (x, y integers)     (1)

i.e. **a binomial-coefficient column (m=3) or figurate column meeting the
polygonal column k=2** — which is precisely the boundary regime of Singmaster's
conjecture where all known high-multiplicity witnesses (3003 = C(78,2), the six
N=6 values 120, 210, 1540, 7140, 11628, 24310) live.

## The theorems (all primary, quoted from the accepted PDF)

- **Thm 2.1 (main)**: for k≥3, (m,n,k) ≠ (5,4,3), (6,4,4), and if k is even
  also k!D not of the form r² or 2r² where D = gcd(k!(n-4)², 8d(n-2)) with
  d = gcd(k, m-2): equation (1) has **only finitely many solutions, which can
  be determined effectively**. The two exceptional triples have infinitely many
  solutions (explicitly constructible).
- **Cor 2.1**: for k≥4 even, if there is a prime p with k/2 < p < k and
  p ∤ n-2, then (1) has effectively finitely many solutions. (Satisfied e.g.
  whenever k > 2n, by Bertrand's postulate.)
- **Thm 2.2**: if k≥3, m≥3, n≥3 and 10m - 26 ≤ n, then (1) has only finitely
  many solutions, effectively determinable. (Erdős-type argument; for the
  binomial case m=3 this covers n ≥ 4 on the polygonal side.)
- **Thm 2.3**: f_{k,k+2}(x) = f_{2,4}(y) in k≥5, x≥k-2, y≥1 has the **unique
  solution (k,x,y) = (5,47,3290)**.
- **Thm 2.4**: for (m,n) = (7,5), the integral points on the associated genus-2
  hyperelliptic curve are exactly {(-3,0),(-2,0),(-1,0),(0,0),(1,1)}; proved via
  Baker's method (log|X| ≤ 6.647×10^412) plus Mordell-Weil sieve
  (log|X| ≥ 3.32×10^494 for any unknown point → contradiction).

## Why it matters for this run

1. **Effective finiteness, not just Faltings/Siegel ineffectivity**, for the
   singularly important subfamily: triangular column (k=2, n=3) intersecting any
   fixed binomial column k (m=3). Every known N≥6 witness has a triangular
   representation, so this is the exact family where a uniform bound is hard.
2. The general two-column case f_{k,m}(x) = f_{l,n}(y) is announced as a
   "forthcoming paper" — that generalization is the run's own family
   C(x,k1)=C(y,k2), so the follow-up is a prime next acquisition.
3. The exception pairs (5,4,3) and (6,4,4) are the only sources of infinite
   families within this whole two-parameter scheme — the same structural
   "exceptional families exhaust the infinitude" shape as Bilu–Tichy.
4. Thm 2.2 gives effective finiteness when the polygonal side is large
   (n ≥ 10m-26): with m=3 (binomial), every pair (k, n≥4) where the triangular
   side is at least a 4-gonal number is effective.

## Claims

```claim
id: hptv-figurate-effective-finiteness
statement: Hajdu-Pinter-Tengely-Varga 2014 (JNT 137, 130-141; author PDF held):
  the equal-values equation f_{k,m}(x) = f_{2,n}(y) for figurate numbers
  f_{k,m}(X)=X(X+1)...(X+k-2)((m-2)X+k+2-m)/k! has EFFECTIVELY finitely many
  integer solutions whenever k>=3 and (m,n,k) not in {(5,4,3),(6,4,4)}, with
  the additional condition for even k that k!D is not of the form r^2 or 2r^2
  (D = gcd(k!(n-4)^2, 8d(n-2)), d = gcd(k,m-2)); and (Thm 2.2) if n >= 10m-26
  then always effectively finite. The two exceptions have infinitely many
  solutions. For m=3 the LHS is the binomial column C(X+k-1,k), so every fixed
  binomial column meets the polygonal (k=2) column in effectively finitely many
  equal values.
hypotheses: k>=3, m>=3, n>=3 integers; f_{2,n} is the polygonal number family;
  even-k condition as stated.
holds-here: yes — with m=3 this is exactly C(x+k-1,k) = P_n(y) (binomial column
  vs polygonal/triangular column), the boundary regime of Singmaster where all
  known high-multiplicity witnesses live.
status: asserted (quoted from accepted author PDF; not independently re-derived)
bearing: supplies EFFECTIVE (computable, per-parameter) finiteness for the
  k2=2 column intersection family — the one place in the Singmaster boundary
  where effective results exist beyond the isolated solved pairs (2,3),(2,4),
  (2,5). It does NOT give uniformity in (k1,k2): constants depend on k,m,n.
anchor: research/sources/hajdu-pinter-tengely-varga-equal-figurate-2014.full.md
```

```claim
id: hptv-exception-pairs-infinite
statement: HPTV 2014: among all triples (k,m,n) with k>=3, m>=3, n>=3, the
  equation f_{k,m}(x) = f_{2,n}(y) has infinitely many solutions only for
  (m,n,k) = (5,4,3) and (6,4,4); all other triples satisfying the even-k
  condition have effectively finitely many solutions. Thm 2.3: f_{k,k+2}(x) =
  f_{2,4}(y) = y^2 has unique solution (k,x,y)=(5,47,3290) in k>=5, x>=k-2,
  y>=1.
hypotheses: as Thm 2.1/2.3.
holds-here: yes (the (5,4,3) exception is the infinite pyramidal-square family;
  the run's own infinite N>=6 family comes from the a=b Pell case, outside this
  theorem's scope — see note)
status: asserted
bearing: delimits where infinite families can hide in the figurate equal-values
  scheme, matching the Bilu-Tichy "exceptional pairs" structure; the run's own
  infinite family C(n+1,k+1)=C(n,k+2) has both columns m=3 with different k,
  so it is outside the f_{*,*}=f_{2,*} scope and does not conflict.
anchor: research/sources/hajdu-pinter-tengely-varga-equal-figurate-2014.full.md
```