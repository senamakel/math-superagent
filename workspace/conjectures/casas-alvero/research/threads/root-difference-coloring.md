# Thread: root-difference-coloring first step

```thread
question: Does the root-difference identity H_i(f)(x) = e_{n-i}(x-beta_1,...,x-beta_n)
      and the resultant form R_i = prod_beta H_i(f)(beta) hold exactly, and where
      does the collapse argument break in characteristic p?
status: open
rests-on: root-difference-coloring (adopted approach), hasse-vs-ordinary (dead),
      polstra-convex-hull, ghosh-complete-intersection
next: EXECUTE code/rootdiff/verify_rootdiff_identity.py (directive 7, no rewrite) with
      a tool_builder/coder executor and capture to code/out/rootdiff_identity.captured.txt —
      the capture does not exist yet and is the gate on everything else. Report the
      verdict on identities (A) H_i(f)(x)=e_{n-i}(x-beta_*) and (B) R_i=prod_beta H_i(f)(beta)
      over QQ (n=4,5,6) and F_p (n=p+1, p=2,3,5) against the script docstring's failure
      criterion verbatim; then run the char-p break test and name the step that breaks.
```

## Findings (on paper)

1. **The identity holds, and is a tautology.** H_i(f) = [t^i] f(x+t) = e_{n-i}(x-beta_*)
   because the coefficient of t^i in prod_j((x-beta_j)+t) is the elementary
   symmetric polynomial (its definition). R_i = prod_beta H_i(f)(beta) with
   c_n = 1 is the resultant-norm identity for monic f. Char-free. See
   research/notes/root-difference-identity-verified.md.

2. **Char-p break located, precisely.** For the witness x^{p+1}-x^p over F_p:
   H_1 = x^p, H_i = 0 for 2 <= i <= p-1 (Lucas), H_p = x-1. Consistent 2-root
   coloring (0 witnesses i<p, 1 witnesses i=p) survives. The break is the
   collapse step: per-color vacuity (H_i = 0 removes constraints) plus no
   F_p analogue of the Polstra/Gauss-Lucas convex-hull propagation.

3. **Correction:** the approach file's "degenerate for i >= p" is the ordinary
   derivative story; for Hasse derivatives of the witness it is {2,...,p-1}.

## Remaining gap

The collapse step itself — "the e_{n-i} = 0 colorings force all n roots to
coincide in char 0" — is the conjecture to establish for small n (5, 6) before
any claim to n = 20. Not yet attacked.
