# On digital sequences associated with Pascal's triangle — Mathonet, Rigo, Stipulanti, Zénaïdi (2022)

Source: https://arxiv.org/pdf/2201.06636
Full text: [[mathonet-rigo-stipulanti-zenaidi-digital-sequences-pascal.full]]

## What it establishes

Study the sequence `t_{p,n} = Σ_i [C(n,i) mod p] · p^i` — the `n`-th row of Pascal's
triangle mod `p` read as a base-`p` number.

- **Lucas theorem restated** (Theorem 1): `C(n,m) ≡ ∏ C(n_i, m_i) (mod p)` over base-p
  digits.
- **Prop 12 / Cor 14 / Prop 15.** The functions involved are p-recognizable /
  p-synchronized; `(t_{p,n})` itself is **not** p-regular (Prop 15).
- **Lemma 16–Lemma 19.** The `N_p(m)` maps (nim-sum-like) are injective; the set
  `{N(m)}` is exactly the set of **evil numbers** (popcount ≡ 0 mod 2). Odious/evil
  vocabulary appears naturally.
- **Prop 27 + conclusion.** For trinomial coefficients, a 3D p-substitution makes the
  sequence of multinomial coefficients mod p p-automatic.
- Recurrence `t_{p,n+1} = t_{p,n} ⊕_p (p·t_{p,n})`.

## Bearing for this problem

Provides the p-automatic / 2-regular vocabulary around Pascal-mod-p rows and the
odious/evil connection. **Weak bearing**: the objects studied are the base-p *number*
`t_{p,n}` and its automaticity, not the specific `Φ_n` fold/`M_d` structure or the
symmetric-difference multiset. It confirms the Lucas framing already imported and adds
little the two Wu run-length papers do not. The run structure of `M_d` (item 5) is not
established here.
