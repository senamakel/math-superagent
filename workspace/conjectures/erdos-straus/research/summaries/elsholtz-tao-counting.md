# Elsholtz & Tao, *Counting the number of solutions to the Erdős–Straus equation on unit fractions*

Source: arXiv:1107.1010 (J. Aust. Math. Soc. 94 (2013) 50–105).
Full text: `research/sources/elsholtz-tao-counting.full.md` (also complete text
stored under `research/sources/pomerance-erdos-straus.full.md`, a misnamed copy
of the ar5iv HTML of this same paper).

## What it establishes (sourced)

- **Prime reduction** (intro): since `f(nm) >= f(n)`, it suffices to solve the
  conjecture for `n` prime. `f(n)` counts `(x,y,z) in N^3` with
  `4/n=1/x+1/y+1/z`. Example values: f(1)=0, f(2)=3, f(3)=12, f(4)=10, f(5)=12.
- **Type I / Type II** (Sec 1): Type I = `n` divides exactly one of `x,y,z`
  (the one divisible denominator); Type II = `n` divides exactly two. For odd
  prime `p`, at least one denominator is divisible by `p`, not all three, so
  `f(p) = 3 f_I(p) + 3 f_II(p)`.
- **Proposition 1.6 (Vanishing)**: for any odd perfect square `n`,
  `f_I(n) = f_II(n) = 0`. No Type-I and no Type-II solution exists at an odd
  square. Proof uses quadratic reciprocity; goes back to Schinzel (1967 refs)
  and Yamamoto (1965). This is the structural fact behind why the six open
  classes (all squares mod 840) resist Type-I/II polynomial identities. Does
  NOT show `f(n)=0` — a solution may be of neither type at a square.
- **Proposition 1.9 (Solvable congruences)**: a complete classification of
  primitive residue classes solvable by polynomials, Type I (4 families) and
  Type II (3 families). Type I families all put `n` in classes of the form
  `n ≡ −f mod 4ad` (with `f | 4a²d+1`), `n ≡ −f mod 4ac & n ≡ −c/a mod f`,
  `n ≡ −f mod 4cd & n² ≡ −4c²d mod f`, `n ≡ −1/e mod 4ab`.
- **Textbook result on `n mod 840`**: any primitive residue class `n ≡ r mod
  840` is solvable by polynomials unless `r` is a perfect square. Perfect
  square primitive classes cannot be solved by polynomials.
- Counting results (used for context, not for construction): average value of
  `f`, `f_I`, `f_II`; `f(p) = O(log^3 p log log p)` for density-1 primes;
  `f(p) ≪ p^{3/5+o(1)}`; lower bounds `f(p) >= (log p)^{0.549}` for density-1
  primes.
- Verification history (Table 1): Straus ≤5000 (1950), ..., Swett 10^14
  (1999), 2×10^14 (2012), Salez 10^17 (2014).

```claim
id: prime-reduction
statement: It suffices to prove the Erdős–Straus conjecture for prime n: f(nm) >= f(n), so a composite counterexample would have a smaller prime-factor counterexample.
hypotheses: none (this is why n prime is the only open case).
holds-here: true.
status: sourced (Elsholtz–Tao intro; Wikipedia; erdosproblems 242).
bearing: all identity work may be restricted to primes n ≡ 1 (mod 840).
anchor: research/sources/elsholtz-tao-counting.full.md
```

```claim
id: type-definition
statement: For odd prime p, every solution to 4/p=1/x+1/y+1/z is Type I (p divides exactly one of x,y,z) or Type II (p divides exactly two), and f(p)=3 f_I(p)+3 f_II(p).
hypotheses: p odd prime.
holds-here: true.
status: sourced (Elsholtz–Tao Sec 1).
bearing: defines the two standard shapes that all known families use.
anchor: research/sources/elsholtz-tao-counting.full.md
```

```claim
id: vanishing-type12-odd-squares
answers: exact-statement-from-b7df
statement: For any odd perfect square n, f_I(n)=f_II(n)=0: there is no Type-I and no Type-II solution to 4/n=1/x+1/y+1/z.
hypotheses: n an odd perfect square.
holds-here: true — the six open residue classes mod 840 (1,121,169,289,361,529) are all squares.
status: sourced (Elsholtz–Tao Prop 1.6; proof in paper via quadratic reciprocity; goes back to Schinzel and Yamamoto).
bearing: THE obstruction. Any identity covering n ≡ 1 (mod 840) cannot be type I or II, else an odd square in the class would have a type-I/II solution. Does not force f(n)=0 at a square (a neither-type solution may exist).
anchor: research/sources/elsholtz-tao-counting.full.md
```

```claim
id: solvable-840-classes
statement: Every primitive residue class n ≡ r mod 840 is solvable by polynomials unless r is a perfect square; perfect-square primitive classes cannot be solved by polynomials.
hypotheses: primitive residue class, type-I/II polynomial solvability.
holds-here: true — the six residuals are the primitive squares mod 840.
status: sourced (Elsholtz–Tao intro; Mordell 1969; Schinzel 2000).
bearing: a new family must not reduce to type-I/II polynomial shape.
anchor: research/sources/elsholtz-tao-counting.full.md
```

## Implication for this run

The six open classes `n ≡ 1,121,169,289,361,529 (mod 840)` are exactly the
primitive classes mod 840 that are perfect squares, hence **cannot** be solved
by Type-I/II polynomial identities. Any new family must therefore be of a
genuinely new type (not one of the 7 constant-coefficient modular equations of
Salez) or a non-polynomial / rational-parametric construction whose positivity
holds on the class. The vanishing fact (Prop 1.6) is the precise obstruction a
new ansatz must dodge: the construction must fail *necessarily* at odd squares,
so a cover that would also cover a square is self-defeating only because a
square *could* still have a neither-type solution.
