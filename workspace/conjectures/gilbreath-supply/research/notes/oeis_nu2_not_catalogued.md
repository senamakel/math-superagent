# ν₂(n) is not in the OEIS

```claim
id: oeis-nu2-not-catalogued
statement: The SUPPLY sequence, first terms 1,1,2,1,2,1,2,1,2,7,4,5,3,5,3,11,7,7,13,10
  (n = 3..22; ν₂(n) = number of 2s in the maximal {0,2} suffix of the right
  diagonal of the absolute-difference triangle of the primes), is NOT found in
  the OEIS.
hypotheses: the values are per the run's oracle; first terms as listed.
holds-here: yes
status: checked (oeis_lookup on the 20-term prefix returned no match)
bearing: no catalogued closed form or recurrence to look up; the sequence's
  structure must come from the problem itself. Directs future work to line-sum
  forms (Northshield) rather than an OEIS match.
anchor: research/notes/oeis_nu2_not_catalogued.md
```

Twenty consecutive terms (n = 3..22) sent to the OEIS returned no entry.
This is a negative result worth recording so nobody searches again.
