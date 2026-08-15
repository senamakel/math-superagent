# exp2 verification — exponent-2 cases, independently searched

Program: `code/exp2_verify.py`. Output: `code/out/exp2.captured.txt`.

The oracle (`code/scholar_oracle/oracle.py`) enumerates the *set* of perfect
powers and checks consecutive values. These three searches use a different
code path: iterate one side directly and solve a perfect-power equation on the
other side with an **exact integer k-th root** (integer Newton iteration). Two
unrelated methods agreeing is the cross-check. A third, fully independent route
(binary-search integer root + direct prime-power detection, run ad hoc) also
agrees, so each verdict is confirmed two ways.

All arithmetic exact integers; no floats, no logarithms, no `math.pow`.

| Task | Statement | N | result | verdict | runtime |
| --- | --- | --- | --- | --- | --- |
| 1 | `x^2 - y^q = 1`, q prime | 1e6 | `[(3,2,2,3)]` (i.e. (x,y,q)=(3,2,3)) | **agree** (unique) | 0.005s |
| 1 | | 1e7 | `[(3,2,2,3)]` | **agree** | 0.019s |
| 2 | `x^p - y^2 = 1`, p odd prime | 1e6 | `[]` | **agree** (none) | 0.003s |
| 2 | | 1e7 | `[]` | **agree** | 0.014s |
| 3 | prime-exponent reduction | 1e6/1e7 | only `(3,2,2,3)`, p,q already prime | **agree** (vacuous) | ~0s |

Task 3 reduces to: the only solution the oracle ever returns is `(3,2,2,3)` and
its exponents 2,3 are both already prime, so no composite exponent exists to
descend; the descent identity `(x^a)^b == x^(a*b)` was additionally confirmed
by exact arithmetic on 5000 random composite-exponent cases. The reduction claim
itself is the tautology `(x^a)^b = x^(ab)`, so any solution with composite p
would yield a prime-exponent one — nothing to do here because none appear.

```claim
id: exp2-independent-searches
statement: Over x^2,y^q<=N for N in {1e6,1e7}, the equation x^2-y^q=1
  (q prime) has exactly one solution (x,y,q)=(3,2,3); over x^p,y^2<=N the
  equation x^p-y^2=1 (p odd prime) has no solutions.
hypotheses: x,y>0, q>1 prime, p odd prime, exact integer arithmetic, finite
  box x^2,y^q<=N / x^p,y^2<=N.
holds-here: TRUE — verified by two independent search routes at N=1e6 and 1e7,
  and both agree with the oracle's filtered output.
status: checked (numerical, finite box; not a proof for all N)
bearing: confirms the two elementary cases the reduction to odd primes relies
  on, for a finite range. Task 2's known solution (3,2,2,3) has y-exponent 3
  and is correctly excluded from the p-odd,q=2 search.
anchor: code/out/exp2.captured.txt
```
