<!-- source: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/242.lean | converted from HTML -->

formal-conjectures/FormalConjectures/ErdosProblems/242.lean at main · google-deepmind/formal-conjectures · GitHub

Skip to content

You signed in with another tab or window. [Reload][1] to refresh your session. You signed out in another tab or window. [Reload][1] to refresh your session. You switched accounts on another tab or window. [Reload][1] to refresh your session. Dismiss alert

{{ message }}

### Uh oh!

There was an error while loading. [Please reload this page][1].

[google-deepmind][2] /**[formal-conjectures][3]**Public

- [Notifications][4] You must be signed in to change notification settings
- [Fork 409][4]
-

[Star 1.2k][4]

[3]

## Files Expand file tree

main

/

# 242.lean

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History][5]

[5] History

54 lines (43 loc) · 1.68 KB

main

/

# 242.lean

Copy path

Top

## File metadata and controls

-

Code

-

Blame

54 lines (43 loc) · 1.68 KB

[Raw][6]

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

/-

Copyright 2025 The Formal Conjectures Authors.

Licensed under the Apache License, Version 2.0 (the "License");

you may not use this file except in compliance with the License.

You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software

distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and

limitations under the License.

-/

import FormalConjecturesUtil

/-!

# Erdős Problem 242

*References:*

- [erdosproblems.com/242](https://www.erdosproblems.com/242)

- [Si56] Sierpiński, W., Sur les décompositions de nombres rationnels en fractions primaires.

Mathesis (1956), 16--32.

-/

open scoped Topology

namespace Erdos242

/--

For every $n>2$ there exist distinct integers $1 ≤ x < y < z$

such that $\frac 4 n = \frac 1 x + \frac 1 y + \frac 1 z$.

-/

@[category research open, AMS 11]

theorem erdos_242 (n : ℕ) (hn : 2 < n) :

∃ x y z : ℕ, 1 ≤ x ∧ x < y ∧ y < z ∧

(4 / n : ℚ) = 1 / x + 1 / y + 1 / z := by

sorry

/--

Schinzel conjectured (see [Si56]) the generalisation that, for any fixed $a$, if $n$ is sufficiently

large in terms of $a$ then there exist distinct integers $1\leq x < y < z$ such that

$\frac{a}{n} = \frac{1}{x}+\frac{1}{y}+\frac{1}{z}.$

-/

@[category research open, AMS 11]

theorem erdos_242.variants.schinzel_generalization

(a : ℕ) (ha : 0 < a) :

∀ᶠ (n : ℕ) in Filter.atTop, ∃ x y z : ℕ, 1 ≤ x ∧ x < y ∧ y < z ∧

(a / n : ℚ) = 1 / x + 1 / y + 1 / z := by

sorry

end Erdos242

You can’t perform that action at this time.


## Links

[1]: 
[2]: /google-deepmind
[3]: /google-deepmind/formal-conjectures
[4]: /login?return_to=%2Fgoogle-deepmind%2Fformal-conjectures
[5]: /google-deepmind/formal-conjectures/commits/main/FormalConjectures/ErdosProblems/242.lean
[6]: https://github.com/google-deepmind/formal-conjectures/raw/refs/heads/main/FormalConjectures/ErdosProblems/242.lean
