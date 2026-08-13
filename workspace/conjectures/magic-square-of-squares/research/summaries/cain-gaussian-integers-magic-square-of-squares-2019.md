# Cain, "Gaussian Integers, Rings, Finite Fields, and the Magic Square of Squares" (arXiv:1908.03236, 2019)

Full text: `research/sources/cain-gaussian-integers-magic-square-of-squares-2019.full.md` (25.5 KB, complete 15-page paper, v2, 12 Aug 2019 — real PDF, not an abstract page).

## What the paper establishes

**Gaussian reformulation of the magic-hourglass problem.** Theorem 2.2: every integer solution of `r² + t² = 2s²` (an AP of two squares about `s²`) is given by three integer parameters `m, n, k`. Lemma 3.1 reinterprets this in `Z[i,√k]`: there is `ω ∈ Z[i,√k]` with `k` an integer such that the AP condition becomes factorisation in the ring.

**Theorem 4.2 (the central structural identity).** If a magic hourglass of squares exists, then there exist `x, y, z ∈ Z[i]` such that
```
Im[x²y²z²] = −4·Im[x²]·Im[y²]·Im[z²]   (Eq. 4.1 / Cor. 4.2)
```
This is the concrete arithmetic identity behind the quartic-factorisation reformulation claimed in the abstract. Proof: the four APs of the hourglass pull back, in the Gaussian integers, to a product identity on imaginary parts.

**Theorem 4.1 + equivalences ⇒ search method.** The 3×3 MSS problem is equivalent to solving quartic polynomials with factorisation constraints over an abelian extension of `Q`; specialising the extension to `Z[i]` (the Gaussian integers) yields a new search method. Cain provides code (Algorithm 6.1) for finite fields.

**Finite-field/ring analysis (§5–7).** A `3×3` magic square of distinct squares exists in a field `F_q` iff `q` has ≥9 distinct squares. Computed results, by case:
- **All even-order fields are "Parker"** (Lemma 5.1, Cor. 5.1) — duplicate entries forced.
- `F_3, F_5, F_7, F_9, F_11, F_13` Parker (fewer than 9 squares, Cor. 5.2).
- `F_19, F_23, F_27` Parker (hand+computed count of solutions to `x²+y²=0,2`, Cor. 5.3).
- `F_17, F_25` Parker (Cor. 5.4, via central-0 parametrisation Lemma 5.4).
- **`F_29` is the smallest non-Parker field** (Theorem 5.1) — the explicit construction lives there.
- Rings `Z/nZ` analysed with conjectures (Cor. 7.1 ff.) enumerating in which rings a MSS can be built.

## Implication for this run

This is the **primary source** behind the `cain-quartic-gaussian-reformulation` claim, which was previously `asserted` from the abstract alone. The full text confirms the reformulation is **real, concrete, and checkable**: Theorem 4.2 gives an *explicit* integer identity (`Im[x²y²z²] = −4 Π Im[xᵢ²]`) that any solution must satisfy, not a vague "it's a quartic over a field". The identity is the run's own `verify_phi_doubling.py` starting point (Im identity = f(m,n)), so the Gaussian route and the Φ-route are the same object seen twice — Cain's Eq. 4.1 is the group law behind `f(m,n) = Im((m+ni)⁴)/4`.

Cain's own near-miss applications (§8) and the finite-field census are a separate, self-contained result (which fields are non-Parker) that does **not** bear on the rational/integer problem except as a check that distinctness is achievable over some finite fields.

```claim
id: cain-quartic-gaussian-reformulation
statement: The 3x3 MSS problem is equivalent to solving quartic polynomials with factorisation
  constraints over an abelian extension of Q; specialising to the Gaussian integers Z[i] gives
  a concrete search method. The central identity is: a magic hourglass of squares exists iff
  there are x,y,z in Z[i] with Im[x^2 y^2 z^2] = -4 Im[x^2] Im[y^2] Im[z^2] (Thm 4.2). Separately,
  the smallest finite field admitting a 3x3 MSS of distinct squares is F_29 (Thm 5.1); all
  even-order fields and F_3..F_11,F_13,F_17,F_19,F_23,F_25,F_27 are Parker (duplicates forced).
hypotheses: none beyond the problem statement for Thm 4.2; finite-field claims over F_q / Z/nZ.
holds-here: yes (the reformulation is exact and gives the explicit Thm 4.2 identity); the
  finite-field census is a different problem (distinctness over finite fields, no bearing on Q)
status: checked (full text read this cycle; previously asserted)
bearing: the Gaussian 2-descent identity is the group law behind the run's own f(m,n)=Im((m+ni)^4)/4
  Φ-reduction — same object, two names; and the finite-field results give an independent
  "distinctness is possible somewhere" check, not a rational obstruction
anchor: research/summaries/cain-gaussian-integers-magic-square-of-squares-2019.md
```

## Sources that do not help / notes

- The earlier scholar digest marked this "only the abstract page downloaded (no body)" — **stale**. The full 15-page PDF has been on disk since this cycle.
- Cain's §5 finite-field work is closer to a recreational census than a theorem about `Q`; cite it as a catalogue-style result (which fields are non-Parker), not as evidence about the rational problem.
