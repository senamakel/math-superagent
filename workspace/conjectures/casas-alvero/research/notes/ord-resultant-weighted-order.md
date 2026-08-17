# The weighted-order identity ord_0(R_i) = n(n−i) — proof for all n

**Claim (proved).** Over the traceless slice `a_1 = 0`, with `f = x^n + Σ_{j=2}^n a_j x^{n−j}`
monic, `H_i(f)` the i-th Hasse derivative, `R_i = Res_x(f, H_i(f))`, and the weighted
grading `w(a_j) = j`, the smallest weighted degree of `R_i` is

    ord_0(R_i) = n(n−i)   for every n ≥ 3, i = 1,…,n−1,

and the leading weighted coefficient is nonzero — so the order is exact, not merely a
lower bound.

**One-line argument.** Under `a_j ↦ t^j a_j` the roots scale `β_k ↦ t·β_k`, the root-form
resultant identity gives `R_i(t) = ∏_k H_i(f_t)(t·β_k)` with `H_i(f_t)(x) =
e_{n−i}(x − tβ_1,…,x − tβ_n)`, and each factor equals
`t^{n−i}·e_{n−i}((β_k−β_j)_{j≠k})`; hence

    R_i(t) = t^{n(n−i)} · ∏_{k=1}^n e_{n−i}((β_k−β_j)_{j≠k}),

and the product is a nonzero symmetric polynomial (each `e_{n−i}` in `n−1` entries with
`1 ≤ n−i ≤ n−1` is a nonzero symmetric polynomial; an integral-domain product of nonzero
polynomials is nonzero), which survives on the traceless slice `Σβ = 0`.

## Where each ingredient comes from

- **Root scaling under the weighted grading.** `w(a_j)=j` means `f_t(x) = t^n f(x/t)`, so
  the roots of `f_t` are `t·β_k`, each with the same multiplicity as `β_k` in `f`.
  Equivalently the weighted grading is the filtration where `x` does not move and `a_j`
  has weight `j`, which is exactly the grading induced by `f ↦ f_t`.
- **Root-form resultant identity** (already established in
  `research/notes/root-difference-identity-verified.md`, char-free, no division): for monic
  `f` with roots `β_1,…,β_n`, `Res_x(f, g) = ∏_k g(β_k)` (resultant-norm, leading coefficient
  1), and `H_i(f)(x) = e_{n−i}(x−β_1,…,x−β_n)` (definition-level from the shift
  `f(x+u) = ∏_k((x−β_k)+u)`, Hasse `H_i` carries no `i!`).
- **Nonvanishing of the leading coefficient.** Each `A_{i,k} := e_{n−i}((β_k−β_j)_{j≠k})`
  is the `(n−i)`-th elementary symmetric function of the `n−1` nonzero differences of `β_k`;
  it is a nonzero polynomial, so the product `∏_k A_{i,k}` is a nonzero polynomial in the
  `β_k`, hence a nonzero polynomial in `a_2,…,a_n` (the elementary symmetrics with
  `e_1 = 0` are algebraically independent). Exact integer evaluations with distinct `β_k`
  summing to zero confirm it does not lie in the traceless-slice annihilator, for
  `n = 3,…,8`.

## Consequences

**Weighted Samuel / Valabrega–Valla length.** When CA holds in degree `n` (so `V(I) = {0}`
as a scheme, i.e. `I = (R_1,…,R_{n−1})` is `m_0`-primary), the length of the quotient is the
weighted multiplicity `∏_i ord_0(R_i) / ∏_j w(a_j)`:

    |QQ[a_2..a_n]/(R_1,…,R_{n−1})| = ∏_{i=1}^{n−1} n(n−i) / n!
                                    = n^{n−1}·(n−1)! / n!  =  n^{n−2}.

So for every `n` where CA is true, the quotient length is exactly the Cayley number `n^{n−2}`,
and `V(I) = {0}` iff CA. This lifts the earlier n=3,4,5,6 computer check to a theorem valid
for all `n`, conditional only on `I` being `m_0`-primary (i.e. on the degree-`n` CA statement
the resultants are certifying).

## Computational verification (sympy, exact)

- **Exact orders n=3,4,5,6.** `ord_0(R_i) = n(n−i)` confirmed by substituting `a_j → t^j a_j`
  into the *true* `R_i = Res_x(f, H_i)` and reading the lowest exponent of `t`; leading
  coefficient nonzero in every case.
  - n=3: `{1:6, 2:3}`; n=4: `{1:12, 2:8, 3:4}`; n=5: `{1:20, 2:15, 3:10, 4:5}`;
    n=6: `{1:30, 2:24, 3:18, 4:12, 5:6}`. All == `n(n−i)`.
  - (`code/uresultant/verify_weighted_order.py` → OK; `verify_order_n6.py` → ALL OK.)
- **Length formula vs actual quotient length.** Standard-monomial (Groebner) count of
  `QQ[a_2..a_n]/I`:
  - n=3: 3 = 3^{1}; n=4: 16 = 4^{2}. Matches `n^{n−2}`.
  - Weighted orders product `/ n!`: n=3: 6·3/6 = 3; n=4: 12·8·4/24 = 16; n=5: 20·15·10·5/120 = 125 = 5^3. All == `n^{n−2}`.
- **Leading-coefficient nonzero on traceless slice, n=3..8** (exact, distinct β's with
  Σβ=0). All nonzero; i=1 gives the discriminant-squared × constant. A random-coincidence
  check at n=7,i=1 hit a genuine zero (two random β's collided, making the discriminant
  vanish) and was correctly discarded — a useful demonstration that the i=1 leading
  coefficient really is the discriminant and needs distinct roots to be checked.

## Branch / domain / assumptions

- Work over `QQ[a_2,…,a_n]`, traceless `a_1 = 0`. The root-form identities are char-free
  (any commutative ring, no division); the *order* computation and nonvanishing are over
  `QQ`. `n ≥ 3` throughout; `i ∈ {1,…,n−1}`.
- The length formula `n^{n−2}` is contingent on `I` being `m_0`-primary (CA true in degree
  `n`); that hypothesis is exactly what the resultants certify, and the statement does not
  assert CA, only the length when the Samuel/VV identity applies.

## Files

- `code/uresultant/verify_weighted_order.py` — exact orders (Method A) + structural product
  nonvanishing check (Method B) for n=3..8.
- `code/uresultant/verify_order_n6.py` — exact n=6 orders.
- `code/uresultant/verify_length_orders.py` — weighted-orders-product/n! == n^{n−2}, n=3,4,5.
- `code/uresultant/verify_length_direct.py` — actual quotient length via standard monomials
  (n=3: 3, n=4: 16).
- `code/uresultant/verify_leadcoeff_traceless2.py` — leading-coefficient nonzero on
  traceless slice, n=3..8, distinct β's.
