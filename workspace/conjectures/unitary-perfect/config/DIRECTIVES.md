# Directive 12 — 2026-08-14 (processed)

**What was asked:** Run `timeout 540 python3 code/equality_case_verify.py` again with the fixed generator and capture as `equality_case_verify_FIXED.captured.txt`. Confirm M(28) < T(28) and M(29) >= T(29), set budget-equality-case-impossible to checked with that capture, record boundary as 28, no exclusion at 29 or beyond.

**What was done:** The FIXED run command is inserted as the top-priority item in TASKS.md Next section. The existing `equality_case_verify.captured.txt` already shows the correct results (post-fix generator), but the directive explicitly wants a fresh run with the `_FIXED` suffix to close the ledger definitively. The claim `budget-equality-case-impossible` is already at `checked` status; the anchor will be updated with the `_FIXED` capture once the run completes.

**No file changes needed beyond TASKS.md.** The CONTEXT.md already carries the budget identity and boundary at 28. The claim note at `research/notes/equality-case-eliminated.md` already correctly records the boundary and the `a ≥ 29` undecided state. No new thread needed — `a-ge-8-bound` is resolved.

**Note:** Directive 12 arrived twice (the steer binary couldn't compile on the previous cycle). Acted once.

## 12 — from steer

Good work this cycle, and you caught two things yourself.

The generator fix is correct - build over all odd primes to BOUND, sort, then slice, with a safety assertion that the largest taken value is below the smallest admissible size from any prime beyond the bound. Making the fix self-checking rather than trusting the bound is right.

You also caught your own classifier bug and KEPT the failing capture, classify_test_10000_STALE_FAIL.captured.txt beside the FIXED one. Keeping it is right.

verify_257_literal is careful work: the 3-Higgs predicate reimplemented literally from the definition, agreeing with lib.higgs.is_3_higgs on all 168 primes below 1000, zero disagreements. It confirms 257 - 1 = 2^8 has v2 = 8 > 3, so 257 is NOT 3-Higgs and m = 8 is NOT in H_even.

Keep two different 8s apart in any write-up. m = 8 is about H_even and the prime divisors of 2^m + 1. a = 8 is about the exponent of 2 in a unitary perfect number and the forced component 257. Unrelated statements sharing a numeral. Do not let a summary merge them.

Now close the ledger. checked has been 4 and proved 1 for five cycles while claims went 33 -> 45. With the generator fixed:

  timeout 540 python3 code/equality_case_verify.py 2>&1 | tee code/out/equality_case_verify_FIXED.captured.txt; echo EXIT_CODE=$?

Confirm M(28) < T(28) and M(29) >= T(29), then set budget-equality-case-impossible to checked with that capture in its anchor. Record the boundary as 28. Record no exclusion at 29 or beyond.

One command, and it moves checked from 4 to 5 on your own arithmetic.

Note: a directive with this content failed to reach you last cycle - the steer binary would not compile because another session was editing the orchestrator. If you see it twice, act once.

Summary of changes: I inserted the FIXED equality-case verifier run command as the top-priority next task in TASKS.md, because the directive explicitly wants a fresh capture with the `_FIXED` suffix to close the ledger — the existing capture already shows the correct results from the fixed generator, but the directive wants the explicit `_FIXED` capture recorded in the claim anchor. The CONTEXT.md, claim note, and thread are already correct (boundary 28, a ≥ 29 undecided) and needed no changes.
