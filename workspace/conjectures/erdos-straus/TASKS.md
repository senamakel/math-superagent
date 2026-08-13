# Tasks

## Directive 4 (steer): stop generating, attack one modulus

The operator's coverage recomputation across all three capture files gives 1451 blocks,
123 distinct (m,s) classes, 96.112676% coverage. The uncovered density factors over
independent prime groups as a product of (p − c_p)/p, every factor strictly positive,
so it is strictly positive for any finite set of families and converges to a positive
limit. It reaches zero only if for some single modulus m the generator realises **all**
m residues. That is now the whole problem.

## 1. The saturation question — modulus 23

23 is the smallest modulus with room: currently 9/23 residues realised, 14 avoided.
The finite, checkable question: can the Salez seven-equation generator produce
families for all 23 residues t mod 23? Either:

- [ ] **Exhibit families** for the 14 missing t-residues of modulus 23.
      Missing: [0,1,2,3,4,6,7,8,10,11,14,16,21,22] (against covered
      [5,9,12,13,15,17,18,19,20]).
      Use `search_subprogression.py` (the Salez-converse engine, 7 equations
      enumerated over (A,B,C,D,E,F) sextuples) focused on a = 840×23 = 19320,
      and check whether any (a,b) pair with the missing residue t appears.
- [ ] If some residues remain unrealised after a bounded search (state the search
      bounds), determine the **obstruction** — the arithmetic condition that stops
      those residues being reachable by the seven-equation generator. An obstruction
      is a proof about the method, worth more than another increment of coverage.
- [ ] State the result: either "modulus 23 can be saturated" (with the families) or
      "modulus 23 cannot be saturated, here is why."

## 2. Promote asserted families to checked — in bulk

The operator's ledger count: asserted went 36→50 while checked went 3→4. Every
family the generator has produced is provable in ℤ[k] by the cleared-denominator
test — that is mechanical. Do it in bulk:

- [ ] Run a script that reads all FOUND lines across all three capture files
      (`subprogression.captured.txt`, `extended_subprogression.full.txt`,
      `extended_subprogression.captured.txt`), re-derives x(k), y(k), z(k) from
      the Salez-equation parameters in each FOUND line, and runs `is_identity`
      (sympy `simplify(4/n - 1/x - 1/y - 1/z) == 0`) on every one.
- [ ] Report: total families, identity-pass count, identity-fail count.
      Write a claim block with all passing families at `status: checked`.
- [ ] Every family that passes is now `checked`, not `asserted`. This moves the
      bulk of them into the checked column at once.

## 3. Fix the failing command

From `code/out/commands.log`: recent runs have retry 6 and run-failed 5.
Read the log, identify which command is failing and why, and fix it before
writing new programs.

- [ ] Read the failing-command entry in commands.log.
- [ ] Fix the syntax or logic error.
- [ ] Re-run to confirm it passes.

## 4. Coverage update (operator-verified)

- [x] The operator has re-parsed all three capture files and recomputed
      coverage: 1451 families, 123 distinct (m,s) classes, 96.112676%
      coverage within n ≡ 1 (mod 840). Recorded in
      `code/out/coverage_update_extended.md`.
- [ ] Absorb the updated coverage claim into CONTEXT.md (replace the old
      94.72% figure; the 96.11% figure is now the established one).

## Done (prior cycles)

Oracle (`code/oracle.py`), parallel self-check, witness cross-check (12/12),
small brute sweep n≤200, the corrected n≡3 (mod 4) + even-case identities, and
the eight classical covering identities — all captured, identity-checked, and
recorded. Yamamoto 1965 tombstoned. MathWorld annotated as orientation-only.
The exa_search is dead (operator directive).