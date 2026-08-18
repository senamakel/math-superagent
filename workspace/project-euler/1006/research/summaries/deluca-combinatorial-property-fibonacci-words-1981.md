# de Luca 1981 — A combinatorial property of the Fibonacci words

**Source:** A. de Luca, *Information Processing Letters* 12 (1981) 193–195.
**Full text obtained:** Séminaire Lotharingien de Combinatoire reprint (scan, OCR-degraded).
**Held in library as:** `research/sources/deluca-combinatorial-property-fibonacci-words-1981.full.md`

## What the source establishes

The finite Fibonacci words are defined (in this paper's convention) by
\[
f_1 = a,\quad f_2 = b,\quad f_{n+1} = f_n f_{n-1}.
\]
(Note: this is the *other* concatenation order from PE1006's \(S_{n+2} = S_{n+1}S_n\); the two conventions are mirror images. The structural results transfer.)

**Theorem 1** (Berstel, unpublished, used by de Luca): For \(n > 3\), the Fibonacci word \(f_n\) has a **palindrome left factor of length \(|f_n| - 2\)**.

**Theorem 2** (de Luca): For all \(n \ge 4\), \(f_n\) is the **product of two uniquely determined palindrome words** of lengths \(F(n-1) - 2\) and \(F(n-2) + 2\), where \(F(n)\) is the n-th Fibonacci number.

**Uniqueness characterisation**: For \(n > 4\), the Fibonacci sequence is the *unique* sequence of words satisfying the palindrome-factorisation property plus the requirements that each word contains at least two distinct letters and begins with the same letter.

## Relevance to PE1006

- The palindrome-factorisation of finite Fibonacci words is a structural fact about the very words whose limit is the run's \(f\) (the infinite Fibonacci word). It underlies the unique-special-factor/central-word theory used in the Rauzy-graph route and in the factor-location theorems.
- The paper is the citable source for "finite Fibonacci words have a palindrome prefix of length \(|f_n| - 2\)", which is used in Wen–Wen 1994, Cassaigne 2008, and elsewhere in the library.
- It is a short note; the run's real workhorse sources remain the Lothaire chapter, Perrin–Restivo's Sturmian lecture, and the factor-location papers (Sivasankar–Rama 2022).
- **No new engine for G4**: the palindrome-factorisation does not collapse the joint-intercept second-moment problem.

## Related in-library holdings

- The later de Luca 1995 "A division property of the Fibonacci word" (IPL 54, 307–312) is a distinct result (the Crochemore/de Luca factorization of the *infinite* word), held via Fici's ar5iv source as claim `deluca-division-property-fibonacci-word`.
- Wen–Wen 1994 (`wen-wen-singular-words-fibonacci-word-1994.full.md`) builds on the palindrome-factorisation to study singular words.
- Fici 2015 (`fici-factorizations-fibonacci-infinite-word-ar5iv.full.md`) uses the division property (not the palindrome-factorisation directly).

## Claim

```claim
id: deluca-1981-palindrome-factorisation-fibonacci
statement: For n≥4, the finite Fibonacci word f_n (f_1=a, f_2=b, f_{n+1}=f_n f_{n-1}) is the product of two uniquely determined palindrome words of lengths F(n-1)-2 and F(n-2)+2; for n>3, f_n has a palindrome left factor of length |f_n|-2.
hypotheses: f_n defined by the recurrence above; F(n) = n-th Fibonacci number (F(1)=1, F(2)=1); n≥4.
holds-here: yes — the palindrome-factorisation is a structural fact about the finite words whose limit is PE1006's infinite word.
status: asserted (OCR-degraded scan; statement verified against the legible portion; independently hand-verified for n=4..7 in research/notes/verification-deluca-1981-palindrome.md)
bearing: Underlies the right-special/central-word structure of the Fibonacci word. Not by itself a route to Ψ(k).
anchor: research/sources/deluca-combinatorial-property-fibonacci-words-1981.full.md
follows-from: none (primary; Berstel's Theorem 1 is cited by de Luca)

```