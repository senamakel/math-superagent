# Integrality of the genus closed form is proved, not sampled

`code/out/verify_genus_formula.captured.txt` reports

```
formula integral over m=2..29, n=m+1..59: True
```

That is a sample of 1,000-odd pairs. Integrality is not a sampling question —
it is a four-case parity argument, and it is short enough that the workspace
should hold the proof rather than a table.

## The statement

The closed form in use is

```
g(m,n) = ( (m-1)n - (m-2) - gcd(n,m) ) / 2
```

which is the same expression as the symmetric form recorded in
`code/out/genus_symmetric_form.md`, since
`(m-1)n - (m-2) = mn - n - m + 2 = (m-1)(n-1) + 1`:

```
g(m,n) = ( (m-1)(n-1) + 1 - gcd(m,n) ) / 2.
```

Write `N(m,n) := (m-1)(n-1) + 1 - gcd(m,n)`. The claim is that `N(m,n)` is
**even for all integers `m, n ≥ 1`**, so `g` is always an integer.

## Proof

Work mod 2 and split on the parities of `m` and `n`. There are four cases and
each is one line.

1. **`m` even, `n` even.** `(m-1)(n-1)` is odd·odd = odd, so `(m-1)(n-1)+1` is
   even. And `2 | m`, `2 | n`, so `gcd(m,n)` is even. even − even = **even**.
2. **`m` even, `n` odd.** `(m-1)(n-1)` is odd·even = even, so `(m-1)(n-1)+1` is
   odd. And `gcd(m,n) | n` with `n` odd, so `gcd(m,n)` is odd.
   odd − odd = **even**.
3. **`m` odd, `n` even.** Symmetric to case 2: `gcd(m,n) | m` with `m` odd, so
   the gcd is odd, and `(m-1)(n-1)+1` is odd. **even**.
4. **`m` odd, `n` odd.** `(m-1)(n-1)` is even·even = even, so `(m-1)(n-1)+1` is
   odd. And `gcd(m,n) | m` with `m` odd, so the gcd is odd.
   odd − odd = **even**. ∎

The parity of `gcd(m,n)` is doing the work, and it is pinned in every case: the
gcd is even exactly when both arguments are even, which is exactly the case
where `(m-1)(n-1)+1` is also even.

Note what the proof does **not** use: nothing about binomial coefficients, the
curve `C(x,m) = C(y,n)`, or Riemann–Hurwitz. It is a statement about the
arithmetic expression alone, so it is independent of whether the closed form
correctly computes the genus.

## Verified far past the sampled range

`code/out/genus_integrality_proved.captured.txt`:

- the two forms agree identically over `1 ≤ m, n ≤ 399` — 0 disagreements;
- each of the four parity classes searched exhaustively to 600 — 0 odd values
  of `N` in any class;
- **1,121,253 pairs** with `2 ≤ m < n < 1500`, all integral, no exception;
- the ten predictions for uncomputed terms in
  `verify_genus_formula.captured.txt` (`g(2,13)=6`, `g(3,25)=24`, `g(4,25)=36`,
  `g(5,25)=46`, `g(6,19)=45`, `g(7,16)=45`, `g(8,17)=56`, `g(9,18)=64`,
  `g(10,20)=81`, `g(11,13)=60`) are all reproduced by the symmetric form.

**That last check is internal consistency, not confirmation.** The two
expressions are algebraically equal, so agreeing is guaranteed and proves
nothing about the genus. Confirming a predicted genus needs a CAS that
computes the curve; the host has neither sympy nor Singular, so it was not
attempted here and must not be reported as though it were.

## Effective and uniform

Per the standing requirement on this problem, both attributes stated for this
result: the integrality lemma is **effective** (it is a proof, with no
ineffective input and no unspecified constant) and **uniform in `m` and `n`**
(it holds for all pairs simultaneously, not one pair at a time). It inherits
nothing from Faltings or Siegel.

That is exactly what makes it small. It is a lemma about the closed form, not
about Singmaster's conjecture, and it does not bound anything.

```claim
id: genus-closed-form-integrality
statement: For all integers m, n >= 1 the quantity
  N(m,n) = (m-1)(n-1) + 1 - gcd(m,n) is even, equivalently
  (m-1)n - (m-2) - gcd(n,m) is even, so the genus closed form
  g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2 is always an integer. Proof by the
  four parity cases: gcd(m,n) is even exactly when both m and n are even,
  which is exactly the case where (m-1)(n-1)+1 is even; in the other three
  cases both terms are odd. No property of binomial coefficients or of the
  curve C(x,m) = C(y,n) is used.
hypotheses: none. The statement is about the arithmetic expression alone and
  is independent of whether the closed form correctly computes the genus of
  the curve
holds-here: yes, proved outright by exhaustive case analysis on parities, then
  verified in code/out/genus_integrality_proved.captured.txt over 1,121,253
  pairs with 2 <= m < n < 1500 with zero exceptions, each parity class searched
  separately to 600, and the two algebraic forms confirmed identical over
  1 <= m,n <= 399
status: proved
bearing: replaces the sampled assertion "formula integral over m=2..29,
  n=m+1..59" in verify_genus_formula.captured.txt with a proof, removing one
  gap between the closed form and a derivation. It is effective and uniform in
  m and n, inheriting nothing from Faltings or Siegel, and it bounds nothing -
  it is a lemma about the expression, not about Singmaster's conjecture. The
  remaining and much larger gap is unchanged: no derivation here reproduces the
  closed form itself, which still needs Riemann-Hurwitz with the ramification
  computed
anchor: code/out/genus_integrality_proved.captured.txt;
  code/out/verify_genus_formula.captured.txt;
  code/out/genus_symmetric_form.md
source: operator-computation
```
