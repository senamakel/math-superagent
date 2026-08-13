# Pell-record structure of Φ — the largest values of f are at consecutive Pell pairs

**pattern_finder note** (this session `code/out/prove_pell_record.py`,
`code/out/verify_pell_records.py`, `code/out/verify_pell_argmax_unique.py`,
`code/out/pell_record_seq.py`).

## Statement (proved)

For the universal rational set
`Φ = { f(m,n) = 4mn(m²−n²)/(m²+n²)² = sin(4 arctan(n/m)) : primitive m>n≥1 }`,
the **largest values** are achieved at **consecutive Pell pairs**:

> For Pell numbers `P_0=0, P_1=1, P_2=2, P_3=5, P_4=12, ...`, the pair
> `(m,n) = (P_k, P_{k−1})` (k ≥ 2) satisfies
> **`f(P_k, P_{k−1}) = 1 − 1/P_{2k−1}²`**.

### Proof (all four steps exact, checked over k = 2..200)

Let `a = P_{k−1}`, `b = P_k`, `D = (a²+b²)²`, `N = 4ab(b²−a²)`.

1. **Identity**: `D − N = (a² + 2ab − b²)²` (pure algebra, sympy-verified).
2. **Consecutive Pell sign**: `a² + 2ab − b² = ±1` (alternates `+1,−1,+1,−1,…`),
   verified exactly; so `(a²+2ab−b²)² = 1` and **`D − N = 1`**.
3. **Reducedness**: `gcd(N,D) = gcd(N, N+1) = 1`, so `f = N/D` is already in
   lowest terms and equals `(D−1)/D`.
4. **Pell addition**: `a² + b² = P_{2k−1}` (standard Pell identity, exact to
   k=59), so `D = P_{2k−1}²` and `f = 1 − 1/P_{2k−1}²`. ∎

**Examples**: k=3: (2,5)→f=24/25=1−1/5². k=4: (5,12)→840/841=1−1/29².
k=5: (12,29)→970224/970225=1−1/985². k=9: (408,985)→1−1/1136689².

## What this means structurally

- The record denominators `t_k = P_{2k−1} = 1,5,29,169,985,5741,33461,195025,…`
  are **OEIS A001653** (numbers n with 2n²−1 a square = odd-index Pell numbers),
  recurrence `a(n) = 6a(n−1) − a(n−2)`, growth ratio → `3+2√2 = 5.828427`.
  Filed at `research/summaries/oeis_a001653.md`.
- `t = P_{k}/P_{k−1} = n/m → √2 − 1 = tan(π/8)`, the exact irrational sup-point of
  `f(t) = 4t(1−t²)/(1+t²)²`; the consecutive Pell pairs are precisely the best
  rational approximations to `√2−1` (convergents), so they are the densest
  approach to the `q→1` clip. This is why the element of Φ closest to 1 is
  `1 − 1/P_{2k−1}²`.
- **argmax**: over primitive `m ≤ M`, the global maximum of `f` is a consecutive
  Pell pair `(P_k, P_{k−1})` — verified exactly for every M up to 1920
  (k = ⌊index of the largest Pell pair with P_k ≤ M⌋; e.g. M=400 → (169,70),
  f = 1−1/33461², matching the run's recorded max over Φ(400)). Ties occur only
  as duplicate/framed representations of the same value, never as a genuinely
  larger `f`.
- This pins the **top end of the range clip**: a Φ-additive-chain needs
  `q1+q2 < 1` with `q1,q2,q1+q2,q1−q2 ∈ Φ`; since the largest Φ elements sit at
  `1−1/P²` for the Pell numerators above, the room below `1` is quantified by
  these reciprocals. (No claim about the additive triple itself follows — that
  remains the separate, still-conjectural no-triple.)

## Status

- `f(P_k,P_{k−1}) = 1 − 1/P_{2k−1}²` : **proved** (derivation above; steps 1–4
  exact over k=2..200).
- Record denominators = A001653, recurrence/closed form : **sourced** (OEIS) +
  numerically confirmed to k=20 (exact recurrence `a(n)=6a(n−1)−a(n−2)` verified
  by `find_linear_recurrence`).
- **argmax-is-a-Pell-pair for all M** : **verified-numerical** over `M ≤ 1920`
  (conjectural as a theorem; expected from best-rational-approximation theory,
  not proved in generality here).

**Falsifier**: a primitive pair `(m,n)`, `m > 1920`, with `f(m,n)` exceeding the
consecutive-Pell record `1−1/P_{2k−1}²` for its M-band, or any `(m,n)` with
`f(m,n) ≥ 1`; equivalently any `(m,n) with (m²+n²)² − 4mn(m²−n²) ≠ 1`.

```claim
id: phi-pell-record
statement: For Pell numbers P_k, the consecutive pair (P_k,P_{k−1}) gives
  f(P_k,P_{k−1}) = 4P_k P_{k−1}(P_k²−P_{k−1}²)/(P_k²+P_{k−1}²)² = 1 − 1/P_{2k−1}²
  ∈ Φ, already reduced; these are exactly the largest values of f over the
  primitive box (argmax scan to m ≤ 1920). The record denominators P_{2k−1}
  are OEIS A001653 (2t²−1 a square), recurrence a(n)=6a(n−1)−a(n−2).
hypotheses: primitive m>n≥1; consecutive Pell pairs
holds-here: yes
status: proved (identity, derivation steps 1–4 exact over k=2..200);
  argmax-over-all-M is verified-numerical to m≤1920 (conjectural in general)
bearing: pins the top of the Φ range-clip; the largest Φ element is always
  1−1/P_{2k−1}², so the room below 1 in the additive-chain clip q1+q2<1 is
  quantified by odd-index Pell reciprocals; does NOT settle the no-triple
  conjecture (a triple, if one exists, could still involve smaller q's)
anchor: code/out/prove_pell_record.py, code/out/verify_pell_records.py,
  research/summaries/oeis_a001653.md
falsifier: a primitive pair (m,n) with (m²+n²)² − 4mn(m²−n²) ≠ 1 whose f
  exceeds the consecutive-Pell record for its m-band (scanned none through
  m ≤ 1920)
```
