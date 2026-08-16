# Pattern-finder note — count-level parity of c0 vs c2 refuted

Prior pass (`regularity_findings_2.md`) reported the running counts
`#{n<=400 : c0(n) odd}` and `#{n<=400 : c2(n) odd}` both equal to 211. That
equal-value row is a natural candidate regularity, so it was tested here to
large N. It fails: the equality is a crossing, not a law.

```claim
id: c0c2-count-parity-not-equal
statement: The running counts #{n<=N : c0(n) odd} and #{n<=N : c2(n) odd} of
  the ternary zero-count and two-count of 2^n are NOT equal in general. They
  coincide at N=400 (both 211), but already differ at N=200 (109 vs 106) and
  diverge widely by N=30000 (14824 vs 15073). The only exact relation among
  the parities is the modular identity c0 == c2 + L(n) (mod 2), where
  L(n) = number of ternary digits of 2^n (consequence of the proved c1-even
  and of c0+c1+c2 = L). There is no exact count-level equality: parities of
  c0 and c2 are not equal in general (197 violations of c0==c2 mod 2 already
  over n=1..400) and their odd-counts drift.
hypotheses: n >= 1.
holds-here: yes — verified by two independent programs (incremental base-3
  digit counter, and direct 2**n digit counting) that agree at N=200,400,30000.
  c0 == c2 + L mod 2 verified for every n < 30000, no exception.
status: checked (negative result; the coincidence is refuted, the modular
  identity is a theorem).
bearing: closes the candidate that "the count of n with an odd zero-count
  equals the count with an odd two-count" could be an invariant of the
  survivor stats. It is not. The only exact parity facts are c1-even and the
  modular identity c0 == c2 + L mod 2. A symbolic invariant cannot rest on a
  c0/c2 count balance.
anchor: code/out/regularity_findings_3.md
```

This replaces the gap left by regularity_findings_2.md, which noted the 211=211
values but did not test them.
