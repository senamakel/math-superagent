# Summary — Meštrović, Lucas' Theorem survey (full text)

Source: Romeo Meštrović, *Lucas' theorem: its generalizations, extensions and applications (1878–2014)*, arXiv:1409.3820. Source URL: https://arxiv.org/html/1409.3820v1. Full text: `[[mestrovic_lucas_theorem_survey_html.full]]`. This is the complete survey (the earlier stored file `mestrovic_lucas_theorem_survey.full.md` was only the arXiv landing page; this is the actual paper).

## What it establishes

The paper surveys all known formulations, proofs, extensions and applications of Lucas' theorem. The statement at the centre:

**Lucas' theorem (1878).** If `p` is prime and `n = n_0 + n_1 p + … + n_s p^s`, `m = m_0 + m_1 p + … + m_s p^s` are the base-`p` expansions, then
```
(n choose m) ≡ ∏_i (n_i choose m_i)  (mod p)
```
In particular, writing `n = Σ n_i 2^i` and `m = Σ m_i 2^i` in binary,
`(n choose m)` is **odd iff `m` is a binary submask of `n`** (every 1-bit of `m` is a 1-bit of `n`). That is the door-2 fact SUPPLY rests on: the depth-`d` fold cell is the XOR over binary submasks of `d`.

It also collects (relevant to this problem's neighbourhood):
- Section 4: sequences with the **Lucas property** `(a_n choose something) ≡ … mod p` and the double Lucas property — the defining family of 2-regular/automatic sequences, which is exactly the closed-door-4 territory (Thue–Morse and dyadic-structured inputs).
- Section 2.2 and Remark 35 (line 999): the **number of odd entries on row `n` of Pascal's triangle mod 2** is `2^{popcount(n)}` (from Lucas applied to `p=2`; the submask count). This is the counting fact behind the fold's dyadic self-similar block structure.
- Kummer's theorem (carries in base `p`) as the companion carry-based characterization, cited alongside Lucas.

## What it means for SUPPLY

It is the primary reference for the *entire* algebraic container of the fold `Φ`: Lucas ⇒ submask-XOR structure ⇒ the run-telescope partition of ↓d into `2^g`-runs and the block recurrences of the fold. It fixes door 2 (Lucas) as a theorem of record, not a derived fact. It does **not** address the primes' `h`, the switch-density barrier, or any arithmetic input beyond the binomial-parity identity.

## Claims

`C-lucas-submask-bin-parity` — **statement:** `C(d,i) ≡ 1 mod 2` iff `i ⊆ d` as binary submasks. **holds-here:** yes (door 2). **evidence:** sourced (Lucas' theorem, Meštrović survey, this full text). **bearing:** it is the exact identity defining the fold cell as a submask-XOR. **anchor:** `research/summaries/mestrovic_lucas_theorem_survey_html.md`.
