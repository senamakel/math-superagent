# Mirror primitive divisor — verification and scope
Exact integer arithmetic (Python ints, sympy.factorint); no floats.

## Task A — Mirror primitive divisor (q-side, condition on x)
For `x^p - y^q = 1` with q odd prime, `x^p = (y+1) Phi_q(-y)`, `Phi_q(-y) = (y^q+1)/(y+1)`. A *primitive* divisor s of `Phi_q(-y)` has `s | Phi_q(-y)`, `s` not dividing `(y+1)`, and order of `(-y)` mod s exactly q (equiv `s == 1 mod q`); since `x^p = (y+1) Phi_q(-y)` and `s` not `| (y+1)`, such an s divides x.
Per-q table (Ymax, successes, failures, largest primitive s):
| q | Ymax | successes | failures | largest primitive s |
|---|------|-----------|----------|--------------------|
| 3 | 120 | 118 | 1 | 14281 |
| 5 | 80 | 79 | 0 | 40454321 |
| 7 | 60 | 59 | 0 | 24344094727 |
| 11 | 40 | 39 | 0 | 2681921038140191 |
| 13 | 30 | 29 | 0 | 21001515080686141 |
| 17 | 20 | 19 | 0 | 274019342889240109297 |

Total (q,y) with NO primitive s: 1 ([(3, 2)]); note (q,1) is excluded from the sweep because Phi_q(-1)=1 has no prime divisor.
Failures with y >= 3: 0 -> none: confirmed. **For y >= 3 no failures occur** over this sweep.

## Task B — Clean statement of the necessary condition
Required deduction: if `x^p - y^q = 1` with p,q odd primes, then
  (i) y has a prime divisor `r == 1 (mod p)` with `r | Phi_p(x)`, `r` not `| x-1` (from `y^q = (x-1)Phi_p(x)`);
  (ii) x has a prime divisor `s == 1 (mod q)` with `s | Phi_q(-y)`, `s` not `| (y+1)` (from `x^p = (y+1)Phi_q(-y)`).
The deductive step is sound because `r | Phi_p(x)` and `r` not `| (x-1)` give `r | (x^p - 1) = y^q`, hence `r | y`; dually `s | (y^q + 1) = x^p` and `s` not `| (y+1)` give `s | x`. We verified the unconditional premises (`r | x^p - 1` with `r` not `| x - 1`; `s | y^q + 1` with `s` not `| y + 1`) over the (p,q,x,y) sweep:
- (p,q,x,y) checked: p,q in {3,5,7,11}, x,y in [2,40].
- failures of `r | x^p-1`, `r` not `| x-1`: 0.
- failures of `s | y^q+1`, `s` not `| y+1`: 156.
- (p,q,x,y) with `x^p - y^q == 1` in range: 0 (none — no odd-prime solution exists here).
- s-premise failures, all attributed to the known small Zsigmondy mirror exception `(q,y)=(3,2)` which has NO primitive divisor (appearing once per (p,x) setting: 4 p * 39 x = 156): {(3, 2): 156}.
**Scope note:** this is a demonstration of the deductive step on constructed data; because no actual (x,p,y,q) with p,q both odd prime satisfies the equation in any reachable range, the antecedent `x^p - y^q = 1` never fires here. This **does not** prove that any solution exists; it verifies the implication is sound as a conditional statement and that its non-trivial premises hold on the data.

## Task C — Non-exclusion / scope
Search over odd primes p,q in [3,30] (9 primes) and x,y in [2,200]: 3207681 4-tuples.
- actual solutions (`x^p - y^q == 1`) in space: 0 (expected 0 for odd primes).
- 4-tuples satisfying ALL elementary conditions `(p | x-1, q | y+1, y has a prime divisor ==1 mod p, x has a prime divisor ==1 mod q)` AND `x^p - y^q != 1`: **1967**.
  - of which `p | y` holds: 143
  - of which `q | x` holds: 157
  - of which BOTH `p | y` AND `q | x` (full Cassels congruences) hold: 17
- triples with BOTH `p | y` AND `q | x` and `x^p - y^q != 1` (Cassels-congruence non-solutions, without the elementary conditions imposed): 40804

**Conclusion (sufficiency):** many non-solutions satisfy the primitive-divisor + elementary Cassels congruences; hence these conditions are **necessary, not sufficient**, and do NOT by themselves close the search space. This makes no claim about the Catalan conjecture; it bounds what the elementary conditions alone can establish.

```claim
id: mirror-prim-div-scope
statement: >
  For q in {3,5,7,11,13,17} and y in [2,Ymax_q], Phi_q(-y) has a primitive divisor s (s | Phi_q(-y), s not | y+1, order of (-y) mod s = q, s == 1 mod q) for all but the small exceptions (3,2) [plus excluded (q,1) with Phi_q(-1)=1]. No failure for y >= 3. The necessary-condition deduction (r | y, s | x) holds as a sound conditional verified on its unconditional premises. Over p,q odd primes <= 29 and x,y in [2,200], 1967 non-solutions satisfy all elementary conditions, so those conditions are not sufficient.
hypotheses: >
  p,q odd primes. Mirror primitive divisor on q-side; Task B checks the deductive chain without any actual solution existing (the antecedent never fires); Task C ranges are p,q in {3,5,...,29}, x,y in [2,200].
holds-here: yes
status: checked (exact integer code; ranges stated; no floats)
bearing: elementary (class-group-free); shows the primitive-divisor + elementary Cassels congruences are necessary but far from sufficient
anchor: code/out/primitive_div_mirror.md
```
