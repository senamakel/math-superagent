# Dupuy & Weirich 2016 — Bits of 3^n in binary (paywalled; held secondhand)

> **Consolidated note.** This file and
> `research/summaries/dupuy-weirich-2015-bits-of-3n-binary-wieferich-erdos.md`
> both document the same situation: the Dupuy–Weirich theorem
> (J. Number Theory 158 (2016) 268–280, DOI 10.1016/j.jnt.2015.05.022) is
> **paywalled, and no free full text is held.** The two source files under
> `research/sources/` are notes/corrections, not primary mathematics:
> - `dupuy-weirich-2015-bits-of-3n-binary-wieferich-erdos.full.md` — correction
>   note (an unrelated astrophysics paper had been downloaded from a wrong
>   arXiv ID).
> - `dupuy-weirich-2016-average-bits-3n-binary.full.md` — Taylor Dupuy's paper
>   list confirming the citation; no mathematics.
>
> The theorem itself is held **secondhand** via `[[li-zhao-2026-non-wieferich-erdos]]`
> (claim `LI-ZHAO-EQUIDISTRIBUTION-DW-GEN`, whose Erdős-relevant ℤ-case hypotheses are
> now verified to hold against the held full body — (3) unramified, N((3))=3, residue
> degree 1, 2 coprime to 3 — so the claim is `holds-here: yes`) and
> `[[zhao-li-2024-beta-adic-powers-omitting-digit]]`.

## What the theorem is (secondhand, asserted-by-source)

For distinct primes p, q and a digit b, the frequency of b in the q-ary expansion
of `p^n` tends to 1/q as n → ∞ — i.e. the ternary digits of `2^n` are
asymptotically equidistributed. This is asymptotic/average behaviour, compatible
with (but much weaker than the specific needs of) Erdős's conjecture; like the
heuristic it does **not** pin down any particular n.

## Exact statement (now held, verbatim via Li–Zhao 2026 full body)

The primary full text is paywalled and no free copy was found (searched
arXiv, author's homepage, general web — no preprint of the JNT 2016 paper
exists). But the **exact statement is now held verbatim** in the Li–Zhao
`None-Wieferich property of prime ideals and a conjecture of Erdős`
(arXiv:2601.12753) full body, which states and then generalises it:

**Theorem (Dupuy–Weirich [JNT 158 (2016) 268–280], Theorem 3).** Let `p` and
`q` be distinct primes and `b ∈ {0,…,q−1}`; with
`f_{p,m}(b) = lim_{N→∞} (1/N) Σ_{n=1}^N f_{p,n,m}(b)` the Cesàro average over
`n` of the proportion of digit `b` in the first `m` digits of the q-ary
expansion of `p^n`, one has `lim_{m→∞} f_{p,m}(b) = 1/q`.

- **Unconditional:** the statement as given carries **no Wieferich condition**
  and is for all distinct primes p, q and all digits b. The request's falsifier
  is answered: the equidistribution theorem is not conditional on a
  non-Wieferich assumption. (The Wieferich material is their Theorem 6, a
  *separate* generalisation about primes p with `2^(p-1) ≢ 1 mod p²`.)
- **Conjecture 1.2** (their stronger belief): pointwise `lim_{n→∞} d_n(b)/(n log_q p)
  = 1/q`; this *would* imply Conjecture 1.1 (Erdős) via the p=2,q=3,b=2 case, but
  it is **only a conjecture** and the equidistribution theorem does not imply it.
- **Cesàro-average caveat:** `f_{p,m}(b)` averages over `n` first; it is an
  average/density statement that does **not** constrain the digits of any
  particular `2^n`. It cannot prove Erdős's conjecture and cannot reach the
  middle ternary digits of a single `2^n`. It is background, not a proof route.

## Gap

The *primary* JNT full text is not freely obtainable (paywalled, no preprint).
The exact statement and hypotheses are nonetheless fully established from the
Li–Zhao full body, which states and proves the theorem; nothing about the
statement's content is missing. Request `primary-full-text-e26b` is answered on
its substantive need (exact statement + whether conditional on Wieferich), even
though the paywalled PDF itself cannot be filed.

```claim
id: DUPUY-WEIRICH-THEOREM3-PRIMARY
statement: (Dupuy–Weirich, JNT 158 (2016) Thm 3) For distinct primes p, q and
  any digit b in {0..q-1}, the Cesàro average over n of the proportion of digit
  b in the first m digits of (p^n)_q, as m -> inf, tends to 1/q. Unconditional
  (no Wieferich hypothesis). For p=2,q=3,b=2 this makes the digit-2 proportion
  average 1/3. It does NOT imply (and is much weaker than) their Conjecture 1.2,
  the pointwise limit, which would imply Erdős.
hypotheses: p, q distinct primes; b any digit. All hold for p=2,q=3,b=2.
holds-here: yes.
status: asserted-by-source (exact statement held verbatim in Li–Zhao
  arXiv:2601.12753 full body, which states and proves it; the paywalled JNT
  primary itself is not filed — no free copy exists).
bearing: the strongest known statement in the digit-uniformity line; a Cesàro
  average over n, so it does not constrain any single 2^n and cannot reach the
  middle ternary digits. Background, consistent with the heuristic; a density
  statement about all exponents, not the specific thin sequence.
anchor: research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md (Thm,
  lines 92-98)
answers: primary-full-text-e26b
```

## Status

Not a primary source in this library (paywalled). The theorem's statement is held
verbatim secondhand via Li–Zhao's full body, which proves it; the Erdős-relevant
ℤ-case hypotheses are verified to hold. Still do not treat the equidistribution
statement as a per-n constraint — it is a Cesàro average over n and does not pin
down any particular power of two.
