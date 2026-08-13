# Library state — Gilbreath conjecture

What the reference library establishes, as of this build. Every claim below is
backed by a downloaded source in `research/sources/`; each carries its
hypotheses and whether they hold here.

## The canonical tier (statement, names, history)

```claim
id: gc-block-lemma-odlyzko
statement: If d_K(1)=1 and d_K(n) ∈ {0,2} for 1 ≤ n ≤ N, then d_k(1)=1 for all K ≤ k ≤ N+K−1. So a leading {0,2} block of length N protects N subsequent rows, not n/2.
hypotheses: d_k are iterated absolute differences of any sequence with d_0(n)=p_n (primes), rows restricted to positions n ≤ N.
holds-here: yes — this is exactly the block lemma the run's argument is about; constant is N (one row per block entry), which is stronger than the ≈ n/2 in problem.md.
status: sourced (Odlyzko 1993, Intro; also Killgrove–Ralston 1959 page 121)
bearing: the run's oracle should check G(N)-type quantities, not just first entries; block profile = A000232−1.
anchor: research/sources/odlyzko-1993-iterated-differences-latex-source.full.md
```

```claim
id: verification-bounds
statement: Gilbreath's conjecture verified for the first 63,419 primes (Killgrove–Ralston 1959, SWAC, primes < 792,722) and for all primes < 10^13 (Odlyzko 1993, k ≤ π(10^13) ≈ 3.4×10^11).
hypotheses: finite initial segments of the primes; exact integer computation.
holds-here: yes; the run's own witnesses.json reproduces rows A_1..A_5 = Odlyzko Table 1 and block profile = Killgrove–Ralston P(i)−1, cross-validating the run's oracle against both published bounds.
status: sourced (two independent published computations; run's oracle agrees)
anchor: research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md; research/sources/odlyzko-1993-iterated-differences-latex-source.full.md
```

## The mod-4 linearization (an invariant candidate)

```claim
id: mod4-linearization
statement: For k ≥ 1, n ≥ 2, d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4), because d_k(n) is even there.
hypotheses: d_k(n) even for k≥1, n≥2 (true for primes and for any 2-then-odds start with even gaps).
holds-here: yes — this converts the absolute-value problem into linear congruences of Pascal-triangle type mod 4, the cleanest algebraic structure the run has.
status: sourced (Odlyzko 1993, §2, eq. (201))
bearing: any invariant of the mod-2 Pascal rule (e.g. via Lucas' theorem) is a candidate for forcing the {0,2} regime; CHT Lemma 3.10 is the general version: a(i,j) ≡ Σ_k C(i,k) a_{j+k} mod 2.
anchor: research/sources/odlyzko-1993-iterated-differences-latex-source.full.md; research/sources/chase-hunter-tao-2026-full-html.full.md (Lemma 3.10)
```

## The current frontier (2026)

```claim
id: cht-inverse-theorem
statement: (Chase–Hunter–Tao 2026, Theorem 1.6) If a_n ≤ 2^M, no 0-block of length L, and no {0,d}-block with 2^{M−m}<d≤2^{M−m+1} of length ≥ R_m−3R_{m−1} at depth ≤ 2R_{m−1} (R_m ≥ 4R_{m−1}, R_0 ≥ 100L·8^M), then a^{(N−1,1)} ∈ {0,1}. I.e. the ONLY ways an array with small initial data can fail to decay are: long zero-blocks, or very long shallow {0,d}-blocks (d≥2).
hypotheses: non-negative integer initial data with Cramér-type size bound (a_n ≤ 2^M ≤ log^O(1) N in the intended application); L ~ log^10 N.
holds-here: for the primes, hypothesis (i) follows from Cramér's conjecture; (ii),(iii) are unproved though heuristically plausible — this is exactly the run's "consumption vs regeneration" obstruction, restated.
status: sourced (arXiv:2607.08712, submitted 9 Jul 2026, 28pp, authors Z. Chase, Z. Hunter, T. Tao)
bearing: the run's attack must either rule out long zero-blocks and long shallow {0,d}-blocks for the primes, or find an invariant that bypasses this dichotomy. A counterexample-invariant approach should target exactly these two structures.
anchor: research/sources/chase-hunter-tao-2026-full-html.full.md
```

