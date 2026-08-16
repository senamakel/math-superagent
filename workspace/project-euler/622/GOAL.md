# Goal

Project Euler 622. The out-faro (riffle) shuffle preserves top and bottom card;
let s(n) be the minimum number of consecutive riffle shuffles to restore an even
deck of size n. Find the sum of all n with s(n) = 60.

**COMPLETION CRITERIA**

1. Restate and reproduce the worked examples: s(52)=8, s(86)=8,
   sum of even n with s(n)=8 is 412. — DONE, three independent Python programs
   (code/brute.py, code/pe622/oracle_check.py) all agree.
2. Establish the reduction s(n) = ord_{n-1}(2) (multiplicative order of 2 mod
   n-1). — machine-confirmed by brute force (runs make s and ord agree on small
   even decks); sourced to Diaconis-Graham-Kantor / Packard / OEIS A002326.
3. Compute the answer. — DONE: **ANSWER = 3010983666182123972**
   (code/pe622/solution.py, cross-checked by code/pe622/solve.py).
   Per-route values: C = 4456 (count of m with ord_m(2)=60),
   S = 3010983666182119516 (sum of those m), ANSWER = S + C.
4. **Lean requirement**: a `.lean` file under code/lean/ with a passing
   `lean-verdict` (lean_check) must carry the final answer as an equality of
   naturals, the last theorem being the answer itself, with no native_decide.
   Every rung it rests on a theorem in the same tree (or a documented Cited
   axiom giving a `conditional` verdict). — IN PROGRESS.

Answer: 3010983666182123972
