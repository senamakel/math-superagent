# Regularity found in the run's computed data

Pattern-finder pass over the sequences the run has actually computed.

## Sequences examined

1. **c2(n)** = number of digit-2s in base-3 of `2^n` (OEIS A260683), n=0..80
   `0,1,0,2,1,1,1,2,0,4,2,4,3,3,2,6,5,5,3,7,4,7,5,4,1,5,2,8,8,7,9,...`
   - `analyze_sequence`: no polynomial fit (differences never become constant).
   - `find_linear_recurrence` (max order 12, 77 terms): **no constant-coefficient
     linear recurrence up to order 12**. Confirmed: this sequence is not
     polynomial and not low-order linear-recurrent. A regular digit distribution
     is what the heuristic `(2/3)^k` predicts; absence of a recurrence is exactly
     what "digits behave irregularly" means. Negative result, not a lead.

2. **c1(n)** = number of digit-1s in base-3 of `2^n` (OEIS A036461)
   `1,0,2,0,2,2,2,2,4,0,4,2,4,2,6,4,2,4,6,2,...`
   Same shape: `find_linear_recurrence` not a lead either.

3. **Survivor residues** `A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r
   avoid 2 }`:
   - k=1: [0]
   - k=2: [0,2]
   - k=3: [0,2,6,8]
   - k=4: [0,2,8,18,20,24,26,42]
   - k=5: [0,2,8,20,24,26,54,56,62,72,74,78,80,96,126,150]
   - k=6: 32 survivors (see output capture)
   - **`|A_k| = 2^(k-1)` confirmed** k=1..6 by direct residue sieve.
   - Every survivor is **even** (2^n mod 3 = 1 forces n even; low ternary digit 1).
   - OEIS lookup: **no catalogued match** for the flattened survivor residues.
     This sequence is not in OEIS; structure must come from the problem.
   - These are the data any symbolic invariant must separate, and the witnesses
     n=0,2,8 survive (n=8 is always a survivor mod any period since 256 has all
     digits in {0,1}).

## The two REGULARITIES that hold exactly (each a theorem)

### R1 — c1(n) is even for every n ≥ 1  (PROVED)
Proof: write `2^n = sum a_i 3^i`. Modulo 2, every `3^i ≡ 1`, so
`2^n ≡ sum a_i = (number of 1s) mod 2`. For n ≥ 1, `2^n` is even, so the number
of digit-1s is even.
Verified by computation: c1(n) even for ALL 1 ≤ n < 3000 (no exception),
and on the witnesses n=2 (c1=2), n=8 (c1=4).
Conjecture status: none — it is an exact proof. The parity fact is elementary.

### R2 — `|A_k| = 2^(k-1)` exactly  (PROVED, bijection)
`2` is a primitive root mod `3^k` (order `φ(3^k)=2·3^(k-1)`); a unit's low k
ternary digits avoid 2 iff low digit is 1 and the other k-1 digits ∈ {0,1},
which is exactly `2^(k-1)` patterns. Direct residue sieve confirms k=1..6.
Consequence (already in CONTEXT.md): the modular sieve can never close by
counting — this is the starting obstruction, not a closing argument.

## What the tools did NOT find
- c2 has no low-order linear recurrence (order ≤ 12 over 77 terms) — recorded
  so nobody else searches for one.
- Survivor residues are not catalogued in OEIS — recorded so nobody searches
  again.

## Where a pattern would have to come from (and does not, yet)
The strong open question is whether any *statistic along n* separates the
survivor paths `n ≡ n_j mod 2·3^(k-1)` from the tail. The low-order data show:
no linear/polynomial recurrence in digit counts, no catalogued residue
structure. This reinforces that the survivor set is "measure-optimal but
path-structured", and the symbolic-invariant route must use the *carry/transducer
coupling* rather than any low-order statistic of the digit counts. (Goal in
`research/backward/erdos-via-symbolic-invariant.md`.)

```claim
id: c1-even-parity
statement: The number c1(n) of digit-1s in the base-3 expansion of 2^n is even
  for every n >= 1. Proof: modulo 2, 3^i ≡ 1 for all i, so 2^n = sum_i a_i 3^i
  ≡ sum_i a_i = c1(n) (mod 2); and 2^n is even for n >= 1, so c1(n) ≡ 0 (mod 2).
hypotheses: n >= 1 a nonnegative integer.
holds-here: yes — exact, holds for ALL n >= 1, not just digit-2-free powers.
status: checked (proved here; verified c1(n) even for all 1 <= n < 3000, and on
  witnesses n=2 [c1=2], n=8 [c1=4]).
bearing: discharges gap G-cong(i) of the symbolic-invariant skeleton: a
  counterexample 2^n (digit-2-free) has |A| = c1(n) even. Also a free structural
  constraint on any invariant/counterexample candidate.
anchor: code/out/regularity_findings.md
answers: (G-cong(i) of research/backward/erdos-via-symbolic-invariant.md)
```

