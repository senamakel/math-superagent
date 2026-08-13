# Elementary reductions — get the reduction chain off "asserted"

The operator's directive: the elementary reductions were still `asserted`, one
was wrong, and the run must check them in code before spending budget on new
identity search for the six square classes mod 840. `n-even-trivial` and the
corrected `n≡3 (mod 4)` identity are now checked
(`code/out/verify_elementary_reductions.py`). `prime-reduction` is the next one
to check.

```thread
question: Is the chain "any counterexample ⇒ some odd prime p ≡ 1 (mod 24)"
verified here by computation, with every ingredient `checked` rather than
`sourced`?
status: open
rests-on: n-even-trivial, n-3mod4-covering-corrected,
  naive-3mod4-identity-is-wrong, prime-reduction, reduction-mod24
blocked-by: prime-reduction not yet run through code
next: write a program proving the scaling lift `4/n = 1/x+1/y+1/z ⇒
  4/(nm) = 1/(mx)+1/(my)+1/(mz)` in exact arithmetic, capture it, and flip
  `prime-reduction` to checked; then flip `reduction-mod24` once the mod-3 and
  mod-8 identities are also checked.
```
