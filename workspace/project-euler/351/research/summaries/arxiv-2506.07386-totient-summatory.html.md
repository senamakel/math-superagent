# Brown, "Computation of the Totient Summatory Function" (arXiv:2506.07386, HTML full text)

Source: https://arxiv.org/html/2506.07386v1 — full text at
`research/sources/arxiv-2506.07386-totient-summatory.html.full.md`
(companion PDF digest: `research/summaries/arxiv-2506.07386-totient-summatory.md`).

## What this source establishes

The canonical reference for computing the totient summatory function
Φ(n) = φ(1) + … + φ(n) at large n. This is exactly the quantity PE 351 reduces
to: H(n) = 6·(C(n+1,2) − Φ(n)) = 3n² + 3n − 6Φ(n).

**The Mertens-first formula** (Dirichlet hyperbola method applied to the
convolution φ = μ ∗ id, with a·b = n):

    Φ(n) = Σ_{x≤a} μ(x)·⌊n/x⌋(⌊n/x⌋+1)/2        (term X)
         + Σ_{y≤b} y·M(⌊n/y⌋)                     (term Y)
         − b(b+1)/2 · M(a)                        (term Z)

**Mertens recursion** (from δ = μ ∗ 1, α·β = n):

    M(n) = 1 + ⌊β⌋·M(α) − Σ_{x≤α} μ(x)·⌊n/x⌋ − Σ_{y=2..β} M(⌊n/y⌋)

**Algorithm 1** (Mertens-first): sieves μ up to a = Θ̃(n^{2/3}), computes M up
to √n directly, evaluates the remaining M values at ⌊n/y⌋ via the recursion,
then assembles X + Y − Z. Time Θ̃(n^{2/3}), space Θ̃(n^{1/2}).

**Algorithm 13** (the paper's contribution): same time Θ̃(n^{2/3}), space
reduced to Θ̃(n^{1/3}) by batching the M(⌊n/y⌋) updates through phases 1–3.
Theorem 7: with a = Θ((n/log log n)^{2/3}), time Θ(n^{2/3}·(log log n)^{1/3}),
space Θ(n^{1/3}·(log log n)^{2/3}).

**Reference values** (Table 1; match OEIS A064018):

    Φ(10^16) = 30396355092701332166351822199504
    Φ(10^17) = 3039635509270133156701800820366346
    Φ(10^18) = 303963550927013314319686824781290348
    Φ(10^19) = 30396355092701331435065976498046398788

The computation of Φ(10^19) is new to this paper; it was run twice and the
results matched. The reference implementation `totientsum.py` is stored at
`research/sources/brown-totientsum-ancillary.full.md`.

## Why it matters here

For n = 10^8, the space-Θ̃(n^{1/2}) Algorithm 1 is entirely feasible (arrays of
size ~10^4 each), so we do not need Algorithm 13's space reduction; but the
paper's formula (1) + (2) is exactly the efficient method the run should
implement, and its Table 1 plus the ancillary code give independent checks at
Φ(10^8) = 303963552391 (the run's target value appears in OEIS A064018 b-file).

## Claims

```claim
id: mertens-first-totient-formula
statement: For ab = n, Φ(n) = Σ_{x≤a} μ(x)·⌊n/x⌋(⌊n/x⌋+1)/2 + Σ_{y≤b} y·M(⌊n/y⌋) − (b(b+1)/2)·M(a).
hypotheses: n ≥ 1; a, b positive integers with ab ≥ n (taken ab = n); μ the Möbius function, M(x) = Σ_{k≤x} μ(k).
holds-here: yes — this is the formula used to evaluate Φ(10^8) sublinearly.
status: sourced
bearing: reduces H(10^8) = 3·10^8·(10^8+1) − 6·Φ(10^8) to a Θ̃(n^{2/3}) computation.
anchor: research/summaries/arxiv-2506.07386-totient-summatory.html.md
```

```claim
id: mertens-recursion
statement: For αβ = n, M(n) = 1 + ⌊β⌋M(α) − Σ_{x≤α} μ(x)⌊n/x⌋ − Σ_{y=2..β} M(⌊n/y⌋).
hypotheses: n ≥ 1; α, β positive integers with αβ ≥ n (taken αβ = n).
holds-here: yes — used to obtain M(⌊n/y⌋) for y ≤ b from the sieved μ and M up to √n.
status: sourced
bearing: supplies the Mertens values the totient formula needs.
anchor: research/summaries/arxiv-2506.07386-totient-summatory.html.md
```
