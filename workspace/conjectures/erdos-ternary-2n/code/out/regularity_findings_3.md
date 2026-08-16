# Pattern-finder third pass — refutation of the c0/c2-odd-count coincidence

Follow-on to `regularity_findings_2.md`, which reported the parity counts
`#{n<=400 : c0(n) odd} = 211` and `#{n<=400 : c2(n) odd} = 211` with equal
values but drew no conclusion from the equality. The equal counts at 400 are a
natural candidate regularity (somebody might propose "the number of n with an
odd zero-count equals the number with an odd two-count"). This pass tests that
candidate to large N.

## Setup (what is exact)

For the ternary digits (c0,c1,c2) of 2^n:
- c1(n) is even for ALL n>=1 (proved: 2^n = sum a_i 3^i ≡ sum a_i = c1 mod 2, and 2^n even).
- c0 + c1 + c2 = L(n) = number of ternary digits of 2^n.
- Hence c0 ≡ c2 + L (mod 2) exactly (this modular identity is a theorem,
  verified every n <= 30000, no exception).

So the parities of c0 and c2 are tied only through the parity of the ternary
digit length. There is NO theorem that #{c0 odd} == #{c2 odd} as counts; that
would require L even exactly half the time in a very regular way, which is not
obvious and is what this pass attacks.

## Result: the count equality is REFUTED

Verified two independent ways (incremental base-3 digit counter, and direct
`2**n` digit counting — they match at every N tested including N=200, N=400,
N=30000):

| N | #{c0 odd} | #{c2 odd} | equal? |
| --- | --- | --- | --- |
| 200 | 109 | 106 | False |
| 400 | 211 | 211 | True (coincidence — the prior 211=211) |
| 30000 | 14824 | 15073 | False |

The N=400 equality (211 = 211) is a crossing, not a regularity: the two running
counts coincide at n=10,13,16,20,21,22,30,31,33,34,42,43,44,156,... then drift
apart and never stay equal. Already at N=200 the counts differ.

**Falsifying witness:** the inequality already holds at N=200 (109 vs 106). A
proponent of the count-equality regularity would need it to hold at every N;
it fails at N=200, so the first term to falsify = N=200 (equivalently, the
first n where the running a0-a2 becomes nonzero, which is n=10; the counts
then re-cross at 400). This is the deliberate attack: the proposed regularity
does not survive it.

## What this means

- The only exact parity fact about the digit counts remains c1-even, and the
  only exact relation is c0 ≡ c2 + L (mod 2) — a modular identity, not a count
  statement. Nothing about the equality or inequality of the *number* of
  odd-count n is exact.
- Recorded to stop anyone proposing "#{c0 odd} == #{c2 odd}" or any
  count-level parity balance between c0 and c2 as an invariant. It is false in
  general.

## Also probed and closed (negative)

Survivor branch structure (`pattern_branch.py`, k<=14): at each level every
survivor r lifts to 3 candidates (r, r+L, r+2L), exactly 2 of which survive.
The excluded (digit-2) child distribution over levels k=1..13 is
asymptotically uniform across {0,1,2} (k=13: 1382/1367/1347), i.e. no exact
structure — each child index is excluded roughly a third of the time. No
2-adic or residue-mod-small-power pattern in which child is excluded (checked
against r mod 8 at k=8: all four even classes spread). This is the branching
any finite-transducer invariant must thread; the excluded index is not a
simple function of r mod 2^m.

## Status of all regularities found in this run

- PROVED (exact theorem): c1(n) even for all n >= 1.
- PROVED (modular identity): c0 ≡ c2 + L(n) mod 2.
- PROVED (exact, bijection): |A_k| = 2^(k-1), survivors all even; sieve can't close by counting.
- REFUTED here: #{c0 odd} == #{c2 odd} as counts (fails by N=200).
- REFUTED earlier: c0≡c2 mod 2; max-survivor = period-12 (breaks at k=12); survivors avoid a 2-adic class (they fill every even class).
- NEGATIVE (no structure): c0,c1,c2 have no constant-coefficient recurrence order<=12 and no polynomial fit; survivor residues not in OEIS.
