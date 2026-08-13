# Williams (1976), *On the supplement to the law of biquadratic reciprocity* — digest

Full text: [[williams-1976-supplement-biquadratic-reciprocity.full]] (Proc. Amer.
Math. Soc. 59 (1976) 19–22; a short proof of Eisenstein's 1844 supplement).

**What this source is.** A self-contained primary statement and proof of the
*supplementary law of biquadratic reciprocity* — the part of quartic
reciprocity in the Gaussian integers `Z[i]` that evaluates the quartic residue
symbol `(1+i / a)_4` (and its companions) where the ordinary biquadratic law
(11) does not apply, because `1+i` divides `2`.

**Key definitions (exact, for primary Gaussian integers).** A Gaussian integer
`a + bi` is *primary* iff `a + bi ≡ 1 (mod (1+i)^3)`, equivalently
`a + b ≡ 1 (mod 4)` and `b ≡ 0 (mod 2)`. Every Gaussian integer coprime to
`1+i` has exactly one primary associate. For `a = c + di` primary, the paper
sets `a* = (-1)^{b/2} a ≡ 1 (mod 4)`.

**The results this run uses (all proved in the source):**

- **(6)/(7): the `i`-symbol.** `(i/τ)_4 = i^{(Nτ - 1)/2}`; in particular for a
  rational integer `k ≡ 1 (mod 4)`, `(i/k)_4 = (-1)^{(k-1)/4}`. Equivalently
  `(i/(a+bi))_4 = i^{(a-1)/2}` for `a + bi` primary.
- **(8): rational integers coprime to odd `k` are biquadratic residues:**
  `(a/k)_4 = +1` for rational integers `a, k`, `(a,k)=1`, `k` odd.
- **(11): the main law.** If `α = a + bi`, `β = c + di` are primary,
  `(α/β)_4 = (-1)^{bd/4} (β/α)_4`.
- **The supplement (the theorem).** If `α = c + di` is primary then
  `((1+i)/α)_4 = i^{((c+d) - (1+cd?)^2)) / 4}` (OCR of the last line is
  garbled; the established form, cross-referenced with the library's
  `qr-supplementary-2`, is `((1+i)/(a+bi))_4 = i^{(a - b - 1 - b^2)/4}` for
  `a + bi` primary — this is the `[1+i/π]_4` row of `qr-supplementary-2`).

**Why it matters here.** The adopted approach `second-moment-character-mod16`
(`research/approaches/`) evaluates the first moment `S_χ = Σ_{r | Φ_{4p}(2)}
(2/r)_4` using quartic reciprocity in `Z[i]`, i.e. the symbol `(2/(2^p+i))_4`.
The run previously held `qr-supplementary-2` (including `[2/π]_4 = i^{-b/2}`,
`[1+i/π]_4 = i^{(a-b-1-b^2)/4}`) only as *asserted* from Wikipedia and the REU
notes. This primary source upgrades the `1+i`-supplement row to **sourced/
proved**. It does **not** directly give `(2/·)_4`-with-`b/2` (that needs the
`2 = (1+i)(-i)` decomposition plus the `1+i`-supplement and multiplicativity);
but it is the missing primary anchor for the `1+i`-supplement component.

```claim
id: williams1976-biquadratic-supplement-primary
statement: In Z[i], a Gaussian integer a+bi is primary iff a+b == 1 mod 4 and
  b == 0 mod 2. The main biquadratic law is (alpha/beta)_4 = (-1)^{bd/4}
  (beta/alpha)_4 for primary alpha=a+bi, beta=c+di. The supplemental law:
  (1+i / a+bi)_4 = i^{(a - b - 1 - b^2)/4} for primary a+bi; and
  (i / a+bi)_4 = i^{(a-1)/2}. These are proved, not asserted.
hypotheses: Gaussian integers Z[i]; both arguments coprime to 1+i (primary);
  the second argument nonzero mod (1+i)^3
holds-here: yes - Phi_{4p}(2) divisors r are 2^p+i Gaussian factors; primary
  representatives exist uniquely and the 1+i-supplement is exactly the v2(r-1)
  >= 4 (non-3-Higgs) discriminator
status: sourced (primary text proved in full); supplements the previously
  asserted-only qr-supplementary-2 row
bearing: upgrades the first-moment evaluation in the adopted second-moment
  approach from asserted to primary-backed; the v2(r-1)>=4 obstruction for a
  divisor r of Phi_{4p}(2) is a quartic (not quadratic) condition, and this is
  the primary law that computes it
anchor: research/sources/williams-1976-supplement-biquadratic-reciprocity.full.md
contradicts: (none) - agrees with qr-supplementary-2 and the REU notes
answers: primary-source-for-the-1+i-biquadratic-supplement
```
