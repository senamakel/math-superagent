# Directive 4 — carried out

**Split the Rule 90 proved core from the refuted absorption wrapper:**

- Created `research/notes/rule90-interior.md` — a clean proved claim (`rule90-interior-xor`): the {0,2} interior evolves under XOR = Rule 90 = Pascal mod 2. Proved by block-lemma diagonal argument, verified exhaustively n ≤ 13. Includes the closed form, the Sierpinski consequence at depths d = 2^j, and the sourcing (CHT §1, Wikipedia). Tagged `splits-from: rule90-identification-real-absorption-refuted`.

- The absorption wrapper (`research/approaches/rule90-absorbing-boundary.md`) remains refuted and unchanged. Its status line and the CLAIMS.md entry for `rule90-identification-real-absorption-refuted` both correctly note the split.

**Opened a thread for the depth prediction:**

- `research/threads/rule90-regeneration.md` — states the prediction sharply: at depths d = 2^j the Sierpinski kernel is all-1, so the halved row is the XOR of the whole width-(2^j+1) window. If XOR=1 for a stretch, the original row is all-2 — a clean regenerated block. The prediction is falsifiable and cheap to test against `blocks_depth1000.json`.

**Rewrote TASKS.md** to put the Rule 90 split and the depth-prediction test at the top, in order. The regeneration-thread content is preserved for its established criterion.

**Amended CONTEXT.md**:
- Run-state paragraph now names the Rule 90 split and the depth prediction as the live work.
- Added "Rule 90 interior dynamics — PROVED" to Established with the closed form, the Sierpinski consequence, and the split note.
- Replaced the stale "Regeneration iff lemma — REFUTED" Ruled-out entry with the correct accounting (off-by-one version refuted and withdrawn, corrected version established).
- Replaced the duplicate trailing "REFUTED" entry with the absorption-wrapper dead end.
- Updated the Gaps section to reflect that the criterion is established and the open question is why the boundary re-enters (2,4).
## 4 — from steer

You did exactly what was asked: candidate-regeneration-iff-refuted is in the ledger with the exact k values, code/out/check_regenerate_lemma.notes.md states it cleanly, and you correctly noted the oracle PASSED so the failures were the lemma's. That is the right handling of a refutation. Keep it.

The more interesting thing you produced is rule90-identification-real-absorption-refuted, which contains a proved part you should separate out and promote on its own: the {0,2} interior of a Gilbreath row evolves under the halved operator as XOR, i.e. Wolfram Rule 90, i.e. Pascal mod 2. If that is proved at the block-lemma apex then it is a structural identification of the interior dynamics and it deserves its own claim, distinct from the absorption idea that was refuted. Splitting them stops a refuted wrapper from burying a proved core. Do that split now.

Then use it. Rule 90 from a single 1 gives the Sierpinski triangle, and its defining feature is that the pattern REGENERATES full-width rows at k = 2^j: at those depths the row is all 1s across the light cone. If the interior really is Rule 90, that is a mechanism for block-length regeneration that is structural rather than empirical, and it predicts regeneration at specific depths you can check against your own record. Your minima were [13,24,96,97,175,2762,5939,31525,...] - test whether the jumps sit where Rule 90 says they should. That is a sharp, falsifiable prediction and it is cheap.

Ledger: asserted went 22 to 27 while checked stayed at 3 and proved went 5 to 6. exa_search 37 to 49, downloads 59 to 74, frontier 309 to 361 with 311 unworked. You are accumulating library faster than you are converting it. Stop downloading and spend the next attempt entirely on the Rule 90 split and the depth prediction above.

Done. Two sentences as promised:

**Split:** `research/notes/rule90-interior.md` now holds the proved Rule 90 interior identification as its own claim (`rule90-interior-xor`), complete with the closed form and the Sierpinski consequence at d = 2^j — tagged `splits-from` the refuted absorption wrapper, which stays dead in `research/approaches/rule90-absorbing-boundary.md`.

**Use:** `TASKS.md` is rewritten so the next attempt's first job is to test the depth prediction from that identification against `blocks_depth1000.json` — the Sierpinski kernel being all-1 at powers of 2 means regeneration at those depths is a structural prediction, not an empirical guess. A new thread `research/threads/rule90-regeneration.md` states it sharply and falsifiably.
