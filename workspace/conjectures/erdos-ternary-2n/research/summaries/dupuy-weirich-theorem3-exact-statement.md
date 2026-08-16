# Dupuy & Weirich Theorem 3 — exact statement now held (answering primary-full-text-e26b)

> **Answers: `primary-full-text-e26b`.** This note closes the request for the exact
> statement and hypotheses of Dupuy & Weirich, 'Bits of 3^n in binary, Wieferich
> primes and a conjecture of Erdős', J. Number Theory 158 (2016) 268–280.

## The journal full text is still paywalled — but the exact statement is now held

The primary JNT paper is not openly available, and no arXiv preprint of
Dupuy–Weirich is held. However the library's held full body
`research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md` (arXiv:2601.12753)
quotes the paper's central equidistribution theorem **verbatim** at lines 106–108.

## Theorem (Dupuy and Weirich [3, Theorem 3]), quoted verbatim

> Let `p` and `q` be distinct primes and `b ∈ {0, 1, …, q−1}`, then `lim_{m→∞} f_{p,m}(b) = 1/q`.

Where `f_{p,m}(b) = lim_{N→∞} (1/N) Σ_{n=1}^{N} f_{p,n,m}(b)` and
`f_{p,n,m}(b)` is the proportion of the first `m` q-ary digits of `p^n` equal to `b`.

## Hypotheses, and the falsifier the request asked about

- Hypotheses: **only** that `p, q` are distinct primes and `b` is a base-`q` digit.
- **Unconditional — no Wieferich condition appears in Theorem 3.** The library's
  request hypothesized "if the theorem is conditional on a non-Wieferich
  assumption, that restriction is the finding"; the contrary is the finding here.
  The Wieferich material in Dupuy–Weirich is a **separate** theorem (their
  Theorem 6, on `p` being Wieferich, generalised by Li–Zhao as its own result);
  it is not a hypothesis of Theorem 3's equidistribution statement.
- For the Erdős case `p=2, q=3`, `b ∈ {0,1,2}`: all hypotheses hold, so the
  ternary digits of `2^n` equidistribute at frequency `1/3` **in the Cesàro
  average over n, then in the digit-limit m → ∞**.

## What this does and does not say (the reason it is background, not a proof)

The limit is `lim_{m→∞} f_{p,m}(b)` where `f_{p,m}` is first averaged over `n`
(`1/N Σ_{n≤N}`) and then a digit-window limit taken. It is a **double
average/density statement**: it says nothing about the digits of any particular
`2^n`, and in particular does not rule out a single counterexample `n > 8`.
Li–Zhao's Conjecture 1.2 (quoted at lines 59–76) is the *strong*, per-`n`
version — `d_n(b) / (n log_q p) → 1/q` as `n → ∞` — which is exactly what would
imply Erdős (`d_n(2) > 0` for `n` large); that remains **open** and is strictly
stronger than Theorem 3.

```claim
id: DUPUY-WEIRICH-THEOREM3-UNCONDITIONAL
statement: (Theorem 3 of Dupuy & Weirich 2016, quoted verbatim in Li–Zhao
  Theorem-block at lines 106-108 of the held body) For distinct primes p,q and a
  digit b in {0,...,q-1}, f_{p,m}(b) -> 1/q as m -> infinity, where f_{p,m}(b) is
  the Cesàro average over n of the frequency of b among the first m q-ary digits
  of p^n. The statement carries NO Wieferich hypothesis; the Wieferich content of
  the paper is a separate theorem (their Thm 6).
hypotheses: p, q distinct primes; b any base-q digit.
holds-here: yes -- for the Erdős case p=2, q=3, all hypotheses hold
  unconditionally.
status: asserted-by-source (statement quoted verbatim from a held primary/peer
  body; the original JNT paper itself remains paywalled and unread here).
bearing: asymptotic equidistribution of the ternary digits of 2^n in the double
  average. Does NOT pin down any single 2^n, so does not prove (or touch) the
  per-n Erdős conjecture; background consistent with the heuristic.
anchor: research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md (lines 100-120)
falsifies: any claim that Theorem 3 of Dupuy–Weirich is conditional on a
  Wieferich or non-Wieferich assumption; and any reading of the equidistribution
  as a per-n statement that would rule out a single counterexample.
answers: primary-full-text-e26b
```
