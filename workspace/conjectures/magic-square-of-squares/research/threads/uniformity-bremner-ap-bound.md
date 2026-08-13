# Thread: Uniformity bound from Garcia-Fritz–Pasten on the Robertson curve

```thread
question: Does the Garcia-Fritz–Pasten theorem (Theorem 1.8: AP length ≤ C^(r+1) on
  elliptic curves) combine with the Robertson reduction to give a finiteness
  result for the 3×3 MSS?  Specifically: a full MSS requires an AP of length 4
  on the Robertson curve E_e: y² = x(x²−e⁴).  If rank(E_e) can be bounded from
  above by something provably small, then length-4 APs may be ruled out by the
  C^(r+1) bound.

status: open

rests_on:
  - robertson-elliptic-reduction (Established)
  - bremner-conjecture-proved (Garcia-Fritz–Pasten Theorem 1.8, newly downloaded)
  - height-uniform-mordell (Dimitrov–Gao–Habegger 2020)
  - uniform-mordell-lang (Gao–Ge–Kühne 2021)

immediate-steps:
  1. Determine the exact form of the Robertson curve for an MSS centre e.
     The reduction: an AP x₁, x₂, x₃, x₄ on E_e: y² = x(x²−e⁴) with
     xᵢ, xᵢ±e² all squares.  This is not quite "points in AP" in the usual
     sense — verify the exact statement.
  2. What is known about rank(E_e) when e = lcm(mᵢ²+nᵢ²) for a putative
     Φ-quadruple?  The K3 surface in Bremner II gives NS rank 12; does this
     bound the rank of the specialised elliptic curve?
  3. The constant C in Theorem 1.8 is NOT explicit in the Garcia-Fritz–Pasten
     paper — it comes from Rémond's quantitative Mordell–Lang bounds.  The
     Dimitrov–Gao–Habegger constant c(g,d) for genus 2, d=1 is also not
     explicit.  So the bound is ineffective for computation.  Still, if
     r ≤ some small number (say ≤ 3) and C is moderate, the bound C^(r+1)
     might still allow length 4 — need to know whether C could be as small as
     ~2 or ~3, or whether it's astronomically large.
  4. Alternative: Theorem 1.2 gives a conditional result: *if* ranks of
     elliptic curves over Q are uniformly bounded, *then* so are AP lengths.
     The uniform rank boundedness conjecture is widely believed (Park–Poonen–
     Voight–Wood heuristic).  If we assume it, the MSS problem reduces to a
     finite computation — though still possibly beyond reach.  This would be
     a genuine partial result: "Assuming uniform boundedness of ranks, the
     3×3 MSS conjecture is decidable by finite computation."

risks:
  - The constant C may be so large that C^(r+1) > 4 for any plausible r,
    giving no contradiction.
  - The Robertson reduction may require points in 2E(Q) (x-coordinates of 2P),
    not arbitrary rational points, and the Garcia-Fritz–Pasten theorem is
    about *all* rational points — but that only helps, since 2E(Q) ⊆ E(Q).
  - "AP" in the Garcia-Fritz–Pasten sense means x-coordinates of distinct
    rational points form an AP.  The Robertson reduction requires specific
    x-coordinates — need to match the definitions precisely.

next: spawn scholar to claim-block the Garcia-Fritz–Pasten paper, then symbolic_math
  to write the Robertson curve and the AP condition as exact polynomial equations,
  then research to find the smallest known rank of E_e for small e with many
  representations as sum of two squares.
```