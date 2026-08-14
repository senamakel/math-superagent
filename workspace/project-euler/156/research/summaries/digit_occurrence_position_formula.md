> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/digit_occurrence_position_formula.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.geeksforgeeks.org/dsa/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/ | converted from HTML -->

## What is in it

- Occurrences of 2 as a Digit in 0 to n
    - [Naive Approach] By checking every number from 0 to n - O(n log n) Time and O(1) Space
    - [Expected Approach] Using Digit Position Counting - O(log n) Time and O(1) Space
- Extract the higher, current, and lower parts
        # with respect to the current digit…
- Count the occurrences of digit 2 contributed
        # by the current digit position.…
    - Explore


## What it claims

- Iterate through every number from 0 to 22 and count the occurrences of digit 2 in each number.
- The digit 2 appears in 2 and 12, contributing 1 + 1 = 2 occurrences.
- It also appears in 20 and 21, contributing 1 + 1 = 2 more occurrences, making the total count 4.
- Finally, 22 contains two occurrences of digit 2, increasing the count from 4 to 6.
- Therefore, the total number of occurrences of digit 2 in the range [0, 22] is 6.

C++`

```
#include <bits/stdc++.h>
using namespace std;

// Count the occurrences of digit 2 from 0 to n.
int count2sInRange(int n) {
    int count = 0;

for (int i = 0; i <= n; i++) {
        int num = i;

while (num > 0) {
            if (num % 10 == 2) {
                count++;
            }

num /= 10;
        }
    }

return count;
}

int main() {
    int n = 22;

cout << count2sInRange(n);

return 0;
}
```

`Java`

```
class GFG {

// Count the occurrences of digit 2 from 0 to n.
    static int count2sInRange(int n) {
        int count = 0;

for (int i = 0; i <= n; i++) {
            int num = i;

while (num > 0) {
                if (num % 10 ==…

*[digest of a 13749 character source; every section, statement, and proof in full at `research/sources/digit_occurrence_position_formula.full.md`]*
