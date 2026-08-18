# Claims: computational verification and Chen's theorem

Established by the sources in `research/sources/`. Each claim cites the source
that establishes it, with hypotheses and falsifier.

```claim
id: goldbach-binary-statement
statement: Every even integer n > 2 is a sum of two primes p + q (p, q prime). Open since 1742.
hypotheses: n even, n > 2. p, q need not be distinct (4 = 2 + 2 valid).
holds-here: yes — this is the target statement itself.
status: conjectured
evidence: Encyclopedia of Mathematics "Goldbach problem"; Wikipedia "Goldbach's conjecture"; MacTutor biography of Goldbach.
falsifies: an even n > 2 with no representation as a sum of two primes, with a machine-checked primality certificate for every attempted factorization.
```

```claim
id: verification-4e18
statement: The binary Goldbach conjecture holds for every even n with 4 < n ≤ 4·10^18, by exhaustive distributed computation.
hypotheses: none beyond the tested range.
holds-here: yes — this is the current computational verification record for the binary conjecture (as of the 2013/2014 paper; no later exhaustive record at or beyond 4×10^18 has been published in a refereed venue).
status: verified-numerically
evidence: Tomás Oliveira e Silva, Siegfried Herzog, Silvio Pardi, "Empirical verification of the even Goldbach conjecture and computation of prime gaps up to 4·10^18", Math. Comp. 83 (2014) 2033–2060, DOI 10.1090/S0025-5718-2013-02787-1 (full text in research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md; author's project page https://sweet.ua.pt/tos/goldbach.html). ~781.8 single-core CPU-years; double-checked up to 4×10^17.
falsifies: an even n ≤ 4·10^18 failing Goldbach, found by an independently written checker.
```

```claim
id: odd-goldbach-8.37e26
statement: Using Ramaré–Saouter (J. Number Theory 98 (2003) 10–33) and the 4×10^18 binary verification, the ternary Goldbach conjecture holds for all odd n up to 8.37×10^26.
hypotheses: Ramaré–Saouter effective short-interval-prime result; binary verification to 4×10^18.
holds-here: yes — but it concerns the ternary variant, not the binary target.
status: verified-numerically
evidence: Oliveira e Silva–Herzog–Pardi abstract (research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md).
falsifies: an odd n ≤ 8.37×10^26 not expressible as a sum of three primes, verified independently.
```

```claim
id: chen-theorem-classical
statement: (Chen 1966/1973) Every sufficiently large even integer N is expressible as N = p + a where p is prime and a has at most two prime factors (a ∈ P2, i.e. a is prime or a semiprime).
hypotheses: N even and sufficiently large; "sufficiently large" not made explicit in the classical statement.
holds-here: yes — this is the closest unconditional sieve-theory approximation to the binary conjecture; the parity problem blocks the P2 → prime step.
status: proved (by source)
evidence: Chen Jing-run, Scientia Sinica 16 (1973) 157–176 (DOI 10.1360/ya1973-16-2-157); see also Y. Zhang, "The contribution of Jing-run Chen to number theory", Sci. China Math. 66 (2023), research/sources/zhang-contribution-jingrun-chen-number-theory-2023.full.md.
falsifies: a counterexample to the statement as sourced (none known).
```

```claim
id: chen-explicit-yamada
statement: (Yamada 2015) Every even number N > exp(exp 36) can be written as a sum of a prime and a product of at most two primes; moreover π2(N) > 0.007·UN·N/log N for such N, where UN = 2e^{−γ}∏_{p>2}(1−1/(p−1)^2)∏_{p>2, p|N}(p−1)/(p−2).
hypotheses: N even, N > exp(exp 36) ≈ 10^(4.7×10^14).
holds-here: yes — an explicit effective threshold for Chen's theorem.
status: proved (by source)
evidence: Tomohiro Yamada, "Explicit Chen's theorem", arXiv:1511.03409 (research/sources/yamada-explicit-chens-theorem-arxiv-1511.03409.full.md).
falsifies: an even N > exp(exp 36) with no p + P2 representation, checked by independent computation.
```

```claim
id: chen-explicit-bordignon
statement: (Bordignon–Johnston–Starichkova, published Int. J. Number Theory 21 (2025), arXiv:2207.09452) Every even integer N > exp(exp 32.7) is a sum of a prime and a product of at most two primes, with π2(N) > 2·10^−4·U_N·N/log²N; also every even N > 4 is a sum of a prime and a product of at most e^29.3 primes.
hypotheses: N even, N > exp(exp 32.7); second part N > 4.
holds-here: yes — currently the best double-exponential explicit Chen-type threshold; BJS corrects gaps in Yamada's exp(exp 36) preprint.
status: proved (by source, published)
evidence: arXiv:2207.09452 (research/sources/bordignon-johnston-starichkova-explicit-chen-linear-sieve-arxiv-2207.09452.full.md); publication venue IJNT 21 (2025) per Dudek–Johnston citation.
falsifies: an even N in the stated range failing the representation, verified independently.
```

```claim
id: chen-explicit-bordignon-solo
statement: (Bordignon solo, "An explicit version of Chen's theorem", Bull. Austral. Math. Soc. 105 (2022) 344–346) Every even number N > exp(36) ≈ 4.3×10^15 is a sum of a prime and a product of at most two primes; every even N > 2 is a sum of a prime and a product of at most exp(33) primes. This is the much stronger single-exponential threshold (vs the BJS exp(exp 32.7)).
hypotheses: N even, N > exp(36) for the first part; N > 2 for the second.
holds-here: yes — a distinct, sharper-threshold explicit Chen result coexisting with BJS.
status: proved (by source, published)
evidence: DOI 10.1017/S0004972721001301 (read via Cambridge Core in this audit).
falsifies: an even N in the stated range failing the representation, verified independently.
```

```claim
id: chen-count-constant-1.9728
statement: (Runbo Li, "On Chen's theorem, Goldbach's conjecture and almost prime twins II", Math. Reports 28(78) (2026) 39–61, published) For every sufficiently large even integer N, the number D_{1,2}(N) of primes p such that N − p has at most two prime factors satisfies D_{1,2}(N) ≥ 1.9728·C(N)·N/(log N)^2, with C(N) = ∏_{p>2}(1 − 1/(p−1)^2)·∏_{p|N, p>2}(p−1)/(p−2). This is within 1.36% of the conjectured asymptotic constant 2, and supersedes the previous records 0.899 (Wu 2008), 1.733 (Runbo Li 2024 preprint) and 0.867.
hypotheses: N sufficiently large even; the constant 1.9728 is a lower-bound coefficient in the Chen-type weighted sieve.
holds-here: yes — the current record lower-bound constant for Chen's theorem (p + P2), superseding claim chen-count-constant-0.867.
status: proved (by source, published in Math. Reports 2026)
evidence: DOI 10.59277/mrar.2026.28.78.1.2.39; arXiv:2405.05727v4, Theorem 1.1.
falsifies: an independent check of the proof showing a gap; a referee rejection identifying a flaw.
```
