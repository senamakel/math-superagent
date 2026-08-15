# NOT EXECUTED by the scholar

This verification script (`scholar_verify_n11.py`) was drafted to re-derive the
C_11 census from the 28 residue-slice files with a fourth, fully independent
oracle. The scholar role has no program-execution tool, so this file was
**never run** and produced **no captured output**. Do not treat anything here
as a result.

The N=11 size-bound result it would have re-checked is ALREADY verified in the
existing captured artifacts:
- code/out/census_kernel_n11_run.captured.txt (228 members, all 4-colourable)
- code/out/census_kernel_n11_test.captured.txt (independent backtracking: 0 fails)
- code/out/crosscheck_kernel_n11.captured.txt (249/249 members agree 4-colourable,
  SAT witness + backtracking, zero mismatches)
- code/out/kernel_slice_0..27.log (all 28 residue classes processed, complete)

See code/out/census-kernel-n11-result.md for the recorded claim blocks.
A coder/sat_solver role wanting a fourth route can run this file; until then it
is unverified draft code.
