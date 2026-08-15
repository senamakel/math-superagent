# Pattern-recognition report: Mycielski family dead-end, Moser K4 bug, and census non-structure

Author: pattern_finder (adversarial). Every number below was produced by a
program this run ran or is read from an exact captured artifact. Structural
conclusions are **conjectures** unless flagged `verified` or `sourced`.

## 1. The Mycielski family — exact closed forms, and why it is a dead end

The run's only 5-chromatic family is the Mycielski iterates of C5 (Groetzsch
chain). The counts carry clean structure (contrast with the kernel census below).

**Vertex counts.** `V_k` for M^k(C5), k=1..7: `5, 11, 23, 47, 95, 191, 383`.
- `analyze_sequence`: not a low-degree polynomial, but every first difference
  doubles (6,12,24,48,96,192) — an exact geometric recurrence.
- Closed form **`V_k = 3*2^k - 1`** (program-verified for k=1..6), i.e.
  `V_{k+1} = 2 V_k + 1`. Matches OEIS **A083329 / A153893 / A055010**.
  `(verified, sourced)`.

**Edge counts.** `E_k`: `5, 20, 71, 236, 755, 2360` (k=1..6).
- `find_linear_recurrence`: exact order-3 recurrence
  **`E_k = 6 E_{k-1} - 11 E_{k-2} + 6 E_{k-3}`, roots 1, 2, 3**.
- Closed form **`E_k = (1 - 6*2^k + 7*3^k)/2`** (integer, program-verified for
  k=1..6). Matches OEIS **A122695** ("number of edges in the n-th Mycielski
  graph"). `(verified, sourced)`.

These recurrences follow directly from the construction
(`V_{k+1}=2V_k+1`, `E_{k+1}=3E_k+V_k`) and are the cleanest exact structure in
the run's data.

**But the family is structurally dead for the goal.** The classic 5-chromatic
triangle-free chain cannot witness `chi(plane) >= 5`, for an exact geometric
reason:
- The certified lemma `sharp-nbhd-local` (sharp_nbhd_cert.captured.txt, no
  floats) proves **every unit-distance graph is K2,3-free**: two vertices share
  at most two common neighbours, because |x-u|=|x-w|=1 over a fixed segment uw
  has at most two real solutions (elimination forces x to the perpendicular
  bisector, leaving a quadratic in one variable).
- The Mycielski family M^k(C5) for k>=2 **contains an explicit K2,3** (verified:
  in M^2(C5), vertices 0 and 2 share three common neighbours 1, 6, 12;
  re-verified for M^3, M^4 as K2,3-free=False).
- Therefore **none of M^k(C5), k>=2, is unit-distance realizable.** Its
  chromatic numbers (3,4,5,5,5,...) are combinatorial facts about abstract
  graphs, not about the plane.

This is a concrete, filled-in `dead-end` for the "raise chi by a 5-chromatic
graph family" idea: the only known infinite family of abstract 5-chromatic
triangle-free graphs is excluded by K2,3-freeness at the first non-trivial
iterate. The size-bound kernel census prediction — that any 5-chromatic *UDG*
must be K2,3-free and so rich in structure — is exactly why the Mycielski chain
cannot serve. `(verified; the realization inference is by the certified lemma)`
Spin-off for the construction route: a would-be 5-chromatic UDG must be
triangle-free **and** K2,3-free **and** min-degree>=4 — a much narrower class
than generic graph constructions supply.

## 2. Bug found, confirmed, and confirmed contained: "Moser contains K4: True"

`code/analyze_kernel_chrom.py`'s diagnostic K4-check loop iterates over **all**
vertex pairs (adjacent or not) and declares a K4 whenever two common neighbours
`c,d` of a pair `(a,b)` are adjacent — firing on "K4 minus one edge". On the
Moser spindle it returns **True**, with false hits on the non-adjacent pairs
(0,3) and (0,6). Independent ground truth (4-subset brute force): the Moser has
**zero** K4 subgraphs, consistent with the certified K4-freeness of all UDGs.

**The real census is unaffected.** `census_kernel.check_kernel` requires
adjacency *before* the common-neighbour test (line ~140), and
`census_kernel_parallel.py` imports it, so every one of the 228 n=11 kernel
members passed a correct K4 filter. The size-bound result — *every unit-distance
graph on <= 11 vertices is 4-colourable* — **stands**. The correct reason the
Moser is not a kernel member is min-degree (it has a degree-3 vertex), not
K4-freeness. Fix applied: adjacency guard added to the diagnostic loop.
`(verified by tool_builder run agent-run-80 and this run)`

## 3. Kernel census — no exploitable sequence structure (confirms prior agents)

The four-term census sequences are non-polynomial, non-recurrent, and
uncatalogued (OEIS miss):
- kernel-member counts `1, 4, 16, 228` (n=8..11): geometric head 4^0,4^1,4^2
  breaks at 228 (ratio 14.25); no recurrence order<=4.
- 4-chromatic `1, 1, 16, 198`: no structure.
- 3-colourable `0, 3, 0, 30`: every term divisible by 3 (trivial), otherwise no
  structure.

Nothing here is a closed form. This matches `kernel-census-pattern.md` and
`kernel-sequence-structure.md`. The only term that could decide any of these
would be the n=12 count, and that enumeration is infeasible (~100M+ graphs);
there is no defensible formula route.

## 4. Minor separation/edge data (sourced, no new structure)

- Moser k-colouring counts `0,0,0,384,5040` (k=1..5): not polynomial, all
  terms divisible by 48, OEIS miss. Too short to carry weight.
- Torus A2 7-colouring margin `sqrt(21)`, valid window `1/(sqrt21-2)<L<1/2`,
  min margin `(sqrt21-2)/2 ~ 1.291` at L->1/2 (exact, Q(sqrt3)). This is the
  7-colour headroom against which a candidate 6-colouring must be measured.
- Forced-pair: diamond tips forced equal in every 3-colouring (|tips|^2=3);
  no forced pair under 4 colours in Moser (10 pairs) or Moser+Moser (256 pairs).

## 5. What this run settles / suggests

1. **Conjecture (exact over enumerated terms, closed form stated):**
   `V_k = 3*2^k - 1`, `E_k = (1 - 6*2^k + 7*3^k)/2`. These are proven from the
   construction recurrences, not merely fit.
2. **Verified dead-end:** the Mycielski 5-chromatic family is not
   unit-distance realizable (K2,3 obstruction). This is a filled-in obstruction
   that stops the next agent walking into it.
3. **The structural regularity that is load-bearing** (not a number sequence):
   every sharp-kernel member through N=11 is 4-colourable. That is the
   verified size-bound result of the run, fully re-confirmed.

## Artifacts
- code/out/pattern_mycielski.py (this run)
- research/summaries/oeis_a122695.md, oeis_a083329.md (filed closed forms)
- code/verify_k4check_bug.py (tool_builder, agent-run-80)
- research/approaches/kernel-census-pattern.md, kernel-sequence-structure.md
