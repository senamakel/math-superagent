# Hand-verified oracle checks of Rampersad–Wiebe structural claims

Program `rw_verify.py` was written but **not executed** — this environment has no
shell-execution tool. The checks below were computed by hand for small `n` and
are labeled accordingly; the larger `rw_verify.py` sweep over `n<20` and the
50-trial transform round-trip remain **unrun** and must not be read as a pass.

## Theorems 5 / 7 / 9 (run-length transforms), hand-checked

Key correction: the linear-recurrence `S` of each theorem starts at `S(0)=1`.
For Thm 9 the "positive integers" sequence is `S(n)=n+1` (so `S(1)=2`, not 1);
for Thm 5 Fibonacci `S(1)=1,S(2)=2`; for Thm 7 `S(L)=1` for `L=0,1` and `2^{L-1}`
for `L≥2`.

- Thm 9: `n=1` → runs `[1]`, RLT `S(1)=2`; direct sum = 2. **Match.**
  `n=3` → runs `[2]`, RLT `S(2)=3`; direct sum `=1+0+1+1=3`. **Match.**
- Thm 5: `n=1`→RLT`1`, sum`1`; `n=2`→RLT`1`,sum`1`; `n=3`→runs`[2]` RLT`S(2)=2`,sum`2`. **Match.**
- Thm 7: `n=2`→runs`[1]` RLT`1`,sum`1`; `n=3`→runs`[2]` RLT`S(2)=2`,sum`2`. **Match.**

## Theorem 20 (run-of-1s divisibility structure), hand-checked, `m=2`

`T_2(n)=Σ_k[C(4k,n+k)C(n,k) mod 2]` should be 1 iff every run of 1s in `[n]₂` has
length divisible by 2.

- `n=3`=`11`, run `[2]` (divisible), direct sum `= 0+1+0+0 = 1`. **Match.**
- `n=5`=`101`, runs `[1,1]` (neither divisible), direct sum `=0+0+0+0+0+0=0`. **Match.**

## Full-cube submask-XOR zeta transform, hand-checked involution (NOT Φ_n)

The fold reads `T(d) = XOR_{i submask of d} h(i)`. For the 4-cell case
(`d=0..3`, submasks of d): `T(0)=h0; T(1)=h0⊕h1; T(2)=h0⊕h2;
T(3)=h0⊕h1⊕h2⊕h3`. This is the F₂ **zeta transform**; its inverse over F₂ is the
**Möbius transform**, which over F₂ coincides with zeta (since
`(−1)^{|·|}=1`). Hence the **full-cube zeta transform** (all 2^n subset-indexed coordinates) is an
involution. This must **not** be read as invertibility of **Φ_n**, the finite
Pascal-mod-2 fold: Φ_n is a rectangular truncation of this map with rank n−2,
nullity 2, ker Φ_n = span(even-alt, odd-alt) (exact F₂ elimination, n=2..20;
corrected rank — see fold-rank-is-n-2-nullity-2-alternating).
Round-trip `Φ∘Φ = id` holds on the full cube by the general F₂ zeta/Möbius identity.

```claim
id: supply-fold-submask-zeta-involution
statement: The submask-XOR map T(d)=XOR_{i⊆d} h(i) (SUPPLY's fold reading) is the F2 zeta
  transform, an involution (self-inverse linear bijection on the Boolean cube).
hypotheses: field F2; indexing over subsets ordered by submask inclusion.
holds-here: yes — this is exactly the coordinate the fold reads each step.
status: checked (hand-verified 4-cell; F2 zeta/Mobius identity is standard)
bearing: Φ_n — the finite Pascal-mod-2 fold — is NOT invertible: rank Φ_n = n−2, nullity 2,
  ker Φ_n = span(even-alt, odd-alt) (corrected rank, fold-rank-is-n-2-nullity-2-alternating;
  not rank n−3/nullity 1 as the earlier copy of this note stated). The involution statement holds only for the full-cube zeta
  transform on 2^n subset-indexed coordinates, which is a different map. Invertibility of a
  linear map bounds its kernel and says nothing about the weight of its images: a bijection
  can carry a balanced input to a weight-1 output, and the witness h = 1^{m/2}0^{m/2}
  reaches fold weight 1 at m = 8,16,24,32 (closed door 4). So this claim supports none of
  the "h is complicated enough" family, which is refuted as a family.
anchor: code/out/rw_verify_out.md
answers: does-the-fold-lose-information
```

```claim
id: rw-hand-oracle-checked
statement: Rampersad–Wiebe Thm 5, 7, 9 (run-length = named linear-recurrence) and Thm 20
  (T_m(n)=1 iff all runs of 1s have length ≡0 mod m) reproduce for the small cases
  hand-checked above.
hypotheses: n, m within the checked ranges (n≤3 for Thm 5/7/9; m=2, n=3,5 for Thm 20).
holds-here: yes within checked range; the full n<20 sweep in rw_verify.py is unrun.
status: checked (hand computation; limited range)
bearing: confirms the run-length (product) reading and both structural characterizations on
  the cases tested; the executable sweep is still needed to extend the check.
anchor: code/out/rw_verify_out.md
```
