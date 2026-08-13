# Eppstein, "Small Numerators" (part of "Algorithms for Egyptian Fractions", ics.uci.edu)

Source: https://www.ics.uci.edu/~eppstein/numth/egypt/smallnum.html (HTML; part of Eppstein's survey with Mathematica implementations, published as "Ten algorithms for Egyptian fractions", Mathematica in Education and Research 4(2):5–15, 1995).
Full text: `research/sources/eppstein-small-numerators.full.md`

## What it establishes

**Numerator 3.** `3/y` has a two-term expansion iff y has a factor ≡ 2 (mod 3). Proof given (credited to N. Nakayama via Klee–Wagon); e.g. `3/(3n+2) = 1/(n+1) + 1/((n+1)(3n+2))`, and conversely via gcd/valuation analysis. Implication: short representations are at least as hard as factoring.

**Numerator 4 (Erdős–Straus).** Cites Mordell (Diophantine Equations, [Mor69]) as the reference for the conjecture's statement and the 840-class analysis; lists the historical workers (Bernstein, Obláth, Rosati, Shapiro, Straus, Yamamoto, Franceschine; Schinzel, Sierpiński, Sedláček, Palamà, Stewart, Webb, Breusch, Graham, Vaughan for generalisations). A positive solution would give Egyptian-fraction representations with x^(log 3 / log 4) ≈ x^0.7925 terms for general x/y (conflict-resolution application).

**Modular conditions (the structural core of the open-class obstruction).**
- In any counterexample `4/y`, y must be ≡ 1 (mod 24), ≡ ±1 (mod 5), and one of three values (mod 7) — exactly `{1, 121, 169, 289, 361, 529} mod 840`, all squares of small numbers.
- If y is a minimal counterexample, y is prime: `y = ab ⇒ divide a representation of 4/a by b` (same reduction as f(nm) ≥ f(n)).
- `y ≡ 2 or 3 (mod 4)`: greedy gives 2 or 3 terms. `y ≡ 1 (mod 4)`: `4/y = 1/⌈y/4⌉ + 3/(y⌈y/4⌉)`, with the last term two-term expandable when y ≡ 2 (mod 3) or ≡ 5 (mod 8) — hence y = 24n+1 is necessary to fail.
- **The seven rule shapes that kill specific residues mod small primes:** `1/(6n+1) + 3/((24n+1)(6n+1))` and `1/((18n+1)(24n+1)) + 3/(18n+1)` work when one of 6n+1, 18n+1, 24n+1 has a prime divisor ≡ 5 (mod 6) — kills n ≡ 4, 3, 1 (mod 5); the `1/(6n+k) + (4k-1)/((6n+k)(24n+1))` shape with factor (4k-2) mod (4k-1) kills n ≡ 2, 3, 4, 6 (mod 7) for k=2; and the `a+b = 4k-1` split (k even) handles cases like n ≡ 7 (mod 13) with `4/(24n+1) = 1/(6n+10) + 26/((6n+10)(24n+1)) + 13/((6n+10)(24n+1))`.
- **Conclusion:** in any counterexample, y must be a quadratic residue mod 7, and all constraints jointly leave exactly the six square classes mod 840.

**Particular values.** Explicit representations for 25 primes in the six open classes up to 12500, e.g. `4/1801 = 1/451 + 1/295364 + 1/3249004`, `4/2521 = 1/636 + 1/69748 + 1/131876031`; most use rules mod 11, 13, 19, two use mod 29 (n=3361) and mod 17 (n=8089). Per Guy, N. Franceschine did similar calculations for y < 10^8.

## Implication for this run

- The **modular-conditions argument is the exact statement the run needs** for why the open classes are exactly the six squares: it is a *derived constraint*, not just a citation — the `1/(6n+k) + (4k-1)/(...)` family is precisely the "type I/type II" obstruction in its concrete form, and it kills every residue except the quadratic residues mod 7 among n ≡ 1 (mod 24) ∩ ±1 (mod 5).
- The **explicit values** (1801 … 12289) are a new independent witness set: 25 primes across all six open classes, each verifiable by `oracle.solves` — extending `code/out/witnesses.json` (which held two per class, mostly squares).
- The "a+b = 4k-1 with k even" shape and the mod-13, mod-29, mod-17 value rules show the **parametric families that *do* fire on open classes**: they are per-prime modular rules (n mod small prime), not single polynomial identities — consistent with Schinzel Theorem 1 forbidding polynomial identity families there.

```claim
id: eppstein-modular-conditions
statement: A counterexample y to ESC must be prime, ≡ 1 (mod 24), ≡ ±1 (mod 5), and a quadratic residue mod 7 — jointly exactly the six classes {1,121,169,289,361,529} mod 840; explicit rule shapes (1/(6n+k)+(4k-1)/((6n+k)(24n+1)) with k=2, factor conditions mod (4k-1); a+b=4k-1 splits) cover all other residues mod small primes.
hypotheses: y minimal counterexample (hence prime); rules stated for y = 24n+1.
holds-here: true — this is the structural statement the run's ansatz search must engage with; it says what identity shapes are already known to cover each non-square residue and why the squares are left.
status: sourced (Eppstein survey, citing Mordell and Guy); the 25 explicit representations are independently verifiable by the oracle; the reduction arguments (prime minimal counterexample, greedy shapes) are re-derived cheaply.
bearing: fixes the exact failure of type-I/II shapes on the six open classes; any new family must be a genuinely new shape (per Schinzel Theorem 1, not a single Z[x]-polynomial identity) — e.g. a per-prime modular rule family or a non-polynomial parametrisation.
anchor: research/sources/eppstein-small-numerators.full.md
```