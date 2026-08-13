# Pech, "Carrés magiques 3×3 de carrés", December 2006

[[pech-carres-magiques-2006]]
Source: http://www.multimagie.com/Pech.pdf (8 pages, French). TIPE (undergraduate supervised project), school year 2005–06, advisor-tracked via Lucien Pech at ENS (lpech@ens.fr).

## What it establishes
A clear, self-contained **Gaussian-integer / sum-of-two-squares algorithm** to search the "magic hourglass" (the 7-square configuration: two diagonals + central column), and the claim that no full 3×3 MSS value with centre up to the searched bound exists.

**Setup (Section 1).** An hourglass `(a−b a−c a−d; a; a+d a+c a+b)`. Writing entries as squares and setting `A² = a`, `x²=a−b`, `y²=a+b`:
`2A² = x²+y²`, and with `x=u−v, y=u+v` this is `A²=u²+v²`. Lemme 1: the primitive Pythagorean parameterisation `(A,u,v)=(m²+n², 2mn, m²−n²)`, giving
`b = 4mn(m²−n²)`, `c = 4rs(r²−s²)`, `d = 4uv(u²−v²)`
for the three decompositions `A = m²+n² = r²+s² = u²+v²`. Hence **A must be a sum of two squares in at least three different ways**. The horizontal lines are equal (`=3a`) iff **`b+c+d = 0` (equation E)**.

**If a is even** then `4|a` and `4|b,c,d`, contradicting pairwise-coprimality of the hourglass entries — so in the primitive case `a` is odd, hence a sum of two squares of opposite parity.

**Algorithms (Sections 2–4).**
- *Buell's algorithm* (Algo 1): test all `A = i²+p² ≤ Amax`, keep lists of pairs per `A` (only odd i, even p), and for each `A` with ≥3 decompositions test equation E modulo `M` (values too big for 64-bit). Complexity `O(Amax + Amax^{3/2}/I)`, linear in `Amax` when the chunk size `I ≈ √Amax`; measured `time/Amax` ≈ 1.2 at `Amax=2·10¹²`. Buell's 1998 run verified no hourglass for `Amax = 5·10¹²` (about a year on an SGI station).
- *Improvement* (Algo 2/3): restrict `A` to products of `P₁` primes (`p≡1 mod 4`), using the Brahmagupta–Fibonacci identity twice, so only `A` with ≥3 divisors of `P₁` type are tested. Recursive `tester_produits` builds `A=∏ p_k^{α_k}`; `tester_gros_facteurs` handles `A` with a large (`>p_max`) prime factor. Also `O(Amax)`.

**Numerical results (table, Section 4).** For `Amax = 10⁹ … 5·10¹²`, counts of solutions to E modulo `2⁵²`–`2⁴⁴`: 6/10, 4/6, 6/10, 6/9, 6/8. One large example, a **perfect square hourglass modulo 2⁵²** (better than Buell's mod 2⁴⁶):
```
m=6881928, n=4357501;  r=1580988, s=7990571;  u=216213, v=8142604
```
plus four odd solutions modulo `2^45`–`2^47` for `Amax=10¹³` (m,n,r,s,u,v listed). These are **modular only** — they satisfy the entries being squares simultaneously modulo a power of two, not over Q.

## Implications for this run
- **Confirms the Gaussian factorisation line already in `research/approaches/gaussian-integer-factorisations.md`** and the `Φ`/Pythagorean-split structure: an hourglass needs the centre to be a three-way sum of two squares, and the four-cell differences come from `4mn(m²−n²)` terms — exactly the run's `S(e)` / `f(m,n)=4mn(m²−n²)/(m²+n²)² ∈ Φ` objects.
- The equation `b+c+d=0` is the additive relation among the three pair-decompositions' differences; at the rational / `Φ` level this is the run's "no Φ-triple" obstruction. Pech's mod-2⁵² example shows the local (mod 2-power) obstruction fails — consistent with the problem being locally solvable, so no modular sieve can prove non-existence.
- Confirms Buell's `5·10¹²` figure is an **hourglass** bound (centre `A ≤ √Amax·...`, in the specific `b+c+d=0` sense), not a full-MSS bound — matching the caveat already in `buell-search-for-magic-hourglass-1999.md`.

```claim
id: pech-hourglass-sum-of-two-squares-and-additive-e
statement: A magic hourglass (7-square: two diagonals + central column) with centre a=A² needs A a sum of two squares in at least 3 ways, A=m²+n²=r²+s²=u²+v², giving cell differences b=4mn(m²−n²), c=4rs(r²−s²), d=4uv(u²−v²); the row/column equality is b+c+d=0. If a is even then 4|a and 4|b,c,d contradicting coprimality; so a primitive hourglass has odd a. Pech gives a perfect-square hourglass modulo 2^52 and odd solutions modulo 2^45..2^47 (modular only, not over Q).
hypotheses: primitive hourglass of distinct squares; A positive
holds-here: yes — this is exactly the Φ/Pythagorean structure the run uses (m²+n² form, 4mn(m²−n²) differences, additive relation among them)
status: asserted (source's derivation reproduced by inspection; algorithms documented but not re-run here)
bearing: corroborates the run's Gaussian-factorisation approach and the local-solvability ↛ global obstruction
anchor: research/sources/pech-carres-magiques-2006.full.md
```
