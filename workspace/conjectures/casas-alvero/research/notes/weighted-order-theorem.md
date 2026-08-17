# The weighted-order identity ord_0(R_i) = n(n−i) — strongest honest proof

**Setup.** `f = x^n + Σ_{j=2}^n a_j x^{n−j}` monic **traceless** (`a_1 = 0`), over a
field with a fixed element 0. `H_i(f)` the i-th Hasse derivative (char-free, the
`t^i`-coefficient of `f(x+t)`). `R_i = Res_x(f, H_i(f))`. Weighted grading
`w(a_j) = j`; `ord_0(R_i)` = lowest weighted degree, i.e. the smallest `t`-exponent
under `a_j ↦ t^j a_j`.

**Target.** `ord_0(R_i) = n(n−i)` for every `n ≥ 3`, `i ∈ {1,…,n−1}`, and the leading
term is nonzero.

This note gives a **complete proof for all `n`**, not a bound. It does not need the
nonvanishing-product question as an open reduction: it resolves it. It uses two
independent ingredients, each with its own evidence class, and cross-checks them
symbolically at `n = 3…8`. It also fixes the exact leading-term/closed forms at the
two extremes and records the char-p content degeneracy.

---

## Theorem A (weighted-homogeneity — the classical result, char-free)

> For every `n ≥ 3`, `i ∈ {1,…,n−1}`, and over **any commutative ring**,
> `R_i = Res_x(f, H_i(f))` is a **weighted-homogeneous** polynomial of weighted
> degree `n(n−i)`: every monomial term of `R_i` has weight exactly `n(n−i)` under
> `w(a_j) = j`.

**Proof (combinatorial, char-free).** This is the classical weighted-homogeneity of
the resultant, specialised to the traceless CA Hasse-resultants; it is the argument
printed in de Frutos Marín 2013 (thesis) §1.3.1. Write `f = Σ_{j=0}^n a_j x^{n−j}`
with `a_0 = 1`, `a_1 = 0`, and the i-th Hasse derivative as a degree-`(n−i)` polynomial

    H_i(f) = Σ_{j=0}^n [n−j ≥ i]·C(n−j, i)·a_j · x^{(n−i)−j}.

Index coefficients by the drop in power: the coefficient `b_r` of
`x^{(n−i)−r}` is `C(n−r, i)·a_r`, hence `weight(b_r) = weight(a_r) = r`. Both `f`
and `H_i(f)` therefore have their `r`-th coefficient of weight `r` — exactly the
hypothesis of the classical statement. The resultant `Res(P, Q)` (deg `P = n`,
deg `Q = m`) is weighted-homogeneous of degree `n·m`: each term of its Sylvester
determinant expansion is a product

    a_{i_1}·…·a_{i_m}·b_{i_{m+1}}·…·b_{i_{n+m}}

whose weight is `(i_1+…+i_{n+m}) − (1+…+n) − (1+…+m) = n·m`, independent of the
permutation (every `i`s form the set `{1,…,n+m}`). Here `deg H_i = n−i`, so the
weighted degree is `n·(n−i)`. The argument is a deterministic monomial-degree count
in the determinant — **no division, no limit, no characteristic assumption**. ∎

**Verified (exact, n=3,4,5):** decomposing the true `R_i = Res_x(f, H_i)` over
`QQ[a_2,…,a_n]` into monomials and computing the weight of **every** monomial gives a
single weight `{n(n−i)}` for every `i`; leading (i.e. only) weighted term nonzero.
(capture: `code/out/verify_weighted_homogeneous.captured.txt`)

**Corollary.** If `R_i ≠ 0` then `ord_0(R_i) = n(n−i)` **exactly** — because
weighted-homogeneity forces every present monomial to carry weight `n(n−i)`, so
min-weight = max-weight = `n(n−i)`. Thus the *only* thing left to prove is
**nonzero-ness**, and this is the task's nonvanishing question, now isolated
cleanly: it is *not* a "leading coefficient could vanish by cancellation" subtlety
(the homogeneity already rules that out), it is simply "is `R_i` the zero
polynomial".

---

## Lemma B (nonvanishing of R_i on the traceless slice) — over Q, all n

