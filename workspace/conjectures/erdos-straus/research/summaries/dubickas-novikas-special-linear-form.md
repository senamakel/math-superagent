# Dubickas & Novikas, "On integers expressible by some special linear form"

Source: Acta Math. Univ. Comenianae 81:2 (2012) 203–209; obtained via Vilnius
University e-publications repository, https://epublications.vu.lt/object/elaba:2089125/2089125.pdf
Full text: `research/sources/dubickas-novikas-special-linear-form.full.md`

## What it establishes (sourced, primary)

**Definition.** E(4) = { n ∈ Z⁺ : n = 4M − d, where (a b) | M and d | (a+b)
for some positive integers a, b }.

**Main results.**
1. **E(4) contains no perfect squares.**
2. **Exactly three exceptional integers** are not in E(4) among all positive
   integers up to 2·10⁹: **288, 336, 4545**. (Computational; "verifier que
   E(4) contient tous les autres entiers jusqu'à 2·10⁹".)
3. **Conjecture**: there are no other exceptions. **The conjecture implies
   the Erdős–Straus conjecture.**
4. Extensions: the same form `tM − d` for t ≥ 3; E(5) relates to
   Sierpiński's conjecture (5/n), E(t) to Schinzel's generalisation.

## Relation to the rest of the library

- OEIS **A287116** (filed in library) carries exactly this: "Nonsquare
  integers that cannot be represented in the form 4M−d ... If there are no
  more terms, the Erdős-Straus conjecture would follow"; terms 288, 336,
  4545; no other terms below 2·10⁹ (Max Alekseyev, 2017).
- The linear form `4M − d` with (ab)|M and d | (a+b) is the Type-I-friendly
  parametrisation: with x = ab, y = 4M − d = n... (the same arithmetic
  family that appears in Mordell's identity and in the Bloom–Elsholtz
  Theorem 1 proof as `4abcd = a + b + cp`).

## Consequence for this run

The E(4) reformulation gives a **second, independent statement of what a
covering would look like**: ESC would follow if every nonsquare n were of the
form 4M − d (with the divisibility conditions). Since the six open classes
contain infinitely many odd squares (Elsholtz–Tao Prop 1.6: squares have no
Type-I/II solutions), and E(4) contains no squares, the obstruction is
exactly that the open classes' *square members* are beyond every E(4) shape.
The verified bound "no exceptions below 2·10⁹" is a computational anchor
below which no exceptional n exists at all (this is a different, stronger
statement than the ESC verification bound 10^18, because it says *every*
n < 2·10⁹, square or not, is in E(4) — except 288, 336, 4545).

```claim
id: dubickas-novikas-e4-no-squares
statement: E(4) = {4M−d : (ab)|M, d|(a+b)} contains no perfect squares.
hypotheses: none.
holds-here: true — squares in the six open classes (e.g. 841=29² in class 1) are therefore unreachable by the E(4) shape, consistent with Prop 1.6 (no Type-I/II at odd squares).
status: sourced (Dubickas–Novikas 2012; in full text).
bearing: any 4M−d-style family cannot be complete on the open classes because those classes contain infinitely many squares.
anchor: research/sources/dubickas-novikas-special-linear-form.full.md
```

```claim
id: dubickas-novikas-exceptions-2e9
statement: The only positive integers not in E(4) below 2·10⁹ are 288, 336, 4545; conjecturally no other exceptions exist, and that conjecture implies the Erdős–Straus conjecture.
hypotheses: none (computational verification up to 2·10⁹).
holds-here: true — the E(4)-exceptions verif. bound (2·10⁹) is a distinct anchor from the ESC bound (10^18); records exactly which n are beyond the linear-form parametrisation below 2·10⁹.
status: sourced (Dubickas–Novikas 2012, main result + conjecture; OEIS A287116 confirms, no more terms ferrari 2·10⁹).
bearing: the run's witness set should include 288, 336, 4545 as the only E(4)-exceptional small integers, so a claimed "E(4)-type family covering everything" is testable.
anchor: research/sources/dubickas-novikas-special-linear-form.full.md
```