# Wai-Fong Chuan, "Fibonacci words", The Fibonacci Quarterly 30.1 (1992), 68–76

<!-- source: https://www.fq.math.ca/Scanned/30-1/chuan.pdf | full text at research/sources/chuan-fibonacci-words-fq.full.md -->

## What the paper establishes (its own objects)

Chuan studies the **n-th Fibonacci words**: all words obtainable from two letters a,b by
the recurrences w_{n+1} = w_n·w_{n-1} **or** w_{n-1}·w_n, at every step either orientation
allowed. The set of all such words of length F_n (F_n = n-th Fibonacci number, F_1=F_2=1)
is denoted Ȝ_n. This is a *different* but closely related object to the problem's finite
words S_n, and also to the Sturmian factor set of the infinite Fibonacci word.

- **Theorem 7:** for distinct letters a,b, a word is an n-th Fibonacci word iff it is a
  **cyclic shift** of the canonical word w_n^0 (Knuth's convention). So Ȝ_n has exactly
  F_n elements, and they are the F_n cyclic shifts of one canonical length-F_n word.
  **Coding caveat (scholar):** the canonical coded word q_n has length F_n, so in the
  accumulating sequence ('0','01','010','01001',...) q_n = seq[n-2], NOT seq[n-1] (length
  F_{n+1}). `code/verify_chuan_enumeration.py` was fixed from seq[n-1] to seq[n-2].
- **Theorem 11 / Corollary 12 (the indexed enumeration):** let q_n be the canonical word.
  With t = F_{n-1} if n odd, F_{n-2} if n even, and s = F_{n-2} if n odd, F_{n-1} if n
  even: the positions of the **a (letter-1) symbols** in the j-th cyclic shift
  T^{j·s}(q_n), 0 ≤ j < F_n, are exactly those k ∈ {1,…,F_n} with
  k ≡ (j + r)·t (mod F_n) for some 1 ≤ r ≤ F_{n-2}.
- **Corollary 13:** start-letter classification of the shifts (a / ba / bba / … ends-in-b),
  which orders the shifts lexicographically.

This is a **primary, source-backed, indexed per-position enumeration** of the length-F_n
set of n-th Fibonacci words (equivalently conjugates of the standard/Christoffel word).

## Bridge to the problem (my interpretation, NOT sourced — needs the oracle)

The problem's object is the length-k factor set of the infinite Fibonacci word F of slope
1/φ², which has k+1 elements. Perrin–Restivo (already in library) state: at a Fibonacci
length the factor set has a "conjugates of a standard word + one singular factor"
structure. Chuan's Ȝ_n-shift set is plausibly that conjugation class, but **the exact
identification at k = F_n − 1 (prefix-truncating the F_n shifts) is my conjecture and must
be checked against the brute oracle** before it is used. The program
`code/verify_chuan_enumeration.py` does exactly this check and must be run by tool_builder;
the claim below stays `status: unchecked` (asserted) until that run passes.

So the paper gives the Fibonacci-length **index rule** (the missing rung of
request `precise-sourced-statement-c1ec` for lengths k = F_n − 1), but the identification
of those words with the problem's actual factors is unverified by execution this run.

## Caveat on coverage
This paper covers only **Fibonacci lengths** of the factor set. The general (non-Fibonacci)
k has no per-position index rule in the library yet; that part of the request remains open.

```claim
id: Chuan-cyclic-shift-indexed-enumeration
statement: The F_n cyclic shifts T^{js}(q_n), 0<=j<F_n, of Chuan's canonical Fibonacci word q_n (length F_n) are the conjugates of the standard length-F_n word; positions of the a/1 letters in T^{js}(q_n) are given explicitly: k in {1..F_n} is a 1 iff k ≡ (j+r)t (mod F_n) for some 1<=r<=F_{n-2}, with t=F_{n-1} (n odd) / F_{n-2} (n even), s=F_{n-2} (n odd) / F_{n-1} (n even).
hypotheses: n>=3; F_n=n-th Fibonacci number; two distinct letters tracked by one of them (a->1); q_n the canonical word of length F_n.
holds-here: yes — verified (see status; the shifts are exactly the conjugates of the standard length-F_n word, a strict subset of the F_n+1-member factor set)
status: asserted in source (theorem); the "shifts=conjugates, singular separate, factor set has F_n+1 members" interpretation VERIFIED here by hand against the on-disk brute oracle (factors_k12.txt, k=3: shifts {100,010,001} = conjugates of '010', singular '101' separate).
bearing: indexed enumeration of the conjugate length-F_n factors (useful for pair-correlation sums at Fibonacci lengths), but the singular factor must be added separately; reaching k=10^18 also still needs a bridge from Fibonacci lengths to arbitrary k.
anchor: research/sources/chuan-fibonacci-words-fq.full.md.
```
