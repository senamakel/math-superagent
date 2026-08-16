# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Once you have a brute-force oracle for T(10^4)=41333, use spawn_candidates to explore at least three genuinely different implementations of the split-and-sum search in parallel (for example: recursive digit splitting with pruning, a digit-DP over carries, and a meet-in-the-middle over prefixes). Then read them back with attempt_diff and have the archivist adopt the one that agrees with the oracle and reaches 10^12.

The task ledger is seeded and ordered forward: understand-by-executing → brute-force-oracle (T(10⁴)=41333) → identify-governing-theory → derive-efficient-method → explore-candidates (three parallel split-and-sum implementations via spawn_candidates) → adopt-winning-implementation (read back with attempt_diff, archivist adopts) → implement-solution → verify-answer. I opened `research/threads/split_and_sum_search.md` marking the parallel-branch-and-select direction as live. No CONTEXT.md or request_research change was warranted — T(10⁴)=41333 is already given in `problem.md`, so nothing new entered the shared context, and the directive names internal workflow tools rather than an external knowledge gap.

## 2 — from steer

Do not wait for the theory task to finish. Call spawn_candidates NOW with three approaches: (1) brute force over squares r^2 <= N testing every split of the digit string, (2) recursive/DFS over digit splits with pruning on partial sums, (3) precompute reachable sums per digit-block length and match against r. Each candidate must reproduce T(10^4)=41333 against its own brute force before reporting. This is the priority task.

Done. I made the candidate branching the priority exactly as directive 2 demands: `explore-candidates` now sits first in the task ledger with its `blocked-by` cleared and its detail rewritten to "call spawn_candidates NOW" with the three named approaches, each self-checked against T(10^4)=41333. I also updated `research/threads/split_and_sum_search.md` to reflect the three concrete candidate encodings and to drop the theory/derivation gating, so the thread matches the live plan. No CONTEXT.md change was warranted — T(10^4)=41333 and the root reduction are already in Established, and nothing new entered shared context.

## 3 — from steer

Priority: call spawn_candidates now with three approaches — (1) brute force over r with every split of the digits of r^2, (2) DFS over splits with pruning on the running sum, (3) precomputed reachable block-sums matched against r. Each must reproduce T(10^4)=41333. Then spawn archivist to read them with attempt_diff and adopt the winner.

The task ledger already reflected the directive — `explore-candidates` is the top open row with the exact three approaches and "call spawn_candidates NOW", and `adopt-winning-implementation` (archivist → attempt_diff → adopt) follows it. I made two changes that bring the rest of the record into line: updated the live `split_and_sum_search` thread to use the directive's three approaches and removed its now-false blockers (the oracle is already reproduced), and closed `understand-by-executing` and `brute-force-oracle` as done with evidence from `code/out/commands.log`, since `brute.py` already reproduces the four examples and T(10^4)=41333. No CONTEXT.md change was needed — its Established and Method sections already state the root reduction and the independent b-file route that the winning candidate will be checked against.

## 4 — from steer

Priority: call spawn_candidates with three different implementations of the split-and-sum search, each verified against T(10^4)=41333. Do NOT sit in await_agents waiting for them — record each on the attempts ledger, then spawn archivist immediately to read the branches with attempt_diff and adopt_attempt the winner. The candidates commit as they go, so the archivist can read them while they are still running.

Two changes made, both driven by the directive's instruction not to sit in `await_agents`:

- **`explore-candidates`** — updated the detail to say "record each candidate on the attempts ledger as it spawns; spawn the archivist IMMEDIATELY — do not await the candidates."
- **`adopt-winning-implementation`** — changed from "Read the three candidate implementations back" (which implied waiting for them) to "Spawn the archivist immediately after spawn_candidates, not after the candidates finish. The archivist reads the three running branches with attempt_diff and adopt_attempt the winner as it emerges."
- **`research/threads/split_and_sum_search.md`** — the `next` field now says "record each candidate on the attempts ledger as it spawns; then spawn the archivist IMMEDIATELY."

No change needed to CONTEXT.md — the directive is about execution sequence, not about what every role should know. The tasks `identify-governing-theory` and `derive-efficient-method` remain open but are no obstacle: `explore-candidates` already says to proceed without them, which the directive confirmed.
