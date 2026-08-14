<!-- source: https://www.geeksforgeeks.org/dsa/find-the-occurrences-of-y-in-the-range-of-x/ | converted from HTML -->

Occurrences of a Digit in 1 to n - GeeksforGeeks

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

# Occurrences of a Digit in 1 to n

Last Updated : 28 Jul, 2026

-
-
-

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

### [Naive Approach] Generate All Numbers and Count Digit Occurrences - O(n × log₁₀ n) Time and O(log₁₀ n) Space

The idea is to iterate through every number from 1 to n, convert each number into a string and count how many times digit d appears in it. The total count of occurrences is returned at the end.

****Note:****This approach does not handle the given constraints efficiently. For large values of n (up to 20 digits), the number may exceed the range of built-in integer types in some languages, and checking every number from 1 to n can lead to TLE.

C++`

```
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int getOccurrence(string &n, int d)
{
    long long limit = stoll(n);
    long long ans = 0;

    // Check every number from 1 to n.
    for (long long num = 1; num <= limit; num++)
    {
        string curr = to_string(num);

        // Count occurrences of digit d.
        for (char ch : curr)
        {
            if (ch - '0' == d)
            {
                ans = (ans + 1) % MOD;
            }
        }
    }

    return (int)ans;
}

int main()
{
    string n = "25";
    int d = 2;

    cout << getOccurrence(n, d) << endl;

    return 0;
}
```

`Java`

```
class GFG {

    static final int MOD = 1000000007;

    static int getOccurrence(String n, int d)
    {
        long limit = Long.parseLong(n);
        long ans = 0;

        // Check every number from 1 to n.
        for (long num = 1; num <= limit; num++) {
            String curr = Long.toString(num);

            // Count occurrences of digit d.
            for (char ch : curr.toCharArray()) {
                if (ch - '0' == d) {
                    ans = (ans + 1) % MOD;
                }
            }
        }

        return (int)ans;
    }

    public static void main(String[] args)
    {
        String n = "25";
        int d = 2;

        System.out.println(getOccurrence(n, d));
    }
}
```

`Python`

```
def getOccurrence(n, d):

    MOD = 1000000007

    limit = int(n)
    ans = 0

    # Check every number from 1 to n.
    for num in range(1, limit + 1):
        curr = str(num)

        # Count occurrences of digit d.
        for ch in curr:
            if ord(ch) - ord('0') == d:
                ans = (ans + 1) % MOD

    return ans

if __name__ == "__main__":
    n = "25"
    d = 2
    print(getOccurrence(n, d))
```

`C#`

```
using System;

class GFG {

    const int MOD = 1000000007;

    static int getOccurrence(string n, int d)
    {
        long limit = long.Parse(n);
        long ans = 0;

        // Check every number from 1 to n.
        for (long num = 1; num <= limit; num++) {
            string curr = num.ToString();

            // Count occurrences of digit d.
            foreach (char ch in curr) {
                if (ch - '0' == d) {
                    ans = (ans + 1) % MOD;
                }
            }
        }

        return (int)ans;
    }

    static void Main()
    {
        string n = "25";
        int d = 2;

        Console.WriteLine(getOccurrence(n, d));
    }
}
```

`JavaScript`

```
function getOccurrence(n, d)
{
    const MOD = 1000000007;

    let limit = BigInt(n);
    let ans = 0n;

    // Check every number from 1 to n.
    for (let num = 1n; num <= limit; num++) {
        let curr = num.toString();

        // Count occurrences of digit d.
        for (let ch of curr) {
            if (Number(ch) === d) {
                ans = (ans + 1n) % BigInt(MOD);
            }
        }
    }

    return Number(ans);
}

// Driver code
let n = "25";
let d = 2;

console.log(getOccurrence(n, d));
```

`

**Output**

```
9
```

### [Expected Approach] Using Digit DP with Count and Contribution - O(len(n) × 10) Time and O(len(n)) Space

The idea is to use Digit DP to build all numbers from 1 to n digit by digit. For every state, we keep track of the current position, whether the constructed prefix is still equal to the prefix of n (tight), and whether a non-leading digit has started. Each DP state returns the number of valid numbers that can be formed and the total occurrences of digit d in those numbers. Whenever digit d is placed at the current position, every valid suffix contributes one additional occurrence, which is added using the number of valid suffixes returned by the recursive call.

Let us understand with example:
Input: n = "25", d = 2

- Start Digit DP from position 0. Since the first digit of n is 2, the DP can choose 0, 1, or 2 at the first position.
- For prefixes 0 and 1, the DP generates all valid suffixes within the limit and counts occurrences of digit 2 in numbers such as 2 and 12.
- When prefix 2 is chosen, the DP remains tight and explores only numbers from 20 to 25. This contributes one occurrence each from 20, 21, 23, 24, and 25, and two occurrences from 22.
- Whenever digit 2 is placed at a non-leading position, the count of all valid suffixes returned by the recursive call is added to the answer.
- Adding occurrences from all numbers in the range 1 to 25 gives a total of 9, which is returned as the answer.

C++`

