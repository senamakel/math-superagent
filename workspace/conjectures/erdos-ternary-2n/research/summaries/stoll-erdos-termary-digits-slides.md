# Stoll: On a problem of Erdős concerning the digits of 2^n in base 3 — and Hensel's lemma

**Source:** CIRM slides (08/11/2019), full text at `research/sources/stoll-erdos-termary-digits-slides.full.md`. Joint work with H. Kaneko.

## What it records (each verifiable from the slides)

1. **Narkiewicz proof sketch (the method, complete):** write 2^n = 3^{m_0} + ⋯ + 3^{m_s} with m_0 = 0; reduce mod 3^k; the RHS takes one of 2^{k-1} values 1 + ε_1·3 + ⋯ + ε_{k-1}·3^{k-1}, ε_i ∈ {0,1}; since 2 is a primitive root mod every 3^k, n can lie in only 2^{k-1} residue classes mod 2·3^{k-1}; count. This confirms the exact |A_k| = 2^{k-1} from the run's own computation (SIEVE-EXACT, ternary-sieve-count-doubles).
2. **Kennedy–Cooper (2001):** for (a,b)=1, #{n<x : (a^n)_b contains no digit ≥ b/2} ≤ C_b x^{log((b+1)/2)/log b}.
3. **Holdum–Klausen–Rasmussen (2015):** improve the multiplicative constants in Narkiewicz and Kennedy–Cooper.
4. **Stewart (1980, linear forms in logarithms):** for a, b multiplicatively independent, (#nonzero digits of n in base a) + (#nonzero digits of n in base b) ≥ c log n / log log n. For n = 2^n: (#1s in (2^n)_3) + (#2s in (2^n)_3) ≥ c log n/log log n — the *total* number of non-zero ternary digits is unbounded, but with no information on the individual counts of 1s vs 2s. This is a provable lower bound that coexists with |A_k| = 2^{k-1}.
5. **Dupuy–Weirich (2016) and Yu (2018+):** average (Cesàro) versions of digit-equidistribution: lim_m lim_N (1/N)Σ_{n≤N} d_{n,m}/m = 1/3, and lim_N (1/N)Σ d_{n,m_n}/m_n = 1/3. (The slides record these results; the precise nature of Yu's is "2018+".)
6. **Kaneko–Stoll (2018):** for any pattern P of length k in the p-ary expansion of m^n, there is a positive proportion of n with ≥ c log n occurrences, and n < c_3 p^{kL} with L consecutive occurrences. Uses a generalized Hensel's lemma (Kaneko–Stoll 2019). Key method: g(u) = (m^{p-1})^u = (1+ap^e)^u, f(u) = g(u) − b_{p,L}, Hensel gives ξ with (m^{p-1})^ξ = b_{p,L}; then N ≡ ξ mod p^{L'} gives m^{(p-1)N} ≡ b_{p,L} mod p^{L'}.
7. **Erdős's weak forms:** the weak form #{n : (2^n)_3 omits 2} < ∞, and the even weaker o(x^{log_3 2}) form, are both widely open; the slides record "flexible form" conjectures too.

## What it implies for this run

- The Narkiewicz count is exactly the bijection structure SIEVE-EXACT; the run's `|A_k| = 2^{k-1}` is confirmed as *the* known count, and the sieve can never close by counting (consistent with `code/out/sieve_cannot_close.md`).
- Stewart's unbounded-nonzero-digits theorem is a *provable* statement applying to every n — it is the one genuine unconditional lower bound on the digit structure. It forces at least c log n/log log n non-zero digits total, but not any specific digit.
- Kaneko–Stoll's Hensel-based construction shows how to *realise patterns* in (m^n)_p by solving g(u) = b in Z_p — this is the same 3-adic-function perspective the run's dense-orbit thread identifies; it is the only known technique that constructs (rather than counts) digit patterns in exponential sequences.
- The "average" results of Dupuy–Weirich / Yu show that on average over n, digit-distribution is uniform, but they say nothing about any single n — exactly the caveat GOAL.md insists on.

## Claims
```claim
id: STOLL-1
statement: Narkiewicz's method: 2^n mod 3^k, expressed as sum of distinct powers of 3, has exactly 2^{k-1} possible residues among the units; by primitivity of 2 mod 3^k, n lies in only 2^{k-1} residue classes mod 2·3^{k-1}; counting gives #{n<x : (2^n)_3 omits 2} ≤ 1.62 x^{log_3 2}.
hypotheses: same as LAG-1; the count derivation is the one written in the slides.
holds-here: yes.
status: asserted-by-source (slide exposition of the published bound)
bearing: confirms |A_k| = 2^{k-1} exactly, matching SIEVE-EXACT and the run's computation.
anchor: research/sources/stoll-erdos-termary-digits-slides.full.md
```
```claim
id: STOLL-2
statement: Stewart (1980): for a,b multiplicatively independent, the number of nonzero digits of n in base a plus in base b is ≥ c log n / log log n; applied to (2^n)_3 this gives (count of 1s) + (count of 2s) ≥ c log n / log log n.
hypotheses: n large; a=2, b=3.
holds-here: yes.
status: proved (theorem in the literature, as exhibited on the slides)
bearing: the only unconditional digit-structure lower bound; coexists with |A_k| = 2^{k-1}.
anchor: research/sources/stoll-erdos-termary-digits-slides.full.md
```
```claim
id: STOLL-3
statement: Kaneko–Stoll (2018): for any finite ternary pattern P, a positive proportion of n have ≥ c_1 log n occurrences of P in (2^n)_3... (their theorem is stated for (m^n)_p generally, p prime, m not a power of p).
hypotheses: p ≥ 2 prime, m not a power of p, P any pattern.
holds-here: yes for p=3, m=2.
status: proved (theorem on the slides)
bearing: shows patterns occur with positive density in the exponent n; direct evidence against the "independent digits" heuristic being the mechanism (patterns are forced by 3-adic continuity).
anchor: research/sources/stoll-erdos-termary-digits-slides.full.md
```