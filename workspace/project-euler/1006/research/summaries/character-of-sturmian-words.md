# Cassaigne–Fici–Sciortino–Zamboni, "Cyclic complexity of words" — governing identification

<!-- source: https://hal.science/hal-01829144v1/document | JCTA 145 (2017) -->

Research note introducing *cyclic complexity* c_x(n) = number of conjugacy classes of
length-n factors of an infinite word x. The relevant content is the recalled characterizations
of Sturmian words.

## What it establishes (relevant to PE1006)
- **Proposition 6**: a word x is Sturmian iff it has exactly n+1 distinct factors of length n
  for every n>=0. (The classical Morse–Hedlund characterization, used here as the definition.)
- The **Fibonacci word** F = 0100101001001... is the fixed point of the substitution
  0->01, 1->0, and is the canonical example of a Sturmian word.
- **Proposition 7**: two Sturmian words have the same set of factors iff they have the same
  slope — so the length-k factor set depends **only on the slope**, not on the intercept or
  on which finite S_n one truncates at.

## What it implies for this problem
This is the **governing identification**: the problem's S_n -> limit = infinite Fibonacci
word, a Sturmian word of slope 1/φ², hence exactly k+1 distinct length-k factors — the
problem's FACT. Prop 7 (factors depend only on slope) licenses treating the set of "Fibonacci
subwords" (finite S_n factors) as *equal* to the Sturmian factor set of slope 1/φ², which
resolves the `unbounded-n` difficulty: it does not matter which finite S_n one uses, the
length-k factor set is the same once it has stabilized (and why it stabilizes at all).

`holds-here: yes` for both Props 6 and 7 (F is Sturmian of fixed irrational slope).

## Full text
[[character-of-sturmian-words.full]]