```
#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1e9 + 7;

array<long long, 2> solve(int pos, int tight, int started, string &n, int d,
                          vector<vector<vector<array<long long, 2>>>> &dp)
{
    // End reached
    if (pos == n.size())
        return {1, 0};

    // Memoized state
    if (dp[pos][tight][started][0] != -1)
        return dp[pos][tight][started];

    long long ways = 0;
    long long occ = 0;

    // Max digit allowed
    int limit = tight ? n[pos] - '0' : 9;

    // Try all digits
    for (int digit = 0; digit <= limit; digit++)
    {

        // Update states
        int newTight = tight && (digit == limit);
        int newStarted = started || (digit != 0);

        // Solve remaining digits
        auto next = solve(pos + 1, newTight, newStarted, n, d, dp);

        // Add valid numbers
        ways = (ways + next[0]) % MOD;

        // Add suffix contribution
        occ = (occ + next[1]) % MOD;

        // Add current digit contribution
        if (digit == d)
        {

            // Skip leading zeros
            if (d == 0)
            {
                if (started)
                    occ = (occ + next[0]) % MOD;
            }
            else
            {
                if (newStarted)
                    occ = (occ + next[0]) % MOD;
            }
        }
    }

    return dp[pos][tight][started] = {ways, occ};
}

int getOccurrence(string &n, int d)
{

    int len = n.size();

    // dp[pos][tight][started]
    vector<vector<vector<array<long long, 2>>>> dp(
        len, vector<vector<array<long long, 2>>>(2, vector<array<long long, 2>>(2, {-1, -1})));

    // Start from first digit
    return solve(0, 1, 0, n, d, dp)[1];
}

int main()
{
    string n = "25";
    int d = 2;

    cout << getOccurrence(n, d) << endl;

    return 0;
}
```

`Java`

```
import java.util.Arrays;

public class GFG {

    static final int MOD = 1000000007;

    static long[] solve(int pos, int tight, int started,
                        String n, int d, long[][][][] dp)
    {
        // End reached
        if (pos == n.length())
            return new long[] { 1, 0 };

        // Memoized state
        if (dp[pos][tight][started][0] != -1)
            return dp[pos][tight][started];

        long ways = 0, occ = 0;

        // Max digit allowed
        int limit = tight == 1 ? n.charAt(pos) - '0' : 9;

        // Try all digits
        for (int digit = 0; digit <= limit; digit++) {

            // Update states
            int newTight
                = tight == 1 && digit == limit ? 1 : 0;
            int newStarted
                = started == 1 || digit != 0 ? 1 : 0;

            // Solve remaining digits
            long[] next = solve(pos + 1, newTight,
                                newStarted, n, d, dp);

            // Add valid numbers
            ways = (ways + next[0]) % MOD;

            // Add suffix contribution
            occ = (occ + next[1]) % MOD;

            // Add current digit contribution
            if (digit == d) {

                // Skip leading zeros
                if (d == 0) {
                    if (started == 1)
                        occ = (occ + next[0]) % MOD;
                }
                else {
                    if (newStarted == 1)
                        occ = (occ + next[0]) % MOD;
                }
            }
        }

        dp[pos][tight][started] = new long[] { ways, occ };
        return dp[pos][tight][started];
    }

    static int getOccurrence(String n, int d)
    {
        int len = n.length();

        // dp[pos][tight][started]
        long[][][][] dp = new long[len][2][2][2];
        for (long[][][] arr2D : dp)
            for (long[][] arr1D : arr2D)
                Arrays.fill(arr1D, new long[] { -1, -1 });

        // Start from first digit
        return (int)solve(0, 1, 0, n, d, dp)[1];
    }

    public static void main(String[] args)
    {
        String n = "25";
        int d = 2;

        System.out.println(getOccurrence(n, d));
    }
}
```

`Python`

