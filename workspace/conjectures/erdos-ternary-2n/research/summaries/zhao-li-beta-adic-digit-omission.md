# Zhao–Li: On β-adic expansions of powers of an algebraic integer omitting a digit

**Source:** arXiv:2405.06220v2, Quaestiones Mathematicae (published 2025), doi:10.2989/16073606.2025.2478908. Full text at `research/sources/zhao-li-beta-adic-digit-omission.full.md`.

## What it establishes

1. **Narkiewicz's bound stated exactly** (eq. (1.1), with the citation): `ℳ(N) ≤ 1.62 N^σ` with `σ = log_3 2 ≈ 0.63092`, where `ℳ(N) = #{1 ≤ n ≤ N : (2^n)_3 omits the digit 2}`. This is the cleanest confirmation in the library of the 1.62 constant and its meaning. (It is the counting function for n ≥ 1; the run's A_k has |A_k| = 2^{k-1} = N^σ at N = 2·3^{k-1} up to constant, consistent.)
2. **Theorem 1.8 (the general theorem)**: for α, β coprime algebraic integers in a number field K, with (β) = 𝔭₁^{e₁}⋯𝔭_h^{e_h} all unramified of prime norm, the number of n ≤ N with the β-adic expansion of α^n omitting a digit b is `≤ C₁ N^{σ(β)}`, `σ(β) = log(|N(β)|−1)/log|N(β)|`, C₁ a constant depending only on β (explicit in the proof: C₀ = u·|N(β)|^{m₀}·C̃₀, C₁ = C₀|N(β)|^{σ(β)} — all three quantities are effectively computed in §4).
3. **Corollary 1.9**: for coprime rational integers p,q, `ℳ_b(p,q,N) ≤ C N^{log(q−1)/log q}` with C effectively computable. For p=2, q=3, digit b=2 (which Theorem 1.5 allows since b ∈ {1,…,|N(β)|−1}): `ℳ_2(2,3,N) ≤ C·N^{log 2/log 3}` — a **complete modern proof of the Narkiewicz-type bound with effectively computable constant**.
4. **Method**: 𝔭-adic interpolation. The sequence α^n is split into finitely many subsequences α^{l}(α^{u})^{n} each having an analytic 𝔭-adic interpolation G_l(x) = α^{l}(α^{u})^x (Lemma 3.2, Cor 3.3); a quantitative nonvanishing of derivatives (Lemma 4.1) bounds how many n can share k prescribed non-b digits (Eq. (4.7)–(4.13)).
5. Also records: Erdős's original reference [4] is the Luminy conference paper "Some unconventional problems in number theory" (Math. Mag. 52 (1979), 67–70); the connection to Sloane persistence (Conjecture 1.3: 2^k omitting digit 0) and to practical binomial coefficients (`(2n choose n)` not practical if 2^n omits digit 2 — Leonetti–Sanna [17]).

## Bearing on the run

- **The open REQUESTS row `full-text-narkiewicz-b0b1` is now answered.** The constant 1.62 is confirmed verbatim as the statement of Narkiewicz's 1980 result (Zhao–Li eq. (1.1)), and the exponent σ = log_3 2 is independently re-proved with an effectively computable constant via 𝔭-adic interpolation. What remains unverified is Narkiewicz's *original derivation* of 1.62 (his two-page note is not in the library; Zhao–Li cite it but prove the bound by their own method).
- The exponent `σ(3) = log 2/log 3 = log_3 2` exactly matches the run's `|A_k| = 2^{k-1}` count: at the period scale N = 2·3^{k-1}, N^{log_3 2} = (2·3^{k-1})^{log_3 2} = 2·2^{k-1}·(3^{k-1})^{log_3 2}·... — the count 2^{k-1} and the bound N^{log_3 2} are the same growth, so the counting obstruction is sharp, not loose.

## Claims
```claim
id: ZL-1
statement: ℳ(N) = #{1 ≤ n ≤ N : (2^n)_3 omits digit 2} satisfies ℳ(N) ≤ 1.62 N^{log_3 2} (Narkiewicz 1980), σ = log_3 2 ≈ 0.63092; stated verbatim in Zhao–Li eq. (1.1).
hypotheses: none.
holds-here: yes — this is the counting-function bound; matches |A_k| = 2^{k-1} at period scale.
status: asserted-by-source (Zhao–Li cite Narkiewicz [19]; they do not reprove the 1.62 constant)
bearing: pins the Narkiewicz constant exactly; the primary derivation remains unverified but the statement is now double-sourced.
anchor: research/sources/zhao-li-beta-adic-digit-omission.full.md
```
```claim
id: ZL-2
statement: For coprime rational integers p,q and digit b, ℳ_b(p,q,N) ≤ C·N^{log(q−1)/log q} with C effectively computable; for p=2,q=3,b=2 this is a Narkiewicz-type bound with exponent log_3 2 and an explicit constant from the proof.
hypotheses: p,q coprime, q ≥ 3, b ∈ {1,…,q−1} (Thm 1.5) or any digit b ∈ D_β (Thm 1.8).
holds-here: yes — exactly the Erdős case with β=3 unramified (𝔭=(3), e=1, N(𝔭)=3).
status: proved (Zhao–Li Theorems 1.5/1.8, Corollary 1.9)
bearing: an independent modern reproof of the counting bound with an explicit constant — the deliverable "reproduce Narkiewicz's bound with its constant made explicit" is achieved in modern form.
anchor: research/sources/zhao-li-beta-adic-digit-omission.full.md
```