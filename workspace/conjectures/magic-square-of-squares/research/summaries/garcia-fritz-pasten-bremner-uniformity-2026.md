# García-Fritz & Pasten, "A note on Bremner's conjecture and uniformity", arXiv:2604.04850 (2026)

[[garcia-fritz-pasten-bremner-uniformity-2026]]

**Status: abstract page only on disk** — the `.full.md` is the arXiv landing page; the paper body (and the cited previous work) was never downloaded. Everything below is at abstract level.

## What it establishes (abstract-level)

- **Bremner's conjecture (1998):** elliptic curves over Q having *long sequences of distinct rational points whose x-coordinates are in arithmetic progression* must have **large rank**.
- **Strong form proved** (by the same authors, some years ago): combining Nevanlinna theory with the **uniform Mordell–Lang theorem of Gao–Ge–Kühne**, one obtains: *if the ranks of elliptic curves over Q are uniformly bounded, then so are the lengths of the AP-of-x-coordinates sequences*.
- **This note's new contribution:** a much more direct proof of that last statement using the **height-uniform Mordell theorem of Dimitrov–Gao–Habegger**. The method is flexible and extends to x-coordinates in finitely generated multiplicative groups and to geometric progressions; connections to a possible semiabelian uniform Mordell–Lang are discussed.

## What it does NOT say

- It does **not** prove uniform boundedness of ranks (that remains open — Elkies' conjecture). The statement is conditional: bounded ranks ⇒ bounded AP-lengths.
- It does **not** address the magic square of squares directly, and it gives no quantitative bound on AP length (no explicit constant is quoted in the abstract).

## Implications for this run — the single most valuable external corroboration on disk

- **Bremner's elliptic reduction** (`robertson-elliptic-reduction`): a 3×3 MSS ⇔ three points of `2E(Q)` on `E: y² = x(x²−c²)` with x-coordinates in **arithmetic progression**. That is exactly the structure of Bremner's conjecture.
- The García-Fritz–Pasten theorem says the *length* of such progressions is controlled by the rank: **long AP of x-coordinates forces high rank**. Combined with Bremner 1999's empirical note (only one non-torsion AP triple found in a small search, on a rank-3 curve), this is the first structural reason the four-AP condition is hard: a full MSS needs three AP points on one curve, and rank is the scarce resource that the AP-length/rank correspondence ties the obstruction to.
- **Conditionality is essential:** if ranks over Q are not uniformly bounded (Elkies), the theorem's conclusion is vacuous. So this source *motivates* a rank/resource view of the MSS obstruction but does **not** prove it.

## Does not help computationally

- No explicit bound, no new variety, no density statement transferable to the K3 or to the Φ-set. The value is at the level of "the additive-AP obstruction is a rank phenomenon", and that is exactly the direction the run's adopted Chabauty–Coleman approach (rk J < g) is already pointed.

```claim
id: bremner-conjecture-uniform-bounded-rank-implies-bounded-ap
statement: (García-Fritz–Pasten, abstract) If the Mordell-Weil ranks of elliptic
  curves over Q are uniformly bounded, then the length of any sequence of distinct
  rational points on a single elliptic curve whose x-coordinates are in arithmetic
  progression is uniformly bounded; the strong form of Bremner's 1998 conjecture
  follows from uniform Mordell-Lang (Gao-Ge-Kühne) and is re-proved here via the
  height-uniform Mordell theorem (Dimitrov-Gao-Habegger).
hypotheses: uniform boundedness of ranks over Q (open); E/Q an elliptic curve;
  AP of x-coordinates. The structure holds for this problem (three AP
  x-coordinates on E: y²=x(x²−c²) via robertson-elliptic-reduction), but the
  decisive rank-unboundedness hypothesis is open and the MSS needs only THREE
  points, not a long sequence.
holds-here: partial
status: asserted (abstract level; body not on disk)
bearing: frames the four-AP obstruction as a rank-scarcity phenomenon; supports the
  adopted Chabauty-Coleman direction (rk J < g is the same resource comparison);
  does not provide an explicit bound or a proof for the 3-point case;
  consistent with Bremner 1999's empirical rank-3 AP observation
anchor: research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md
```