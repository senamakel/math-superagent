> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/digit-count-place-value-algorithm.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.geeksforgeeks.org/dsa/find-the-occurrences-of-y-in-the-range-of-x/ | converted from HTML -->

## What is in it

- Occurrences of a Digit in 1 to n
    - [Naive Approach] Generate All Numbers and Count Digit Occurrences - O(n × log₁₀ n) Time…
- Check every number from 1 to n.
    for num in range(1, limit + 1):
        curr =…
- Count occurrences of digit d.
        for ch in curr:
            if ord(ch) - ord('0')…
    - [Expected Approach] Using Digit DP with Count and Contribution - O(len(n) × 10) Time and…
- End reached
    if pos == len(n):
        return (1, 0)
- Memoized state
    if dp[pos][tight][started] != (-1, -1):
        return…
- Max digit allowed
    limit = int(n[pos]) if tight else 9
- Try all digits
    for digit in range(limit + 1):
- Update states
        newTight = 1 if (tight and digit == limit) else 0…
- …


## What it claims

Given a number ****n****represented as a string and a digit ****d****, count the total number of times digit d appears in all numbers from 1 to n (inclusive). Since the answer can be very large, return it modulo 10^9 + 7.

****Examples:****

****Input: ****n = "25", d = 2
****Output: ****9
****Explanation:****The occurrences are "2", "12", "20", "21", "22" (two occurrences), "23", "24", "25". Total 9 occurrences.

****Input:****n = "25", d = 3
****Output:****3
****Explanation:****The occurrences are "3", "13" and "23". Total 3 occurrences.

Table of Content

- [Naive Approach] Generate All Numbers and Count Digit Occurrences - O(n × log₁₀ n) Time and O(log₁₀ n) Space
- [Expected Approach] Using Digit DP with Count and Contribution - O(len(n) × 10) Time and O(len(n)) Space

*[digest of a 19896 character source; every section, statement, and proof in full at `research/sources/digit-count-place-value-algorithm.full.md`]*
