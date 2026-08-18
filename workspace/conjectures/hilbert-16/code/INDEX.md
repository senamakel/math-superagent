# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle: exact count of limit cycles for radially symmetric polynomial fields (displacement function sign = roots of A(u), u=r²). Reproduces all worked examples: cubic→1 (r=1), linear centre→0, linear expanding focus→0, two-cycle A=(1−u)(2−u)→2, semi-stable A=(1−u)²(2−u)→1 (u=1 double root excluded). Non-radial fields refused honestly. Exact rational arithmetic, Sturm counts; avoids float/integration/sampling. Runs as `python code/brute.py`. |
| `df2a_slow_divergence_symbolic.py` | Exact symbolic slow-divergence/ECT reconnaissance for the DF2a validation model; guards against all problem.md worked examples via brute.verify_all, then computes Wronskians of polynomial and logarithmic channels. Evidence only for the narrow local toy, not a DF2a cyclicity theorem. |
| `i6b_four_passage_oracle.py` | Exact oracle for claim h16-i6b-four-passage-ect-obstruction: reproduces all problem.md worked radial examples through the naive oracle, then refutes closure of ECT systems under addition and detects boundary rank loss via exact Wronskians. |
| `i6b_second_type_toy.py` | Exact symbolic toy probe testing Wronskian rank of iterated-log second-type Dulac contributions; evidence against an unjustified ECT shortcut, not a dynamical counterexample. |
| `i6b_second_type_transseries_oracle.py` | Exact bounded-support transseries oracle testing four second-type Dulac-passage composition and projected Wronskian; evidence for the restricted ECT route. |
| `inspect_reduce.py` | _(undescribed)_ |
| `lu_analytic_remainder_probe.py` | Bounded exact symbolic counterprobe showing finite Taylor/Bautin data plus analyticity does not imply root uniqueness; evidence delimiting Lu H^3_14 analytic remainder gap. |
| `lyap_audit.py` | _(undescribed)_ |
| `lyap_extend.py` | _(undescribed)_ |
| `lyap_extend2.py` | _(undescribed)_ |
| `membership_check.py` | _(undescribed)_ |
| `membership_full.py` | _(undescribed)_ |
| `mono_counts.py` | _(undescribed)_ |
| `naive_examples_oracle.py` | Small bounded naive radial limit-cycle oracle reproducing all worked examples in problem.md; validation oracle only, not a general solver. |
| `problem_examples_and_i6b_report.py` | Exact SymPy oracle reproducing all worked displacement examples and testing the minimal ECT cancellation obstruction for the adopted I^1_6b route. |
| `sequence_audit_current.py` | Exact audit of extracted Bautin monomial-count, complement, and denominator sequences; tests recurrence candidates and exact formulae. |
| `sequence_check_complement.py` | Exact independent check of the Bautin monomial-count complement formula on the seven supplied terms. |
| `sequence_check_d18.py` | Exact regression check of the Bautin monomial-count complement conjecture through the computed d=16 term and explicit d=18 prediction. |
| `sequence_current_patterns.py` | Exact polynomial and recurrence checks for newly available Bautin monomial-count terms through degree 16; evidence for sequence-pattern audit. |
| `sequence_deeper_audit.py` | Exact audit of computed Bautin monomial-count, complement, and denominator sequences; tests the surviving quadratic complement conjecture and recurrence hypotheses. |
| `sequence_extract_rerun.py` | Exact audit of computed Bautin monomial-count and complement sequences, including recurrence checks and falsifier predictions. |
| `sequence_falsifier_check.py` | Exact check of the provisional quadratic complement formula for Bautin monomial counts against computed terms and its first uncomputed falsifier. |
| `sequence_falsifier_d18.py` | Exact arithmetic target for the first falsifier of the observed Bautin complement formula; deliberately does not claim an L18 computation. |
| `sequence_pattern_breaker.py` | Exact continuation and falsifier calculator for the reported Bautin complement formula; also checks denominator ratios. |
| `sequence_tool_run.py` | Exact SymPy audit of the investigation-produced Bautin focal-value monomial-count sequence and its complement; checks differences, constant-coefficient recurrences, and the proposed quadratic complement formula. |
| `sk_ceil_structure.py` | Exact-arithmetic verifier for the ceil(S_k) sequence: fractional-part periodicity mod 3 (k>=2), delta period 3, order-6 minimal annihilator check over k=2..199, sympy order-5/order-6 elimination; input: none, prints claims A-E. |
| `sk_crosscheck.py` | _(undescribed)_ |
| `sk_integerity.py` | Verifies by exact arithmetic (k=1..400) that S_k is integer iff 3 |
| `sk_recurrence.py` | _(undescribed)_ |
| `sk_sequence.py` | Computes exact S_k = 4^{k-1}(k-13/6)+(2k-1)/3 (Christopher-Lloyd/Li lower bound on H(2k-1)) and the guaranteed-count sequence. |
| `sk_solve_recurrence.py` | Solves and verifies constant-coefficient order-4 recurrences for S_k ((E-4)^2(E-1)^2) and S_{3j} ((E-64)^2(E-1)^2) by exact Gaussian elimination. |
| `sk_structure.py` | _(undescribed)_ |
| `sk_subseq_recurrence.py` | _(undescribed)_ |
| `sk_weight_hypothesis.py` | _(undescribed)_ |