```
def solve(pos, tight, started, n, d, dp, MOD):

    # End reached
    if pos == len(n):
        return (1, 0)

    # Memoized state
    if dp[pos][tight][started] != (-1, -1):
        return dp[pos][tight][started]

    ways = 0
    occ = 0

    # Max digit allowed
    limit = int(n[pos]) if tight else 9

    # Try all digits
    for digit in range(limit + 1):

        # Update states
        newTight = 1 if (tight and digit == limit) else 0
        newStarted = 1 if (started or digit != 0) else 0

        # Solve remaining digits
        nxtWays, nxtOcc = solve(
            pos + 1, newTight, newStarted, n, d, dp, MOD
        )

        # Add valid numbers
        ways = (ways + nxtWays) % MOD

        # Add suffix contribution
        occ = (occ + nxtOcc) % MOD

        # Add current digit contribution
        if digit == d:

            # Skip leading zeros
            if d == 0:
                if started:
                    occ = (occ + nxtWays) % MOD
            else:
                if newStarted:
                    occ = (occ + nxtWays) % MOD

    dp[pos][tight][started] = (ways, occ)
    return dp[pos][tight][started]

def getOccurrence(n, d):

    MOD = 1000000007
    lenN = len(n)

    # dp[pos][tight][started]
    dp = [[[(-1, -1) for _ in range(2)]
           for _ in range(2)]
          for _ in range(lenN)]

    # Start from first digit
    return solve(0, 1, 0, n, d, dp, MOD)[1]

if __name__ == "__main__":
    n = "25"
    d = 2

    print(getOccurrence(n, d))
```

`C#`

```
using System;

public class GFG {

    const int MOD = 1000000007;
    long[, , , ] dp;

    long[] Solve(int pos, int tight, int started, string n,
                 int d)
    {

        // End reached
        if (pos == n.Length)
            return new long[] { 1, 0 };

        // Memoized state
        if (dp[pos, tight, started, 0] != -1)
            return new long[] {
                dp[pos, tight, started, 0],
                dp[pos, tight, started, 1]
            };

        long ways = 0;
        long occ = 0;

        // Max digit allowed
        int limit = tight == 1 ? n[pos] - '0' : 9;

        // Try all digits
        for (int digit = 0; digit <= limit; digit++) {

            // Update states
            int newTight
                = (tight == 1 && digit == limit) ? 1 : 0;
            int newStarted
                = (started == 1 || digit != 0) ? 1 : 0;

            // Solve remaining digits
            long[] next = Solve(pos + 1, newTight,
                                newStarted, n, d);

            // Add valid numbers
            ways = (ways + next[0]) % MOD;

            // Add suffix contribution
            occ = (occ + next[1]) % MOD;

            // Add current digit contribution
            if (digit == d) {

                // Skip leading zeros
                if (d == 0) {
                    if (started == 1)
                        occ = (occ + next[0]) % MOD;
                }
                else {
                    if (newStarted == 1)
                        occ = (occ + next[0]) % MOD;
                }
            }
        }

        dp[pos, tight, started, 0] = ways;
        dp[pos, tight, started, 1] = occ;

        return new long[] { ways, occ };
    }

    public int getOccurrence(string n, int d)
    {

        int len = n.Length;

        // dp[pos][tight][started]
        dp = new long[len, 2, 2, 2];

        for (int i = 0; i < len; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    for (int l = 0; l < 2; l++)
                        dp[i, j, k, l] = -1;

        // Start from first digit
        return (int)Solve(0, 1, 0, n, d)[1];
    }

    // Driver Code
    public static int Main()
    {

        string n = "25";
        int d = 2;

        GFG obj = new GFG();

        Console.WriteLine(obj.getOccurrence(n, d));

        return 0;
    }
}
```

`JavaScript`

```
function getOccurrence(n, d)
{
    const MOD = 1000000007;
    let memo = new Map();

    function solve(pos, tight, started)
    {

        // End reached
        if (pos === n.length)
            return [ 1, 0 ];

        let key = `${pos},${tight},${started}`;

        // Memoized state
        if (memo.has(key))
            return memo.get(key);

        let ways = 0;
        let occ = 0;

        // Max digit allowed
        let limit = tight ? Number(n[pos]) : 9;

        // Try all digits
        for (let digit = 0; digit <= limit; digit++) {

            // Update states
            let newTight = tight && digit === limit;
            let newStarted = started || digit !== 0;

            // Solve remaining digits
            let [nextWays, nextOcc]
                = solve(pos + 1, newTight, newStarted);

            // Add valid numbers
            ways = (ways + nextWays) % MOD;

            // Add suffix contribution
            occ = (occ + nextOcc) % MOD;

            // Add current digit contribution
            if (digit === d) {

                // Skip leading zeros
                if (d === 0) {
                    if (started)
                        occ = (occ + nextWays) % MOD;
                }
                else {
                    if (newStarted)
                        occ = (occ + nextWays) % MOD;
                }
            }
        }

        memo.set(key, [ ways, occ ]);

        return [ ways, occ ];
    }

    // Start from first digit
    return solve(0, true, false)[1];
}

// Driver Code

let n = "25";
let d = 2;

console.log(getOccurrence(n, d));
```

