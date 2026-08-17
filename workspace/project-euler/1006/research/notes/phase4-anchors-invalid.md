# Scholar cycle — Phase-4 anchors are invalid (contradiction resolved toward chisel)

## What this cycle established

The reference library is fully digested and its claims are anchors-verified
(see scholar-digest-complete.md and library-build-status.md). This cycle the
scholar re-verified the load-bearing claim anchors against the full texts and
encountered one genuine **contradiction within the run itself** that nothing
else had closed: the standing Phase-4 acceptance anchors are computed by an
invalid method.

## The contradiction

- **Standing belief (CONTEXT.md, tasks `implement-solution` / `solution-builder`,
  threads file, solution.py Phase 4):** Ψ(10^4) ≡ 16242174 and
  Ψ(10^6) ≡ 77578256 (mod M) are the **acceptance anchors** the O(log)
  universal-Euclidean method must reproduce.
- **Direct evidence against (chisel board post + the run's own exact code):**
  both anchors were produced by `Psi_collapse`, which uses the Toeplitz
  autocorrelation identity A(d) = max(0,m−t)+max(0,m−(N−t)). Phase 3 of the
  *same file* (solution.py) proves C(j,jp) = A(jp−j) holds **only at
  k = F_n − 1**, and P3-extra shows collapse disagrees with the valid direct
  method at general k (k=200: collapse 64554455 vs direct 83031232).

## Verification (analytic, this cycle — no execution tool available)

The collapse is valid exactly when the k+1 factors are the F_n cyclic rotations
of a standard/Christoffel word, i.e. k = F_n − 1.

- k = 10000: needs F_n = 10001; no Fibonacci equals 10001 (F_21=10946).
  → **NOT of form F_n − 1.**
- k = 10^6 = 1000000: needs F_n = 1000001; no Fibonacci equals 1000001
  (F_31=1346269). → **NOT of form F_n − 1.**

Corroborated by the run's own exact tools (`pattern-hunt-pe1006-cycle3.md`,
`check_toeplitz_defect.py` k=1..400): the pair-correlation matrix is fully
Toeplitz (all defects 0) exactly at k = 1,2,4,7,12,20,33,54,88,143,232,376 =
F_n − 1, and not at 10^4 or 10^6.

**Conclusion:** both Phase-4 anchors (16242174, 77578256) were computed by a
method proved invalid at those k, so they are **wrong acceptance criteria**.
Reproducing them is not a valid gate; the O(log) method should instead be
checked against the **valid direct method** (psi_direct / mech_psi, verified
== brute for k ≤ 400) at several general-k values, and against brute at the
largest oracle-reachable k.

```claim
id: phase4-anchors-invalid
statement: The Phase-4 acceptance anchors Psi(10^4) mod M = 16242174 and
Psi(10^6) mod M = 77578256 are invalid: both were computed by Psi_collapse,
which uses the Toeplitz autocorrelation identity A(d) that Phase 3 of
solution.py proves holds only at k = F_n - 1 (k = 1,2,4,7,12,20,33,54,88,143,
232,376,...). Since 10^4 and 10^6 are not of the form F_n - 1 (no Fibonacci
equals 10001 or 1000001), the collapse is out of domain there, so both
numbers are wrong acceptance criteria and must not gate the O(log) method.
hypotheses: the collapse identity C(j,jp)=A(jp-j) is valid iff k = F_n - 1;
k=10^4 and k=10^6 are both not of that form.
holds-here: yes (verified analytically: F_21=10946 not 10001; F_31=1346269
not 1000001; and the run's exact Toeplitz-defect scan k=1..400 is fully
Toeplitz only at F_n - 1).
status: asserted (chisel board post, corroborated by solution.py P3-extra and
pattern-hunt-pe1006-cycle3.md; independent recomputation by the valid direct
method is still pending a Python execution tool)
bearing: Removes 16242174 / 77578256 as the acceptance test; the O(log)
monoid should instead be validated against the valid direct method
(psi_direct / mech_psi, == brute for k <= 400) at general- k values such as
10^3 and 10^4.
contradicts: (the standing tasks/CONTEXT belief that these two residues are
the Phase-4 acceptance anchors)
answers: no open request id (this corrects a task gate, not a research
request)
anchor: code/out/solution_checks.md (P3 FAIL, P3-extra FAIL, Phase 4 values),
code/pattern_hunt/check_toeplitz_defect.py, pattern-hunt-pe1006-cycle3.md
```

## Action for the solver

1. Do NOT use 16242174 / 77578256 as the acceptance test.
2. To get valid anchors at moderate size, run the O(k) valid direct method
   (`psi_direct` from solution.py, or `mech_psi`) at e.g. k = 10^3, 10^4
   (O(k^2) = 10^8 big-int ops — feasible) and record those as the residues the
   O(log) monoid must match. `code/out/verify/check_phase4_anchors.py` is
   written to do the k=10^4 case but needs a Python execution tool.
3. The O(log) universal-Euclidean monoid remains the correct primary route;
   only its acceptance anchors were wrong, not the method.

## Sources / anchors

- solution.py Phase 3, P3-extra; code/out/solution_checks.md
- pattern-hunt-pe1006-cycle3.md (Toeplitz defect list, exact k=1..400)
- chisel board post (teams/BOARD.md)
- The O(log) monoid itself: fhq `universal-euclidean-geometric-weight-fhq.full.md`,
  OI-wiki, LOJ138, AtCoder floor_sum — all anchors verified intact this cycle.
