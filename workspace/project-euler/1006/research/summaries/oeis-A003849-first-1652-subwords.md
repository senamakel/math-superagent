# OEIS A003849 factor corpus — the first 1652 distinct subwords

Source: https://oeis.org/A003849/a003849.txt
Full text: [[oeis-A003849-first-1652-subwords.full]]

## What this source establishes

A b-file-style corpus: the first 1652 **distinct factors (subwords) of the
infinite Fibonacci word A003849**, listed as binary strings *with leading
zeros*, in order of length then lexicographic order. Lines 1–2 are the length-1
factors, 3–5 the length-2, 6–9 the length-3, 10–14 the length-4, etc.
(Line count per length follows the k+1 rule: 1→2, 2→3, 3→4, ….)

**Length-3 block (lines 6–9): 001, 010, 100, 101.**
These are exactly the problem statement's four length-3 Fibonacci subwords and
the brute oracle's set — full agreement, independent of the problem's own text
and of any computation in this workspace.

**Length-1 block: 0, 1; length-2 block: 00, 01, 10; length-4: 0010, 0100,
0101, 1001, 1010** — each block count = length+1, confirming the k+1 factor
complexity from an on-disk authority.

## What it implies for PE1006

1. **Independent oracle for small k.** The first 10 lines of this file are an
   authoritative list of the length-1..4 factors: any solver construction
   (mechanical-word with arc midpoints, position theorem, floor-sum) must
   reproduce these exact strings for k ≤ 4. The brute oracle already does;
   the mechanical-word check at k=3 with slope 34/89 also does.
2. It pins the *problem's* digit convention: the corpus lists the factors of
   the *problem's* word (0-heavy, slope 1/φ²), NOT of the rabbit-sequence
   complement — so it can be used to catch a 0↔1 swap in any implementation
   (the swap would give {011,101,110,010}, none of which appear in the
   length-3 block).
3. The k+1-per-length pattern in the line numbering means the corpus could in
   principle extend a brute oracle up to k=57 (1652 ≈ Σ(k+1) ⇒ k ≈ 57) without
   recomputing the word.

## Claims anchored here

Corroborates `governing-factor-complexity` (count k+1) and
`mechanical-word-digit-rule` (the exact factor set at slope 1/φ²).

## What it does NOT establish

- No decimal values / no Ψ. The corpus gives the strings, not their numeric
  interpretations; the sum-of-squares is still the run's computation.
- No statement about the *ordering* convention beyond "length then
  lexicographic", which is fine for set-comparison purposes.