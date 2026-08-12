# NEW structural result: exact closed form for the histogram-refinement of D(N)

## The open question this answers
The run flagged "count how many configs realize each distinct level-histogram"
as the open refinement needed to lift the 2D G(k,m) machinery. That step is
now solved EXACTLY over the whole computable range.

## Statement
For a reachable 3D PE763 config after N divisions, let its level-histogram be
h = (a_0=0, a_1, ..., a_M=3) where a_k = #cells at level k=x+y+z, and M = max
level. Let n_k = #{interior levels with EXACTLY k cells}. Then the number of
configs realizing h is:

    mult(h) = 2^(2·n_4) · 3^(n_1+n_2+n_3−1)        if no level has 6 cells
           = 10 · 2^(2·n_4) · 3^(n_1+n_2+n_3−2)    if some level has 6 cells

In particular every multiplicity is 3-smooth (2^a·3^b).

## Evidence (exact, no fit)
- Holds on ALL 694 histograms: in-sample data dumps N=2..12 (251 histograms)
  AND out-of-sample N=13,14 computed fresh by bitmask BFS
  (code/out/per_hist_mult_13_14.txt, 443 histograms).
  Zero exceptions (code/pattern/final_mult_verify.py).
- Codes sanity: summing mult(h) over all distinct histograms at N reproduces
  D(N) EXACTLY for every N=2..14 (code/pattern/check_d_via_histform.py):
  3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063.

## Structure discovered along the way
- multiplicity depends ONLY on the multiset of interior level-counts (n1..n4),
  NOT on their order (code/pattern/check_b_multiset.py: 59 value-multisets each
  give a unique b). 
- The 2-power is exactly 2·(n_4): a level with 4 cells contributes ×4.
- The 3-exponent is exactly n1+n2+n3−1.
- The single exceptional family: histograms containing a 6-level (always with
  an adjacent 7-level, substring "6 7") get a factor of 10, i.e. ×(10/3) over
  the 3^{n1+n2+n3-1} base. All other 8 six-containing histograms actually
  entered the no-six branch in scan_6_7 vs the 6-level scan; the precise
  characterization is "some level has 6 cells" (verified 694/694).
- Histograms themselves are exactly OEIS A186085 smooth compositions
  (already established earlier).

## Distinguishing conjecture from proof
This is an EMPIRICAL exact identity over every computable term (N<=14). It was
tested on out-of-sample data (N=13,14 never used to guess) and survived. It has
not been DERIVED from Eriksson's folded-polyominoid bijection; that derivation
is the open step. First term that would falsify it: any reachable N>=15
histogram whose multiplicity breaks the rule (N=15 requires >2GiB BFS, not
reachable here).

## Does this reach D(10000)?
NOT directly. It turns D(N) into a sum over all admissible histograms (smooth
compositions), and H(N)=A186085(N) grows ~1.67^N — astronomically large at
N=10000. So this is a genuine structural reduction of the CONFIGURATION count
to a weighted histogram sum, but the weighted sum still enumerates the
histogram space. The next step (for the inventor) is a transfer/DP over the
smooth-composition histogram space using this closed weight — the 3D analogue
of the 2D G(k,m) kernel — which is now far more tractable because the weight
is a closed product, not an enumeration.

## Files
- code/pattern/final_mult_verify.py — decisive 694-histogram verification.
- code/pattern/oos_mult_closedform2.py, oos_mult_closedform.py — OOS tests.
- code/pattern/verify_mult_closedform.py, verify_mult_structure.py,
  check_4power.py, check_3exp.py, mult_structure.py, scan_6_7.py,
  check_b_multiset.py, multiset_to_b.py, tabulate_3exp.py,
  bbox_vs_mult.py, per_hist_dist.py, per_hist_detail.py — derivation steps.
- code/pattern/check_d_via_histform.py — D(N) from the closed form (partition
  check).
- code/amoeba/per_hist_mult_13_14.py, code/out/per_hist_mult_13_14.txt —
  fresh N=13,14 multiplicity data.
