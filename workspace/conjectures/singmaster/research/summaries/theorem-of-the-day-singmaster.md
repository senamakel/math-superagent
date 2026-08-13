# Theorem of the Day — Singmaster's Binomial Multiplicity Bound (R. Whitty)

Source: https://theoremoftheday.org/Binomial/Singmaster/TotDSingmaster.pdf
Full text: `research/sources/theorem-of-the-day-singmaster.full.md`

## What it is

An expository one-page exposition (Robin Whitty, Theorem of the Day series) of
Singmaster's N(k) = O(log k) bound, with the full proof and the construction
history. Secondary source (expository), valuable for the clean proof and the
history table; the primary 1971 note itself is still not in the library.

## Proof of N(k) = O(log k) (as expounded)

N(k) = # of (a,b) ∈ Z², 1 ≤ a ≤ b, with k = C(a+b, a). Since C(a+b, b)
increases in each of a and b, any choice of a (or b) admits at most one
solution value. Take the least s with k < C(2s, s). Then k = C(a+b, a) forces
a or b < s, so the solution count N(k) ≤ 2s. Since 2^{s-1} ≤ C(2(s-1), s-1) ≤ k,
we get s ≤ 1 + log_2 k and N(k) ≤ 2 + 2 log_2 k = O(log k). □

(The "2+2 log_2 k" form is the exact bound attested from Singmaster 1971.)

## Construction history (from the sheet)

- 1971: Singmaster proves N(k)=O(log k); checks N(k) ≤ 8 up to k = 2^23
  (later 2^48).
- 1974: Abbott–Erdős–Hanson prove N(k) = O(log k / log log k).
- 2004: Kane proves N(k) = O((log k) log log log k / (log log k)^2).
- 2007: Kane increases the denominator to (log log k)^3.

(This "Kane 2004 exponent-2, Kane 2007 exponent-3" history matches the run's
ledger and the construction-notes sequence; the Fermat's Library slip of
exponent 2 was correctly resolved to exponent 3 by MRSTT/Wikipedia/Jenkins.)

Also gives the Fibonacci family: for even n,
C(F_n F_{n+1} − 1, F_{n−1} F_n) = C(F_n F_{n+1} − 1, F_{n−1} F_n − 1), and for
n=4 gives 3003; N(3003)=8 is stated as the largest known value.

## Claims

```claim
id: totd-ologk-proof-and-history
statement: Theorem of the Day (Whitty) exposition: Singmaster's proof that
  N(k) <= 2 + 2 log_2 k = O(log k) (least s with k < C(2s,s); monotonicity of
  the binomial in each parameter; N(k) <= 2s; s <= 1 + log_2 k). Construction
  history: 1971 Singmaster O(log k) + N<=8 up to 2^23 (later 2^48); 1974 AEH
  O(log k/log log k); 2004 Kane exponent-2; 2007 Kane exponent-3 (record).
hypotheses: standard binomial monotonicity; k > 1.
holds-here: yes; matches the attested statements and the run's ledger
  (including the exponent-2 vs exponent-3 resolution).
status: asserted (secondary exposition; the primary 1971 note is still not held)
bearing: gives the run a clean, citable secondary proof of the O(log k)
  baseline and a compact history table; does not replace the missing primary.
anchor: research/sources/theorem-of-the-day-singmaster.full.md
```