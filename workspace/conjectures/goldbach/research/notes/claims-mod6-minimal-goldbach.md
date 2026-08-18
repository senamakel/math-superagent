```claim
id: mod3-law-minimal-goldbach
statement: For even n, let p(n) be the least prime in a Goldbach partition
  n = p(n) + q(n).  If n ≡ 2 (mod 6) and p(n) ≠ 3 then p(n) ≡ 1 (mod 3);
  if n ≡ 4 (mod 6) and p(n) ≠ 3 then p(n) ≡ 2 (mod 3); if n ≡ 0 (mod 6)
  there is no constraint.  Equivalently on S(p) = least n with p(n) = p:
  p ≡ 1 (mod 3) ⟹ S(p) ≡ 0 or 2 (mod 6), p ≡ 2 (mod 3) ⟹ S(p) ≡ 0 or 4 (mod 6).
hypotheses: n even; p(n) the minimal Goldbach prime; the congruence is
  elementary (primes > 3 are ±1 mod 3; p + q ≡ n mod 3).
holds-here: yes — this is exact, not statistical.
evidence: verified by exhaustive enumeration: 0 violations over all even
  n ≤ 5×10^4 (full-partition and minimal-prime versions,
  code/verify_mod3_structure.py), and over the OeS Top-50 tail
  (p ~ 10^4, S ~ 10^18, code/test_tail_oes.py: 0 violations).
status: proved (by congruence), verified-numerically
falsified-by: an even n ≡ 2 (mod 6) whose minimal Goldbach prime is ≡ 2
  (mod 3) (with p(n) ≠ 3); none exists — the residue law rules it out.
```

```claim
id: sp-mod6-avoidance-conjecture
statement: (C) For every minimal prime p > 7, S(p) ≢ 0 (mod 6).  Stronger
  (C'): for p > 3, S(p) ≡ 2 (mod 6) ⟺ p ≡ 1 (mod 3) and S(p) ≡ 4 (mod 6)
  ⟺ p ≡ 2 (mod 3); the only minimal primes with S(p) ≡ 0 (mod 6) are
  p ∈ {5, 7}, with S(5) = 12, S(7) = 30.
hypotheses: n ≤ 10^7 for the head data; p ~ 10^4, S ~ 10^18 for the OeS tail.
holds-here: yes — verified, but conjectural (no proof found).
evidence: N=10^7 (code/extend_sp_10m.py): residue table {(1,2): 56, (2,4): 52,
  (1,0): 1, (2,0): 1}, the two (·,0) entries exactly p=5,7; 0 violations of
  (C) over 108 primes p>7.  OeS Top-50 tail: residue table exactly
  {(1,2): 30, (2,4): 20}, 0 violations of (C') over all 50 points.
  Cross-checked: pair-enum and vectorized methods agree exactly on all
  overlapping S(p) values (0 disagreements).
status: conjectured (data), attacked and survived
falsified-by: a prime p > 7 with S(p) ≡ 0 (mod 6) — none found with
  S(p) ≤ 10^7 nor in the 50 tail points.  This is the first term that would
  falsify (C).
```

```claim
id: sp-sequence-not-in-oeis
statement: The first-appearance sequence S(p) = [4, 6, 12, 30, 98, 122, 124,
  220, 308, 346, 418, 556, 962, 992, 1144, 1274, 1382, 1856, 2512, 2642,
  3526, 3818, 4618, ...] is not catalogued in the OEIS (no match on 18- and
  22-term lookups), is not a polynomial (differences never stabilize over 41
  terms), and satisfies no constant-coefficient linear recurrence of order
  ≤ 8 over 41 terms.
hypotheses: none — negative finding.
holds-here: yes.
evidence: oeis_lookup returned no match on both lookups; analyze_sequence and
  find_linear_recurrence over 41 computed terms.
status: verified-numerically (negative)
falsified-by: an OEIS entry matching these terms, or a recurrence of order ≤ 8
  fitting all 41 terms (neither exists as of this run).
```
