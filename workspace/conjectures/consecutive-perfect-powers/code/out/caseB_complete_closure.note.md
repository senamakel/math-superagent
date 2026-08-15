# Case B complete closure via the Nagell-Ljunggren theorem (exact for the slice)

Program: `code/caseB/caseB_complete_closure.py`
Output: `code/out/caseB_complete_closure.captured.txt` (EXIT 0, RESULT:
ALL CHECKS PASS, TOTAL runtime 8.49 s).  Exact integer arithmetic only
(`pow` for the p-th power, `math.isqrt` for the exact square test; no
floats).  The box [3] is parallelised over the odd primes with
`ProcessPoolExecutor` (28 workers, 7.78 s).

## The reduced problem (already established in-workspace)

Case B of Catalan, `x^p - y^2 = 1` (p an odd prime >= 3), x, y > 0.  The
machine-certified reduction (claim `exp2-caseB-reduction`,
`code/out/caseB.note.md`) forces

    x = c^2 + 1  (c >= 1),   y = c·m,   m^2 = T(c,p) := Σ_{k=0}^{p-1} (c^2+1)^k
                                = ((c^2+1)^p - 1) / c^2.

Whether `T(c,p)` is ever a square is exactly the Case-B obstruction.  The
mod-8 classification (claim `exp2-caseB-t-mod8-classification`,
`code/out/prove_T_mod8_classification.note.md`) is PROVED in-workspace and
leaves only the residual class `c even AND p ≡ 1 (mod 8)` open; a
fixed-modulus hunt (claim `caseB-no-fixed-modulus-closes-residual`) showed
no fixed modulus closes even that class.

## What this program adds

It completes the residual (and redundantly every) class by applying the
classical **Nagell-Ljunggren theorem** to this exact slice:

>  (X^n − 1)/(X − 1) = Y²  has, for n > 2, exactly the solutions
>  (n, X, Y) = (4, 7, 20) and (5, 3, 11).

**Slice:** n = p (odd prime >= 3), X = c^2+1 (>= 5, odd), and for the
residual class X ≡ 1 (mod 4).

## Exact exclusion of the two exceptions (assertions, all printed)

- (`4,7,20`): n = 4 is EVEN, excluded since our n = p is an odd prime.  ✔
  (checked the identity (7^4−1)/6 = 400 = 20² first)
- (`5,3,11`): n = 5 is odd (in slice range) but X = 3 requires
  c²+1 = 3, c² = 2 — impossible for integer c.  ✔
- Independently, X = 3 and X = 7 both fail the congruence X ≡ 1 (mod 4)
  that c even forces.  ✔

So neither exception can be a Case-B `T(c,p)`, and Nagell-Ljunggren closes
the whole slice (all classes, hence in particular the residual class).

## Independent exact oracle (point 3)

`T(c,p)` computed exactly by the integer formula, tested for square by
`isqrt`, for **c even in [2, 200000]** and **odd primes p in [3, 199]**
(4,500,000 pairs, 0 squares, 7.78 s wall).  This is a WIDER box on the
small-c side than the prior `verify_bundle` box (c <= 1e5, p <= 251) and
than the mod-8 box (c <= 4000).  It settles **nothing new** beyond those
boxes: it is a large-sample confirmation consistent with the classical
theorem, not a proof; the effective bound is far beyond any box.

## Independent direct enumeration (point 4)

For n in {2,3,4,5}, X in [2, 10^6], enumerating `Y² = (X^n−1)/(X−1)`:

