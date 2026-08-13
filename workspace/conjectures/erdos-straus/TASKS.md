# Tasks

## Directive 5 (steer): modulus 11 saturation, and run verify_current_coverage.py

The coverage triangulation is settled: 0.945305 and 0.961127 differ only by
input scope (one capture file vs three), and `independent_density_check.py`
confirms the density method by a structurally independent direct count over
K < 3·10⁶ converging to 0.94530. The density method is sound — stop
re-verifying it. The saturation question now has data from
`aggregate_subprogression.py`: M=11 has only 3/11 residues covered, missing
[0,1,2,3,4,6,8,9]. It is the smallest modulus and the cheapest test of
whether any modulus can be saturated at all.

**The next attempt is exactly one thing**: can the Salez seven-equation
generator realise the 8 missing residues mod 11, or is there an obstruction
forbidding some of them? Either answer is a result. An obstruction is a proof
about the method and ends the family search honestly.

- [ ] **Run `verify_current_coverage.py`** — the operator cannot run it (it
      imports sympy), so this run must. It identity-checks every FOUND line in
      `code/out/subprogression.captured.txt` and recomputes coverage. Capture
      to `code/out/verify_current_coverage.captured.txt`.
- [ ] **Modulus 11 saturation.** M=11 covered residues: [5, 7, 10]; missing:
      [0, 1, 2, 3, 4, 6, 8, 9].
      - Run `code/search_subprogression.py` focused on modulus a = 840×11 =
        9240, enumerating b ≡ 1 (mod 840) that are QNR mod 9240. Record which
        t-residues mod 11 appear.
      - For any residues remaining missing after a bounded search, attempt to
        prove an obstruction: the Salez seven equations with a = 9240 constrain
        b modulo the constants B,C,D,E,F; show that some residues
        s = (b−1)/840 mod 11 cannot satisfy any of the seven congruences for
        any choice of the constant parameters within bounded ranges.
      - State the result: either families for all 8 missing residues, or a
        precise statement of which residues are unreachable and why.
- [ ] **Bulk promote asserted → checked.** Run `is_identity` on every FOUND
      line across all three capture files (`subprogression.captured.txt`,
      `extended_subprogression.full.txt`, `extended_subprogression.captured.txt`).
      Report: total families, identity-pass count, identity-fail count. Every
      passing family flips from `asserted` to `checked`. (Carried from dir 4.)
- [ ] **Fix the failing command.** Read `code/out/commands.log`, identify which
      command is failing and why, and fix it before writing new programs.
      (Carried from dir 4.)

## Done (prior cycles)

Oracle (`code/oracle.py`), parallel self-check, witness cross-check (12/12),
small brute sweep n≤200, the corrected n≡3 (mod 4) + even-case identities, and
the eight classical covering identities — all captured, identity-checked, and
recorded. Yamamoto 1965 tombstoned. MathWorld annotated as orientation-only.
The exa_search is dead (operator directive). The 23-saturation thread is
deferred per directive 5 in favor of modulus 11.