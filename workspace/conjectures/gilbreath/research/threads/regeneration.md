```thread
question: Under the sublinear jump law j ~ C·b^0.388, does the inter-giant gap grow strictly slower than b^0.388? If so, b_k ≥ 1 for all k follows.
status: live — Directive 25 reconciles geometric description (×1.68/event over 12 points) with sublinear exponent 0.388 (asymptotic decay of b_next/b → 1). The target is now: prove the inter-giant gap G_k is bounded, or grows as o(b^0.388).
rests-on: |
  - Step law (PROVED): b_{k+1} ≥ b_k ⟺ (x,y) = (2,4), else b_{k+1} = b_k − 1.
  - Recharge identity (PROVED): b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1).
  - Sublinear jump exponent: log(jump) vs log(b) slope 0.388 over 43 positive-jump events (depth 1000). Anchors: code/out/surplus_renewal_structure.md. Under this, j ~ C·b^0.388, so b_next/b = 1 + C·b^(-0.612) → 1.
  - Geometric growth description (Directive 24): ×1.68/event, R²=0.94 vs linear 0.78 over 12 genuine giants at b ~ 10³–10⁶. Description of the record, not a proved law — inconsistent with sublinear exponent in the limit.
  - Giant jumps (13): at i = 34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161. 12 genuine, 1 capped (i=161). Claim bigjump-cap-characterization-1000.
  - Inter-giant gaps in rows: 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15. Δi between consecutive giant events.
  - Width-degradation: k* = 162, all 12 genuine giants have flooring ≥ 536,885 > 1000. code/out/directive24_width_degradation.md.
  - CHT 2026, Eppstein 2011, block lemma, Rule 90 interior, drain law — all as before.
blocked-by: nothing — Directive 24 items 1-2 DONE. Next is inter-giant gap trend analysis.
next: |
  1. **Inter-giant gap trend (Directive 25 core).** Gaps in rows between consecutive giants (i=34,56,64,68,94,96,110,112,126,130,134,146,161): 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15. Fit against i (event index) and b (post-jump block). Report alongside j. If gaps bounded while j ~ b^0.388 → ∞, b_k ≥ 1 follows.
  2. **Reconcile geometric description with sublinear exponent.** Compute expected ratios b_next/b = 1 + j/b from j ~ C·b^0.388 at the 12 b-values; compare to observed ratios. Is the discrepancy a sample-size effect or a tension?
  3. **Restate the reduction.** Under j ~ C·b^0.388, the conjecture holds if inter-giant gap G_k < C·b_k^0.388 — i.e., gap grows strictly slower than b^0.388. The "geometric growth → giants keep arriving" framing is too weak if the ratio decays; the correct object is the gap-vs-jump inequality.

# Regeneration thread — the gap-between-giants reduction

**Directive 25 points out an internal inconsistency.** Two established facts:

1. **Sublinear exponent** (depth 1000, 43 positive-jump events):
   log(jump) vs log(b) slope = 0.388. So j ~ C·b^0.388.

2. **Geometric growth description** (Directive 24, 12 genuine giants):
   post-jump b grows ×1.68/event (R²=0.94).

These are inconsistent in the limit:

```
b_next / b = 1 + j/b = 1 + C·b^(-0.612) → 1   as b → ∞
```

The ×1.68/event over 12 points at b ~ 10³–10⁶ is a finite-sample description,
not an asymptotic law. If 0.388 is real, the ratio must decay.

**What survives.** The sublinear exponent is based on all 43 positive-jump
events, not only the 12 giants, and is the more robust statistic. If it holds:

> b_k ≥ 1 for all k  ⇐  G_k < C·b_k^0.388 for all k after startup

where G_k is the inter-giant gap (rows between consecutive giant events)
and C is the constant from j ~ C·b^0.388. Since consumption is exactly 1 per
row, each giant jump j must exceed the gap G. If G grows strictly slower than
b^0.388 while j grows as b^0.388, then eventually j > G for all future giants
and b never reaches 0.

**Inter-giant gaps from the 13 giants.** Event indices i = 34, 56, 64, 68, 94,
96, 110, 112, 126, 130, 134, 146, 161. Gaps in rows:

```
22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15
```

Range 2–26, mean 10.6, median 9. No clear upward trend from 12 points. If the
gap is bounded (or grows as log b, or any o(b^0.388)), the conjecture follows.

**The open question.** Does the inter-giant gap grow, and at what rate? Fit
against i and against b. The answer determines whether the reduction closes
or whether the gap growth itself is the obstruction.

## Prior work absorbed

- **Step law + recharge identity** reduce the conjecture to Σ(j_i+1) ≥ k−2.
- **Sublinear exponent** says j ~ C·b^0.388.
- **Giants are genuine** (12/13) — the heavy tail is real.
- **Giants are not erosion-recovery** (arrive 1–13 rows after previous event).
- **×1.68/event** is a finite-sample description, not an asymptotic law.
- **Mean event rate λ̂=0.585** (Directive 19) is superseded.

## Data available
- `code/out/blocks_depth1000.json`; `code/out/surplus_renewal_table.captured.txt`; `code/out/directive24_geometric_growth.md`; `code/out/directive24_width_degradation.md`; `code/out/event_gap_analysis.captured.txt`