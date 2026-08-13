# Blokhuis–Brouwer–de Weger, "Binomial collisions and near collisions" (2017 preprint)

<!-- source: https://aeb.win.tue.nl/preprints/binomcoll.pdf | converted from PDF -->

Full text at `research/sources/brouwer-binomial-collisions-near.full.md`. Authors
Aart Blokhuis (TU/e), Andries Brouwer (CWI), Benne de Weger (TU/e), preprint
dated July 21 2017 — the preprint form of the already-held published paper
`blokhuis-brouwer-deweger-collisions` (INTEGERS 17 #A64). This version carries
more detail than the held INTEGERS text: the complete sieve algorithm, the full
d=1 near-collision table, and seven infinite families of near collisions.

## What it establishes / states

**Collisions (equal values).** With `2 ≤ k ≤ n/2, 2 ≤ l ≤ m/2, k < l`, the known
collisions are:

- the **double collision** `C(78,2) = C(15,5) = C(14,6) = 3003`;
- **six sporadic**: 120=`C(16,2)=C(10,3)`, 210=`C(21,2)=C(10,4)`,
  1540=`C(56,2)=C(22,3)`, 7140=`C(120,2)=C(36,3)`, 11628=`C(153,2)=C(19,5)`,
  24310=`C(221,2)=C(17,8)`;
- the **infinite family** `C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) =
  C(F_{2i+2}F_{2i+3}-1, F_{2i}F_{2i+3}+1)` (i=1,2,...), due to **Lind [9]**,
  rediscovered by Singmaster [15] and Tovey [18]. Examples: `(15,5)=(14,6)`,
  `(104,39)=(103,40)`, `(714,272)=(713,273)`, `(4895,1869)=(4894,1870)`.
  Same parametrization as the run's family `C(n+1,k+1)=C(n,k+2)` with
  `n=F_{2i+2}F_{2i+3}-1, k=F_{2i}F_{2i+3}-1`: substituting gives exactly
  `(n+1,k+1)=(F_{2i+2}F_{2i+3},F_{2i}F_{2i+3})` and
  `(n,k+2)=(F_{2i+2}F_{2i+3}-1,F_{2i}F_{2i+3}+1)`, i.e. the same two pairs.
  (Checked by direct substitution; a runnable checker is at
  `code/librarian_check_family_forms.py`, NOT yet executed by any role.)

**Conjecture 2.1 ([20], de Weger JNT 1997):** there are no other collisions than
those above.

**Theorem 2.2:** no unknown collisions in these cases, each referenced to the
primary that settled it:
- `(k,l) = (2,3),(2,4),(2,5),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8)` ([2] Avanesov
  for (2,3); [12]/[19] for (2,4); [5] BMSST for (2,5); [16] Stroeker–de Weger
  for the rest; [11] Mordell for (3,4));
- `(m,l) = (n-1,k+1)` ([18] Tovey, yields the infinite family), `(n-1,k+2)`,
  `(n-2,k+1)` ([17]);
- `n ≤ 10^6` and `C(n,k) ≤ 10^60` (the two computer searches, below).

So the **verification bound** (Blokhuis–Brouwer–de Weger 2017): no collision
unknown to the above list for `n ≤ 10^6` or value `≤ 10^60`.

## Methods (worth keeping)

- **n ≤ N sweep** (`n ≤ 10^6`): generate values `C(n,k)`, sort, compare; done as
  a priority-queue/table merge of the "sheet" of the triangle, the new value
  `C(n+k+1,k+1)` computed from `C(n+k,k)+C(n+k,k+1)`; interval arithmetic with
  exact arithmetic only where intervals collide. `N=10^6` in 56h14m on a 2 GHz
  PC.
- **Value ≤ M sieve** (`C(n,k) ≤ 10^60`): for each pair `(k,l)` with `5 ≤ l` (the
  `(k,l)` with `l ≤ 4` already settled), `f(x)=C(x,k)` is a degree-k polynomial;
  for primes `p > k` a fraction of residues `mod p` is not in the image of `f`
  (image size `A(k,p) ≈ (1-e^{-1})p` for odd k, `≈ (1-e^{-1/2})p` for even k — the
  even-k symmetry `f(x)=f(k+1-x)`). Sieve on those residues, restarting every
  500. Largest prime needed p=401.

## Near collisions (novel here)

- **Complete d=1 list** (difference exactly 1), table of 20 entries incl.
  `C(160403633,2) = C(425779,3)+1`. Complete for `(k,l),(l,k) =
  (2,3),(2,4),(2,6),(3,4),(4,6)` (via integral points on elliptic curves) and
  for `C(n,k) ≤ 10^30`.
- **Conjecture 3.1**: no other d=1 near collisions. **Conjecture 3.2**: for a
  fixed d, finitely many near collisions of difference d.
- **Seven infinite families of near collisions** (identities (1)-(7), e.g.
  `C(12x²-12x+3,3) + C(x,2) = C(24x³-36x²+15x-1,2)`), of "quality" 3 or 5.

## Bearing on Singmaster's conjecture

Corroborates the witness set exactly (3003 + six sporadic + infinite family = the
complete known collision list per Conjecture 2.1), and gives the strongest
current verification bound (n ≤ 10^6, value ≤ 10^60) with the method made
explicit. The near-collision families are adjacent structure (difference-1 / 
product-of-nearly-equal), not equal-value multiplicity, so they bear on Singmaster
only as the shape of the boundary regime MRSTT leaves open. The `A(k,p)` sieve
is a reusable elementary tool: it bounds, for a prime p, how few residues a
binomial-value column can hit mod p — relevant to the binary-digit/Lucas line of
attack. Conjectures 2.1/3.1/3.2 are asserted by the authors, not proved here.
