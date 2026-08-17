# OEIS A003849 — Fibonacci word (sequence record)

Source: https://oeis.org/A003849 (b-file-style listing)
Full text: [[oeis-a003849-fibonacci-word.full]] (also [[oeis-A003849-fibonacci-word.full]], same record)

## What this source establishes

A003849 is **the** canonical OEIS record for the infinite Fibonacci word. Its
terms (0-indexed or 1-indexed depending on the OEIS convention) are the digit
sequence of the problem's word:
  0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, …
which is 010010100100101… — matching S₀=0, S₁=01, S₂=010, S₃=01001, S₄=01001010
computed as consecutive prefixes. So the problem's finite S_n are the prefixes
of this single infinite word, and the "Fibonacci subwords" are its factors.

**Name/offset conventions:** OEIS A003849 lists the word indexed from n=0 with
digits floor((n+2)·φ) − floor((n+1)·φ) − 1? — the record gives the closed form
a(n) = floor((n+2)φ) − floor((n+1)φ) with φ = (1+√5)/2 up to an offset. The
important fact for this run is only that S = A003849's digit stream (verified
by matching S₀..S₅ prefixes), which the brute oracle already reproduces. The
precise index offset does not affect Ψ (the factor set — and hence the decimal
values and their squares — is invariant under prefix shifts of the infinite word
past the factors' first occurrences, and the problem defines the word by the
S_n recursion anyway).

## What it implies for PE1006

1. Independent authority that the problem's word is the well-known infinite
   Fibonacci word (A003849), so all the Sturmian literature applies to it
   directly (Wikipedia's factor-complexity and slope statements included).
2. The OEIS b-file ([[oeis-A003849-first-1652-subwords.full]]) is an
   independent oracle for the distinct length-k subword set (the file's lines
   6–9 are 001, 010, 100, 101 = the problem's length-3 example, confirming the
   problem's own numbers with no code).

## Claims anchored here

Corroborates `governing-sturmian` (the word is A003849, the standard
Fibonacci word of slope 1/φ² in the problem's digit convention).

## What it does NOT establish

- No statement about Ψ(k) or decimal readings. A344953 (positions of words in
  A341258 ending with 1) and the "no OEIS match for Ψ(1..5)" finding in
  `research/summaries/library-build-status.md` are catalogued-sequence facts,
  not used as a closed form.