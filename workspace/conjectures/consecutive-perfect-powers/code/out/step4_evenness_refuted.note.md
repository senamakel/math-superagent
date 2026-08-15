# Refutation: lemma (E) "Im((c+i)^p) is even for all integers c" is false

## What was claimed

In `code/caseB/probe_step4_lemmas.py` the docstring states two facts intended to
make step 4 of the Lebesgue Case-B proof elementarily provable:

    (E) evenness: Im((c+i)^p) is even for all integers c, odd prime p >= 3.
    (N) nonzero:  Im((c+i)^p) != 0 for c != 0.

## What was executed

`probe_step4_lemmas.py 3000 401` — 468 000 `(c,p)` pairs, c in [-3000,3000]\{0},
odd primes p in [3,401]. Output in `probe_step4_lemmas.captured.txt`:

    (E) evenness:  failures = 234000
    (N) nonzero:   failures = 0
    VERDICT: FAIL

First failure: `(c,p)=(-3000,3)`: Im((−3000+i)^3) = 3·3000² − 1 = 26999999, odd.
Exactly half the tested pairs failed, all with even `c`.

## The correct statement (verified)

For p an odd prime, `Im((c+i)^p) = sum_j (-1)^j C(p,2j+1) c^(p-2j-1)`.
Modulo 2 the alternating signs vanish, leaving `sum_j C(p,2j+1) = 2^(p-1) ≡ 0
(mod 2)` times a power of c. The result is that **`Im((c+i)^p)` is even iff `c`
is odd** (the parity lives in the single `2^(p-1)`-weighted odd term, which is
even times `c^(p-1)`, itself even only when c is odd). Verified over 11 629
`(c,p)` pairs, c in [-200,200], p in [3,119], 0 fails
(`correct_evenness.captured.txt`).

Demonstration p=3: `Im((c+i)^3) = 3c² − 1`; c even ⟹ 3c² even ⟹ −1 odd; c odd
⟹ 3c² odd ⟹ −1 even.

## Why this does NOT break the main Case-B certification

The certified chain in `certify_lebesgue_caseB.py` does **not** depend on (E).
Its step 4 only uses `d | 1` (from `1 = Im((c+di)^p) = d·(integer)`), giving
`d = ±1`; step 5 derives `x = c²+1` and `m² = T(c,p)`; step 6 invokes the
Ljunggren-type theorem that `T(c,p)` is never a square. No step needs the false
"even for all c" claim. So the refutation is of a **supporting-lemma attempt**,
not of the certified reduction.

What remains needed for a self-contained step 4 (forcing c = 0 rather than
handing off to Ljunggren) is the claim `|Im((c±i)^p)| != 1` for `c != 0`. This
was NOT refuted: over c in [1, 4000), all 24 odd primes ≤ 101, a hunt for
`|Im| == 1` found **0 hits** (`probe_evenc_abs1.captured.txt`). It remains
open/verified-numeric. Note the false (E) did not hide a counterexample: even
c give odd |Im|, yet none equal 1.

## Status

- Claim `Im((c+i)^p)` even for all c: **REFUTED** (counterexample c even, e.g.
  c=2,p=3). Recorded as refuted, not weakened.
- Claim `Im((c+i)^p)` even iff c odd: verified-numerically (exact ints).
- Claim `|Im((c±i)^p)| >= 2` for all c != 0: check_step4_bound PASS to
  c<=2000, p<=401 (156000 pairs, min |Im| = 2, 0 hits ==1); Ljunggren handoff
  in step 6(b) remains asserted-classical.
