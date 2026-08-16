# Publication status, re-confirmed (current)

Fresh confirmation of the published/preprint split, so the open request
`exact-current-published-c8b8` carries a current as well as a historical marker.
This updates, rather than replaces, `published-record-status.md`.

## Result

As of this confirmation (live arXiv/EJC searches), nothing in the
published/preprint split has moved since `published-record-status.md` was
written:

```claim
id: published-status-current
answers: exact-current-published-c8b8
statement: The published record for the union-closed constant remains Yu,
  "Dimension-Free Bounds for the Union-Closed Sets Conjecture", Entropy
  25(5):767, 2023 (arXiv:2212.00658), giving ≈ 0.38234. The iid-entropy bound
  (3−√5)/2 is separately peer-reviewed: Alweiss–Huang–Sellke, Electron. J.
  Combin. 31(3):P3.35 (2024), doi:10.37236/12232. Cambie (arXiv:2212.12500,
  c≈0.3823455) and Liu (arXiv:2306.08824, c≈0.38271) remain arXiv preprints;
  Liu appears only at the IEEE CISS 2024 conference (58th Annual Conf. on
  Information Sciences and Systems), not in a journal. No source exceeds
  ≈0.38271 unconditionally.
hypotheses: F nonempty finite union-closed, F ≠ {∅}; constant is fraction of |F|.
holds-here: true
status: sourced (current live-search confirmation)
bearing: confirms the record the run must beat and that the (3−√5)/2 barrier,
  though now peer-reviewed (AHS EJC 2024), is NOT the best published constant —
  Yu's 0.38234 is. Prevents citing Liu's conditional 0.38271 as the record.
anchor: exa_search on arXiv listings 2212.12500 (marked Preprint), 2306.08824
  (CISS 2024), 2212.00658 (Entropy 2023), and EJC 10.37236/12232 (2024-09-20)
```

The order of events, confirmed against the sources themselves (all full texts
held):
Gilmer (0.01, 2211.09055) → five concurrent refinements to (3−√5)/2 above
the iid-entropy barrier (AHS, Chase–Lovett, Sawin, Pebody) → Sawin's
dependent-coupling escape → Yu (≈0.38234) and Cambie (≈0.3823455) make it
computable → Liu's conditionally-iid ≈0.38271 (conditional, appears from the
conditional hyperplane/inequality literature and is confirmed numerically
under stated hypotheses).

## What this means for the run

- The number to beat in print is **0.38234...** (Yu, Entropy 2023).
- (3−√5)/2 is the **iid-entropy barrier**, now a theorem in print (AHS, EJC
  2024), but NOT the record: dependent couplings escape it.
- Liu's ≈0.38271 is the strongest known value but is conditional on
  numerically-verified structural hypotheses and is not journal-published; cite
  it as a conditional preprint result at most.
