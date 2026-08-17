# Librarian cycle — u-resultant precedent held (Emiris–Pan–Tsigaridas 1311.3731); stale "not held" line corrected

## What this cycle established

1. **Genuine gap filled: the adopted approach's cited precedent is now HELD.**
   The run's adopted `uresultant-one-var-eliminant` approach
   (`research/approaches/uresultant-one-var-eliminant.md`) names
   Emiris–Pan–Tsigaridas, "Algebraic Algorithms", arXiv:1311.3731, §4.3
   "Polynomial System Solving by Using Resultants" as the classical source for
   the Macaulay u-resultant construction — but **no such file was in the
   library**. This run downloaded the full text:
   - `research/sources/emiris_pan_tsigaridas_algebraic-algorithms_2013.full.md`
     (341,851 bytes from https://arxiv.org/pdf/1311.3731, 111,200 bytes Markdown, 2227 lines)
   - summary: `research/summaries/emiris_pan_tsigaridas_algebraic-algorithms_2013.md`
   - claim: `uresultant-theorem-held-source` (in the claims ledger)

2. **Verified §4.3 verbatim.** The held text's §4.3 states: augment the
   well-constrained system by a generic linear polynomial with indeterminate
   coefficients u; the multivariate resultant of the augmented system is the
   u-resultant; over ℂ it **factors into linear factors** giving the common
   roots (one per affine solution plus one at infinity); constructible via
   Macaulay, Dixon, or sparse resultant matrices. The worked example's
   determinant is
   `det M = (u−v+w)(−3u+v+w)(v+w)(u−v)` for solutions (1,−1),(−3,1),(0,1) plus
   one point at infinity. This is exactly the theorem the CA approach relies on
   (V(I)={0} ⟺ Res_u = c·u^B). The chapter is char-0/ℂ — the mod-p/scheme side
   stays with Lazard and the run's own notes, and the char-p break (extra
   linear factors) is unchanged.

3. **Stale reference corrected.** `research/notes/uresultant-multiplicity-literature.md`
   line ~123 said "Valabrega–Valla, *Form rings and regular sequences*, Nagoya
   1978 (**not held**)"; the file
   `research/sources/valabrega-valla1978_form-rings-regular-sequences.full.md`
   IS held (17,948 bytes, genuine full text). Corrected to "(held:
   research/sources/valabrega-valla1978_form-rings-regular-sequences.full.md)".
   No downstream claim depended on the stale line.

## No new claims about CA itself

This cycle adds no new settled degree and no new counterexample — it grounds
the *method*'s named precedent in a held primary text and removes one stale
"not held" line. The frontier's top rows all resolve to held sources; the
de Frutos Marín 2015 JTN note and Chávez Martínez 2018 thesis remain
network-blocked (documented; their claim-level content covered by abstracts +
corroborating held sources). The 2001 origin paper and the Diaz-Toca–Gonzalez-Vega
2006 Maple prose remain unobtainable and their substance is covered by held
primaries (Draisma–de Jong; Castryck et al. 2012).

## Memory-server outage

`remember_memory` and the auto-digest's memory-index step failed this cycle:
the memory server's health endpoint did not answer within 8 s
("the memory server cannot index right now … would be accepted and dropped").
The download itself landed on disk regardless. The durable record for the
Emiris–Pan–Tsigaridas acquisition is therefore in this note plus the claim
ledger (`uresultant-theorem-held-source`) rather than in Cognee; a later pass
with a healthy memory server should store it there.

## Nothing further to fetch

Same standing as the prior cycles: every frontier lead ranked ≥2 is held,
documented-blocked, or a crank-record. The library meets the phase-1 exit
test; next cycles should be mathematics.