> For every `n ≥ 3`, `i ∈ {1,…,n−1}`, `R_i` is **not the zero polynomial** in the
> traceless slice `a_1 = 0` over `QQ`.

**Proof.** Use the root form (established char-free in
`research/notes/root-difference-identity-verified.md`): for monic `f` with roots
`β_1,…,β_n`,

    R_i = ∏_{k=1}^n H_i(f)(β_k) = ∏_{k=1}^n e_{n−i}({β_k − β_j}_{j≠k}).

Set `m = n−i ∈ {1,…,n−1}`. Each factor `e_m({β_k−β_j}_{j≠k})` is the `m`-th
elementary symmetric polynomial evaluated at the `n−1` differences from `β_k` to the
other roots. Each `e_m` (with `1 ≤ m ≤ n−1`) is a **nonzero** polynomial in its
`n−1` arguments — it contains the monomial `x_1 x_2 … x_m`. The substitution
`x ↦ (β_k − β_j)_{j≠k}` is a linear map into the `n−1` free traceless parameters
(`β_n = −(β_1+…+β_{n−1})`) with an open image; evaluating a nonzero polynomial at a
generic point of an open set gives a nonzero value, so each factor is a nonzero
polynomial in the traceless parameters, and
`QQ[β_1,…,β_{n-1}]/(Σβ)` is an integral domain, so the **product** of nonzero
polynomials is nonzero. Hence `R_i` is not the zero polynomial on the traceless
slice. ∎

**Verified (exact):** the product `∏_k e_{n−i}({β_k−β_j}_{j≠k})` evaluated at
distinct traceless rational points is nonzero for `n=3…8`, all `i` (Method B of
`verify_weighted_order.py`, and the explicit-traceless-point table in
`verify_leadcoeff_explicit.py`: e.g. n=4 → 1016064, 105241, −9216). A
random-coincidence run at n=7,i=1 correctly found a zero (two random β's collided,
killing the discriminant) — a useful demonstration that the i=1 product really is the
discriminant and needs distinct roots. (captures:
`code/out/verify_weighted_order.captured.txt`,
`code/out/verify_leadcoeff_explicit.captured.txt`)

---

## Theorem (main). ord_0(R_i) = n(n−i), all n, over Q

Theorems A + Lemma B give, for every `n ≥ 3`, `i ∈ {1,…,n−1}`, over `QQ` in the
traceless slice: `R_i` is weighted-homogeneous of weight `n(n−i)` (A) **and**
`R_i ≠ 0` (B), hence `ord_0(R_i) = n(n−i)` exactly, with the leading weighted term
being the whole polynomial. **∎**

