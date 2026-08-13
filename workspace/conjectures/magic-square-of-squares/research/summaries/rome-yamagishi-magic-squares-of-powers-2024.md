# Rome–Yamagishi: On the existence of magic squares of powers (2024)

Full text: `research/sources/rome-yamagishi-magic-squares-of-powers-2024.full.md`
(arXiv:2406.09364v2, 4 Sep 2024, 37 pages — now real PDF, not a wrapper).

## What it establishes

**Theorem 1.2.** For every integer n ≥ 4, there exists an n×n magic square of
squares (all entries distinct positive integers, all squares, all 2n+2 line sums
equal).

**Theorem 1.3.** For any d ≥ 3, there exists n₀(d) such that for all n ≥ n₀(d)
there exists an n×n magic square of d-th powers.

**Method**: Hardy–Littlewood circle method.  The problem reduces to finding a
sufficient number of disjoint linearly independent subsets of the columns of the
coefficient matrix of the magic square equations.  The authors prove an optimal
(up to a constant) lower bound for this quantity.

This settles a conjecture of Várilly-Alvarado (Conjecture 1.1) that asked for
existence of n×n magic squares of squares for all sufficiently large n.

## Bearing on the 3×3 MSS

**This paper does NOT address the 3×3 case.**  The n = 3 case is excluded from
Theorem 1.2 (which covers n ≥ 4) and is precisely the open conjecture.  The
circle method requires enough degrees of freedom in the coefficient matrix, and
at n = 3 the matrix is too constrained — the method's linear-independence count
drops below the threshold needed for the circle method to apply.

The paper is thus a **major result in a neighbouring problem** but provides no
new structural information about the 3×3 case specifically.  It demonstrates
that the obstruction at n = 3 is genuinely different from the higher-n cases
where existence is now settled.

```claim
id: btva22-quasihyperbolic-3x3-surface
statement: (Rome-Yamagishi 2024 intro, citing Bruin-Thomas-Varilly-Alvarado
  2022, "Explicit computation of symmetric differentials and its application
  to quasihyperbolicity", ANTS 16): the 3x3 MSS variety cut out by 6 quadrics
  in P^8 contains only finitely many curves of genus 0 or 1. A deep conjecture
  of Lang then predicts only finitely many rational points outside those
  curves, so a 3x3 MSS would be remarkably rare or non-existent.
hypotheses: quasihyperbolicity theorem of BTVA22 as cited; Lang's conjecture
  applied to the resulting exceptional set (unproved)
holds-here: yes (as a structural-rarity hint about the actual 3x3 surface; not
  a proof of emptiness)
status: asserted (Rome-Yamagishi cite BTVA22 as having established the
  finiteness of genus-0/1 curves; the BTVA22 paper itself is NOT in this
  library, so the statement is second-hand)
bearing: the strongest published structural hint toward rarity/emptiness for
  the 3x3 case; separates n=3 (quasihyperbolic surface, hard) from n>=4
  (circle-method abundance, solved by Rome-Yamagishi). To rely on it further,
  fetch BTVA22 and verify the exact statement (which curves, which degrees,
  over which field).
anchor: research/sources/rome-yamagishi-magic-squares-of-powers-2024.full.md
  (introduction, p. 2)
```

```claim
id: ry-proof-nuance-explicit-examples-for-4-to-36
statement: The Rome-Yamagishi proof of Theorem 1.2 (n>=4 magic squares of
  squares) is a union of two ranges: the circle-method machinery (Theorem 2.4,
  T0 >= floor(n/4)-1) yields existence for all n >= 36; the range 4 <= n <= 64
  is covered by previously known EXPLICIT examples catalogued by Boyer
  (multimagie.com). So Theorem 1.2's n>=4 statement relies on Boyer's
  catalogue for 4..36 and on the new circle-method result for n>=36 (the two
  ranges overlap on 36..64).
hypotheses: n >= 4; distinct positive integer entries
holds-here: yes (precision about what the theorem's proof actually establishes)
status: checked (read directly from the proof of Theorem 1.2, p. 7 of the full
  text: "It follows from the proof of Theorem 1.3 above that there exists an
  n x n magic square of squares as soon as n >= 36. Since the statement is
  already known for 4 <= n <= 64, in fact explicit examples have been
  discovered and listed in [Boy], this completes the proof.")
bearing: if a future run wants an independently-produced witness in 4..64 it
  must reproduce a Boyer example, not the circle method; the circle-method
  lower bound alone starts at 36.
anchor: research/sources/rome-yamagishi-magic-squares-of-powers-2024.full.md
  (Proof of Theorem 1.2)
```

```claim
id: n-by-n-mss-exist-for-n-ge-4
statement: For every integer n >= 4 there exists an n x n magic square of
  squares (all entries distinct positive integers, all squares, all 2n+2 line
  sums equal). More generally for d >= 3 there is n0(d) such that an n x n magic
  square of d-th powers exists for all n >= n0(d).
hypotheses: n >= 4; distinct positive integer entries; proof is by the
  Hardy-Littlewood circle method (system too singular for Birch/Rydin-Myerson;
  needs the diagonal-form version of Brudern-Cook and a partition result on the
  coefficient matrix)
holds-here: no (the n = 3 case is EXCLUDED from Theorem 1.2 and is precisely the
  open conjecture this run targets; the circle method's column-independence
  threshold is not met at n = 3)
status: proved (settles Várilly-Alvarado's Conjecture 1.1 that n0(2) = 4)
bearing: neighbouring-result only. Shows the obstruction at n = 3 is genuinely
  different from n >= 4 (existence settled there); gives no structural
  information about the 3x3 case. Corroborates that the 3x3 difficulty is
  small-n-specific and is not a saturation/quasihyperbolicity fact that would
  also forbid n >= 4.
anchor: research/sources/rome-yamagishi-magic-squares-of-powers-2024.full.md
  (Theorem 1.2, Theorem 1.3, eq. (2.2))
answers: may-exist-large-n (closes the "do magic squares of squares exist at
  all" question for n >= 4; n = 3 stays open)
```

## Does this source help?

**Marginally — it is a neighbouring result, not a 3x3 input.** It settles
existence for n >= 4 by the circle method and leaves n = 3 open. The value to
this run is (a) confirming the open question is n=3-specific, and (b) the
intro's geometric note: Bremner/BTVA22 show the 3x3 surface cut out by 6 quadrics
in P^8 contains only finitely many genus-0/1 curves and (per Lang) only finitely
many rational points outside them — a supporting hint that 3x3 is rare or empty,
not a proof. No claim here bears directly on the 3x3 modern proof.

## Source

Rome, Nick and Yamagishi, Shuntaro. "On the existence of magic squares of
powers." arXiv:2406.09364v2 [math.NT], 4 Sep 2024.
https://arxiv.org/abs/2406.09364