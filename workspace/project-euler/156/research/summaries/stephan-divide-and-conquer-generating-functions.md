# Ralf Stephan — "Divide-and-conquer generating functions, Part I: Elementary Sequences"

**Source:** arXiv:math/0307027v1 [math.CO], 2 Jul 2003 (preprint). Full text: `research/sources/stephan-divide-and-conquer-generating-functions.full.md`. Downloaded because the Ruskey paper (on disk) cites this as [8] for the divide-and-conquer/morphism recurrence route to digit-count generating functions.

## What it establishes

Divide-and-conquer (DC) sequences satisfy recurrences like a_{2n} = f(a_n, …, n), a_{2n+1} = g(a_n, …, n); their ordinary generating functions satisfy functional equations of the form

- **Mahlerian** (no right member): c₀(z)F(z) + c₁(z)F(z²) + … + c_N(z)F(z^{2^N}) = 0;
- **DC type** (with right member b(z)): the same with = b(z).

The paper's terms: a series is *elementary DC* if it is a sum/product of rational functions and infinite sums/products where z appears only as a rational function of z^{2^k}.

**Main theorem** (with recurrences attached to each g.f. family (2.1)–(2.6)), e.g.:

- (2.1) Σ c^k z^{2^k}/(1−z^{2^k})  ⟹  a_{2n} = c·a_n + 1, a_{2n+1} = 1.  Example: a_n = v₂(n)+1 = A001511.
- (2.3) Π(1 + c·z^{2^k})  ⟹  a_n = c^{e₁(n)}; Gould's sequence 2^{e₁(n)} = A001316, Thue–Morse on {1,−1} for c=−1.
- (2.4) 1/(1−z) · Σ α^k (d·z^{2^k} + c·z^{2^{k+1}})/(1+z^{2^k})  ⟹  a_{2n} = α·a_n + c, a_{2n+1} = α·a_n + d.  With α=1, c=0, d=1 this is the **binary ones-count e₁(n)** (A000120), whose g.f. is 1/(1−z)·Σ z^{2^k}/(1+z^{2^k}); c=1,d=0 gives zeros-count e₀(n) = A023416.

(2.5)–(2.6) are stated as conjectures. Section 2.7 relates 2-rational sequences (Dumas) to matrix products λ·A_{n_ℓ}···A_{n₀}·γ over the binary digits — the same linear-representation machinery Allouche–Shallit use for k-regular sequences. Section 3 tabulates example sequences with OEIS A-numbers.

## Bearing on PE156

- Background/theory tier, not a solver input. The problem's f(n,d) is the prefix sum of the per-number digit count c_d(n); its d=1 generating function (A094798) g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))²·g(x^10) is a **base-10 analogue** of the DC/Mahler functional equations this paper develops over base 2. That equation is quoted in `research/notes/oeis-catalogue-pe156.md` and is the object of the approach note `research/approaches/mahler-generating-function.md`.
- The paper establishes that digit-count sequences are exactly of this DC/Mahler type — supporting the generating-function reformulation route — but it does **not** address the fixed-point equation f(n,d)=n, its finiteness, or any bound. Those come from Khovanova–Marton Prop 9.1 (`G2-solution-bound`), not from this source.
- Preprint status, largely empirical (the author says the theorems are backed by computation to index 100+, "we can now only encourage the reader to find more formal proofs"); treat as a structural lead, not a proved theorem to rest on.

## Does not settle

Nothing about solution counts, sums, or bounds for f(n,d)=n. Not an answer source and not needed for the solver's correctness — it only frames the generating-function approach already recorded as proposed (not taken) in `research/approaches/`.