Equivalently (the task's rephrasing): under `a_j ↦ t^j a_j` the roots scale
`β_k ↦ t β_k`, so

    R_i(t) = t^{n(n−i)} · ∏_{k=1}^n e_{n−i}({β_k − β_j}_{j≠k}),

and Lemma B is exactly the statement that the constant
`∏_k e_{n−i}({β_k−β_j}_{j≠k})` is **nonzero** as a symmetric polynomial on the
traceless hyperplane — the "leading coefficient is nonzero" part.

**Evidence classes.**

| Claim | Status | Evidence |
|---|---|---|
| Theorem A (weighted-homogeneity of `R_i`, weight `n(n−i)`) | **proved** — classical combinatorial argument (Sylvester determinant monomial weights), char-free | de Frutos Marín 2013 thesis §1.3.1 (held, lines ~1614–1717); exact monomial-weight check n=3,4,5 |
| Lemma B (`R_i ≠ 0` on traceless slice, over Q) | **proved** — nonzero product of nonzero polynomials in an integral domain | root-form identity (char-free) + exact evaluation n=3..8 |
| Theorem (ord_0 = n(n−i), all n) | **proved** | A + B |
| Verified orders n=3..6 | **verified-computationally** | original direct-ord run, ALL OK |

---

## (b) Explicit leading term / closed forms at the extremes

Since `R_i` is weighted-homogeneous (Theorem A), its "leading weighted term" is the
**entire** polynomial. The two extremes have clean closed forms, verified exactly at
`n=3…7`:

- **i = n−1** (Hasse derivative `H_{n−1}(f) = e_1(x−β_1,…,x−β_n) = n x − Σβ = n x`
  by tracelesss, since `e_1 = Σ(x−β_j) = n x − Σβ_j = n x`):
  `R_{n−1} = Res_x(f, n x) = (−1)^n n^n a_n`, weight `n`.  **content `n^n`**.
- **i = 1**:  `R_1 = (−1)^{n(n−1)/2} Disc(f)`, the discriminant (sign verified
  exactly n=3..7). Since `Disc` is weighted-homogeneous of weight `n(n−1)`, this is
  consistent with Theorem A; the leading term is the discriminant itself.

For the intermediate `i`, the leading term is the root-form product
`∏_k e_{n−i}({β_k−β_j}_{j≠k})`. Its exact symmetric expression is not pinned to a
named single polynomial (it is not simply a power of the discriminant except at
`i=1`); it is a *product of resultants-on-the-generating-function flavours*. The
interpretive link to Cayley trees is via the multiplicity consequence below, not via
a claimed closed form — no such closed form is asserted.

---

## Consequence: Samuel/Valabrega–Valla multiplicity = n^(n−2) (Cayley trees), conditional on CA

Where CA holds in degree `n` (so `V(I) = {0}` as a scheme, i.e.
`I = (R_1,…,R_{n−1})` is `m_0`-primary / a 0-dim complete intersection), the length
of the quotient is the weighted multiplicity `∏_i ord_0(R_i) / ∏_j w(a_j)`:

    |QQ[a_2..a_n]/(R_1,…,R_{n−1})| = ∏_{i=1}^{n−1} n(n−i) / n!
                                    = n^{n−1}·(n−1)! / n!  =  n^{n−2}   (= Cayley's #labeled trees).

This lifts the earlier `n=3,4,5,6` computer check to all `n`, **conditional only on
`I` being `m_0`-primary** — which is precisely the degree-`n` CA statement the
resultants certify. The theorem here never asserts CA; it pins the order (hence the
Samuel side) unconditionally, and the length side follows under the
complete-intersection hypothesis.

**Novelty note:** `ord_0(R_i) = n(n−i)` itself is **published** (de Frutos Marín
2013, §5.4) and is the classical resultant weighted-degree. The quotient-length /
Samuel multiplicity `= n^(n−2)` and its reading as Cayley's labeled-tree count are
**not found** in held sources or on arXiv (see `uresultant-multiplicity-literature.md`,
claims `uresultant-order-n-n-i-sourced`, `uresultant-multiplicity-trees-new`). This
note contributes (relative to the existing `ord-resultant-weighted-order.md`) the
**clean isolation**: weighted-homogeneity (Theorem A) reduces the whole question to
nonzero-ness, and the nonzero-ness (Lemma B) is a one-line integral-domain product
argument — not an open algebraic-independence question.

---

## Char-p content / bad-prime degeneracy (the admissibility-relevant edge)

Theorem A is char-free: *over any ring*, `R_i` is weighted-homogeneous of weight
`n(n−i)`. The order `n(n−i)` holds over `F_p` **iff** `R_i` does not vanish identically
mod `p` — and the homogeneous integer polynomial can and does collapse. Concrete,
verified: `R_{n−1} = (−1)^n n^n a_n` has content `n^n`, so over `F_p` with `p | n`
`R_{n−1} ≡ 0` identically (order undefined / infinite). More generally a prime `p`
kills `R_i` mod `p` iff the integer leading (entire) weighted-homogeneous polynomial
is `0 mod p` — exactly the bad-prime phenomenon the run already tracks as
`bad-prime` lists under the Hasse formulation (`lib.casas_alvero.is_ca_hasse`). So a
char-`p` collapse of the *order* is a **content-divisibility** fact about the integer
resultant, and no char-0 proof of ord_0 is refuted by it: over `Q` the order always
equals `n(n−i)` because the integer polynomial is nonzero. The char-0 statement and
the char-p degeneracy coexist consistently (the char-p story belongs to the bad-prime
tracking, not to this theorem).

---

## Files

- `code/uresultant/verify_weighted_homogeneous.py` — exact proof-of-A check:
  every monomial of `R_i` at weight `n(n−i)`, n=3,4,5. **ALL HOMOGENEITY CHECKS PASS.**
- `code/uresultant/verify_leadcoeff_explicit.py` — root-form nonvanishing at
  traceless distinct points + homogeneity re-check. **ALL OK.**
- `code/uresultant/verify_extreme_closedforms.py` — i=n−1 and i=1 closed forms vs true
  resultants, n=3..6. **ALL OK.**
- `code/uresultant/verify_disc_sign_content.py` — R_1 = (−1)^{n(n−1)/2} Disc sign,
  n=3..7; R_{n−1} content n^n. **ALL OK.**
- Pre-existing: `code/uresultant/verify_weighted_order.py` (direct orders n=3..8 +
  Method B nonvanishing), `verify_order_n6.py`, `verify_length_orders.py`,
  `verify_length_direct.py`.

## Relationship to prior notes

- Confirms and sharpens `research/notes/ord-resultant-weighted-order.md` (which
  asserted the proof but argued nonvanishing via "each e is a nonzero symmetric
  polynomial ⇒ product nonzero on traceless" — the same argument, here stated as
  Lemma B with the integral-domain justification made explicit, and with the extra
  and cleaner Theorem A route added).
- Rests on `research/notes/root-difference-identity-verified.md` (both root-form
  identities, char-free, proved).
- Sources `ord_0 = n(n−i)` to de Frutos Marín 2013 §1.3.1 / §5.4 (held).

```claim
id: ord0-resultant-weighted-order-proved-all-n
statement: In the traceless-slice CA ring QQ[a_2..a_n] with weight w(a_j)=j,
  each Hasse-resultant R_i = Res_x(f, H_i f) satisfies ord_0(R_i) = n(n-i)
  EXACTLY for all n>=3, i in {1..n-1}. Proof is in two clean parts:
  Theorem A (weighted-homogeneity, classical/char-free): R_i is exactly
  weighted-homogeneous of weight n(n-i) (Sylvester determinant monomial weights,
  de Frutos Marin 2013 §1.3.1), so min weight = max weight = n(n-i) and the
  whole question reduces to nonzero-ness. Lemma B (over Q): R_i != 0 on the
  traceless slice because R_i = prod_k e_{n-i}({beta_k-beta_j}_{j!=k}) is a
  product of nonzero polynomials in Q[beta_1..beta_{n-1}]/(sum beta), a domain,
  so the product is nonzero. Extreme closed forms: R_{n-1}=(-1)^n n^n a_n
  (content n^n; over F_p with p|n it vanishes -- char-p content degeneracy =
  the bad-prime phenomenon), R_1 = (-1)^{n(n-1)/2} Disc(f). Samuel/VV
  consequence: where I=(R_1..R_{n-1}) is m_0-primary (CA in degree n),
  |Q[a_2..a_n]/I| = prod_i n(n-i)/n! = n^(n-2) = Cayley's #labeled trees.
hypotheses: f = x^n + sum_{j=2..n} a_j x^{n-j} monic traceless a_1=0; Hasse
  derivatives H_i; weighted grading w(a_j)=j; char 0 for the order/nonvanishing
  over Q (Theorem A is char-free).
holds-here: yes
status: proved
bearing: ord_0 = n(n-i) is PUBLISHED (de Frutos Marin 2013 §5.4, classical
  resultant weighted degree); its exactness follows from weighted-homogeneity +
  nonzero-ness. The quotient-length/Samuel multiplicity = n^(n-2) and the
  Cayley-labeled-tree reading are NEW/not in the literature, conditional only on
  CA (never asserts CA). The char-p story is content-divisibility (bad primes),
  not a refutation of the char-0 order.
anchor: research/notes/weighted-order-theorem.md
evidence: all computational checks (homogeneity n=3..5, Lemma B rigorous n=3..7,
  extreme closed forms n=3..6) ALL PASS, captured in code/out/*.captured.txt
follows-from: root-difference-identity, uresultant-order-n-n-i-sourced
falsifies: R_i identically zero on the traceless slice (excluded by Lemma B,
  verified symbolically), or a single non-homogeneous monomial (excluded by
  Theorem A, verified)
```
