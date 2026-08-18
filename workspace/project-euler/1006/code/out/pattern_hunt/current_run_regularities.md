# Current run regularities (2026-08-18)

Executed `python code/refute/fib_block_state_counterexample.py`. Exact minimal collision: `k=2,n=3`; `010` and `101` both have summary `(2,11,101)`, but appending `0` gives `(3,11,101)` versus `(3,21,201)`. Therefore `(count,sum,sum^2)` is not a closed concatenation state. Fibonacci split checks k=2..7 also show additive summary failure.

Rerun exact checks:
- `c1=1+floor(k/phi^2)` holds k=1..400.
- factor count `k+1` holds k=1..400.
- `Lmin=k+NextFib_strict(k)-1` holds k=1..400 (existing run verified to k=6764).
- right-extension recurrence and `J=c1(k+1)` hold k=1..400.
- run increment law holds over 1145 proper runs.

Sequence tools:
- c1 prefix has exact recurrence `a(n)=a(n-1)+a(n-5)-a(n-6)` over 30 supplied terms, but this is only a finite observed regularity. OEIS lookup matches A057354 (`floor(2n/5)`); with the problem's indexing, c1(k)=floor(2k/5)+1, equivalently `1+floor(k/phi^2)` because `1/phi^2=(3-sqrt5)/2` is not 2/5, so the apparent A057354 match is not the same sequence globally. Do not promote the match.
- Psi exact prefix: no constant-coefficient recurrence order <=12 over 25 terms.
- ext final column: no such recurrence through 40 terms.

These are finite checks and diagnostics; none supplies the missing joint intercept/Fibonacci-block collapse needed for Psi(10^18).
