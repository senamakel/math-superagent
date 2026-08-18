# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `PE1006.lean` | _(undescribed)_ |
| `Problem1006.lean` | Lean statements (all := by sorry) of the PE1006 structural claim: the infinite Fibonacci word as a characteristic/mechanical Sturmian word of slope 1/phi^2; the count |
| `brute.py` | Naive exponential oracle for Fibonacci subwords; reproduces the statement's F3, Psi(3), and Psi(10) anchors. |
| `check_christoffel_class.py` | _(undescribed)_ |
| `directive9_transfer.py` | Finite doubled-Fibonacci contiguous-window rolling transfer recurrence for directive-9 validation; compares the k+1 window square sum with mech_psi for k<=150. This is an O(N) oracle/diagnostic, not a full-size solver. |
| `explore.lean` | _(undescribed)_ |
| `factor_m.py` | _(undescribed)_ |
| `g4_circle_partition_test.py` | Bounded executable oracle testing circle interval-indicator expansion and correlation-state growth for G4. |
| `g4_joint_diagnostic.py` | Bounded G4 joint-collapse diagnostic: reproduces statement examples, validates existing O(k) route, tests additive Fibonacci-block summaries and small fixed-order level recurrences; intentionally does not claim a full-size solver. |
| `investigate_bivariate_diagonal.py` | Exact bounded oracle falsifying the bivariate-diagonal closure claim: builds the rational left-limit floor matrix G_m(t)=floor((t-m)p/q)-[t=m] and counts, per diagonal h=j-m, distinct local affine/boundary data. An h-only affine state is falsified as soon as a diagonal carries more than one datum (guaranteed by -[t=m]). Exponential in the oracle dimension; not a full-size method. |
| `probe_M.py` | _(undescribed)_ |
| `read_problem.lean` | _(undescribed)_ |
| `read_problem.py` | _(undescribed)_ |
| `run_probe.py` | _(undescribed)_ |
| `solution.py` | Explicitly refuses to print an unsupported PE1006 answer; documents that the efficient joint-intercept recurrence is still unproved. |
| `verify_new_source_claims.py` | _(undescribed)_ |
| `verify_z_index.py` | Small decisive z^0 indexing harness: compares ue0 universal-Euclidean moments against direct 0-indexed floor sums and mech_psi at k=1,2,3; bounded oracle, not the full evaluator. |
