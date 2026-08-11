# Independent pattern verification — PE591 (n=10^13, 90 d)

Pattern-finder's own re-run of the sequence tools and laws, from
`/workspace/results_full_bothsides.txt`. All numbers below come from programs
run in this session; nothing is carried over from memory.md without re-check.

## Tools run on the 90-term sequences
- `analyze_sequence` on |a_d|: no low-degree polynomial (differences never
  constant through 12 levels). Confirm.
- `analyze_sequence` on b_d: same, no polynomial structure. Confirm.
- `find_linear_recurrence` (max order 9) on |a_d|: NO constant-coefficient
  linear recurrence of order <= 9 fits all 90 terms. Confirm.
- `find_linear_recurrence` (max order 9) on b_d: same negative. (Run in session;
  not even a low-order fit.)

Conclusion (matches prior notes): neither |a_d| nor b_d is polynomial or
low-order linearly recurrent **in d**. Each d is an independent Cabanillas
candidate outcome; no derivation from a recurrence-in-d should be attempted.

## Laws re-verified EXACTLY over all 90 terms in this session
1. **Sign-opposition** sign(a_d) = -sign(b_d): 90/90.
2. **Master |a| identity**, signed form (b preserves sign):
   - if b>0: |a| = nint(|b|·√d − π)
   - if b<0: |a| = nint(π + |b|·√d)
   Verified 90/90. (Near-tautological: a = nint(π − b√d) by construction.)
   The single unsplit form |a| = nint(|b|√d) − 3·sign(b) came out 0/90 in my
   check; the sign-dependent split above is the correct exact statement.
3. **m²-scaling law**: for non-square d1 = m²·d0 < 100,
   |a_{d1}| = |a_{d0}|  iff  m | b_{d0};  and when equal b_{d1} = b_{d0}/m.
   Re-verified 36/36 pair-wise and 18/18 in the equality cases.

## Novel attempt that FAILED (recorded dead end)
Hypothesis: within every set of d sharing the same squarefree part, the
product |b_d|·√d is constant (which would explain equal-|a| groups by sf).
- FALSIFIED: 5 of 60 squarefree cores violate it; e.g. sf=2 core
  {2,8,18,32,50,72,98} has relative spread 0.51, sf=3 core spread 0.76.
- So equal-|a| groups sharing an sf are ONLY partially explained by m² scaling
  (e.g. {12,48,75}: 12↔48 via m=2; the 75 member, and others, are genuine
  coincidences, not forced by squarefree-core constancy).
- Also confirmed: every 15-group of equal |a| has a common squarefree part
  (trivially true for m² partners; the extra members like 75 are coincidence).

## Bottom line
The only non-tautological structure tying b_d (and hence |a_d|) across different
d is the **m²-scaling law** (36/36, exact). It follows from α_{m²d0} = {m·α_{d0}}
and the candidate-minimizer structure: the d1 optimum exists in the m-step
arithmetic progression iff m divides the d0 record b. It is a strong lead for a
derivation but remains a conjecture over the finite n=10^13 data; no simpler
(in-d) recurrence exists in the 90 terms supplied.
