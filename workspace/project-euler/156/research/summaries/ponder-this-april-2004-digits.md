# IBM Ponder This, April 2004 — "the first cassette that cannot be labelled"

**Source:** https://research.ibm.com/haifa/ponderthis/challenges/April2004.html (IBM Research "Ponder This" challenge, April 2004, authored by Michael Brand). Full text: `research/sources/ponder-this-april-2004-digits.full.md`.

## What it is

The original published version of the **"more than"** variant of the VHS-sticker puzzle: number cassettes 1, 2, 3, ... with one of each digit sticker per cassette; find the first cassette N that can no longer be labelled (i.e. the first x with fd(x) > x for some digit d, where fd(x) counts occurrences of digit d in the numbers 1..x). Khovanova & Marton (in the "Archive Labeling Sequences" paper, §3 and its Table 1) refer to this as their a>(d) sequence and credit Michael Brand; it is OEIS A164321.

## The lemmas it proves (base B, general)

- **c(1,n) ≥ c(b,n) for every digit b** (and every base B): a 1-to-1 map pairs each occurrence of digit b in position B^d of numeral n' with an occurrence of digit 1 in the same position of the lesser numeral n' − (b−1)·B^d (or n' − (B−1)·B^d for b=0). So sticker 1 runs out no later than any other sticker.
- **The leading digit of N is 1**: if N's leading digit were b > 1, decomposing E(N) = C(N) − N as E(M) + (d−2)E(m) + E(m') with M < N, m < N, m' < N all having E ≤ 0 gives E(N) ≤ 0, contradicting E(N) > 0.
- (Full solution section on disk gives the answer for general base B.)

## Relevance to PE156

- Not a primary source for the run's answer: it solves the a>(1) ("first time the count exceeds the index") variant, whose answer in base 10 is 199 991 — **10 more than** PE156's first non-trivial solution 199 981. The "exactly" variant (fd(x) = x) is the one PE156 asks for, and its solutions are the E_d sequences of Khovanova & Marton and the OEIS entries A014778/A101639–A101641/A130427–A130431.
- Useful as: (a) historical provenance for the puzzle family; (b) the c(1,n) ≥ c(b,n) monotonicity fact, which independent verifiers can reuse; (c) a second, independent route to the *structure* of solutions in a different base when cross-checking the run's base-10 solver.