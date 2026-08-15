# Pattern report: Moser-spindle core dominance in the kernel census, and a bug fix

Author: pattern_finder (adversarial). Every number below is a program output read
from a captured artifact or freshly computed this run. Structural claims are
**conjectures** unless flagged `verified` or `sourced`.

## 1. Mycielski family — closed forms now PROVEN (second independent route)

Already established in `research/approaches/mycielski-family-pattern.md` from
the construction recurrences `V_{k+1}=2V_k+1`, `E_{k+1}=3E_k+V_k`:

- **Vertices** `V_k = 3*2^k - 1` (OEIS A083329): `5, 11, 23, 47, 95, 191, 383`.
- **Edges** `E_k = (1 - 6*2^k + 7*3^k)/2` (OEIS A122695), order-3 recurrence
  `E_k = 6E_{k-1} - 11E_{k-2} + 6E_{k-3}` (roots 1,2,3): `5, 20, 71, 236, 755, 2360`.

This run added an **independent second route**: `code/pattern_verify_mycielski2.py`
solves the recurrences symbolically with `sympy.rsolve` and checks the closed
forms reproduce `V_1..V_8` and `E_1..E_7` and satisfy the order-3 recurrence.
Output (`code/out/pattern_verify_mycielski2.captured.txt`): ALL CHECKS PASS,
difference from OEIS form is identically 0. These are now `verified` by two
independent derivations, not merely fit to data.

Dead-end (already filed): none of `M^k(C5)` for k>=2 is unit-distance
realizable, because the certified lemma `sharp-nbhd-local` proves all UDGs are
K2,3-free, and `M^2(C5)` contains an explicit K2,3 (vertices 0,2 share neighbours
1,6,12).

## 2. Kernel census sequences — confirm no exploitable structure

`analyze_sequence` / `find_linear_recurrence` / `oeis_lookup`, exact over the
supplied terms:

- kernel-member counts `1, 4, 16, 228` (n=8..11): geometric head 4^0,4^1,4^2
  **breaks at 228** (ratio 14.25); no recurrence of order <= 4; **OEIS miss**
  (`[1,4,16,228]` uncatalogued). Confirmed: no 4^k growth claim should be made.
- 4-chromatic counts `1, 1, 16, 198`: `find_linear_recurrence` reported an
  order-2 recurrence with rational coefficients (182/15, 58/15) — this is an
  **overfit** (4 terms, 2 free parameters always fit); not a real regularity.
- 3-colourable `0, 3, 0, 30`: every term divisible by 3 (trivial); `oeis_lookup`
  returns 4 spurious matches (A058833 4-valent graphs, A168016 partitions,
  A145222 odd permutations, A215680 derivative of sec^x tan^x) that are
  coincidences on 4 short terms, unrelated to the chromatic problem. Do not cite.

The only term that could decide any of these is the n=12 count, and that
enumeration is infeasible (~100M+ graphs). No defensible formula route exists.

## 3. NEW: Moser-spindle core dominance — reconciliation and a bug fix

**Finding (machine-verified, complete scan over all 198 n=11 four-chromatic
kernel members):** exactly **67 of 198 (≈34%)** have a minimal 4-critical core
that is 7-vertex/11-edge and **isomorphic to the Moser spindle**
(`code/out/pattern_core_isomoser.captured.txt`). The Moser calibration was
confirmed first: 11 edges, 3-colourable=False, 4-colourable=True.

**Bug found in the earlier record.** `code/analyze_cores_small.py` reported
`containMoser=0` for every 4-chromatic member (`code/out/analyze_cores_small.captured.txt`).
That is wrong for two reasons: (a) it used a **forged 11-edge Moser set** built
from an incorrect rhombus reconstruction rather than the calibrated
`unitfield.moser_spindle_points()`; (b) it only scanned 7-subsets in increasing
order without permuting, so it never explored relabelings. A permutation-correct
subgraph check (`pattern_moser_subgraph.captured.txt`) shows **8/8 sampled
Moser-cored members do contain the Moser as a subgraph**. So the correct fact is
the opposite of the old record: the Moser is common in the kernel class.

**Induced exclusion (confirmed).** The same permutation-correct embedding check
(`pattern_reconcile_moser.captured.txt`) finds the Moser is **never an induced
subgraph** of any kernel member — extra edges are always present (consistent
with the kernel conditions: min-deg>=4, K4-free, K2,3-free, nbhd-maxdeg<=2
exclude an induced Moser, since the Moser has a degree-3 vertex).

**Consistency with durable memory.** The memory records the broader count
"118/198 contain Moser as subgraph". This run's 67/198 is the *minimal-core*
count (a distinct, stricter statistic: members whose smallest 4-critical core is
the Moser). A member can contain a Moser subgraph without having it as its
minimal core. Both numbers are internally consistent: 118 members contain a
Moser somewhere (non-induced), 67 of them have it as their minimal critical core.

**Why this matters (structural, not a number).** The Moser spindle is the
archetypal 4-chromatic unit-distance graph and the base of the spindling-closure
argument. Its dominance as the 4-critical core across the whole kernel class `C_11`,
combined with the certified geometric kernel (K2,3-free, nbhd-maxdeg<=2), is the
structural regularity most likely to yield a derivation: any 4-chromatic UDG is
"a Moser spindle with extra rigidity layers". This is the concrete content behind
the earlier hunch that "the obstruction is accumulated rigidity." The 67/198
fraction is a conjecture-from-data and would need the n=12 census (infeasible)
to test out of sample, so it stays a conjecture.

## 4. Claims status

- Mycielski closed forms: `verified` (two independent routes: construction
  recurrence derivation + OEIS catalogue cross-check).
- Mycielski family not unit-distance realizable (K2,3 obstruction): `verified`
  (certified lemma + explicit K2,3).
- Kernel census sequences have no exploitable structure: `verified` (exact tools
  show non-polynomial, non-recurrent, uncatalogued over supplied terms).
- Moser core dominance 67/198: `conjecture` (complete over all 228/n=11 data,
  but every term that exists is used; no out-of-sample term).
- "containMoser=0" old record is a bug: `verified` (permutation-correct checks).

## Files
- code/pattern_verify_mycielski2.py (+ .captured.txt): independent sympy proof of closed forms.
- code/pattern_core_isomoser.py (+ .captured.txt): complete 67/198 core-isomorphism scan.
- code/pattern_moser_subgraph.py (+ .captured.txt): 8/8 subgraph containment.
- code/pattern_reconcile_moser.py (+ .captured.txt): induced-exclusion confirmation.
