# Summary — Sums of products of binomial coefficients mod 2 and 2-regular sequences (full text)

Source: N. Rampersad, M. Wiebe, arXiv:2309.04012 (16 pp). URL
https://arxiv.org/html/2309.04012v1. Full text:
`[[rampersad_wiebe_2regular_fulltext.full]]`. Note: the earlier abstract-only
copy `rampersad_wiebe_2regular_binomial.md` was superseded by this reading of the
complete paper.

## What the paper actually establishes

It studies sums of the form
`T(n) = Σ_{k=0}^{n} [ C(a₁n+a₂k, a₃n+a₄k)·C(n,k) (mod 2) ]`  (Eq 1.1).
By Lucas (Eq 2.1–2.2), `C(n,k) mod 2 = 1` iff the base-2 expansion of `k` has no
`1` where `n` has `0` — i.e. exactly the submask condition (so the paper's core
input *is* the submask/Lucas reading, but the SUMS it analyses are over `k`, not
over submasks of a fixed `d`). The sum mand `T(n)` therefore counts the `k ≤ n`
where **both** binomials are odd.

**Definition 1 (run-length transform).** The run-length transform of a sequence
`(S(n))` is `T(n) = Π_{i ∈ ℒ(n)} S(i)`, product over the lengths `ℒ(n)` of the
maximal runs of 1s in the binary expansion of `n`. (The text's "sum" is a
mis-transcription; the example `T(11)=S(1)S(2)` and all theorems are products.)

**Theorem 4.** The run-length transform of a linear-recurrence sequence `S` (Def
2) is a 2-regular sequence: `T(n) = v·γ([n]₂)·w` with `γ(0)²=γ(0)` and the run
structure decoded as products `S(a_k)⋯S(a_1)`. **Lemma 3** gives `S(n) =
v·γ(1)ⁿ·w`. Consequences: the weight, average, and run structure of such `T` are
finite-state / Walnut-decidable, and averages are closed-form via the eigenvalues
of `M = γ(0)+γ(1)` (Section 6).

**Catalogue (Theorems 5–18).** Specific `(a₁,a₂,a₃,a₄)` make `T(n)` the
run-length transform of a named sequence: Fibonacci (Thm 5), truncated Fibonacci
(6), 1 followed by powers of 2 — i.e. `T(n) = 2^{wt(n) − #runs(n)}` (7), 1,2,2,2,…
(8), the positive integers (9), Narayana's cows (10), doubled integers (11),
Lucas numbers prepended by 1,1 (12), and several new ones (13–18) including
Padovan and the period-`(1,1,0)` sequence.

**Section 6 — averages.** For `n` in `[2^r, 2^{r+1})`, the average value is
`g(r+1)−g(r))/2^r` where `g(r) = v·M^r·w`, `M=γ(0)+γ(1)`. Explicitly for Thm 5,
`μ(r) = ((1+√2)^{r+1}+(1−√2)^{r+1})/2^{r+1} ≈ (1+√2)((1+√2)/2)^r` — i.e. **the
average grows like a constant times `((1+√2)/2)^r ≈ 1.207^r`**, sub-exponential
but super-polynomial, *not* linear in `n≈2^r`. This is the paper's closest thing to
a growth/weight statement for a binomial-mod-2 sum.

**Theorem 20 (the structure result most relevant here).** For `m ≥ 2`,
`T_m(n) = Σ_k [ C(2^m k, n+k)·C(n,k) (mod 2) ]` equals **1 iff every run of 1s in
`[n]₂` has length divisible by `m`, and 0 otherwise** (identity given as the
run-length transform of the period-`(1,0^{m−1})` sequence). This is an exact,
combinatorial 0/1 characterization of a binomial-product mod-2 sum — a concrete
image-structure theorem, proved by a bit-failure argument on carries (Lemma 19
is the `n=2^ℓ−1` case).

## What it does NOT establish

It never treats the fold `Φ` of SUPPLY — the **submask-XOR zeta transform**
`T(d) = XOR_{i⊆d} h(i)`. Its sums are over `k` of *products* `C(·)C(n,k)`, not
XORs over submasks, and its `T(n)` is a scalar (run-length product) rather than a
vector family in `d`. So "this is the fold Φ itself" in the earlier note is an
**overstatement**: the paper shares Lucas-as-submask machinery and hands the run
is 2-regular/automatic, but it gives no statement about `wt(Φ_n h)` for arbitrary
`h`, and no bound on a submask-XOR sum.

