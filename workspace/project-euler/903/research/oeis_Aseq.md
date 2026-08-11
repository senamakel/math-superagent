# Summary: OEIS absence results (fetched 18 Sep 2025)

All five lookups used https://oeis.org/search?q=<terms>&fmt=text (the fmt=json
endpoint returned a blocked 4-byte payload, so fmt=text was used instead).  Every one
returned "No results":

- 1,10,184,5052,191232,9851040        (A_n = f_n(1); n=2..7)        -> oeis_Aseq.md
- 5,88,4808,597876,133103808          (Q(n); n=2..6)                -> oeis_Qseq.md
- 30,290,2464,23130,235080,2728368    (|B_n|/(n-1)!, n=6..11)       -> oeis_Bdiv.md
- 0,1,1,16,39,168,425,928,1743,3008,4971   (probe)                 -> oeis_invpowers.md
- 1,4,82,1448,24832,415968,6983744,117072128 (probe)               -> oeis_invpowers2.md

Conclusion: neither the rank-sum sequence Q(n), nor the gap statistic A_n, nor the
normalized slope sequence is catalogued in the OEIS.  No closed form, recurrence, or
generating function is available there.  These sequences are apparently unstudied.
