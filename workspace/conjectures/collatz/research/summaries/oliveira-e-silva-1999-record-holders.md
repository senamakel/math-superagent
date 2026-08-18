# Oliveira e Silva 1999 — maximum excursion and stopping time record-holders

<!-- src: Tomás Oliveira e Silva, "Maximum excursion and stopping time record-holders for the 3x+1 problem: computational results", Math. Comp. 68(225) (1999) 371–384, DOI 10.1090/S0025-5718-99-01031-5. Full text: research/sources/oliveira-e-silva-1999-record-holders.full.md (AMS free PDF). -->

## What the source establishes

This is the primary source for the pre-Barina verification frontier and the
record-holder statistics:

- **Verification bound**: the 3x+1 conjecture was verified by exhaustive
  search up to n = 3·2^53 ≈ 2.702×10^16 (as a byproduct of the
  maximum-excursion search).
- **Maximum excursion**: for initial value n, max iterates empirically
  bounded above by roughly n^2·f(n) with f(n) constant or very slowly
  increasing; all t-record-holders (max-excursion records) found up to
  3·2^53, all σ-record-holders (stopping-time records) up to 6.8×10^12
  (earlier related work up to 5.6×10^13).
- Defines σ(n) = least positive k with T^(k)(n) < n; total stopping time
  σ∞(n) = least k with T^(k)(n) = 1.
- The record n below 10^17 cited in later work: n = 1,008,932,249,296,231
  with σ∞(n) = 1142.

This is the bound that later powered the Simons–de Weger m-cycle exclusions
(the "exterior computations" X0 referenced in the 2005 Acta paper) and was
superseded for verification by Barina's 2^71.

## Claims

```claim
id: oliveira-1999-verification-bound
statement: The 3x+1 conjecture was verified by exhaustive search up to n = 3·2^53 ≈ 2.702×10^16, finding all maximum-excursion record holders up to that bound and all stopping-time record holders up to 6.8×10^12. (Oliveira e Silva, Math. Comp. 68 (1999) 371–384.)
hypotheses: accelerated map T; exhaustive search implementation correct
holds-here: yes — this is the verification bound in force at the time of the Simons–de Weger 2005 m-cycle exclusions; superseded by Barina 2^71 for verification
evidence: proved in source (full text held)
status: verified-numerically
falsifies: a reproducible counterexample below 3·2^53, or an error in the search
```

```claim
id: oliveira-1999-record-holders
statement: The record-holder n below 10^17 has total stopping time σ∞(n) = 1142 (n = 1,008,932,249,296,231), and the maximum excursion t(n) is empirically bounded by n^2 f(n) with f slowly varying. (Oliveira e Silva 1999; the record figure as cited in Applegate–Lagarias 2002.)
hypotheses: none
holds-here: yes — documented extremal behavior of the map, relevant to the divergent-orbit arm
evidence: asserted by source and corroborated by Applegate–Lagarias 2002 (also held)
status: verified-numerically
falsifies: a reproducible computation giving a different σ∞ for that n
```
