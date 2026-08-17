# Thread grounding: binary-digit & zsigmondy — what is now actually on disk

## Granville survey — canonical p-adic grounding (NEW, fetched this cycle)

`research/sources/granville-binomial-intro.full.md` (+ elementary, genlucas sections),
from https://dms.umontreal.ca/~andrew/Binomial/intro.html.

Fixes the exact statements the `binary-digit` thread leans on:
- **Glaisher (1899):** the number of odd entries in row n is 2^{#1s(n)}; C(n,m)
  is odd iff the 1-bits of m ⊆ 1-bits of n (Lucas mod 2).
- **Kummer (1852):** v_p(C(n,m)) = number of carries adding m and n−m in base p.
- **Lucas (1878):** C(n,m) ≡ product of digitwise C(n_i, m_i) mod p.
- **Anton–Stickelberger–Hensel + Granville Thm 1:** full mod p^q formula.

Claim block filed in `research/summaries/granville-arithmetic-properties-binomial.md`
(id: granville-arith-properties-binom).

This is the reference for "k ⊆ n as bit-masks" (binary-lucas-submask approach)
and for any p-adic valuation argument on C(x,k1)=C(y,k2).

## Zsigmondy approach — PHANTOM CITATION corrected

`research/approaches/zsigmondy-primitive-prime.md` cites:
> "Granville–Ramaré (1996, J. London Math. Soc. 54): for n > max(k+1, 2k−3),
> the product n(n−1)…(n−k+1) has a prime divisor p not dividing any product of
> k consecutive integers with smaller starting value" — claimed held in NTIP
> Vol. 2 pp. 299+.

**This citation does not exist.** Checked three ways (full detail in
`research/notes/zsigmondy-phantom-citation.md`):
1. Granville–Ramaré 1996 is "Explicit bounds on exponential sums and the
   scarcity of squarefree binomial coefficients", *Mathematika* 43 (1996)
   73–107 — about squarefree binomial coefficients; journal AND volume wrong.
2. Grep across all of `research/sources/` finds no Granville–Ramaré theorem;
   held NTIP is Vol. 1 and has no Granville–Ramaré content; Vol. 2 not on disk.
3. Search corroborates the squarefree-binomial scope.

**Action for the run:** the primitive-prime-divisor engine of the zsigmondy
approach is unsupported as written. Its Sylvester step is real and now grounded
in the held Laishram PhD thesis (Ch. 1):
- Sylvester (1892)/Schur (1929): product of k consecutive integers each > k has
  a prime divisor > k.
- Laishram–Shorey Thm 1.2.1: ω(Δ(n,k)) ≥ π(k) + ⌊¾π(k)⌋ − 1 + δ(k), explicit
  exceptions (1.2.6).
- Laishram–Shorey (Acta Arith 120 (2005) 199–211): P(Δ(n,k)) > 2k for
  n > max(k+13, (279/262)k).

**Falsifier:** a genuine Granville–Ramaré primitive-prime-divisor theorem for
consecutive-integer products, with a citable location. Until produced, the
approach must cite Sylvester–Schur/Laishram–Shorey and note Zsigmondy applies
to a^n − b^n, NOT directly to falling-factorial blocks.