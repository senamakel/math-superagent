# Char-p break of the Ghosh proof — computational verification

`verify_break.py` verifies, computationally and exactly, the claim of
`research/threads/ghosh-char0-step.md`: the Ghosh proof of Casas-Alvero
(arXiv:2501.09272) has a named char-0-only step — the divisibility
`f(n,n,n) = -n` needed by Eq (4.18) of the proof — and it dies exactly when
the characteristic divides the induction step.

The program faithfully implements the source's own objects
(`research/sources/ghosh2025_proof_html.full.md` §2), via
`code/lib/ghosh2025.py`:

- **HD^i_n(x_n)** — the multivariate Hasse–Schmidt derivation (eq 2.1) of  `x_1…x_n`, computed from the definition; verified to equal the elementary
  symmetric polynomial `e_{n-i}`.
- **Φ^#_{d,j}** — the algebra automorphism (eq 2.2):
  `x_l → x_l − x_j (l ≠ j)`, `x_j → −x_j`, `Φ^#_{d,d+1} = id`, applied by
  simultaneous substitution (algebra-map semantics), and verified to be an
  automorphism (linearity, multiplicativity, involution, identity case).
- **F(i,j,n) = Φ^#_{n,j}(HD^{i-1}_n x_n)** — since `HD^{i-1}_n x_n = e_{n-i+1}`
  is multilinear and Φ is affine, F is linear in `x_n`:
  `F = x_n·f(i,j,n) + g(i,j,n)`.

Checks (all exact, sympy over QQ and GF(p), no floating point):

1. **The divisibility**: `f(n,j,n) = 1` for `j ≠ n` and `f(n,j,n) = −n` for
   `j = n`, for all `n = 2..10`, `j = 1..n+1`, over QQ and GF(p),
   `p ∈ {2,3,5,7}`. Independently re-derived via `Poly.coeff_monomial`.
2. **The char-0 unit / char-p death**: over QQ, `f(n,n,n) = −n ≠ 0`; over
   GF(p) with `p | n`, `−n ≡ 0` — the unit Eq (4.18) needs has vanished.
   Concrete images: `Φ^#_{n,n}(e_1) = (x_1+…+x_{n−1}) − n·x_n` and
   `Φ^#_{n,j}(e_1) = e_1 − (n+1)·x_j` for `j ≠ n`.
3. **The witnesses**: `f = x^{p+1} − x^p` over GF(p) is reported by the
   canonical oracle (`lib.casas_alvero.is_counterexample`) as satisfying the
   hypothesis and not being a pure power, for `p = 2,3,5,7` (the same list
   holds with `is_ca_hasse`, the univariate Hasse-derivative hypothesis, for
   every p — checked). Its degree is
   `n = p+1`, so the downward induction would need the step `d = p` where
   `char | p` kills the unit — exactly the step the witness escapes through.
   The witness check is against the **ordinary**-derivative hypothesis
   (`is_ca`), which is what the Ghosh proof's gcd formulation uses; since
   `n = p+1 > p`, the ordinary and Hasse hypotheses diverge for this family,
   but the witness satisfies BOTH (`is_ca_hasse` agrees), so this check is
   unaffected by the ordinary-vs-Hasse distinction.  The Ghosh `HD` objects
   are Hasse–Schmidt derivations of the multivariate monomial (eq 2.1), not
   the univariate Hasse derivatives of the CA hypothesis — the break
   verification (checks 1–2) is about `Φ^#` automorphisms and is
   characteristic-independent, so the ordinary-vs-Hasse issue does not touch
   it.  Re-verified after the `is_ca_hasse` library addition: all 1313 checks
   still PASS.

Result: **all 1313 checks PASS** (exit 0),
captured in `code/out/ghosh_break.captured.txt`.

Run: `python code/ghosh_charp/verify_break.py` (exit 0 iff all pass).
