<!-- source: https://www.geeksforgeeks.org/dsa/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/ | converted from HTML -->

Occurrences of 2 as a Digit in 0 to n - GeeksforGeeks

[image: geeksforgeeks]

[1]

[image: search icon]

-

Courses

Sale

**
-

Tutorials

**
-

Interview Prep

**

**

- [DSA][2]
- [Practice Problems][3]
- [C][4]
- [C++][5]
- [Java][6]
- [Python][7]
- [JavaScript][8]
- [Data Science][9]
- [Machine Learning][10]
- [Courses][11]
- [Linux][12]
- [DevOps][13]

# Occurrences of 2 as a Digit in 0 to n

Last Updated : 9 Jun, 2026

-
-
-

Given a non-negative integer ****n****, determine the total number of times the digit ****2****appears in the decimal representation of all integers from ****0****to ****n****(inclusive).

****Examples:****

****Input:****22
****Output: ****6
****Explanation:****The digit 2 appears in the numbers 2, 12, 20, 21, 22. Counting all occurrences gives 1 + 1 + 1 + 1 + 2 = 6. Hence, answer is 6.

****Input: ****100
****Output: ****22
****Explanation: ****The digit 2 appears 10 times in the units place and 10 times in the tens place between 0 and 100. Therefore, the total count is 20.

[image: redirect icon]

[Try It Yourself][14]

Table of Content

- [Naive Approach] By checking every number from 0 to n - O(n log n) Time and O(1) Space
- [Expected Approach] Using Digit Position Counting - O(log n) Time and O(1) Space

### [Naive Approach] By checking every number from 0 to n - O(n log n) Time and O(1) Space

The idea is to iterate through all numbers from 0 to n and count the occurrences of digit 2 in each number by examining its digits one by one.

****Step By Step Dry Run For n = 22:****

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
                if (num % 10 == 2) {
                    count++;
                }

                num /= 10;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int n = 22;

        System.out.println(count2sInRange(n));
    }
}
```

`Python`

```
# Count the occurrences of digit 2 from 0 to n.
def count2sInRange(n):
    count = 0

    for i in range(n + 1):
        num = i

        while num > 0:
            if num % 10 == 2:
                count += 1

            num //= 10

    return count

if __name__ == "__main__":
    n = 22

    print(count2sInRange(n))
```

`C#`

```
using System;

class GFG {

    // Count the occurrences of digit 2 from 0 to n.
    static int count2sInRange(int n) {
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

    static void Main()
    {
        int n = 22;

        Console.WriteLine(count2sInRange(n));
    }
}
```

`JavaScript`

```
// Count the occurrences of digit 2 from 0 to n.
function count2sInRange(n) {
    let count = 0;

    for (let i = 0; i <= n; i++) {
        let num = i;

        while (num > 0) {
            if (num % 10 === 2) {
                count++;
            }

            num = Math.floor(num / 10);
        }
    }

    return count;
}

const n = 22;

console.log(count2sInRange(n));
```

`

**Output**

```
6
```

### [Expected Approach] Using Digit Position Counting - O(log n) Time and O(1) Space

Instead of checking every number individually, process each digit position (1s, 10s, 100s, ...) independently. For every position, compute the contribution of digit 2 using the digits to its left (higher), the current digit (curr), and the digits to its right (lower). Summing the contributions from all digit positions gives the total count efficiently.

****Step By Step Dry Run For n = 22:****

- For the units place (factor = 1), we have higher = 2, curr = 2, and lower = 0. Since curr == 2, the contribution is higher × factor + lower + 1 = 2 × 1 + 0 + 1 = 3. The current count becomes 3.
- For the tens place (factor = 10), we have higher = 0, curr = 2, and lower = 2. Since curr == 2, the contribution is higher × factor + lower + 1 = 0 × 10 + 2 + 1 = 3. The current count becomes 6.
- The next factor is 100, which exceeds n, so no further positions need to be processed.
- Therefore, the total number of occurrences of digit 2 in the range [0, 22] is 6.

C++`

