# The suprema of Phi sit exactly on Pell pairs, and Phi stays strictly below 1

Run by the operator. Four programs that had been written and left unexecuted —
`verify_pell_records.py`, `verify_pell_argmax_unique.py`, `pell_record_seq.py`,
`prove_pell_record.py` — all exit 0. Captures are beside this file as
`<name>.captured.txt`.

## What they establish

Write `f(m,n) = 4mn(m^2 - n^2)/(m^2 + n^2)^2` and let `P_k` be the Pell
numbers `1, 2, 5, 12, 29, 70, 169, 408, 985, ...`.

**The record identity.** `f(P_k, P_{k-1}) = 1 - 1/P_{2k-1}^2`, verified for
`k = 2..59`, together with the supporting identity `P_{2k-1} = P_k^2 +
P_{k-1}^2`. Equivalently `(m^2+n^2)^2 - 4mn(m^2-n^2) = 1` exactly at Pell
pairs, verified `k = 2..79`.

**The records are where the maxima are.** Over primitive `m > n >= 1` with
`m <= M`, the argmax of `f` is a Pell pair at every bound tested:

```
M =   20  ->  (12, 5)     = 28560/28561              = (P_4, P_3)
M =  100  ->  (70, 29)    = 32959080/32959081        = (P_6, P_5)
M =  500  ->  (408, 169)  = 38034750624/...625       = (P_8, P_7)
M = 1000  ->  (985, 408)  = 1292061882720/...721     = (P_9, P_8)
```

**`f < 1` throughout the searched box.** Over `m <= 5000` the maximum is
`1 - 1/6625109^2` at `(2378, 985)`, and no `f >= 1` occurs.

**The underlying recurrence fact.** `a^2 + 2ab - b^2 = ±1` alternating in sign
for consecutive Pell numbers `(a,b) = (P_{k-1}, P_k)`, verified `k = 2..200`.
The record denominators grow with ratio tending to `5.828427… = 3 + 2*sqrt(2)
= (1 + sqrt(2))^2`, the square of the silver ratio, which is the dominant
eigenvalue of the Pell recurrence — so the records thin out geometrically.

## The caveat that must not be dropped

`verify_pell_argmax_unique.py` is named for a uniqueness claim, and **the
uniqueness does not hold as stated**. Its own output reports ties:

```
M <=   30: ties=0   record-strictly-increasing=True
M <=   60: ties=2   record-strictly-increasing=False
M <=  120: ties=1   record-strictly-increasing=True
M <=  240: ties=1   record-strictly-increasing=True
M <=  480: ties=0   record-strictly-increasing=True
M <=  960: ties=2   record-strictly-increasing=False
M <= 1920: ties=1   record-strictly-increasing=True
```

So the argmax is attained at a Pell pair at every bound tested, but it is not
always attained *only* there, and the record sequence is not strictly
increasing in `M`. Any claim of a unique argmax is false; the true statement
is that a Pell pair is always among the maximisers.

## Bearing

This is a statement about the size of elements of `Phi`, not an impossibility
result, so the witness set does not apply to it — nothing here forbids any
configuration. It bounds `Phi` strictly below 1 with an explicit approach rate,
and it says the extremal structure is the Pell recurrence rather than anything
special to the magic-square problem.

```claim
id: phi-suprema-are-pell-pairs
statement: For f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2 over primitive m > n >= 1,
  the identity f(P_k, P_{k-1}) = 1 - 1/P_{2k-1}^2 holds for k = 2..59 with
  P_{2k-1} = P_k^2 + P_{k-1}^2, equivalently (m^2+n^2)^2 - 4mn(m^2-n^2) = 1 at
  Pell pairs for k = 2..79. A Pell pair attains the maximum of f over every
  box m <= M tested (M = 20, 100, 500, 1000 and M = 30..1920), and f < 1
  throughout m <= 5000, where the maximum is 1 - 1/6625109^2 at (2378, 985).
  The record denominators grow with ratio tending to 3 + 2*sqrt(2). The
  maximiser is NOT unique: ties occur at M <= 60 and M <= 960, and the record
  is not strictly increasing in M, so any uniqueness claim is false.
hypotheses: primitive pairs m > n >= 1; bounds exactly as stated, nothing
  proved beyond m <= 5000
holds-here: yes, computed in this workspace with exact integer arithmetic
status: checked
bearing: bounds Phi strictly below 1 with an explicit rate and identifies the
  extremal structure as the Pell recurrence. Not an impossibility statement,
  so the witness set does not apply. The stated bounds are part of the result
  and must travel with it
anchor: code/out/pell_records_established.md;
  code/out/verify_pell_records.captured.txt;
  code/out/verify_pell_argmax_unique.captured.txt;
  code/out/prove_pell_record.captured.txt;
  code/out/pell_record_seq.captured.txt
source: operator-computation
```
