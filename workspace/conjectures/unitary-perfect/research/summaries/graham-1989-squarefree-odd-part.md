# Graham (1989), *Unitary perfect numbers with squarefree odd part* — digest

Full text: [[graham-1989-squarefree-odd-part.full]] (Fib. Quart. 27 (1989)
317–322; submitted July 1987; OCR moderately noisy but readable).

## The theorem

> **Theorem.** If `2^m s` is a unitary perfect number and `s` is squarefree
> odd, then exactly one of
> `m = 1, s = 3` (gives `6`);
> `m = 2, s = 3·5` (gives `60`);
> `m = 6, s = 3·5·7·13` (gives `87360`).

So the UPNs whose odd part is squarefree are exactly `6, 60, 87360`. In
particular **90 and the fifth UPN (whose odd parts contain `3^2` and `5^4`)
are excluded from this classification** — they are the two known examples with
a repeated odd prime power, and any *sixth* UPN must have a repeated odd prime
power (a non-squarefree odd part).

## Method (why it is not a search)

The proof is "top-down/bottom-up" ratio analysis of the identity

```
σ*(2^m s)/(2^m s) = ((2^m+1)/2^m) · Π (p_i+1)/p_i = 2
```

- Every odd prime dividing `2^m + 1` must appear as a denominator on the RHS;
  forcing a prime to appear twice kills the case (e.g. `m=1`: `3 | 2^1+1`,
  `43 | 2^1+1`, `11 | 43+1`, `3 | 11+1` ⇒ 3 twice).
- Some `p_i` must be a Mersenne prime (a prime with `p_i + 1` a power of 2).
- For a Mersenne prime `q | s`, the chains `p_1 = q, p_{i+1} | p_i + 1` grow
  at least geometrically (`p_2 ≥ 2p_1 − 1`, `p_3 ≥ 4p_1 − 3`, …), bounding the
  product `G(q) = Π (p_i+1)/p_i`. Lemmas 1–4 give explicit `G(q)` bounds
  (e.g. `G(q) < (2^m)/(2^m − 1)` for q a Mersenne prime; products for
  `q ≥ 127` and `q ≥ 8191`).
- The balance forces `Π G(q_i) = 2`; splitting `m` odd / `m ≡ 0 mod 4` /
  `m ≡ 2 mod 4`, each case is shown to have LHS `< 2` if `s` is any larger
  product. The cases `m ≤ 10` are checked directly, then `m > 10`.

## Consequences for this run

- Any sixth UPN `n = 2^a·m` (m odd) has a **repeated odd prime power**. This
  is the sharpest structural restriction from the "squarefree" side: the two
  kernels that actually occur are `3^2` (in 90) and `5^4` (in the fifth).
- Any lemma that kills all repeated odd prime powers is **false** (it kills 90
  and the fifth example). Run every candidate lemma against all five witnesses
  before recording it as anything but `asserted`.
- The Mersenne-prime chain structure (`p_{i+1} | p_i + 1`, geometric growth)
  is the ancestor of the odd dependency graph / Pratt-tree machinery that
  Maciejewski uses for the 3-Higgs primes.

**Hypotheses:** `s` squarefree odd; `n = 2^m s` unitary perfect. Held as
`sourced` (proved in the paper; the OCR's Lemma statements are partial but the
theorem statement and the three-case bounding argument are fully legible).

```claim
id: graham1989-squarefree-odd-part
statement: A unitary perfect number with squarefree odd part s, n = 2^m s,
  is exactly one of 6 (2^1*3), 60 (2^2*3*5), 87360 (2^6*3*5*7*13); so any
  sixth UPN has a repeated odd prime power.
hypotheses: n = 2^m s unitary perfect, s odd squarefree
holds-here: yes - applies to every hypothetical sixth UPN, forcing a
  non-squarefree odd part
status: asserted (proved in Graham 1989; not re-derived here)
bearing: the two occurring non-squarefree kernels are 3^2 (90) and 5^4
  (fifth); a lemma ruling out all repeated odd prime powers is false
anchor: research/sources/graham-1989-squarefree-odd-part.full.md
contradicts: (none) -- 90 and 5^4 lie outside the squarefree-odd-part
  hypothesis, so the theorem does not touch them
answers: whether-a-sixth-has-repeated-odd-prime
```