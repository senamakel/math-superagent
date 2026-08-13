# OEIS A000232 — block length before first term > 2 in the Gilbreath difference triangle

Source: https://oeis.org/search?q=id:A000232&fmt=text (fetched this run; plain text, 2898 bytes)

## Definition (verbatim)
%N A000232 Construct a triangle as in A036262. Sequence is one less than the position of the first number larger than 2 in the n-th row (n-th difference).
%O A000232 1,1

That is, A000232(n) = (index of the first entry > 2 in the n-th row of the iterated-absolute-difference triangle of the primes, 1-based) minus 1. The block-profile quantity this run computes is the count of consecutive leading {0,2} entries in row A_k; both are the same "position of first term > 2, minus 1", so block_profile(k) = A000232(k).

## Terms (verbatim)
3, 8, 14, 14, 25, 24, 23, 22, 25, 59, 98, 97, 98, 97, 174, 176, 176, 176, 176, 291, 290, 289, 740, 874, 873, 872, 873, 872, 871, 870, 869, 868, 867, 866, 2180, 2179, 2178, 2177, 2771, 2770, 2769, 2768, 2767, 2766, 2765, 2764, 2763, 2763, 2763, 2763, 3366, 4208, 4207, ...

Minus 1 gives the block profile: 2, 7, 13, 13, 24, 23, 22, 21, 24, 58, 97, 96, 97, 96, 173, 175, 175, 175, 175, 290, 289, 288, 739, 873, 872, 871, 872, 871, 870, 869, 868, 867, 866, 865, 2179, 2178, 2177, 2176, 2770, 2769, ... — matching the run's computed block profile (k=1..6: 2,7,13,13,24,23).

## References cited in the entry (the catalogue's own bibliography)
- W. Sierpiński, A Selection of Problems in the Theory of Numbers, Macmillan NY 1964, p. 35.
- R. B. Killgrove and K. E. Ralston, "On a conjecture concerning the primes", Math. Comp. 13 (1959) 121–122. doi 10.1090/S0025-5718-59-99262-2
- Chris Caldwell, "Gilbreath's conjecture", Prime Glossary t5k.org/glossary/page.php?sort=GilbreathsConjecture
- Albert N. Debono, "More on primes", Numbers and Computers (11).
- Eric Weisstein, MathWorld "Gilbreath's Conjecture".
- Sloane, A Handbook of Integer Sequences (1973); Sloane & Plouffe, Encyclopedia of Integer Sequences (1995).

## Relation / confirmations
- %F: A000232(n) = A036277(n) − 1 (T. D. Noe, 2007).
- %C: "Related to Gilbreath conjecture." and (Bartlomiej Pawlik, 2025-11-28): "In particular, if a(n) > 2 for every n, then the Gilbreath conjecture is true." (a(n) large ⟹ a long {0,2} block protects rows — the block lemma.)
- %Y: Cf. A001549.
- Note the entry does NOT itself carry a closed form; the growth must come from the mathematics, confirming the OEIS lookup "the block-profile sequence is uncatalogued" finding for the OFFSET-MINUS-1 form that was searched.

## Purpose in this library
This is the concrete catalogue file backing the claim `block-profile-equals-a000232-minus-1` (`research/ROOT.md`), which was previously anchored at `oeis-A000232` with no file on disk. It is now a read-from-catalogue claim whose catalogue is present, and it independently confirms the run's computed block lengths against a published table.