```claim
id: cht-random-analogue
statement: (Theorem 1.3) If a_1,a_2,... are independent non-negative integer random variables with (i) a_n ≤ δn eventually (a.s.) and (ii) P(a_n∈A) ≤ 1−ε for every 2-separated set A eventually, then a.s. the left diagonal is eventually {0,1}-valued. The uniform-on-{0,..,f(n)−1} model works for f(n) up to δn; and the threshold is between δn and 2^{n+1} (Remark 4.5: a_n uniform on {0,..,2^{n+1}} fails with prob ≥ 1/2 i.o.).
hypotheses: independence + sublinear growth + no 2-separated concentration. The geometric Cramér model (parameter 2/(2+log n)) satisfies these; uniform-on-{0,..,2^{n+1}} violates (i).
holds-here: primes are expected to behave like the geometric Cramér model (Cramér–Granville), so this is the strongest known heuristic support; it does NOT prove the prime case (independence is only conjectural for gaps, and the model needs no-2-separated-concentration which is only heuristic for primes).
status: sourced (arXiv:2607.08712 Theorem 1.3 & Remark 4.5; improves Chase 2024's f(n) ≤ (1/10) loglog n/logloglog n)
bearing: "2-separated concentration" is the precise form of the randomness hypothesis; the primes' evenness (gaps ≡ 0 mod 2 after dividing by 2... careful) is the 2-separated-set trap that the formulation (p_{n+1}−p_n)/2 − 1 avoids.
anchor: research/sources/chase-hunter-tao-2026-full-html.full.md
```

## The negative result: small gaps alone do not suffice

```claim
id: anti-gilbreath-construction
statement: (Eppstein 2011) For any unbounded monotone f(n) ≥ 2, however slowly growing, there is a sequence X whose n-th gap is ≤ f(n) but whose triangle's right edge switches between 1 and other values infinitely often.
hypotheses: none beyond f unbounded monotone; construction is explicit and builds backwards from partial triangles.
holds-here: yes — this refutes the blanket Croft claim (also noted by Odlyzko and by CHT paper's reference [3]) and is quoted in the CHT paper. Small gaps plus the 2-then-odds parity are NOT sufficient; non-concentration/randomness is essential.
status: sourced (Eppstein blog, 2011-02-20, also cited by CHT 2026)
bearing: any invariant argument must use more than the first row's gap bounds. It says nothing against the primes specifically, but kills any "gap bound alone" proof strategy.
anchor: research/sources/eppstein-anti-gilbreath-sequences.full.md
```

## History correction: the Proth "failed proof" is a retracted myth

```claim
id: proth-myth-retracted
statement: The widespread claim "Proth (1878) claimed to prove Gilbreath's conjecture and his proof was wrong" is unsupported and was retracted by its originator H.C. Williams ("On rereading his actual paper...I can find no support for my assertion...My apologies for seeming to have started a myth", email 2020, quoted in Chase 2024 §7). Proth's actual paper "Sur la série des nombres premiers" (Nouv. Corresp. Math. 4 (1878) 236–240) states the property as a "theorem" but gives no proof; the editor E. Catalan appended "is it not true that the theorems of Mr. Proth...are, rather, postulates?" (quoted in Arias de Reyna 2020).
hypotheses: the two papers (Chase 2024 §7 and Arias de Reyna 2020) independently document the retraction and the reading of Proth's paper.
holds-here: yes — this run must NOT claim to "locate the error in Proth's proof"; there is no proof to locate. GOAL.md's item "a located error in Proth's 1878 claimed proof" is based on the myth; the corrected finding is the retraction itself.
status: sourced (two independent accounts; the primary scan at GDZ is JS-blocked and could not be downloaded — recorded as unobtainable)
anchor: research/sources/chase-2024-random-analogue-gilbreath.full.md (Sect. 7); research/sources/arias-de-reyna-gilbreath-blog.full.md
```

