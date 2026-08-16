<!-- source: https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md | converted from HTML -->

project-euler-solutions/solvers/719.md at master · cirosantilli/project-euler-solutions · GitHub

Skip to content

You signed in with another tab or window. [Reload][1] to refresh your session. You signed out in another tab or window. [Reload][1] to refresh your session. You switched accounts on another tab or window. [Reload][1] to refresh your session. Dismiss alert

{{ message }}

[cirosantilli][2] /**[project-euler-solutions][3]**Public

- [Notifications][4] You must be signed in to change notification settings
- [Fork 5][4]
-

[Star 10][4]

[3]

## Files Expand file tree

master

/

# 719.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History][5]

[5] History

51 lines (34 loc) · 2.12 KB

master

/

# 719.md

Copy path

Top

## File metadata and controls

-

Preview

-

Code

-

Blame

51 lines (34 loc) · 2.12 KB

[Raw][6]

Copy raw file

Download raw file

Outline

Edit and raw actions

# Project Euler 719 Solution - Number Splitting

[https://projecteuler.net/problem=719][7]:

- [719.py][8]

This solution computes **T(N)**, the sum of all *S-numbers*`n ≤ N`, where an **S-number**is a perfect square whose square root can be obtained by splitting the square’s decimal digits into **2 or more**parts and summing those parts.

## Key techniques

### 1) Search only perfect squares

If `n`is an S-number then `n = r²`for some integer `r`, so we only need to examine roots `r ≤ ⌊√N⌋`.

For `N = 10¹²`, this means checking `r ≤ 10⁶`.

### 2) Strong modular pruning (mod 9)

Splitting a decimal string into chunks and summing them preserves the value **mod 9**:

- each chunk’s numeric value is congruent to its digit sum (mod 9),
- so the sum of chunks is congruent to the whole number’s digit sum, hence to the number itself (mod 9).

Therefore, for any valid split of `r²`summing to `r`:

- `r ≡ r² (mod 9)`, which forces `r mod 9 ∈ {0, 1}`.

This cuts the search by ~4.5× immediately.

The same invariant is also used *inside*the recursion as a fast reject test for partial prefixes.

### 3) Right-to-left recursive splitting with bounds

To test whether `r²`is an S-number, we split from the **rightmost digits**:

`num = prefix * 10ᵏ + suffix`

If `suffix ≤ remaining_target`, we recurse on `(prefix, remaining_target - suffix)`.

Pruning rules:

- if `remaining_target < 0`⇒ impossible,
- if `remaining_target > num`⇒ impossible (the maximum sum occurs with no further splits),
- if `(num - remaining_target) % 9 != 0`⇒ impossible,
- when `remaining_target`is small, use a digit-sum lower bound:

  - minimal achievable sum is splitting into single digits ⇒ `digit_sum(num) ≤ remaining_target`.

### 4) Memoization per square

Within a single square check, different split paths can lead to the same `(prefix, remaining_target)`state. A small dictionary memo avoids re-solving identical subproblems.

## Files

- `main.py`– implementation + asserts for the examples and the provided `T(10⁴)`value.
- Run:

  - `python3 main.py`(prints `T(10¹²)`)
  - `python3 main.py <N>`(prints `T(N)`)

You can’t perform that action at this time.


## Links

[1]: 
[2]: /cirosantilli
[3]: /cirosantilli/project-euler-solutions
[4]: /login?return_to=%2Fcirosantilli%2Fproject-euler-solutions
[5]: /cirosantilli/project-euler-solutions/commits/master/solvers/719.md
[6]: https://github.com/cirosantilli/project-euler-solutions/raw/refs/heads/master/solvers/719.md
[7]: https://projecteuler.net/problem=719
[8]: /cirosantilli/project-euler-solutions/blob/master/solvers/719.py
