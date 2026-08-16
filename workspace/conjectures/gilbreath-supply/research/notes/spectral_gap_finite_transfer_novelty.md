# Novelty check: 'spectral-gap finite transfer' via Parseval for Φ = 1+σ

**Question.** Does Pivato–Yassawi (math/0306136 Thm 7.1, and the affine-limit,
LCA-entropy, LCA-randomization papers) or Takei already contain the proposed
spectral-gap/Parseval form of the finite transfer — `wt(Φ_n h) = Σ_ω
|1+e^{2πiω}|²·|ĥ(ω)|²` with zero set tied to the 4-element kernel — or is it new
to this run?

**Sources read.** summaries/pivato_yassawi_affine_limit_measures.md,
_affine_limit_measures_II.md, takei_limiting_measures_rule90.md,
pivato_lca_entropy_randomization.md, pivato_yassawi_sofic_randomization.md,
and grep of the two full texts + notes/pivato_lucas_mixing_equivalence.md +
approaches/walsh-{subset-sum-fold-structure,discrepancy-erdos-turan}.md.

---

## (1) Do any sources state Φ=1+σ as a complex Fourier multiplier (1+e^{2πiω}) with zero set, connected to Lucas mixing or image weight?

**No.** None of the five papers does any of this:

- **Pivato–Yassawi** (all three: affine-limit, sofic-randomization):
  Fourier analysis appears only as *characters on the infinite product group*
  `A^M` and the *correlation / mixing* of a measure. Theorem 7.1 is an
  equivalence `(Φ asymptotically randomizes µ) ⟺ (µ is Lucas mixing)` in the
  weak-* / Cesàro-density-one sense on infinite configurations. There is **no
  finite L² Parseval identity**, no complex multiplier `1+e^{2πiω}`, no zero
  set, and no statement about `wt` (Hamming weight) of a fixed string.
- **Takei** is measure *rigidity* for the fold (nontrivial mixing input → uniform
  in Cesàro); no Fourier multiplier, no Parseval.
- **Pivato (LCA entropy)** is a *negative* result (entropy neither necessary nor
  sufficient for randomization) — explicitly no weight bound.
- The library's own `walsh-subset-sum-fold-structure` approach **already refuted**
  the Φ-alone Fourier/Walsh weight-bound idea: the Walsh identity is correct but
  is controlled by the *input*, and the all-ones + alternating kernel vectors kill
  any Φ-only lower bound. `walsh-discrepancy-erdos-turan` also notes Parseval over
  the digital group gives `Σ|ŝ(ω)|² = N` exactly, an L¹-vs-L² scale error.

The phrase "finite transfer" is the **run's own name** for the open gap (recorded
in notes/pivato_lucas_mixing_equivalence.md and
approaches/lucas-mixing-finite-transfer.md: "The open content is the finite
transfer, which is not in any source"). No external source names a "spectral-gap
finite transfer".

## (2) Is the identity elementary-Parseval, and does anything contradict it?

**It is *not* a correct Hamming-weight identity as written, and this is the load-bearing finding.** Parseval applies to the **L² norm (energy)** of a complex shift
operator — it does **not** return a Hamming weight, and the complex multiplier
cannot see the mod-2 structure of the actual F₂ fold. Three concrete defects,
each from hand arithmetic (no exec tool is held; unverified by machine):

**(a) Energy ≠ weight; the ±1 encoding is required and the DC/complement coupling
is dropped.** Take `N=4`, `h=(1,0,0,0)`. The F₂ single fold `(1+σ)h` is
`(1,0,0,1)`, `wt = 2`. But `Σ_ω |1+e^{2πiω}|²·|ĥ(ω)|²` with the *complex DFT of the
0/1 vector* `ĥ` = `Σ_ω 4cos²(ω/2)·1` = `4+2+0+2 = 8` (since `|1+e^{iθ}|²=4cos²(θ/2)`,
`θ=kπ/2`). `8 ≠ 2`. To connect Parseval to a weight you must (i) pass to the ±1
encoding `f=1-2h`, and (ii) use the fact that `f(x)+f(x+1) ∈ {0,±2}` with a nonzero
exactly where `h(x)=h(x+1)`, i.e. **complement** of the fold's 1-set. For a single
fold the correct relation is `wt(h⊕σh) = N − ‖(1+σ)f‖²/4`, not the stated equality.
The proposed identity is missing the encoding, the factor, and the weight–energy
conversion.

**(b) It fails for the n-fold, which is the whole object of SUPPLY.** `Φ_n`
means `(1+σ)^n` over **F₂**, where by Lucas `(1+σ)^n = Σ_j [n|j]₂ σ^j` and the
mod-2 cancellation `1+1=0` is essential. The complex multiplier
`(1+e^{2πiω})^n` cannot represent that cancellation: over ℂ `1+1=2≠0`, so the
all-ones direction (DC mode, complex multiplier `2`) is **not** annihilated, and
the Nyquist-only zero set misses the real structure. For `n≥2` the ±1 encoding
also stops tracking the F₂ fold (e.g. `(1+σ)²f = f+2σf+σ²f` vs `h⊕σ²h` disagree
in support). So the "Fourier multiplier on the dyadic group" is not the multiplier
of the F₂ fold.

**(c) Zero-set is wrong: 1 complex character ≠ 2-dimensional F₂ kernel.** The
complex multiplier `1+e^{2πiω}` vanishes only at `ω=1/2` (the alternating
direction). But the run's *proved* fact (`fold-rank-n-minus-2-binomial-proved`) is
`ker Φ_n = span(even-alt, odd-alt)`, a **2-dimensional** space
`{0ⁿ, 1ⁿ, (01)*, (10)*}` — it kills the **constant (all-ones, ω=0)** direction
too. Over F₂, `1+1=0` annihilates the DC mode; over ℂ it does not. So "zero set =
the 4-element kernel" does not hold; the presenter conflated the F₂ kernel with
the complex multiplier's zero set.

None of the four sources **states** the (correct parts of the) Parseval identity,
so none contradict it directly; but the proposal's claim that a spectral gap forces
a Hamming-weight lower bound contradicts the run's *proved* kernel/rank facts and
re-enters the very value-domain-vs-F₂ world mismatch the run just refuted for
Matomäki–Radziwill, Green–Tao/U², and Furstenberg.

## (3) Verdict (one line)

**New label, unsound method as stated:** no held source names a "spectral-gap
finite transfer", so the composite is new to this run — but it rests on Parseval
in a form that is dimensionally a weight-vs-energy mismatch and that the complex
Fourier basis (value-domain, ≠ F₂ arithmetic) cannot see for `n≥2`; the only
correct part (single-fold ±1 Parseval) is textbook, and the F₂ kernel / zero-set
correspondence it asserts is false against this run's proved facts.

## What survives (the part worth keeping)

The one correct, non-trivializable seed is the **single-fold** identity on the ±1
encoding: `wt(h⊕σh) = N − ‖(1+σ)f‖²/4`, i.e. a Parseval link saying weight is
controlled by energy away from the constant and alternating modes. That is
textbook and already deducible from the run's own Walsh/weight notes; it does not
survive iteration to `Φ_n`. Getting the *iterated* F₂ fold into Fourier terms
requires an F₂-native (Walsh/ANF or 2-adic) transform, which is precisely the
basis the three closed external engines rejected — so this route does **not**
circumvent the parity barrier by changing basis; it repeats the same mistake.

Status: **commentary / analytic check, unverified by machine** (no exec tool held).