- n=2: many solutions — irrelevant (n=2 is outside the slice n>2; it is
  just `X+1 = Y²`, all-always in the slice's excluded sense).
- n=3: none.
- n=4: exactly `(X,Y) = (7,20)`.
- n=5: exactly `(X,Y) = (3,11)`.

Both Nagell-Ljunggren exceptions reproduced by direct enumeration, and no
OTHER solution exists in the odd indices n=3, n=5 relevant to our slice
(the only in-slice candidate would be (5,3), excluded by X=3).  Small-box
confirmation; not a proof for all X.

## Falsifier / over-elimination check

The known Catalan solution `3^2 − 2^3 = 1` has y-exponent 3, so it sits
OUTSIDE Case B's hypothesis (y-exponent 2) and is neither eliminated nor
touched.  A lemma implying the whole equation has no solution would be
false; nothing here does — Case B is the y-exponent-2 branch only, and its
conclusion is a negative statement about hypothetical second solutions,
consistent with the oracle `(3,2,2,3)` unique below 10^12.

Every "classical" ingredient is flagged as asserted, not re-proved: the
single load-bearing classical fact is Nagell-Ljunggren, cited as a standard
reference (Ljunggren 1943, Norske Vid. Selsk. Skr. (Trondheim), No. 9,
"Zur Theorie der Gleichung x²+1 = Dy⁴" family of results giving the
classification of (X^n−1)/(X−1) = Y² for n > 2).  **This citation is
asserted from standard literature, not fetched or verified in-workspace** —
no primary source was downloaded.  The exception set itself is confirmed in
this run by the direct enumeration of point 4 within X <= 10^6.

## Claim

```claim
id: caseB-complete-closure-nagell-ljunggren
statement: For Case B of Catalan (x^p - y^2 = 1, p an odd prime >= 3),
  the reduction gives x = c^2+1, y = c*m, m^2 = T(c,p) =
  sum_{k=0}^{p-1}(c^2+1)^k.  By the Nagell-Ljunggren theorem
  ((X^n-1)/(X-1) = Y^2 has for n > 2 exactly (n,X,Y) = (4,7,20),(5,3,11)),
  with our slice n = p odd prime (>=3), X = c^2+1 (>=5) and for the
  residual class X == 1 (mod 4): (4,7,20) is excluded (n=4 even),
  (5,3,11) is excluded (X=3 needs c^2=2, impossible; and X=3,7 both fail
  X == 1 mod 4).  Hence T(c,p) is never a square, so x^p - y^2 = 1 has no
  solution for p an odd prime.  In particular this closes the residual
  class (c even, p == 1 mod 8) left open by the mod-8 classification.
hypotheses: x,y > 0, p odd prime >= 3, exact integer arithmetic; the
  Nagell-Ljunggren theorem is a classical proved result ASSERTED here, not
  re-proved in-workspace (standard citation, not fetched); its exception
  set is independently confirmed by direct enumeration of X in [2,10^6]
  for n in {3,4,5} (only (4,7,20) and (5,3,11)).
holds-here: yes -- the known solution (3,2,2,3) has y-exponent 3, outside
  Case B's hypothesis (y-exponent 2); no over-elimination.
status: reduction-proved + mod8-classification-proved in-workspace; the
  completing step is asserted-classical (Nagell-Ljunggren) verified exactly
  for the slice's exception-exclusion and confirmed numerically to
  c <= 200000 even, p <= 199 (0 squares) and by direct enumeration to
  X <= 10^6.  NOT status: proved for the Ljunggren step itself.
bearing: completes the honest Case-B closure: the theorem x^p - y^2 = 1
  (p odd prime) is PROVED conditional on the Nagell-Ljunggren theorem
  (a classical proved result, the single load-bearing classical fact),
  whose only in-slice candidate (5,3) is excluded exactly.
anchor: code/out/caseB_complete_closure.captured.txt
```

## Proved-in-workspace vs asserted-classical (explicit list)

PROVED in this workspace:
- the reduction `x=c^2+1, y=c·m, m^2=T(c,p)` (claim `exp2-caseB-reduction`);
- the mod-8 classification leaving only c even & p ≡ 1 (mod 8)
  (claim `exp2-caseB-t-mod8-classification`);
- the exact slice-exclusion of both Nagell-Ljunggren exceptions (n=4 even;
  c²=2 impossible; X=3,7 fail X ≡ 1 mod 4) — verified here as assertions,
  and by direct enumeration to X <= 10^6 (point 4);
- numerical agreement of the oracle with Ljunggren over the stated box
  (point 3: 0 squares, 4.5e6 pairs).

ASSERTED CLASSICAL (not re-proved or sourced here):
- the Nagell-Ljunggren theorem itself: `(X^n−1)/(X−1)=Y²` for n>2 has only
  `(4,7,20)` and `(5,3,11)`.  Standard-reference citation asserted, full
  text not fetched; the exception pair reproduced numerically.

Remaining `sorry`: the Nagell-Ljunggren step is asserted, not proved in
this workspace.  Everything downstream of it is a proof conditional on that
one classical theorem.
