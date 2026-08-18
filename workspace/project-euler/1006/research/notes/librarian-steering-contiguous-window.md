# Steering — contiguous-window reformulation of Ψ(k) (asserted, unverified) + librarian source map

Source: operator steering redirect, this run's active cycle. Not a claim — a
hypothesis every item below must be verified by the solver (tool_builder)
against `code/mech/mech_psi.py` / `code/brute.py` before being built on.

## The redirect's three claims

- **Claim 1 (the key set identity).** For every n with F_n > k, the k+1
  DISTINCT length-k factors of the Fibonacci word are exactly the k+1
  CONTIGUOUS windows at positions r = F_n−k−1 .. F_n−1 of the doubled standard
  word q_n q_n. The steer reports this verified outside the container at
  k = 3,5,6,8,10,13,17,21,26,34,40,55,70,100,144,200 and for EVERY n with F_n>k.
- **Claim 2 (the computation).** Ψ(k) = (full cyclic sum over all F_n windows of
  q_n q_n) − (sum over the FIRST F_n−k−1 windows). So Ψ is a prefix partial sum
  of the window values v_r² — no dedup, no O(k) intercepts.
- **Claim 3 (rehabilitates directive 1 for general k).** The full cyclic sum
  equals Σ_{j,jp} A(jp−j)·10^(2k−2−j−jp), A the cyclic autocorrelation of q_n,
  for ANY k < F_n. Directive 1's identity was never k=F_n−1-only as a statement
  about the CYCLIC sum; it was only that the cyclic sum ≠ Ψ in general, and
  claim 2 is precisely the correction.
- **Algorithm.** v_(r+1) = 10·v_r − y_r·10^k + y_(r+k), y the Fibonacci word;
  carry (v, Σv², Σv, 1) as a constant-size transfer matrix with step depending
  on the pair (y_r, y_(r+k)); collapse the product over the range by
  Fibonacci-block renormalisation (~87 blocks at 10^18).
- **Worked check at k=3** (consistent with the oracle): the five windows of
  q_4 q_4 = 0100101001 are 010,100,001,010,101; the last four are the four
  distinct factors; 10000+1+100+10201 = 20302 = Ψ(3). ✓

## Librarian source map — what the library holds that this route rests on

| Route component | On-disk source anchor |
| --- | --- |
| Position theorem (where each length-k factor occurs) | Sivasankar–Rama: **Theorem 7** — for F(n) ≤ k < F(n+1), the k+1 factors are z_j = f[j+1..j+k] (0≤j≤F(n)−1), else f[j+F(n+1)−k..+k] (F(n)≤j≤k) — `research/sources/fibonacci-word-2d-factor-complexity-ar5iv.full.md` (claim `fibonacci-sturmian-complexity`) |
| Standard word q_n, rotations/conjugates, PER/Farey | de Luca 1997 (`deluca-sturmian-words-structure-arithmetics-1997-docslib.full.md`, claim `standard-sturmian-PER-farey-construction`), Berstel DLT'95, richomme-saari-zamboni (`fibonacci-standard-factors-l0l1`) |
| "Conjugates of a Christoffel word = factors of a Sturmian word" bridge | `conjugate-christoffel-factor-sturmian` (bugeaud-reutenauer) |
| Cyclic autocorrelation A(d), three-distance/gap bookkeeping | `three-gap-three-distance-autocorrelation`, alessandri-berthe, van-Ravenstein three-gap |
| O(log) floor-sum / transfer-matrix / block-renormalisation machinery | `universal-euclidean-geometric-weight-fhq`, `oi-wiki-universal-euclidean-floor-sum`, `loj138`, `atcoder-math-floor_sum-doc`, `oi-wiki-euclidean-like-algorithm-en` |

**Honest limitation:** no single held source states Claim 1's exact
contiguous-position statement formula. The constituents (Sivasankar–Rama
position theorem + standard-word rotation structure + conjugate-Christoffel
bridge) all support the identity, but the exact "windows at
F_n−k−1..F_n−1 of q_n q_n" claim is verified in-container, not found verbatim in
the literature. A search for it returned no dedicated source (the position
theorem comes closest). So Claim 1 is solver-verification, not a literature
citation — the source map confirms the supporting theory is on disk.

## Stored
- Remembered to Cognee (this cycle's `remember_memory`).
- Full library-build record in `research/summaries/library-build-status.md`.
