# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `fibword.py` | Fibonacci-word helpers: fibs_upto, next_fib (least Fibonacci > k), fib_prefix (doubling to length >= L), lmin_seq (Lmin(1..kmax) by exact-integer bit-mask scanning with early stop), lmin_formula (k + NextFib(k) - 1). All exact integer arithmetic. |
| `ueuclid.py` | Universal-Euclidean (Chtholly/AtCoder floor_sum generalisation) monoid, O(log) evaluator of the geometric second-moment floor-sum. 1-INDEXED convention (t=1..n, weight z^(t-1), floors floor((p*t+q)/r)) matching fhq/LOJ138/OI-wiki exactly. Node(dR,dU,w,S0,S1,S2); compose (directive-4 rule); ueuclid (O(log), verbatim literature recursion, untouched); ueuclid_direct (O(n) 1-indexed oracle); ue0 (0-indexed wrapper ue0=ueuclid(p,q-p,..) with k-lift/undo for p>q); floor_sum_plain. Acceptance 1-3 PASS (captured code/out/ueuclid_main.captured.txt: ALL MONOID TESTS PASSED — 30/30 random, 30/30 floor_sum-at-z=1, 6/6 deterministic, ue0 30/30; large-n ueuclid(514229,3,1346269,10^18,10^-1) dU=381966011250351898, dR=10^18). Verified on fresh seeds: 1-indexed oracle==log==literal 60/60, ue0==0-indexed 60/60. Do NOT re-derive the recursion; it is the verbatim literature translation by design. |
