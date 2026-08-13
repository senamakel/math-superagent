# Elementary reductions — verified exactly, not merely asserted

Computed by the operator (not this run's agents) with `fractions.Fraction`
exact rational arithmetic — no floating point, no sympy (unavailable in this
sandbox). Program: `code/out/verify_elementary_reductions.py`. Captured
output: `code/out/verify_elementary_reductions.captured.txt`.

Two things were checked. One is fine. One flags a bug already recorded in
`research/approaches/oracle-findings.md`: the n≡3(mod4) identity as it is
commonly stated (and as it appeared in this babysitter's own task brief) —
`x=n, y=(n+1)/2, z=n(n+1)/2` — does **not** solve 4/n. It solves 3/n. Checked
for k=0..49 (n=3,7,...,199): every one leaves a residual of exactly `1/n`.

The identity that does work is the one `oracle-findings.md` already recorded:
`n=4k+3, x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1)`. Verified `4/n - 1/x - 1/y - 1/z
== 0` exactly, and x,y,z positive integers, for k=0..4999 (n up to 19999).

```claim
id: n-even-trivial
statement: For every even n=2m (m>=1), 4/n = 1/m + 1/(2m) + 1/(2m) exactly, with m, 2m positive integers.
hypotheses: n even, n=2m, m>=1
holds-here: yes
status: checked
bearing: reduces the conjecture to odd n; combined with prime-reduction, to odd prime n.
anchor: code/out/verify_elementary_reductions.py:check_even, code/out/verify_elementary_reductions.captured.txt
source: operator-computation
```

```claim
id: naive-3mod4-identity-is-wrong
statement: The identity x=n, y=(n+1)/2, z=n(n+1)/2 for n=4k+3 does NOT solve 4/n=1/x+1/y+1/z; it solves 3/n=1/x+1/y+1/z (residual 4/n - 1/x-1/y-1/z = 1/n exactly, nonzero, for every k checked).
hypotheses: n=4k+3, k>=0
holds-here: yes (i.e. the claim that it is wrong holds)
status: checked
bearing: this identity must not be cited as covering n≡3(mod4); any downstream note or claim asserting it does is itself unverified and should be corrected or retracted.
anchor: code/out/verify_elementary_reductions.py:check_naive_3mod4, code/out/verify_elementary_reductions.captured.txt
source: operator-computation
```

```claim
id: n-3mod4-covering-corrected
statement: For every n=4k+3 (k>=0), setting x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1) gives x,y,z positive integers with 4/n = 1/x + 1/y + 1/z exactly.
hypotheses: n=4k+3, k>=0
holds-here: yes
status: checked
bearing: covers the n ≡ 3 (mod 4) residue class unconditionally; combined with n-even-trivial and prime-reduction, narrows the open cases to odd primes p not ≡ 3 (mod 4) — consistent with the six open mod-840 classes all being ≡ 1 (mod 4) squares.
anchor: code/out/verify_elementary_reductions.py:check_corrected_3mod4, code/out/verify_elementary_reductions.captured.txt
source: operator-computation
```