Against the run's single hypothesis (can `Φ` do work the switch-density form
cannot see): the paper's bearing is indirect. It shows that *some* binomial-F₂
sums carry explicit structure (Thm 20) and tractable growth/average machinery
(Sec 6), supporting the program of making the parity barrier porous on average.
But it supplies no theorem pinning down the image or weight of the submask-XOR
fold.

```claim
id: rw-runlength-is-2regular
statement: The run-length transform T(n)=Π_{i∈ℒ(n)}S(i) of a linear-recurrence sequence S
  is a 2-regular sequence, computable as v·γ([n]₂)·w, hence Walnut-decidable.
hypotheses: S satisfies a linear recurrence of finite order (Def 2, Eq 3.1).
holds-here: yes as a general phenomenon about binomial-mod-2 sums; the SUPPLY ^ is not
  itself a run-length transform of a linear-recurrence sequence of h.
status: proved (Rampersad–Wiebe, Thm 4 + Lemma 3)
bearing: machinery route: if wt(Φ_n h) were a run-length transform or otherwise 2-regular
  in n, its growth would be decidable. Supports the "porous average" programme; does not
  by itself bound the SUPPLY fold's weight.
anchor: research/sources/rampersad_wiebe_2regular_fulltext.full.md
```

```claim
id: rw-thm20-binomialsum-structure
statement: For m≥2, T_m(n)=Σ_k [C(2^m k,n+k)C(n,k) mod 2] equals 1 iff every run of 1s in
  [n]₂ has length divisible by m, and 0 otherwise (run-length transform of period-(1,0^{m-1})).
hypotheses: m≥2; summands ordinary binomials mod 2.
holds-here: n/a — this is a different sum family from SUPPLY's submask-XOR fold; kept as the
  paper's example that binomial-F2 sums can carry exact 0/1 structure.
status: proved (Rampersad–Wiebe, Thm 20, via Lemma 19 bit-failure/carry argument)
bearing: precedent that an F2-binomial sum can have an exact, decidable image structure;
  motivates seeking such a characterization for the SUPPLY fold rather than a mere bound.
anchor: research/sources/rampersad_wiebe_2regular_fulltext.full.md
```

```claim
id: rw-average-nonlinear
statement: The average of the Thm-5 run-length transform on n∈[2^r,2^{r+1}) is
  ((1+√2)^{r+1}+(1−√2)^{r+1})/2^{r+1}, i.e. ≈(1+√2)·((1+√2)/2)^r ≈ 1.207^r, sub-exponential
  but super-polynomial in 2^r — not linear.
hypotheses: sums of the specific Fibonacci form (Eq 1.1, Thm 5); M=γ(0)+γ(1) eigenvalues.
holds-here: unchecked as a model for the SUPPLY fold; shown here as the paper's only
  growth statement for a binomial-mod-2 sum.
status: proved (Rampersad–Wiebe, Sec 6)
bearing: warns that even "natural" binomial-F2 sums need not grow linearly; if wt(Φ_n h)
  did resemble such a sum its growth could be ~1.2^n, not ~n — a caution against assuming
  the weight is large.
anchor: research/sources/rampersad_wiebe_2regular_fulltext.full.md
```

```claim
id: rw-not-the-submask-xor-fold
statement: Rampersad–Wiebe analyses sums over k of products C(a1n+a2k,a3n+a4k)C(n,k) mod 2
  expressed as run-length transforms; it does not treat the submask-XOR zeta transform
  T(d)=XOR_{i⊆d} h(i) that is SUPPLY's fold Φ, and gives no theorem about its image or weight.
hypotheses: —.
holds-here: yes — this is the correction: the source is not "the fold Φ itself".
status: asserted (reading of the full text)
bearing: prevents the run from citing this paper for a weight bound on Φ it does not contain.
anchor: research/sources/rampersad_wiebe_2regular_fulltext.full.md
contradicts: rw-described-as-the-fold-itself (earlier abstract-based note)
```
