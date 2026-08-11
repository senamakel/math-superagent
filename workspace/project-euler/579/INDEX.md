# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace-wide method and evidence rules (restate the problem, run the small-case oracle first, exact integer arithmetic, no answer-space search, cite sourced claims). |
| `Folder` | Purpose |
| `README.md` | Short overview of the problem workspace and its file-map conventions. |
| `brute.py` | Brute-force oracle (naive, exact integer). Enumerates all distinct lattice cubes inside [0,n]^3 and counts C(n), S(n); the reference checker every other method is tested against. |
| `brute_output.txt` | Output of `brute.py` for n=1..6,10; all five oracle C/S values match (n=3, 6 extras also recorded). |
| `config.toml` | Runtime configuration: solver settings (exact arithmetic, cite sources, forbid exponential time/space) and the artifact file paths. |
| `frame_method.py` | Validates the efficient frame-based method: every cube = primitive frame × integer scale; Ehrhart pts(t); box-fit translation T(t). Enumerates primitive frames by direct vector-pairing. Verified against the oracle up to n=50 and collects frame-growth data. |
| `frame_method_output.txt` | Output of `frame_method.py`: n=1,2,4,5,10,50 all match oracle; primitive-frame growth n=20:119, n=100:3053, n=200:12129. |
| `goal.md` | The objective (PE 579) restated, the oracle values, and the 6 completion criteria. All 6 criteria DONE; final answer S(5000) mod 10^9 = 3,805,524 recorded. |
| `memory.md` | Working memory: established results (oracle values, frame method, power-sum), growth data, failed approaches, open questions. |
| `pointcount.py` | Independent lattice-point-count-only implementation, validated against the statement's two worked cubes (A total 64 = 56+8, B total 40 = 20+20). |
| `power_validate.txt` | Evidence `solution_power.py` is correct: Faulhaber P(k,n) vs a literal loop (k=0..6, n=0..200), oracle match, and exact (asserted) equality with the direct t-loop at n=50. |
| `problem.html` | The PE 579 problem statement, converted from the source page. |
| `problem.url` | Source URL (`https://projecteuler.net/minimal=579`), single line. |
| `prompts/` | Role-specific guidance files for each agent (see `prompts/INDEX.md`). |
| `reflections/` | Archived attempt verdicts; written by the solution loop itself (see `reflections/INDEX.md`). |
| `research/` | Externally sourced material: source summaries, full texts, and the run's verification scripts against them (see `research/INDEX.md`). |
| `scratchpad.md` | Temporary calculations not yet promoted to `memory.md`. Currently empty. |
| `solution.py` | Final PE579 solution: canonical primitive-frame enumeration via primary Hurwitz quaternions (Euler-Rodrigues, streaming, O(1) memory) + O(1) Faulhaber power-sum summation. THIS IS THE ANSWER SOURCE. Validated: frame-set identity vs frame_method n=1..200 (ALL YES), C/S oracle all OK, power-sum==direct-loop bit-for-bit PASS, independent route (verify_final.py) matches. S(5000) mod 10^9 = 3805524. Evidence in `solution_output.txt`. |
| `solution_power.py` | O(1)-per-frame Faulhaber power-sum summation. Reuses `frame_method.py`'s enumeration unchanged (import); only the t-summation differs. Validated bit-for-bit against the direct t-loop at n=50 and against the oracle. |
| `solution_output.txt` | Final evidence for `solution.py`: frame-set identity per n (1..200 ALL YES), C/S oracle matches, n=5000 C / S / S mod 1e9 = 3805524, bit-for-bit cross-check PASS, wall time, and independent-route (verify_final.py) confirmation. |
| `tasks.md` | Task checklist. All items DONE, including the final one: full `solution.py` verified and S(5000) mod 10^9 computed (3805524) and checked by an independent route. |
| `toolkit.md` | Documents every `toolkit.py` function (signature, returns, what verified it); kept in step with `toolkit.py`. |
| `toolkit.py` | Reusable exact-integer helpers shared by the scripts: `dot`, `norm2`, `corner_and_edges`, `count_points`. |
| `toolkits/` | One-function-per-file helper library (currently empty; see `toolkits/INDEX.md`). The working helpers live in root `toolkit.py` instead. |
| `verify_final.py` | Independently re-derived (no imports from solution.py) second route for n=5000: primary quaternion scan + self-written O(1) Faulhaber power sums. Confirms C,S,S mod 1e9, frame count match solution.py. |
| `verify_independent.py` | Independent machinery checks, not the final answer: (1) primary-quat logic — primary primitive odd-norm quats generate each primitive frame exactly once, N==edge length; (2) no primitive frame inside [0,n]^3 has even edge length (n<=80, incl. norm-cap-relaxed + box-fit variant); (3) C/S recomputed via frame+power-sum match the oracle; (4) `solution.py` quaternion key-set vs `frame_method`. Writes `verify_independent_output.txt`. |
| `verify_independent_output.txt` | Saved output of `verify_independent.py`. Tasks 1–3 all PASS. Task 4 was reported N/A because `solution.py` did not exist when this ran — that run predates `solution.py`, so Task 4 is now stale and should be rerun. |
