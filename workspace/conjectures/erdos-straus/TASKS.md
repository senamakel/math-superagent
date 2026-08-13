# Tasks

## Directive 7 (steer): stop generating families. Saturate modulus 11, verify, and promote.

Three things only. Nothing else goes on the task list until these are done.

**Do NOT generate more families at new primes.** The last round tripled the
family count for 1.39 percentage points, and the newest primes gave the least —
41 gave 6/41, 43 gave 3/43. Generating further families at new primes is a
sunk-cost trap: it costs compute and produces nothing the saturation question
does not already settle. The uncovered density factors as a product of strictly
positive terms and reaches zero only if some modulus has all its residues
realised. M=11, the smallest modulus, has only 3 of 11 covered. Either saturate
it or prove it cannot be saturated. Either answer is a result.

The ledger is asserted=54, checked=6, proved=0. Every family in the capture
files has already been checked as an identity in ℤ[k] by the operator — the
work to flip them from `asserted` to `checked` is mechanical and still not
done.

### Priority 1: run `verify_current_coverage.py` and capture its output

The operator cannot run it (it imports sympy). This run must. The script
identity-checks every FOUND line in `code/out/subprogression.captured.txt` and
recomputes coverage from the verified set. Capture to
`code/out/verify_current_coverage.captured.txt`.

```
timeout 540 python3 code/pattern_mining/verify_current_coverage.py 2>&1 | tee code/out/verify_current_coverage.captured.txt
```

If the script fails, fix it and re-run. The capture file must exist and must
report `identity failures: 0` before anything else proceeds.

- [ ] Run `verify_current_coverage.py`, capture to `code/out/verify_current_coverage.captured.txt`

### Priority 2: modulus 11 saturation

M=11 covered residues: [5, 7, 10]; missing: [0, 1, 2, 3, 4, 6, 8, 9].

The Schinzel analysis (`code/pattern_mining/schinzel_residue_gap.py`) already
shows that for M=11 the QNR-allowed residues meeting the Schinzel requirement
are [3, 4, 5, 7, 10] — five classes. Of those, the generator has realised
[5, 7, 10] and left [3, 4] as the gap. The other six residues [0, 1, 2, 6, 8,
9] are either QR-blocked (b is a QR mod 11 when s=0,1,2,6,9) or non-unit
(s=8 makes b divisible by 11), and are Schinzel-forbidden: **no ℤ[k]-polynomial
identity can exist for them at modulus 11.**

So the saturation question reduces to two residues: can the generator realise
s=3 and s=4? Two approaches, run both:

- [ ] **Search for s=3 and s=4.** Run `code/search_subprogression.py` with a =
      9240, b values giving s=3 and s=4, with widened parameter bounds.
- [ ] **Prove obstruction for s=3,4 if search fails.** For residues the search
      cannot reach, examine the seven equations (14a–15d) with a=9240 and b
      fixed to show no choice of the constant parameters yields a valid family.
- [ ] **State the result.** Either families for s=3 and s=4 (closing the QNR
      gap at M=11), or a precise obstruction statement: "the Salez
      seven-equation generator cannot realise residues s=3 and s=4 at modulus
      11 because …". If the obstruction holds, M=11 proves the method has a
      hard ceiling below saturation.

### Priority 3: bulk promote asserted → checked

Every FOUND line in `subprogression.captured.txt` (838 blocks) is already
identity-checked by the operator at 0 failures. The extended files add 613
more. Run `is_identity` on every one across all three capture files, report the
counts, and flip every passing family's status. This is mechanical and blocked
only on Priority 1 completing.

- [ ] Run `is_identity` on all 1451 families across the three capture files.
      Report pass count, fail count. Flip passing families to `checked`.

### Housekeeping

- [ ] The `${PIPESTATUS[0]}` pattern in `commands.log` fails under `/bin/sh`
      (it is a bash feature). Use `python3 prog > out.txt 2>&1; echo
      EXIT_CODE=$?` instead of piping through tee when exit-code capture
      matters. Not urgent — the programs themselves ran fine.

## Done (prior cycles)

Oracle, parallel self-check, witness cross-check (12/12), small brute sweep
n≤200, corrected n≡3 (mod 4) + even-case identities, eight classical covering
identities — all captured and identity-checked. Yamamoto 1965 tombstoned.
MathWorld annotated as orientation-only. Exa_search dead (operator directive).
Modulus-23 saturation thread deferred.