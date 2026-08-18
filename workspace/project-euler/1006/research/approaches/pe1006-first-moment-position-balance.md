---
status: conjecture-verified
idea: The first moment of the PE1006 factor values has an exact closed form at k = F_n - 1.
theme: first-moment / position-balance / repunit
---

# PE1006 — first-moment position-balance at k = F_n − 1

**Suggestion: computational conjecture (verified exactly over every term
supplied); a derivation is given in outline, not a proof.**

## Statement

Let the k+1 distinct length-k Fibonacci subwords be read as decimal numbers
(leading zeros ignored) with values v_1..v_{k+1}.  Define the FIRST moment

    M1(k) = sum_{i=1}^{k+1} v_i.

Then at every k = F_n − 1 (k = 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, ...),

    M1(k) = c1(k) * R(k),

where c1(k) = 1 + floor(k/phi^2) = A189663 is the number of length-k factors
starting with '1', and R(k) = (10^k − 1)/9 is the length-k repunit.

Equivalently: at k = F_n − 1, every decimal position among the k+1 factors
carries exactly c1(k) ones (the factors are POSITION-BALANCED), and
c1(k) = F_{n−2} = the number of 1s in the standard word q_n.

## Verification (all exact)

- Independent mechanical construction `code/mech/mech_psi.py` (formulation A
  == B in every case): M1(k) == c1(k)·R(k) exactly at ALL k = F_n−1 up to
  143 (k = 1,2,4,7,12,20,33,54,88,143).
- Independent brute string oracle `code/brute.py`: position-balance holds at
  k = 4, 7, 12 (ones per position = 2, 3, 5 = c1).
- The balance FAILS at every non-F_n−1 k (corrections M1 − c1·R appear at
  k = 3, 5, 6, 8, 9, ...).  The deviation is not a catalogued sequence and
  shows no clean closed form — so the balance is exactly anchored to the
  k = F_n−1 domain.

## Why this domain

This is exactly the Toeplitz / translation-invariant domain of directive 1's
identity C(j,jp) = A(jp−j): at k = F_n − 1 (only) the k+1 length-k factors
are the contiguous cyclic windows of the standard word q_n (length F_n),
with no de-duplication loss.  The position-balance is the FIRST-moment
transpose of that cyclic-autocorrelation symmetry: at k = F_n−1 each of the
F_n factor-windows contributes F_{n−2} = c1 ones, so the cyclic symmetry
equates the per-column sum (the transpose) to the per-window ones count.

## Weight of the claim

A computational conjecture only.  It does NOT gate the O(log) evaluation at
k = 10^18 (10^18 is not of the form F_n − 1), so it is a cross-check /
structural handle, not the committed route.  The first-moment sequence
M1(1..10) = 1, 11, 212, 2222, 22322, 323323, 3333333, 43433434, 444434444,
4454444544 is NOT in OEIS (miss recorded), consistent with the general
negative finding that these enumerative quantities carry no catalogued closed
form.

Files: this note.  Verification done in-run (commands in commands.log).