## Finding: the shifted block-length sequence is uncatalogued

```claim
id: oeis-miss-A000232-minus-1
statement: The run's leading-{0,2}-block lengths at row k (k=1..40: 2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,175,175,175,290,...) equal OEIS A000232(k) − 1 exactly (A000232 is "one less than the position of the first number > 2 in row n of the difference triangle", = Killgrove–Ralston's P(k)). The OEIS lookup of the run's terms returned NO match: the shifted sequence A000232−1 is not catalogued, so no closed form is available from OEIS for it.
hypotheses: run's oracle correct (cross-validated against Odlyzko Table 1 and K-R table); OEIS A000232 entry correct.
holds-here: yes — this was checked term-by-term against the b-file.
status: checked (this run; oracle vs two published sources; OEIS lookup miss recorded)
bearing: nobody should re-search OEIS for these terms; the structure (why the block lengths grow ~ like A000232) must come from the mathematics, not a lookup.
anchor: research/summaries/oeis-A000232-bfile-block-lengths.md; code/out/witnesses.json
```

## What could not be obtained

- **Proth 1878, Sur la série des nombres premiers** (Nouv. Corresp. Math. 4:236–240): the GDZ scan is JavaScript-rendered; both the resolver URL and the gdz.sub.uni-goettingen.de ID returned only stub pages. The Deutsche Digitale Bibliothek metadata record confirms the item (pages 236–240, public domain) but the page images need a JS browser. Two independent reader accounts (Arias de Reyna 2020; Chase 2024 §7) cover its content: Proth states the property, gives no proof, Catalan's note calls it a postulate.
- **Guy, Unsolved Problems in Number Theory, §A10** (Springer): paywalled book; content is reflected in Odlyzko 1993 and MathWorld.
- **Sierpiński, A Selection of Problems in the Theory of Numbers, pp. 34–35**: paywalled; the block observation is reported in Odlyzko 1993 (ref [Sier]).
- **Gardner, Scientific American Dec 1980**: paywalled; bibliographic record (ERIC EJ235152) and its mapping into *The Last Recreations* ch. 12 (Peter Rowlett's Gardner index) confirm content, which is already covered by Caldwell's glossary and MathWorld.
- **Gilbreath, "Processing process: the Gilbreath conjecture", J. Number Theory 131 (2011) 2436–2441**: paywalled at ScienceDirect; abstract-level metadata only.

## Angled coverage summary

- Statement/names/history: Odlyzko 1993, Killgrove–Ralston 1959, Encyc. of Math, MathWorld, Caldwell glossary, Arias de Reyna 2020, Chase 2024 §7.
- Methods that worked/are current: Chase 2024 (random analogue, block lemmas), Chase–Hunter–Tao 2026 (Cramér model + inverse theorem + continuous model), Bhat–Cobeli–Zaharescu 2023 (quasi-periodicity of Proth–Gilbreath triangles; filtered rays 2023), Muney 2026 (valid-extension sets).
- Methods that fail/limits: Eppstein anti-Gilbreath (gap bounds alone insufficient); CHT Remark 4.5 (2^{n+1} growth breaks a.s. result); Chase 2024 exotic {0,3}-type examples (randomness necessary).
- Adjacent/computational: OEIS A000232/A036262/A100820/A397880/A395556, Odlyzko's G(N) table, Eppstein practical numbers (verified 212,000 rows).
- Counterexample constructions: Eppstein anti-Gilbreath; CHT §1.1 zero-block and {0,d}-block examples, Sierpinski-triangle {0,3} example.