```
#include <bits/stdc++.h>
using namespace std;

// Count the occurrences of digit 2 from 0 to n.
int count2sInRange(int n) {
    int count = 0;

    for (int factor = 1; factor <= n; factor *= 10) {

        // Extract the higher, current, and lower parts
        // with respect to the current digit position.
        int lower = n % factor;
        int curr = (n / factor) % 10;
        int higher = n / (factor * 10);

        // Count the occurrences of digit 2 contributed
        // by the current digit position.
        if (curr < 2) {
            count += higher * factor;
        } else if (curr == 2) {
            count += higher * factor + lower + 1;
        } else {
            count += (higher + 1) * factor;
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

        for (int factor = 1; factor <= n; factor *= 10) {

            // Extract the higher, current, and lower parts
            // with respect to the current digit position.
            int lower = n % factor;
            int curr = (n / factor) % 10;
            int higher = n / (factor * 10);

            // Count the occurrences of digit 2 contributed
            // by the current digit position.
            if (curr < 2) {
                count += higher * factor;
            } else if (curr == 2) {
                count += higher * factor + lower + 1;
            } else {
                count += (higher + 1) * factor;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int n = 22;

        System.out.println(count2sInRange(n));
    }
}
```

`Python`

```
# Count the occurrences of digit 2 from 0 to n.
def count2sInRange(n):
    count = 0

    factor = 1
    while factor <= n:

        # Extract the higher, current, and lower parts
        # with respect to the current digit position.
        lower = n % factor
        curr = (n // factor) % 10
        higher = n // (factor * 10)

        # Count the occurrences of digit 2 contributed
        # by the current digit position.
        if curr < 2:
            count += higher * factor
        elif curr == 2:
            count += higher * factor + lower + 1
        else:
            count += (higher + 1) * factor

        factor *= 10

    return count

n = 22

print(count2sInRange(n))
```

`C#`

```
using System;

class GFG
{
    // Count the occurrences of digit 2 from 0 to n.
    static int count2sInRange(int n)
    {
        int count = 0;

        for (int factor = 1; factor <= n; factor *= 10)
        {
            // Extract the higher, current, and lower parts
            // with respect to the current digit position.
            int lower = n % factor;
            int curr = (n / factor) % 10;
            int higher = n / (factor * 10);

            // Count the occurrences of digit 2 contributed
            // by the current digit position.
            if (curr < 2)
            {
                count += higher * factor;
            }
            else if (curr == 2)
            {
                count += higher * factor + lower + 1;
            }
            else
            {
                count += (higher + 1) * factor;
            }
        }

        return count;
    }

    static void Main()
    {
        int n = 22;

        Console.WriteLine(count2sInRange(n));
    }
}
```

`JavaScript`

```
// Count the occurrences of digit 2 from 0 to n.
function count2sInRange(n) {
    let count = 0;

    for (let factor = 1; factor <= n; factor *= 10) {

        // Extract the higher, current, and lower parts
        // with respect to the current digit position.
        const lower = n % factor;
        const curr = Math.floor(n / factor) % 10;
        const higher = Math.floor(n / (factor * 10));

        // Count the occurrences of digit 2 contributed
        // by the current digit position.
        if (curr < 2) {
            count += higher * factor;
        } else if (curr === 2) {
            count += higher * factor + lower + 1;
        } else {
            count += (higher + 1) * factor;
        }
    }

    return count;
}

const n = 22;

console.log(count2sInRange(n));
```

