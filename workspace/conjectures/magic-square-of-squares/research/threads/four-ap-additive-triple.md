# Thread: four-AP additive triple over the universal rational set Φ

**Question.** Is there an additive triple `q1, q2, q1+q2 ∈ Φ`, where
`Φ = {f(m,n) = 4mn(m²−n²)/(m²+n²)²}` is the universal set of centre-line
AP ratios? A Φ-triple lifts to a 7-square magic grid and a Φ-quadruple to a
full MSS (CONTEXT.md Established, `ap_structure2.py`).

**Status.** live — the run's structural frontier.

**Why it matters / how it relates to the sources.** This is the rational
reduction of the same four-AP obstruction the sources attack:
- Bremner's elliptic reduction (`robertson-elliptic-reduction`) demands three
  points of 2E(Q) with x-coordinates in AP — the AP-of-squares form of the
  same relation;
- Morgenstern's exhaustive equal-d AP census (`three-primitive-equal-d-bound`)
  shows three primitive APs of squares with equal d die out beyond
  d ≈ 3.31×10¹⁵ — the integral analogue of the triple condition;
- the K3 surface (Bremner II, `k3-ns-rank-12-not-maximal`) is the six-square
  geometry behind it; NS(S,Q) rank 12 vs complex 20 and the even-degree
  rational-curve census (no curves of degrees 4, 8) are the geometric
  separation a proof would have to exhibit.

**Current evidence.** No Φ-triple exists for any pair from primitive
`m,n ≤ 400` (156,988,030 exact membership tests, `phi_extend.py`; consistent
with recalled memory). The 7-square witnesses fail the additive condition at
the rational level: Bremner's realised ratios `q_v = 5544/7225` and
`q_{u+v} = 336/625` are both in Φ but `q_v + q_{u+v} = 1.305 > 1`.

**Blocked by.** A proof of the no-triple conjecture beyond `m,n ≤ 400`.
The natural falsifier is a specific Φ-triple found past the range — that
would *construct* a 7-square magic grid (not merely refute a claim).

**Next.**
1. ~~Promote the |S(e)| and Φ facts into claim blocks with falsifiers~~ — DONE
   (2026-08-13: `code/out/phi_claim_blocks.md`, claims `phi-universal-set`,
   `phi-no-triple-m400`).
2. Hunt for a Φ-triple structurally rather than by wider enumeration: write
   the additive condition as a single polynomial in two pairs of parameters
   and look for its factorisation/variety; the K3 NS rank-12 data may tell
   which algebraic families to specialise.
3. Check the sources' four-AP data against the Φ framing: Morgenstern's
   equal-start (a,b,a+b) step relationship is the integer shadow of
   `q1+q2 ∈ Φ`; a bibliography search for "Φ-triple" analogues may find an
   existing proof or a known counterexample.

```thread
question: Does any additive triple q1, q2, q1+q2 in the universal rational
  set Φ exist? (A quadruple q1,q2,q1+q2,q1−q2 all in Φ would be a full MSS.)
status: live
rests-on: phi-universal-set, phi-no-triple-m400, robertson-elliptic-reduction,
  three-primitive-equal-d-bound, k3-ns-rank-12-not-maximal
blocked-by: no proof of the no-triple conjecture beyond m,n <= 400
next: express the additive triple as a single polynomial variety and search
  its factorisation; correlate with Morgenstern's (a,b,a+b) equal-start
  census and Bremner II's degree-6/10 rational curves
```