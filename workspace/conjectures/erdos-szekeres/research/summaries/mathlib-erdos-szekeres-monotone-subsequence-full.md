<!-- source: https://leanprover-community.github.io/mathlib_docs/wiedijk_100_theorems/ascending_descending_sequences.html | converted from HTML -->

mathlib-archive / wiedijk_100_theorems.ascending_descending_sequences - mathlib3 docs

# Erdős–Szekeres theorem #

THIS FILE IS SYNCHRONIZED WITH MATHLIB4. Any changes to this file require a corresponding PR to mathlib4.

This file proves Theorem 73 from the [100 Theorems List][1], also known as the Erdős–Szekeres theorem: given a sequence of more than `r * s`distinct values, there is an increasing sequence of length longer than `r`or a decreasing sequence of length longer than `s`.

We use the proof outlined at [https://en.wikipedia.org/wiki/Erdos-Szekeres_theorem#Pigeonhole_principle.][2]

## Tags #

sequences, increasing, decreasing, Ramsey, Erdos-Szekeres, Erdős–Szekeres, Erdős-Szekeres

[source][3]

theorem [theorems_100. erdos_szekeres][4] {α : [Type][5] u_1} [[linear_order][6] α] {r s n : [ℕ][7] } {f : [fin][8] n [→][9] α} (hn : r [*][10] s [function.injective][11] f):

( [∃][12] (t : [finset][13] ( [fin][8] n)) [,][12] r [card][14] [∧][15] [strict_mono_on][16] f [↑][17] t) [∨][18] [∃][12] (t : [finset][13] ( [fin][8] n)) [,][12] s [card][14] [∧][15] [strict_anti_on][19] f [↑][17] t

**Erdős–Szekeres Theorem**: Given a sequence of more than `r * s`distinct values, there is an increasing sequence of length longer than `r`or a decreasing sequence of length longer than `s`.

Proof idea: We label each value in the sequence with two numbers specifying the longest increasing subsequence ending there, and the longest decreasing subsequence ending there. We then show the pair of labels must be unique. Now if there is no increasing sequence longer than `r`and no decreasing sequence longer than `s`, then there are at most `r * s`possible labels, which is a contradiction if there are more than `r * s`elements.


## Links

[1]: https://www.cs.ru.nl/~freek/100/
[2]: https://en.wikipedia.org/wiki/Erdos-Szekeres_theorem#Pigeonhole_principle.
[3]: https://github.com/leanprover-community/mathlib/blob/master/archive/wiedijk_100_theorems/ascending_descending_sequences.lean#L44
[4]: https://leanprover-community.github.io/mathlib_docs/wiedijk_100_theorems/ascending_descending_sequences.html#theorems_100.erdos_szekeres
[5]: https://leanprover-community.github.io/mathlib_docs/foundational_types.html#codetype-ucode
[6]: https://leanprover-community.github.io/mathlib_docs/init/algebra/order.html#linear_order
[7]: https://leanprover-community.github.io/mathlib_docs/init/core.html#nat
[8]: https://leanprover-community.github.io/mathlib_docs/init/data/fin/basic.html#fin
[9]: https://leanprover-community.github.io/mathlib_docs/foundational_types.html#pi-types-codeπ-a--α-β-acode
[10]: https://leanprover-community.github.io/mathlib_docs/init/core.html#has_mul.mul
[11]: https://leanprover-community.github.io/mathlib_docs/init/function.html#function.injective
[12]: https://leanprover-community.github.io/mathlib_docs/init/logic.html#Exists
[13]: https://leanprover-community.github.io/mathlib_docs/data/finset/basic.html#finset
[14]: https://leanprover-community.github.io/mathlib_docs/data/finset/card.html#finset.card
[15]: https://leanprover-community.github.io/mathlib_docs/init/core.html#and
[16]: https://leanprover-community.github.io/mathlib_docs/order/monotone/basic.html#strict_mono_on
[17]: https://leanprover-community.github.io/mathlib_docs/init/coe.html#coe
[18]: https://leanprover-community.github.io/mathlib_docs/init/core.html#or
[19]: https://leanprover-community.github.io/mathlib_docs/order/monotone/basic.html#strict_anti_on
