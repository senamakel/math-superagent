# Scholar digest — the un-read catalogue/citation stubs, evaluated against the goal

This run's goal: f(n) = min{ D(S) : S ⊆ {0,1}^n, |S| = 2^{n-1}+1 } (max internal
degree), its known exact values f(1..5) = 1,2,2,2,3 = ceil(sqrt(n)), and the
spectral proof f(n) >= sqrt(n) that closes the log–sqrt gap from below. This
note records the scholar's verdict on the eight files that were fetched by
lookup (OEIS/citation graph) but never read. They are catalogue/citation data,
not theorems, so each verdict is: does it bear on the goal, and does it
contradict durable memory?

## Four OEIS sequences — NONE helps

All four carry an exact, catalogued closed form (status: catalogued), and none
of them equals f(n) or any quantity in the max-internal-degree problem. They
look like an over-eager lookup for a closed form that would turn the f(n)
enumeration into an evaluation; the fetched sequences are not that sequence.

| Sequence | Closed form | Why not f |
| --- | --- | --- |
| A002264 (floor(n/3), art-gallery/Chvátal) | a(n)=floor(n/3) | grows linearly; terms 0,0,0,1,1,1,2,... ≠ f(1..5)=1,2,2,2,3; no hypothesis links it to D(S). |
| A003056 (n appears n+1×, inverse triangular) | a(n)=floor((√(1+8n)−1)/2) ~ √(2n) | √-type closed form is a red herring: f(n)'s sqrt comes from A_n²=nI (a quadratic/Hadamard relation), NOT from an inverse-triangular index. Terms 0,1,1,2,2,2,3,... ≠ f. |
| A053251 (3rd-order mock theta ψ(q)) | partitions; ~exp(π√(n/6))/(4√n) | partition-theoretic; no connection to hypercube internal degree. |
| A202453 (Fibonacci self-fusion matrix) | F(n)·F(k+1) etc. | Fibonacci matrix fusion; unrelated. |

None contradicts durable memory; they are orthogonal catalogue noise. The
relevant search-target if the run ever wants one is the sequence "ceil(sqrt(n))"
itself (matches f(1..5)), not any of these four.

## Four citation graphs — one useful lead, one noise, two confirmations

These are lead-lists per their own banners ("not evidence"). Verdicts:

- **citations_w1871596124 (Falik–Samorodnitsky, 37 cites):** confirms the
  Falik claim is well-cited (O'Donnell, Ellis, Ellis–Keller–Lifshitz [in
  library]). The one genuinely relevant NEW lead: **Ambainis–Bavarian–Gao–Mao–
  Sun–Zuo 2014, "Tighter Relations between Sensitivity and Other Complexity
  Measures"** — squarely on the Boolean-sensitivity side problem.md lists under
  "Connections to Boolean function complexity." Lead only; transfer to D(S) is
  the library's recorded unproved gap. Worth chasing, not evidence.
- **citations_w2103749128 (KKL, 628 cites):** surfaces **Nisan–Szegedy 1994**
  (404 cites), the pre-2019 Ω(log n) source the library already records as
  withheld-by-screen. This row CONFIRMS that paper exists and is heavily cited
  but says nothing about its content — so the library's "Nisan–Szegedy
  recalled-not-sourced" status is unchanged. No contradiction.
- **citations_w2745097389 (Keevash–Long refs):** Keevash–Long's reference
  list (Beckner 1975, Harper 1964, Bonami 1970, Friedgut–Kalai, Mossel et al.).
  Confirms the "outer-boundary/Fourier family" the library already labels as
  the stuck tools. No new result; does not help D(S).
- **citations_w2914000451 (Lipari, cosmic-ray positrons):** pure noise — an
  astrophysics paper (arXiv:1902.06173) unrelated to the hypercube problem,
  evidently a mis-attributed OpenAlex ID. **Discard; does not help.**

## Contradictions

None of the eight contradicts recalled memory. They are catalogue/citation
data orthogonal to the run's claims. The only framing contradiction already
resolved elsewhere (problem.md's "gap open" vs the run's spectral f(n) >= sqrt(n))
is not reopened by any of these.

## Bottom line for the run

These eight add no new theorems and no f(n) closed form. The only actionable
item is the Ambainis et al. 2014 lead (sensitivity-complexity side). Everything
that closes or approaches the goal remains the spectral chain already on disk.
