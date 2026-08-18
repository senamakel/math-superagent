# Verification of de Luca 1981 palindrome-factorisation claim (hand-checked, exact)

Claim `deluca-1981-palindrome-factorisation-fibonacci` (note:
`research/summaries/deluca-combinatorial-property-fibonacci-words-1981.md`):
for n≥4, f_n (f_1=a, f_2=b, f_{n+1}=f_n f_{n-1}) is the product of two
uniquely determined palindrome words of lengths F(n−1)−2 and F(n−2)+2; for
n>3, f_n has a palindrome left factor of length |f_n|−2.

Convention here: F(1)=1, F(2)=1 (standard Fibonacci numbers), so
|f_n| = F(n). |f_4|=3, |f_5|=5, |f_6|=8, |f_7|=13.

## Direct computation (exact, by hand)

f_1 = a
f_2 = b
f_3 = f_2 f_1 = ba          (|f_3| = 2 = F(3))
f_4 = f_3 f_2 = ba·b = bab  (|f_4| = 3 = F(4))
f_5 = f_4 f_3 = bab·ba = babba  (|f_5| = 5 = F(5))
f_6 = f_5 f_4 = babba·bab = babbabab  (|f_6| = 8 = F(6))
f_7 = f_6 f_5 = babbabab·babba = babbababbabba  (|f_7| = 13 = F(7))

### n=4: lengths F(3)−2=1 and F(2)+2=3
f_4 = bab = (b)(ab·?) — split at position 1: p=b (pal), q=ab? no.
Wait: the claimed split lengths are F(n−1)−2 and F(n−2)+2.
For n=4: F(3)−2 = 2−2 = 0 and F(2)+2 = 1+2 = 3. p=ε, q=bab.
ε is a palindrome; bab is a palindrome. ✓ (p = empty palindrome, q = bab)
So f_4 = ε·bab, both palindromes. ✓

### n=5: lengths F(4)−2 = 3−2 = 1, F(3)+2 = 2+2 = 4
f_5 = babba. Split at position 1: p=b (pal), q=abba (pal? a b b a reversed =
a b b a ✓). f_5 = b·abba. ✓

### n=6: lengths F(5)−2 = 5−2 = 3, F(4)+2 = 3+2 = 5
f_6 = babbabab. Split at position 3: p=bab (pal ✓), q=babab (b a b a b is a
palindrome ✓). f_6 = bab·babab. ✓

### n=7: lengths F(6)−2 = 8−2 = 6, F(5)+2 = 5+2 = 7
f_7 = babbababbabba. Split at position 6: p=babbab (b a b b a b; reversed
b a b b a b ✓ palindrome), q=babba = f_5 (pal? b a b b a reversed a b b a b ✗
NOT palindrome).

Hmm — f_7 split at 6 gives q = "babba" (positions 7–13), which is NOT a
palindrome. Let me re-check the claimed lengths.

The summary's claim says "palindrome words of lengths F(n−1)−2 and F(n−2)+2".
For n=7: F(6)−2 = 8−2 = 6, F(5)+2 = 5+2 = 7. Total 13 = |f_7| ✓ lengths sum
correctly. But my hand split at 6 gives q = babba, not a palindrome.

Let me recompute f_7 carefully.

f_5 = f_4 f_3 = bab·ba = babba  (5 chars: b a b b a)
f_6 = f_5 f_4 = babba·bab = b a b b a b a b  (8 chars: b a b b a b a b)
f_7 = f_6 f_5 = b a b b a b a b · b a b b a
     = b a b b a b a b b a b b a   (13 chars)

Index: 1:b 2:a 3:b 4:b 5:a 6:b 7:a 8:b 9:b 10:a 11:b 12:b 13:a

Split at 6: p = chars 1-6 = b a b b a b. Reverse: b a b b a b ✓ palindrome.
q = chars 7-13 = a b b a b b a. Reverse: a b b a b b a ✓ palindrome!

I mis-transcribed q earlier. q = a b b a b b a IS a palindrome. ✓

So for n=7: p=babbab (len 6 = F(6)−2), q=abbabba (len 7 = F(5)+2). Both
palindromes. ✓

### Palindrome left factor of length |f_n|−2 (Berstel, n>3)
n=4: f_4=bab, |f_4|−2=1, prefix "b" palindrome ✓
n=5: f_5=babba, |f_5|−2=3, prefix "bab" palindrome ✓
n=6: f_6=babbabab, |f_6|−2=6, prefix "babbab" palindrome ✓
n=7: f_7=babbababbabba, |f_7|−2=11, prefix "babbababbab" (chars 1-11):
  b a b b a b a b b a b reversed b a b b a b a b b a b ✓ palindrome

## Verdict

The claim block's statement is CONFIRMED by direct exact computation for
n = 4, 5, 6, 7. The two-palindrome product (lengths F(n−1)−2, F(n−2)+2) and
the palindrome-prefix-of-length-|f_n|−2 both hold in every checked case.
Status upgrade possible: asserted → verified-for-n≤7 (the note already says
"verified against the legible OCR portion"). No contradiction found.

Note the convention detail: the claim uses F(1)=F(2)=1, and the palindrome
lengths for n=4 give p=ε, q=f_4 — the empty word counts as a palindrome,
consistent with "product of two palindromes".

Recorded 2026-08-20 by scholar digest cycle (memory server down).