`

**Output**

```
9
```

Comment

### Explore

DSA Fundamentals**

  - **[Logic Building Problems 2 min read][14]
  - **[Analysis of Algorithms 1 min read][15]

Data Structures**

  - **[Array 3 min read][16]
  - **[String 2 min read][17]
  - **[Hashing 2 min read][18]
  - **[Linked List 3 min read][19]
  - **[Stack 2 min read][20]
  - **[Queue 2 min read][21]
  - **[Tree 2 min read][22]
  - **[Graph 3 min read][23]

Algorithms**

  - **[Searching Algorithms 2 min read][24]
  - **[Sorting Algorithms 3 min read][25]
  - **[Introduction to Recursion 15 min read][26]
  - **[Greedy Algorithms 3 min read][27]
  - **[Graph Algorithms 3 min read][28]
  - **[Dynamic Programming 2 min read][29]
  - **[Bitwise Algorithms 4 min read][30]

Advanced**

  - **[Segment Tree 2 min read][31]
  - **[Binary Indexed Tree 12 min read][32]
  - **[Trie Data Structure 15+ min read][33]
  - **[Square Root (Sqrt) Decomposition Algorithm 15+ min read][34]

Interview Preparation**

  - **[Software Developer Interview Preparation 2 min read][35]
  - **[GFG 160 2 min read][36]
  - **[Coding Practice 1 min read][37]
  - **[POTD 2 min read][38]

Courses**

  - **[Placement 360 Course 2 min read][39]
  - **[DSA and System Design Course 2 min read][40]


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
[14]: https://www.geeksforgeeks.org/dsa/logic-building-problems/
[15]: https://www.geeksforgeeks.org/dsa/analysis-of-algorithms/
[16]: https://www.geeksforgeeks.org/dsa/array-data-structure-guide/
[17]: https://www.geeksforgeeks.org/dsa/string-data-structure/
[18]: https://www.geeksforgeeks.org/dsa/hashing-data-structure/
[19]: https://www.geeksforgeeks.org/dsa/linked-list-data-structure/
[20]: https://www.geeksforgeeks.org/dsa/stack-data-structure/
[21]: https://www.geeksforgeeks.org/dsa/queue-data-structure/
[22]: https://www.geeksforgeeks.org/dsa/tree-data-structure/
[23]: https://www.geeksforgeeks.org/dsa/graph-data-structure/
[24]: https://www.geeksforgeeks.org/dsa/searching-algorithms/
[25]: https://www.geeksforgeeks.org/dsa/sorting-algorithms/
[26]: https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/
[27]: https://www.geeksforgeeks.org/dsa/greedy-algorithms/
[28]: https://www.geeksforgeeks.org/dsa/graph-data-structure-and-algorithms/
[29]: https://www.geeksforgeeks.org/dsa/dynamic-programming/
[30]: https://www.geeksforgeeks.org/dsa/bitwise-algorithms/
[31]: https://www.geeksforgeeks.org/dsa/segment-tree-data-structure/
[32]: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-or-fenwick-tree-2/
[33]: https://www.geeksforgeeks.org/dsa/trie-insert-and-search/
[34]: https://www.geeksforgeeks.org/dsa/square-root-sqrt-decomposition-algorithm/
[35]: https://www.geeksforgeeks.org/interview-prep/interview-corner/
[36]: https://www.geeksforgeeks.org/courses/gfg-160-series
[37]: https://www.geeksforgeeks.org/dsa/geeksforgeeks-practice-best-online-coding-platform/
[38]: https://www.geeksforgeeks.org/problem-of-the-day
[39]: https://www.geeksforgeeks.org/courses/placement-360-cip-complete-tech-interview
[40]: https://www.geeksforgeeks.org/courses/interviewe-101-data-structures-algorithm-system-design
