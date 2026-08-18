# Frid, "Sturmian numeration systems and decompositions to palindromes" (2017/2024)

**Source:** arXiv:1710.11553 (https://arxiv.org/pdf/1710.11553), Anna E. Frid,
European J. Combin. (2024). Full text: `[[frid-sturmian-numeration-palindromes-2018.full]]`.

## What it establishes

**Set-up.** Classical Ostrowski numeration (1921) generalises the Zeckendorf
(Fibonacci) system: for a characteristic Sturmian word w with directive
sequence (d_i) (the continued-fraction partial quotients of its slope), a
representation N = k_n···k_0 with 0 ≤ k_i ≤ d_i ("legal", standard Ostrowski)
decomposes the word's prefix: **Lemma 1** — w(0..N] = s_n^{k_n} s_{n-1}^{k_{n-1}}···s_0^{k_0}, where s_i are the standard words of the directive sequence. **Proposition 2** — any word s_n^{k_n}···s_0^{k_0} with k_i ≤ d_i is a prefix of c_{n+1}.

**The extension.** Coefficients are allowed wider ranges (valid representations,
Prop 3: k_0 ≤ d_0+1, k_1 ≤ d_1+1, k_i ≤ d_i+2 for i ≥ 2), and the set of valid
representations is closed under "unbending"/"bending" transformations; every
valid representation reduces to the Ostrowski one and conversely (Theorem 1,
Corollary 2). This keeps the decomposition identity w(0..N] = s_n^{k_n}···s_0^{k_0} valid for valid representations (Props 5, 8).

**Application (the paper's goal).** Occurrences of palindromes in a
characteristic Sturmian word are described by representations of their two
endpoints (Theorem 2); this proves for Sturmian words the 2013 Puzynina–
Zamboni–Frid conjecture: a non-periodic word has, for every Q > 0, a prefix
that cannot be decomposed into at most Q palindromes (unbounded palindromic
length).

## Hypotheses and whether they hold here

- Requires the characteristic Sturmian word and its continued fraction
  (directive sequence). PE1006's S IS characteristic Sturmian of slope
  α = 1/φ² = [0;2,1,1,1,...], so the Fibonacci/Zeckendorf case is exactly
  the classical Ostrowski system with all d_i = 1.
- The palindromic-length application is the paper's own objective; not needed
  for Ψ(k).

## Bearing on PE1006

**Side axis only** — the run's own digits-dp / Zeckendorf-automatic route
(`pe1006-zeckendorf-automatic-digit-dp`) is structurally the same
"represent n in Fibonacci numeration, read off the word" device; the
library's primary source for that is the Fici factorisation + Zeckendorf
parity claim (`fibonacci-zeckendorf-parity-characterization`). This paper adds
the *general* Ostrowski (continued-fraction) setting in which the Fibonacci
word is the d_i ≡ 1 case, confirming the slope/characteristic-word link but
not contributing a new computation for Ψ(10^18). Verdict: **background**, not
load-bearing; no new claim needed on disk (the O(log) monoid does not use
palindromic structure).

```claim
id: ostrowski-prefix-decomposition-characteristic
statement: For a characteristic Sturmian word w with directive sequence (d_i)
and standard words s_i, the prefix w(0..N] equals s_n^{k_n}···s_0^{k_0} for the
(Ostrowski/Zeckendorf) representation N = k_n···k_0 with 0 ≤ k_i ≤ d_i; the
identity is preserved under the wider 'valid' coefficient ranges. (Frid, Lemma
1 and Props 2, 5 — the classical case d_i ≡ 1 is the Fibonacci/Zeckendorf
system and w is the Fibonacci word.)
hypotheses: w characteristic Sturmian; directive sequence (d_i) = continued
fraction of slope; representation legal/valid.
holds-here: yes — PE1006's S is characteristic Sturmian of slope 1/phi^2 =
[0;2,1,1,...], so the d_i ≡ 1 Fibonacci case applies.
status: sourced
bearing: confirms the Zeckendorf-numeration axis (same family as the
zeckendorf-automatic digit-dp approach, recorded in approaches/); not on the
committed universal-Euclidean critical path.
anchor: research/sources/frid-sturmian-numeration-palindromes-2018.full.md
```