`

**Output**

```
6
```

Comment

### Explore

DSA Fundamentals**

  - **[Logic Building Problems 2 min read][15]
  - **[Analysis of Algorithms 1 min read][16]

Data Structures**

  - **[Array 3 min read][17]
  - **[String 2 min read][18]
  - **[Hashing 2 min read][19]
  - **[Linked List 3 min read][20]
  - **[Stack 2 min read][21]
  - **[Queue 2 min read][22]
  - **[Tree 2 min read][23]
  - **[Graph 3 min read][24]

Algorithms**

  - **[Searching Algorithms 2 min read][25]
  - **[Sorting Algorithms 3 min read][26]
  - **[Introduction to Recursion 15 min read][27]
  - **[Greedy Algorithms 3 min read][28]
  - **[Graph Algorithms 3 min read][29]
  - **[Dynamic Programming 2 min read][30]
  - **[Bitwise Algorithms 4 min read][31]

Advanced**

  - **[Segment Tree 2 min read][32]
  - **[Binary Indexed Tree 12 min read][33]
  - **[Trie Data Structure 15+ min read][34]
  - **[Square Root (Sqrt) Decomposition Algorithm 15+ min read][35]

Interview Preparation**

  - **[Software Developer Interview Preparation 2 min read][36]
  - **[GFG 160 2 min read][37]
  - **[Coding Practice 1 min read][38]
  - **[POTD 2 min read][39]

Courses**

  - **[Placement 360 Course 2 min read][40]
  - **[DSA and System Design Course 2 min read][41]


## Links

[1]: https://www.geeksforgeeks.org/
[2]: https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/
[3]: https://www.geeksforgeeks.org/explore
[4]: https://www.geeksforgeeks.org/c/c-programming-language/
[5]: https://www.geeksforgeeks.org/cpp/c-plus-plus/
[6]: https://www.geeksforgeeks.org/java/java/
[7]: https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
[8]: https://www.geeksforgeeks.org/javascript/javascript-tutorial/
[9]: https://www.geeksforgeeks.org/data-science/data-science-for-beginners/
[10]: https://www.geeksforgeeks.org/machine-learning/machine-learning/
[11]: https://www.geeksforgeeks.org/courses
[12]: https://www.geeksforgeeks.org/linux-unix/linux-tutorial/
[13]: https://www.geeksforgeeks.org/devops/devops-tutorial/
[14]: https://www.geeksforgeeks.org/problems/occurences-of-2-as-a-digit/1
[15]: https://www.geeksforgeeks.org/dsa/logic-building-problems/
[16]: https://www.geeksforgeeks.org/dsa/analysis-of-algorithms/
[17]: https://www.geeksforgeeks.org/dsa/array-data-structure-guide/
[18]: https://www.geeksforgeeks.org/dsa/string-data-structure/
[19]: https://www.geeksforgeeks.org/dsa/hashing-data-structure/
[20]: https://www.geeksforgeeks.org/dsa/linked-list-data-structure/
[21]: https://www.geeksforgeeks.org/dsa/stack-data-structure/
[22]: https://www.geeksforgeeks.org/dsa/queue-data-structure/
[23]: https://www.geeksforgeeks.org/dsa/tree-data-structure/
[24]: https://www.geeksforgeeks.org/dsa/graph-data-structure/
[25]: https://www.geeksforgeeks.org/dsa/searching-algorithms/
[26]: https://www.geeksforgeeks.org/dsa/sorting-algorithms/
[27]: https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/
[28]: https://www.geeksforgeeks.org/dsa/greedy-algorithms/
[29]: https://www.geeksforgeeks.org/dsa/graph-data-structure-and-algorithms/
[30]: https://www.geeksforgeeks.org/dsa/dynamic-programming/
[31]: https://www.geeksforgeeks.org/dsa/bitwise-algorithms/
[32]: https://www.geeksforgeeks.org/dsa/segment-tree-data-structure/
[33]: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-or-fenwick-tree-2/
[34]: https://www.geeksforgeeks.org/dsa/trie-insert-and-search/
[35]: https://www.geeksforgeeks.org/dsa/square-root-sqrt-decomposition-algorithm/
[36]: https://www.geeksforgeeks.org/interview-prep/interview-corner/
[37]: https://www.geeksforgeeks.org/courses/gfg-160-series
[38]: https://www.geeksforgeeks.org/dsa/geeksforgeeks-practice-best-online-coding-platform/
[39]: https://www.geeksforgeeks.org/problem-of-the-day
[40]: https://www.geeksforgeeks.org/courses/placement-360-cip-complete-tech-interview
[41]: https://www.geeksforgeeks.org/courses/interviewe-101-data-structures-algorithm-system-design
