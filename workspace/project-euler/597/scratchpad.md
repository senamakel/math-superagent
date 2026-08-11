# Scratchpad

## Task
Run `/workspace/verify_hypothesis.py` with N=200000; report the four MC
estimates (expect p(3,160)≈0.4148, p(4,400)≈0.5108) and whether any w-order
bucket holds both parities.

## Run result (verbatim)
```
MC p(3,160)   = 1.000000  (exact 4.15+4/27 = 56/135 = 0.414815)
MC p(4,400)   = 1.000000  (given 0.5107843137)
n=3 L=160: 60000 samples, 6 distinct w-orders seen, 0 order(s) with inconsistent parity
n=4 L=160: 60000 samples, 24 distinct w-orders seen, 0 order(s) with inconsistent parity
n=4 L=400: 60000 samples, 24 distinct w-orders seen, 0 order(s) with inconsistent parity
n=5 L=400: 60000 samples, 120 distinct w-orders seen, 0 order(s) with inconsistent parity
n=5 L=1800: 60000 samples, 120 distinct w-orders seen, 0 order(s) with inconsistent parity
```

## Diagnosis: MC=1.000000 is a BUG, not a finding
Both MC estimates came out exactly 1.0, but the stated values are ≈0.4148 and
≈0.5108. So the parity computation in `brute.parity_of_new_order` is broken.
The `lower(a,b)` comparator uses the wrong `above` test:

```python
def lower(a, b):
    if a in above and b in above[a]:   # WRONG
        return True
    ...
    return a < b
```
`above[i]` = boats placed BELOW i (bump chain under i). So "a placed lower
than b" means `a in above[b]`, not `b in above[a]`. As written every case whose
bump structure is non-trivial falls to the `return a < b` fallback, producing
identity order [0,1,2] and parity 0 for essentially everything.

Table reproduction with the buggy routine (expected parity from problem table):
```
none                   -> [0,1,2] parity=0 expected=even  OK
B bumps C              -> [0,1,2] parity=0 expected=odd   FAIL
A bumps B              -> [0,1,2] parity=0 expected=odd   FAIL
B then A both bump C   -> [0,1,2] parity=0 expected=even  OK
A bumps B then B bumps C -> [0,1,2] parity=0 expected=odd FAIL
```
Only identity/easy cases agreed; all odd cases were misreported as even. Hence
the "0 inconsistent orders" verdict is also meaningless, and the structural
hypothesis test is not yet usable.

## Fix
Correct comparator: a is placed lower than b  <=>  a in above[b].
```python
def lower(a, b):
    if a in above[b]: return True      # b above a, so a lower
    if b in above[a]: return False     # a above b, so a higher
    return a < b
```
Then re-verify: parity routine must reproduce the 5-table parities, and MC
must give p(3,160)≈0.41 and p(4,400)≈0.51. Only then is the w-order
consistency check meaningful.

## verifier for the hypothesis
`verify_hypothesis.py` also has a cosmetic bug in a print string:
`exact 4.15+4/27` should be `4/15+4/27`. Not functional, but note.
