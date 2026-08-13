# Approach: genus of C(x,k1) = C(y,k2) and the Faltings threshold

## Result achieved

For the family of plane curves `F_{k1,k2}(x,y) = C(x,k1) - C(y,k2) = 0`,
`C(z,k) = z(z-1)...(z-k+1)/k!`, the geometric genus is now computed exactly
and verified two independent ways (Singular `genus(ideal)` and Sage
`Curve.genus()`) for `2 <= k1,k2 <= 12` plus the k2=3,4,5 columns to k1=24.
Table: see `code/out/genus_table.captured.txt`, machine-readable table in
`code/genus/genus_table.py`.

**The Faltings threshold is crossed immediately.** For fixed
`(k1,k2) != (2,3),(3,2),(2,4),(4,2)`, the genus is `>= 2`, so Faltings gives
finitely many *rational* points on every other fixed pair. The genus-1 cases
are exactly `{2,3}` (elliptic, solved by Avanesov) and `{2,4}` (solved by de
Weger/Pintér via Gelfond–Baker). Every other distinct pair has genus >= 2.

## Verified closed forms (with the larger parameter n)

- **k2=2, pair {2,n}:** `y(y-1) = 2C(x,n)`, **hyperelliptic** (2:1 over P^1),
  `genus = floor((n-1)/2)`. Reproduces the stated formula.
- **k2=3, pair {3,n}:** `C(y,3) = (Y^3-Y)/6` with `Y=y-1` (proved symbolically),
  so the curve is **cyclic trigonal** (3:1 cover of P^1),
  `genus = n-1` if `3 ∤ n`, else `n-2`.
- **k2=4, pair {4,n}:** `y(y-1)(y-2)(y-3) = (y^2-3y)^2 + 2(y^2-3y)` (proved
  symbolically), so with `w = y^2-3y+1` the curve is a **2:1 cover of the
  hyperelliptic curve `w^2 = 1 + 24C(x,n)`** (superelliptic),
  `genus = 3(n-1)/2` (n odd), `3(n-2)/2 + 1` (n even, n≡2 mod 4),
  `3(n-2)/2` (n even, n≡0 mod 4).

## Literature cross-checks (all confirmed by the computed table)

- `(3,4) = genus 3` — matches de Weger (1997), who proved `C(n,3)=C(m,4)` is
  genus 3 and a double cover of the elliptic `Y^2+Y=X^3-X` (therefore **not**
  hyperelliptic).
- `(2,5) = genus 2` — matches Bugeaud–Mignotte–Siksek–Stoll–Tengely (2008),
  who solved it on a hyperelliptic curve via the Mordell–Weil sieve.
- Adjacent pairs `(n-1,n)` attain the smooth-plane-curve genus
  `(n-1)(n-2)/2`: these are the nonsingular members of the family.

## How this maps to the GOAL, honestly

This computes the genus as a function of `(k1,k2)` and makes the Faltings
threshold explicit — one of GOAL.md's listed partial results. BUT it is a
**geometric fact about fixed pairs**, and per the problem's own structure note
("finiteness is not a bound") it does NOT give a bound **uniform in k**. Faltings
is ineffective in the parameter. What the computation genuinely contributes:

1. It makes precise *which* pairs are genus 1 (only {2,3},{2,4}), i.e. which
   pairs need Siegel rather than Faltings for finiteness, and confirms all the
   rest have genus >= 2 where Faltings applies.
2. It gives the exact, verified genus as a function of the pair, which any
   future effective-height or Baker-method argument would need as an input.
3. It confirms the small-k structures are not all hyperelliptic: (3,4) is
   cyclic-trigonal-cover-of-elliptic (de Weger), k2=3 is cyclic trigonal,
   k2=4 is a 2:1 cover of hyperelliptic — a richer structure picture than "all
   small pairs are hyperelliptic".

**The uniform-bound obstruction is unchanged and is the structural wall:**
Beukers–Shorey–Tijdeman / Siegel give finiteness for each fixed pair with no
bound computable in `(k1,k2)` (documented in `research/summaries/
singmaster-literature-exact.md` as deweger-smallk-effective). The genus table
is a necessary ingredient, not itself the conjecture.

## Why not brute force

Genus is a fixed-algebraic object per pair: computing it is a finite
Gröbner/singularity computation whose cost depends only on `(k1,k2)`, not on
any search bound. This is the honest, non-exhaustive part of the Diophantine
program, exactly as GOAL.md's thread `research/threads/diophantine-curves.md`
anticipated.
