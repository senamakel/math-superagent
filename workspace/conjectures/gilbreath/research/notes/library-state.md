# Library state — Gilbreath conjecture

What the reference library establishes, as of this build. Every claim below is
backed by a downloaded source in `research/sources/`; each carries its
hypotheses and whether they hold here.

## Refuted this cycle: the run-count / turning-point potential lemma

```claim
id: runcount-lemma-refuted
statement: The lemma r(T(x)) <= r(x) — the number of maximal constant runs is non-increasing under the absolute-difference map T(x)_i = |x_i − x_{i+1}| — is FALSE, and so is the turning-point analogue t(T(x)) <= t(x). Hand counterexample x = (5,5,0,0): r(x) = 2 (runs [5,5], [0,0]) but T(x) = (0,5,0) has r = 3; t(5,5,0,0) = 0 while t(0,5,0) = 1. Machine-verified exhaustively by code/out/check_runcount_lemma.py over all 6,725,600 strings of length 1..8 with values 0..6: the first counterexample found is (6,6,6,6,6,6,5,5) (2 runs → 3), worst increase 3 (at (0,0,1,1,0,0,1,1) — 2 runs → 5). The class-restricted check (same file's variant run, code/out/check_runcount_lemma_class.captured.txt) shows the failure persists IN THE CLASS THE TRIANGLE ACTUALLY LIVES IN: over all even-valued strings with values {0,2,4,6} (length ≤ 8, 87,380 tested), over all halved {0,1,2,3} strings, and over all {0,1}-halved strings (length ≤ 10) — the minimal valid counterexample is (0,0,1,1) with T(0,0,1,1) = (0,1,0): 2 runs → 3. (0,0,1,1) is the halved form of the {0,2}-block interior string (0,0,2,2), so the lemma fails exactly in the leading-block regime the conjecture targets. The counterexample (a,a,c,c) is exactly Chamberland's rigid borderline class from the Ducci max-factoring proof (Ducci Lemma 3.1), i.e. the equality case where the factored-max potential does NOT decrease.
hypotheses: T is the non-cyclic absolute-difference map on finite strings (the Gilbreath row operator); r, t as defined.
holds-here: yes — machine-verified that the lemma fails even in the halved {0,1} interior class ((0,0,1,1) → (0,1,0)), the exact regime where the target A_k(1) ∈ {0,2} lives; so no invariant can be built on raw r or t monotonicity anywhere in the triangle.
status: refuted (machine-verified exhaustive: 6,725,600 strings len ≤ 8 val 0..6 + class-restricted full enumeration of {0,2,4,6}-even, {0,1,2,3}-halved, {0,1}-halved classes; both runs captured in code/out/)
bearing: the total-variation-oscillation-potential approach is refuted as stated, WITHIN the actual regime (not just on exotic strings) — a corrected potential must handle the (a,a,c,c)-type equality cases explicitly (e.g. weighted or max-factored run count), which is where the Ducci borderline classification (ducci-max-factoring-potential-template) becomes the right tool. The Schoenberg/Pólya-frequency/total-positivity variation-diminishing theory is LINEAR-operator theory and does not transfer to the nonlinear absolute-difference map.
anchor: research/approaches/total-variation-oscillation-potential.md; code/out/check_runcount_lemma.py; code/out/check_runcount_lemma.captured.txt; code/out/check_runcount_lemma_class.captured.txt
```

```claim
id: rule90-relative-depth-null
statement: The relative-depth measure of block-length minima of the prime triangle (depth of each local min from the previous local-min row) is 21/27 within tolerance 1 of a power of 2. Against the exact binomial null X ~ Binomial(27, 9/16) — p = (9 near-2^j values in [0,15])/16, the program's own depth>0 guard excluding 0 — P(X >= 21) = 0.017299, significant at 5% but not 1%. The signal is tolerance-dependent: at tol=0 (exact powers {1,2,4,8,16}) 10/27 hit with p = 0.113, and conditioning on the observed concentrated range [2,9] post hoc gives p = 0.68. The permutation null is degenerate (the predicate tests depth values, not positions, so every shuffle of the 27 depths has the same hit count).
hypotheses: regime lengths are comparable to independent draws uniform over the observed range [0,15]; the 27 genuine regime lengths (k=1000 tail depth 841 dropped); tolerances as stated.
holds-here: yes — the numbers are read from the depth-1000 record the run computed (code/out/blocks_depth1000.json -> code/out/rule90_depth_results.json), and the exact p-value is machine-verified three independent ways (Fraction tail, scipy.stats.binom.sf, direct float sum; agree to 8 digits).
status: checked (this run; code/rule90_test/null_rule90_depth.py, capture code/out/null_rule90_depth.captured.txt, JSON code/out/rule90_depth_null.json)
bearing: closes the rule90-regeneration thread's timing-corollary question: the mild tol=1 concentration is not strong enough to support a structural regeneration mechanism on its own (dead at tol=0). The proved rule90-interior-xor identification is unaffected; the honest open question remains regeneration (thread research/threads/regeneration.md).
anchor: research/threads/rule90-regeneration.md; code/out/rule90_depth_results.json; code/out/null_rule90_depth.captured.txt
```

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
id: cht-inverse-theorem-library
statement: If a_n ≤ 2^M, no 0-block of length L, and no {0,d}-block with 2^{M−m}<d≤2^{M−m+1} of length ≥ R_m−3R_{m−1} at depth ≤ 2R_{m−1} (R_m ≥ 4R_{m−1}, R_0 ≥ 100L·8^M), then a^{(N−1,1)} ∈ {0,1}. I.e. the ONLY ways an array with small initial data can fail to decay are: long zero-blocks, or very long shallow {0,d}-blocks (d≥2).
hypotheses: non-negative integer initial data with Cramér-type size bound (a_n ≤ 2^M ≤ log^O(1) N in the intended application); L ~ log^10 N.
holds-here: no — checked against the real prime rows (sieve 2e7, code/cht/check_cht_hypotheses.py, code/out/cht_hypotheses.captured.txt / cht_hypotheses.md): max normalised gap a_n = 89 → M = ceil(log2 89) = 7, longest 0-run L = 2, longest {0,d}-block = 7 (d=1), so R_0 = 100·L·8^M = 419,430,400 ≫ 1000 (419,430× the reachable depth). The theorem's no-{0,d}-block hypothesis is not satisfiable at any reachable depth; the two obstruction families (long zero-blocks, long shallow {0,d}-blocks) are not surveyable within 1000 rows.
status: sourced (arXiv:2607.08712, submitted 9 Jul 2026, 28pp, authors Z. Chase, Z. Hunter, T. Tao)
bearing: the run's attack must either rule out long zero-blocks and long shallow {0,d}-blocks for the primes, or find an invariant that bypasses this dichotomy. A counterexample-invariant approach should target exactly these two structures.
anchor: research/sources/chase-hunter-tao-2026-full-html.full.md; code/out/cht_hypotheses.captured.txt; code/out/cht_hypotheses.md
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

(The Eppstein anti-Gilbreath construction is recorded in the authoritative source summary at `research/summaries/eppstein-anti-gilbreath-sequences.md` — see claim `anti-gilbreath-construction` there.)

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

- **Fine, N. J., "Binomial Coefficients Modulo a Prime", Amer. Math. Monthly 54 (1947) 589–592** — the original paper proving the Lucas correspondence (the mod-2/Sierpiński structure). Paywalled (JSTOR); no clean free PDF found; Scribd is a user-uploaded summary, not primary. Content is fully covered by Granville's e-survey chapters (held) and MathWorld/ProofWiki. Recorded so nobody re-searches.
- **Proth 1878, Sur la série des nombres premiers** (Nouv. Corresp. Math. 4:236–240): the GDZ scan is JavaScript-rendered; both the resolver URL and the gdz.sub.uni-goettingen.de ID returned only stub pages. The Deutsche Digitale Bibliothek metadata record confirms the item (pages 236–240, public domain) but the page images need a JS browser. Two independent reader accounts (Arias de Reyna 2020; Chase 2024 §7) cover its content: Proth states the property, gives no proof, Catalan's note calls it a postulate.
- **Guy, Unsolved Problems in Number Theory, §A10** (Springer): paywalled book; content is reflected in Odlyzko 1993 and MathWorld.
- **Sierpiński, A Selection of Problems in the Theory of Numbers, pp. 34–35**: paywalled; the block observation is reported in Odlyzko 1993 (ref [Sier]).
- **Gardner, Scientific American Dec 1980**: paywalled; bibliographic record (ERIC EJ235152) and its mapping into *The Last Recreations* ch. 12 (Peter Rowlett's Gardner index) confirm content, which is already covered by Caldwell's glossary and MathWorld.
- **Gilbreath, "Processing process: the Gilbreath conjecture", J. Number Theory 131 (2011) 2436–2441**: paywalled at ScienceDirect; abstract-level metadata only.

## Crank-alert: unrefereed "resolutions" of Gilbreath's conjecture — never cite

Two preprints found on Zenodo claim a complete proof of Gilbreath's
conjecture. Both are single-author, h-index 0, 0 citations, unrefereed, and
argue from bespoke frameworks (not number theory): (1) Hedi ZARKOUNA,
"Gilbreath's Conjecture Demystified by the Absolute Space (AIT)",
Zenodo 10.5281/zenodo.20577831 (2026-06-07), book chapter — claims convergence
to a static "invariant vector V = [1,2,0,0,…]" via an "Arithmetic Index
Theory", primes as a subset of a generating function; (2) Okolo, Hanyelichukwu
Paul, "A Resolution of Gilbreath's Conjecture and the Principle of Invariant
Dissipation", Zenodo 10.5281/zenodo.16658834 (2025-08-01) — argues from an
"Organized Complexity" framework, a "Harmonic Divisor Fan lattice", and an
"axiom of Global Harmony". Neither engages the block/regeneration structure the
run has proved, and neither has been checked by anyone. They are recorded here
so that no agent in this run mistakes a Zenodo "resolution" for a result; the
conjecture remains open as of the current literature (Colonna 2026 verification
to 1.5×10^15, nothing more).

## New holdings this cycle (July 2026 update)

```claim
id: parity-wave-theorem
statement: For any sequence beginning (2, odd, odd, ...), the leading term of every row of iterated absolute differences is odd. The shape (odd, even, even, ...) is preserved by the operator.
hypotheses: A_0 = (2, odd, odd, ...); absolute-difference iteration.
holds-here: yes — the primes satisfy the hypotheses; the run's reduction already proves the stronger {0,2} statement but not from this spare hypothesis.
status: proved (elementary induction, Ross 2026 parity note; independent of the run's own parity argument)
bearing: pins down the boundary: parity gives *odd*, not *1*; the conjecture lives between the two. Guranteeing the leading term is 1 is a separate claim about the {0,2} regime.
anchor: research/sources/ross-gilbreath-parity-note.full.md
```

```claim
id: closure-0d-double-edge
statement: {0,d} is closed under absolute differencing for every d ≥ 2 (|0−d|=d, |d−d|=0, |0−0|=0), so a leading 1 against {0,2} stays 1 — but the same closure preserves a large disturbance against {0,d} for d ≥ 4.
hypotheses: none beyond the closure identity.
holds-here: yes — this is why long shallow {0,d}-blocks with d≥2 are obstructions (CHT inverse theorem), and why the {0,2} regime is exactly the right target.
status: proved (one-line identity; Ross 2026; also implicit in CHT and Odlyzko)
bearing: any invariant that forces the second entry into {0,2} must use more than closure; the d=2-versus-d≥4 distinction is the crux.
anchor: research/sources/ross-gilbreath-parity-note.full.md
```

```claim
id: two-separation-hypothesis
statement: The operative general-class hypothesis is not "gaps grow slowly" but that gaps do not concentrate in an arithmetically rigid (2-separated) set — a set with no two consecutive integers (e.g. evens, multiples of 3). If gaps were trapped in a 2-separated set, the whole array would be trapped with them and collapse to 1 could genuinely fail.
hypotheses: general Gilbreath-like sequences; 2-separation as defined.
holds-here: yes — this is the precise form of "sufficiently random" that Odlyzko left undefined; the primes' gaps are believed (heuristically) not to be 2-separated-concentrating.
status: asserted-by-source (Ross 2026; consistent with CHT 2026 Theorem 1.3 condition (ii) and Eppstein's anti-Gilbreath)
bearing: refines the run's "general class with bounded gaps" goal: the class must be carved down to non-concentration, per CONTEXT ruling-out of the blanket bounded-gap strategy.
anchor: research/sources/ross-gilbreath-parity-note.full.md
```

```claim
id: cht-decay-lower-bound-logn
statement: In the stationary continuous Gilbreath model (i.i.d. standard exponential top row), Σ_{i≤n} c_i ≥ log(n+e) with c_i = E[a(i,j)]; hence c_i cannot decay faster than 1/i, and neither convergence to 0 nor boundedness of (c_i) is proved.
hypotheses: continuous model; expected values.
holds-here: yes (as a model statement; not a statement about the primes' discrete rows).
status: sourced (Chase–Hunter–Tao 2026, via Ross 2026 parity note and OEIS A397880 in the library)
bearing: the averaged decay rate of a Gilbreath array is itself open — the regeneration obstruction has a quantified, still-open shadow.
anchor: research/sources/chase-hunter-tao-2026-full-html.full.md; research/sources/ross-gilbreath-parity-note.full.md
```

```claim
id: verification-record-2026
statement: Current literature verification record: Odlyzko 1993 to 10^13 (G=635); Plouffe 2025 to 10^14, independent confirmation of G(π(10^14))=693 (arXiv:2510.06688); Colonna/Delahaye 2025-2026 to all primes < 1.5×10^15 (completed 03/18/2026; 57,600 G(π(x)) values), current absolute record G(π(x))=811 at x≈1.2125×10^15 (02/15/26) — prior absolute records G(π(2.8×10^14))=788 (11/08/25), G(π(6.15×10^14))=800 (12/13/25), G(π(10^15))=800 (01/23/26), G(π(1.0025×10^15))=806 (01/24/26), G(π(1.2075×10^15))=809 (02/15/26). Relative (vicinity-only) records reach G=1935 near 6.02×10^27 (exploratory 128-bit, NOT a verification bound). Still open.
hypotheses: exact integer computation; G(π(x)) = row index whose row begins 1 and is followed only by 0s and 2s.
holds-here: yes.
status: sourced (Wikipedia en rev 1348550815; Plouffe arXiv abstract; Colonna CNRS record page; all three downloaded this run)
bearing: the run must report 1.5×10^15 as the current record, strictly separate from its own depth-1000; the block criterion G is the same quantity the run's oracle computes as block_profile.
anchor: research/sources/wikipedia-gilbreaths-conjecture.full.md; research/sources/plouffe-2025-verification-10e14.full.md; research/sources/colonna-proth-gilbreath-record-2026-08.full.md (refresh 2026-08; supersedes the earlier 1.5e15/800 record page)
```

```claim
id: colonna-deletion-left-edge-failure
statement: (Colonna 2025-26, record-page footnote) Removing one prime (7, 5, or 11) from the prime list gives a 2-then-odds sequence with gaps ≤ 6 (≤ 4 for delete-5) whose left edge fails: for (2,3,5,11,13,17,19) (gaps 1,2,6,2,4,2), A1=(1,2,6,2,4,2), A2=(1,4,4,2,2) — second entry 4 — A3=(3,0,2,0) — leading 3 at row 3 — A4=(3,2,2), A5=(1,0); for (2,3,7,11,...) (gaps ≤ 4) A2=(3,0,2,2,...), leading 3 already at row 2. So the deterministic class "2 followed by odds with gaps ≤ g" has a counterexample for every g ≥ 4 (g = 4 suffices); only g = 2 (consecutive odds) is proved.
hypotheses: 2-then-odds start; finite initial segments with those gap bounds.
holds-here: yes — this is exactly the class GOAL.md's general-class theorem would need to beat Eppstein AND the open left-side second-entry question; it shows the "gaps ≤ g" carve-down fails already at g = 4 (second entry 4 → leading 3).
status: sourced (Colonna record page footnote [04]; triangle arithmetic hand-checked against the source's own display, verified independently)
bearing: sharpens the REQUESTS open row "deterministic bounded-gap class": gaps ≤ 3 is the only possibly-open window below the counterexample; any general-class theorem needs a further restriction (CHT's 2-separated non-concentration) — no bounded-gap statement can hold at g ≥ 4.
anchor: research/sources/colonna-proth-gilbreath-record-2026-08.full.md
```

```claim
id: deepmind-formal-conjectures-gilbreath-lean
statement: Google DeepMind's formal-conjectures repo (commit ed75a6dd) contains FormalConjectures/Wikipedia/Gilbreath.lean: it defines the difference operator d 0 = p_n (via n.nth Nat.Prime), d^{k+1}(n) = Int.natAbs (d k (n+1) − d k n), and states the conjecture as theorem gilbreath_conjecture (k : ℕ+) : d k 0 = 1 with a single `sorry` placeholder — no proof of the parity/shape reduction or of the conjecture is formalised there. mathlib4's Nat.dist (Mathlib/Data/Nat/Dist.lean) provides the concrete absolute-difference primitive (comm, self=0, dist_eq_sub_of_le) that this run's own Lean formalisation should build on.
hypotheses: Lean 4 / mathlib4 formalisation environment.
holds-here: yes — confirms the open REQUESTS row "Lean 4 formalisation status" is still open (no prior proof artifact in the repository), and gives the run a ready-made statement file to reuse; nothing to cite for the mathematics itself.
status: sourced (downloaded file, 41 lines, Apache 2.0)
bearing: GOAL.md's Lean 4 deliverable (define operator, prove (odd,even,even,...) preserved, reduce to the {0,2} second-entry claim, report #print axioms and sorrys) remains this run's to produce; Nat.dist is the right primitive; the DeepMind file shows the standard statement shape.
anchor: research/sources/deepmind-formal-conjectures-Gilbreath-lean.full.md
```

```claim
id: modulo-k-gilbreath-family
statement: (Li 2026, preprint) For any odd k, the sequence of primes of the form kn+2 has a difference triangle whose leading entry eventually stabilises to k; classical Gilbreath is k=1. Verified computationally for all odd k < 100,000.
hypotheses: primes in one residue class mod k, k odd; iteration of absolute differences.
holds-here: yes (it is a generalisation; k=1 is this run's object).
status: asserted-by-source (Zenodo preprint v2, 9 Mar 2026, single author, 0 citations; not peer-reviewed; verification data not independently checked here)
bearing: an extra generalisation family supporting the "not about primes" framing; the k>1 stabilisation is a consistency check — any k=1 invariant that too-cheaply proves the k>1 stabilisation too is likely vacuous. Spot-checking the k-stabilisation with the run's oracle is a natural small task.
anchor: research/sources/li-2026-modulo-k-gilbreath-family-kn2-pdf.full.md (full PDF, 240.8 kB, landed this cycle) + research/summaries/li-2026-modulo-k-gilbreath-family-kn2-pdf.md
```

```claim
id: chase-2024-arxiv-id
statement: Chase, "A random analogue of Gilbreath's conjecture", Math. Ann. 388 (2024) 2611–2625 = arXiv:2005.00530, doi 10.1007/s00208-023-02579-w.
hypotheses: bibliographic.
holds-here: yes.
status: sourced (Wikipedia en, retrieved this run — supplies the arXiv ID and DOI missing from earlier holdings)
bearing: gives the run a canonical citation for the random-analogue theorem.
anchor: research/sources/wikipedia-gilbreaths-conjecture.full.md
```

## The Gilbreath-polynomial route (MDPI 2023, recorded by search digest only)

```claim
id: gatti-2020-not-load-bearing
statement: gatti-2020-preprints-gilbreath-conditions (doi 10.20944/preprints202003.0145.v1, 8 Mar 2020, 10pp, NOT PEER-REVIEWED, 0 views 0 downloads 0 comments) is a claimed "proof of conditions" for GC via a global valid-extension equation (Eq. 2: signed sum of the whole right anti-diagonal) and an induction on prime bounds. Its Theorem 4 proof is LOCATED INVALID (right-inequality assumes conclusion), Lemma 4 interval-completeness of K_S is REFUTED by Muney 2026 (holes at length 5) and by hand example S={2,3,5} (|K_S|=5, not 2^{n−1}=4). The valid-extension formula (Eq. 2–3) is sound general-class machinery already extracted into claims above and is independently held from Alkan 2023 and Muney 2026. The paper contains no lemma testable against code/out/blocks_depth1000.json or the run's {0,2} data that is not already covered. The 2023 MDPI polynomial claim (gilbreath-polynomials-imply-gc) is a DIFFERENT paper (Mathematics 11(18):4006) whose PDF remains 403-unobtainable; the 2020 preprint does not contain the polynomial inequality.
hypotheses: none load-bearing beyond what is already extracted.
holds-here: classified as not-load-bearing — same class as granville-2026-piercing-gilbreath-not-load-bearing. Do not re-download or re-fetch.
status: source held, claims extracted, invalid-proof located; the wrapper-page download destroyed the frontier on 2026-08-13 (recorded: research/notes/frontier-collapse-alarm.md). The filter on FRONTIER.md prevents recurrence.
bearing: prevents re-fetching; the sound parts (valid-extension global formula, parity alternation) are already claims above.
anchor: research/sources/gatti-2020-preprints-gilbreath-conditions.full.md; research/summaries/gatti-2020-preprints-gilbreath-conditions.md
```

```claim
id: gilbreath-polynomials-imply-gc
statement: (Riccardo Gatti, Mathematics 2023, 11(18), 4006, doi 10.3390/math11184006 — author CONFIRMED, affiliation INBB/Eldor Lab Bologna, 7 pages, RePEc record held) In the "Gilbreath equation / Gilbreath polynomials" framework, GC is claimed to be implied by the bound p_n − 2^{n−1} ≤ P_{n−1}(1), where P_{n−1} is the (n−1)-st Gilbreath polynomial evaluated at 1, built from the first n primes. A finite sequence S=(s_1..s_n) is a "Gilbreath sequence" iff s_1 has some parity and s_2..s_n the opposite, and min K(s_1..s_m) ≤ s_{m+1} ≤ max K(s_1..s_m) for all m ≤ n, with max K_S = s_1·(n−1)! + s_2·(n−2)! + ... + s_n·0! + 1, min K_S = 2·s_n − max K_S (weighted factorial bounds).
hypotheses: ordered primes; the framework's own definitions (Gilbreath polynomials from the prime sequence).
holds-here: the framework is now FULLY pinned down and checkable — the polynomial object P_m is defined exactly in OEIS A347924/A347925 (held) and constructively in Gatti's own generator code gttrcr/rescode OEIS/A347924.cs (held): P_m is the degree ≤ m−1 polynomial interpolating the m+3 values U(S)_x − 2^(m+x−1), with U(S) the upper-bound Gilbreath extension by largest valid prime candidate; P_6 = (−57−55x−15x²−2x³)/3. The IMPLICATION's proof is still asserted-by-source (MDPI/preprints full text 403s from MDPI, /pdf, and preprints.org mirrors — recorded unobtainable); the inequality itself is numerically testable now via sympy/PARI and the machinery is implementable.
status: asserted-by-source (framework held and independently implementable; proof steps not in hand)
bearing: a genuinely different-looking handle on the {0,2} regime (size bound on p_n vs a polynomial in the primes). Do not build on the implication until the derivation is obtained; the polynomial machinery is now checkable so the claim can be stress-tested numerically without the paper.
anchor: research/sources/oeis-A347924-gilbreath-polynomials.full.md; research/sources/oeis-A347925-gilbreath-polynomial-denominators.full.md (summary file); research/sources/gatti-researchcode-A347924-cs.full.md; research/sources/gatti-2023-repec-record.full.md
```

## New holdings this cycle (librarian, this build) — Lean 4 formalisation COMPLETE

```claim
id: gilbreath-second-entry-equivalence
statement: In Lean 4 with Mathlib, the Gilbreath difference operator Step s i = Nat.dist (s i) (s (i+1)), the shape predicate StartsOddEvenEven s = (Odd (s 0) ∧ ∀ n, Even (s (n+1))), and the reduction lemma |1−n| = 1 ↔ n = 0 ∨ n = 2 are formalised and kernel-checked. Nine theorems (dist_odd_even, dist_dist_even, dist_one_eq_one, shape_theorem, shape_rows, reduction, reduction_lemma, gilbreath_reduction) are proved. gilbreath_reduction : GilbreathConjecture X ↔ SecondEntryIn02 X — an IFF. Every declaration's axiom footprint is exactly [propext, Classical.choice, Quot.sound] (the three standard Mathlib base axioms). Zero sorry, zero sorryAx. The IFF is an equivalence: it proves the {0,2} second-entry statement is exactly as hard as the conjecture, not a stepping stone to a proof. It reformulates rather than reduces.
hypotheses: X is a RowStream (X (k+1) = Step (X k)); X 1 has StartsOddEvenEven shape; X 1 0 = 1 (leading 1 at row 1). These hold for the prime triangle by computation (witnesses.json), not by Lean instantiation.
holds-here: yes — proved (Lean kernel-checked, EXIT=0, #print axioms = [propext, Classical.choice, Quot.sound], zero sorry/sorryAx)
status: proved (this run, Lean 4 / Mathlib; GOAL.md deliverable)
bearing: any future argument can target either the left-column statement or the {0,2} second-entry statement and the equivalence is beyond doubt; it closes no distance toward a proof of the conjecture itself — the {0,2} regime is exactly the conjecture, not a simplification.
anchor: code/lean/gilbreath_reduction.lean; code/out/lean_gilbreath_reduction.captured.txt
```

## New holdings this cycle (librarian, this build)

```claim
id: gilbreath-2011-expository
statement: Gilbreath's only substantive journal paper "Processing process: the Gilbreath conjecture" (J. Number Theory 131 (2011) 2436–2441) is autobiographical and expository, not a proof attempt. Its introduction (quoted verbatim in Houston 2012) records that Gilbreath developed the conjecture ~1958, and that "the great number theorist Erdős believed it was true, he also believed it would take about 200 years to prove".
hypotheses: the quotation in Kevin Houston's blog post (written after emailing Gilbreath, from an author offprint).
holds-here: yes — settles that no theorem about the {0,2} regime is to be found in the eponym's own paper.
status: sourced (Houston 2012 blog, full text on disk; original paywalled at ScienceDirect, PII S0022314X11001740)
bearing: history/context only; Erdős's "200 years" is now quotable from a held source. Not load-bearing for the mathematics.
anchor: research/sources/houston-2012-gilbreath-conjecture-blog.full.md
```

```claim
id: agama-trace-restatement
statement: (Agama 2021) In the trace/circuit language of the iterate-difference triangle of a finite originator, Gilbreath's conjecture is equivalent to: every leading entry A_k(0) > 0 and the partial sums of the leading entries satisfy Σ_{k≤m} A_k(0) = m for every m. Since each leading entry is a positive integer, "all A_k(0) = 1" ⟺ "partial sums = index".
hypotheses: primes as originator; parity gives each leading entry odd, hence ≥ 1.
holds-here: yes — exact restatement of GC, not a new theorem.
status: sourced (Agama 2021, arXiv:2104.05258, Prop 5.1–5.2; the paper proves no new theorem about the primes — the trace condition is the conjecture itself)
bearing: converts GC into a statement about an increasing quantity (partial sums) with slope 1, which is the shape an invariant argument could target; also a caution that "trace/reduction" frameworks can be pure restatement.
anchor: research/sources/agama-2021-gap-sequence-gilbreath.full.md
```

## New holdings this cycle (librarian, this build)

```claim
id: ross-2026-decay-constants
statement: (Ross, Zenodo 10.5281/zenodo.21326026, July 2026) In the CHT continuous Gilbert model (top row i.i.d. standard exponentials, c_i = E a(i,j)), exact sign-cone computations give c_4 = 778959731701/1447295850000 = 0.5382173463..., c_5 = 0.5532582996..., c_6 = 0.448388672133... (reduced fractions deposited, partition-of-unity certificates, reproduces CHT's c_2=7/9, c_3=227/288, Monte Carlo agreement at 2e8-5e8 samples). Monte Carlo to depth 8192 (768 pyramids): digit-sum law c_i ≈ C·λ^{s_2(i)}/i, λ≈1.14-1.20 drifting; conditioned on digit-sum class the decay is consistent with 1/i; pooled dyadic sawtooth with exponent ≈ −0.90…−0.86. Transient: full-row grind-down τ(G) ≍ G^β, β≈0.63-0.66; spike survival distance d*(G)/G→1 (observed 0.79,0.85,0.93,0.96,0.98,0.99). Author's open target: prove (14) c_i ≤ A·B^{s_2(i)}/i; and the light-cone distance d*(G)≈G+O(1).
hypotheses: continuous i.i.d. exponential model; the exact values are rational-certified, the laws are Monte Carlo (author explicitly: "identify theorem-shaped targets, not substitute for proofs").
holds-here: yes as a model statement — the digit-sum/Pascal structure is the same Rule-90/Sierpinski structure as the run's mod-4 linearization; the decay-rate question is the averaged shadow of the regeneration obstruction. It does NOT prove anything about the primes (author's close: "That remains a separate arithmetic problem").
status: sourced (full PDF landed in sources/ross-gilbreath-decay-constants-zenodo-2026.full.md; c_4 hand-checked to ~7 digits by this run; c_5, c_6 asserted-by-source with deposited certificates, not re-derived); empirical laws empirically-claimed only.
bearing: theorem-shaped targets for the inventor (digit-sensitive comparison (14); slope-one propagation); consistency constraint on any claimed regeneration mechanism; corroborates the Rule-90 microscope.
anchor: research/sources/ross-gilbreath-decay-constants-zenodo-2026.full.md; research/summaries/ross-gilbreath-decay-constants-zenodo-2026.md
```

## New holdings this cycle (librarian, this build)

```claim
id: granville-lucas-kummer-sierpinski
statement: (Granville, "Arithmetic properties of binomial coefficients", dynamic e-survey, chs. "Elementary Number Theory" + "Pascal's triangle via cellular automata") Kummer: the exponent of p in binom(n,m) equals the number of carries adding m and n−m base p (from Legendre's formula v_p(n!)=(n−s_p(n))/(p−1)); Lucas' theorem improves via Anton–Stickelberger–Hensel. Mod 2: Pascal's triangle is self-similar; rows 2^j are all 1s; row 2^j+r is two copies of row r with zeros between; Glaisher: row n has 2^{s_2(n)} odd entries; subtriangles of Pascal mod p obey the same addition law.
hypotheses: none beyond binomial-coefficient arithmetic in Z/p.
holds-here: yes — this is the primary reference for the run's Rule-90 interior dynamics (halved {0,2} entries evolve under XOR = Pascal mod 2) and for the 2^{s_2(i)} digit-sum statistic (Glaisher) that Ross 2026 finds modulating the decay constants.
status: sourced (Granville's own page; the original Fine 1947 AMM 54:589-592 proving the Lucas correspondence is paywalled — recorded unobtainable as clean PDF; Wikipedia/CHT agree).
bearing: anchors the Sierpinski kernel / binom(2^j,m)≡1 mod 2 fact used by the rule90-regeneration thread and the mod-4 linearization in a primary reference, not just Wikipedia.
anchor: research/sources/granville-binomial-cellular-automata.full.md; research/summaries/granville-binomial-lucas-elementary.md (the elementary chapter is carried in full by its summary — no separate .full.md exists for it)
```

## New holdings this cycle (librarian, this build) — short-interval prime theorem sharpened

```claim
id: li2023-short-interval-052
statement: (Runbo Li, arXiv:2308.04458 v8, Oct 2025) The interval [x − x^θ, x] contains at least one prime for every θ ≥ 0.52 and all sufficiently large x; equivalently the maximal prime gap satisfies G(x) ≤ x^0.52 ultimately. This sharpens Baker–Harman–Pintz 2001 (θ = 0.525) toward 0.52 and answers Harman–Pintz's argument. Theorem 2 gives nontrivial upper and lower bounds on the prime count in [x − x^θ, x] for 0.52 ≤ θ ≤ 0.525.
hypotheses: primes; unconditional short-interval analytic number theory (Harman's sieve, Watt's mean-value, explicit integral estimates).
holds-here: yes — the primes satisfy it; it is the demand side of Granville's ν_2 reduction (Route B).
status: asserted-by-source (arXiv v8, not peer-reviewed as downloaded; the α = 0.525 form is independently confirmed by the held Warwick Visser survey and BFT 2023); the 0.20-improvement claim verified against the paper's abstract and theorem statement.
bearing: WEAKENS GRANVILLE'S DEMAND SIDE. Theorem 5.5 reduces GC to ν_2 > n^β with β > α, where α is the short-interval exponent; the run's recorded α = 0.525 (BHP) can now be lowered to 0.52, so β > 0.52 (not β > 0.525) suffices. Since the measured ν_2/n ∈ [0.42, 0.52] is already far above n^0.52, the ν_2 route is a little more plausible than the BHP-based threshold suggested. Do not overstate: the 0.52→0.525 gap is small, and n^0.52 is still ≪ n/2.
anchor: research/sources/li-2023-primes-in-short-intervals-harman-sieve.full.md; research/summaries/li-2023-primes-in-short-intervals-harman-sieve.md
```

## Angled coverage summary

```claim
id: torelli-prime-gap-bound
statement: (Torelli 2006, Thm 2) For all n >= 1, p_{n+1} <= p_n + n — the n-th prime gap never exceeds the prime index. Equivalently every prefix of the primoids a_n = (p_{n+2} − 1)/2 is a sub-permutation: a_n <= a_{n−1} + ceil(n/2). Proved from Dusart's bounds (p_n >= n(ln n + ln ln n − 1); p_n <= n(ln n + ln ln n − 0.9484) for n >= 39017) plus a computer check of the small range.
hypotheses: none beyond the primes; Dusart's proven bounds.
holds-here: yes — the primes satisfy it identically; it is the strongest deterministic (non-heuristic) prime-gap bound in the library.
status: sourced (peer-reviewed RAIRO-ITA 40:107-121, 2006, doi 10.1051/ita:2006017, full PDF held)
bearing: bounds the width of the input feeding the {0,2} block: combined with the run's proved block lemma (length-N block protects N+1 rows), erosion can be bounded in terms of the prime index; Torelli also proves the Gilbreath and Goldbach iis classes are incomparable and notes GC is still open. Does not by itself give regeneration.
anchor: research/sources/torelli-2006-increasing-integer-sequences-goldbach-pdf.full.md
answers: is-there-a-proved-prime-gap-bound
```

- Statement/names/history: Odlyzko 1993, Killgrove–Ralston 1959, Encyc. of Math, MathWorld, Caldwell glossary, Arias de Reyna 2020, Chase 2024 §7, Wikipedia (retrieved this run).
- Verification record (current): Colonna 2026 to 1.5×10^15, Plouffe 2025 to 10^14, Odlyzko 1993 to 10^13.
- Generalisations: Li 2026 modulo-k family; Chase 2024 random analogue; CHT 2026 Cramér model; Croft's bounded-gap generalisation refuted by Eppstein 2011 (triple-sourced).
- Methods that worked/are current: Chase 2024 (random analogue, block lemmas), Chase–Hunter–Tao 2026 (Cramér model + inverse theorem + continuous model), Bhat–Cobeli–Zaharescu 2023 (quasi-periodicity of Proth–Gilbreath triangles; filtered rays 2023), Muney 2026 (valid-extension sets).
- Methods that fail/limits: Eppstein anti-Gilbreath (gap bounds alone insufficient); CHT Remark 4.5 (2^{n+1} growth breaks a.s. result); Chase 2024 exotic {0,3}-type examples (randomness necessary).
- Adjacent/computational: OEIS A000232/A036262/A100820/A397880/A395556, Odlyzko's G(N) table, Eppstein practical numbers (verified 212,000 rows).
- Counterexample constructions: Eppstein anti-Gilbreath; CHT §1.1 zero-block and {0,d}-block examples, Sierpinski-triangle {0,3} example.
- Ducci-sequence theory (NEW this cycle, four primary papers): Calkin–Stevens–Thomas 2005 (cyclic cycle-lengths via minimal polynomial (1+λ)^n+1 over Z2; Table 1 n≤40), Chamberland 2003 (Ciamberlini–Marengoni zero-iff-2^m; the factored-max + rigidity-classification proof template; Webb's no-uniform-bound), Glaser–Schöffl 1995 (basic Ducci sequence = Pascal mod 2; all-1s row at 2^r−1; 2^{s2(k)} ones), Avart 2011 (nilpotent over Z2 iff concatenation of power-of-2-length copies). Governing finding: ALL classical Ducci theorems are CYCLIC (wraparound |xn−x1|) and do not transfer their zero-convergence/cycle conclusions to the half-infinite Gilbreath triangle; the mod-2/Pascal local law (rule90-interior-xor) and the max-factoring template DO transfer. Claims: ducci-classical-nilpotence-iff-power-of-2, ducci-pascal-mod2-rule90, ducci-max-factoring-potential-template, ducci-avart-nilpotent-concatenation.

## New holdings this cycle (librarian, this build) — Gatti 2020 located flaws

This cycle obtained the full text of Gatti's 2020 Gilbreath-sequences preprint
(the earlier, downloadable form of the same machinery as the 403-blocked MDPI
2023 "Gilbreath polynomials" paper), via the Wayback Machine. It is the
independent primary form of the valid-extension machinery the run already
holds from Alkan 2023 and Muney 2026, and — more importantly — it is now
possible to check what that framework actually proves. Verdict: its Theorem 4
does not prove the prime case, and its Lemma 4 (interval completeness of the
valid-extension set) is false in general.

The claim blocks for `gatti-2020-theorem4-proof-invalid`,
`gatti-2020-lemma4-interval-completeness-refuted`,
`gatti-2020-valid-extension-global-formula`, and
`gatti-2020-parity-alternation-independent` live in the authoritative source
file `research/summaries/gatti-2020-preprints-gilbreath-conditions.md` (the
summary that digested the full text); the duplicates formerly here have been
collapsed to that single source. The earlier note in this file was the source's
own summary, not an independent claim — the deriver was emitting one row per
note per id, so any claim written up in both the summary and this ledger
appeared twice.

Also obtained this cycle: the missing full text of
`research/sources/caldwell-gilbreaths-conjecture-glossary.full.md` (Wayback
capture of t5k.org glossary; its claim block `caldwell-proth-myth-repeats`
stays — the glossary repeats the retracted Proth myth and cites the wrong
C.R. pages). MathWorld full text is carried by its summary file (the fetch
stored the text there; a re-download is refused as a duplicate). The Gatti
2020 preprint's parity-alternation lemmas (s_1 even ⟹ all later odd) are a
general-class statement independent of the primes — claim
`gatti-2020-parity-alternation-independent` lives in
`research/summaries/gatti-2020-preprints-gilbreath-conditions.md`.

## New holdings this cycle (librarian, this build) — Blair Morgan's frontier/local-condition notes, full texts landed

```claim
id: morgan-local-condition-sufficiency
statement: (B. Morgan, "Reducing Gilbreath's Conjecture to a Local Condition", Zenodo 10.5281/zenodo.19143644, March 2026) Gilbreath's Conjecture follows from Conjecture L: |G_r[2] − G_r[1]| ≤ 2 for all r ≥ 1. Proof: by the parity invariant G_r[1], G_r[2] are even for r ≥ 1, so Conjecture L forces G_{r+1}[1] = |G_r[2] − G_r[1]| ∈ {0, 2}; boundary stability |1 − {0,2}| = 1 then gives G_{r+1}[0] = 1; base G_1[0] = 1, G_1[1] = 2. The CONVERSE (Gilbreath ⇒ Conjecture L) is NOT claimed. The author verifies Conjecture L numerically through 100,000 rows (position 1 ∈ {0,2}: 49,737 zeros, 50,263 twos).
hypotheses: G_0 = primes; absolute-difference iteration; parity lemma (position ≥ 1 even for r ≥ 1).
holds-here: yes — Conjecture L is a strengthening of the run's proved reduction (A_k(1) ∈ {0,2}); the run's depth-1000 + literature data to 1.5×10^15 are consistent with it. The sufficiency proof is elementary and correct (it is the run's reduction with one extra position of slack).
status: asserted-by-source (working paper, not peer-reviewed; AI-collaborator credited; the sufficiency argument is reproduced in the full text and verified here as an elementary consequence of parity)
bearing: independently confirms the run's central reduction and names the precise strengthened target (|G_r[2] − G_r[1]| ≤ 2). The open part is identical to the run's: prove the local bound propagates. The author is upfront that "we ran out of compute" — no claimed proof of Conjecture L.
anchor: research/sources/blair-morgan-2026-local-condition-frontier.full.md; research/summaries/blair-morgan-2026-local-condition-frontier.md
```

```claim
id: morgan-frontier-basin-and-corridor-obstruction
statement: (B. Morgan, "The Return of the Lemma: Launchpads, corridor obstructions, and the shape of a counterexample", Zenodo 10.5281/zenodo.19144967, March 2026) (i) {0,2} is closed under |a−b|, so a position that enters {0,2} never leaves (basin/one-way membrane). (ii) If the frontier (leftmost position ≥ 1 not in {0,2}) stays at position ≥ 4 for all r ≥ 2 — equivalently G_r[3] ∈ {0,2} — then Gilbreath's Conjecture holds (induction via parity, closure, boundary stability, propagation of positions 1,2,3, and the initial conditions G_1[1]=2, G_1[2]=2, G_2[1]=0, G_2[2]=2, G_2[3]=2). (iii) PROVED OBSTRUCTION: no pure minimal erosion corridor 8 → 7 → 6 → 5 → 4 from the initial frontier-8 Row 2 is possible: such a corridor forces the launchpad prefix x_4 = x_5 = x_6 = x_7 = 0 (successive steps give y_7=|4−x_7|, z_6=|4−x_6|, u_5=|4−x_5|, v_4=|4−x_4| all outside {0,2} ⇒ all x_i = 0), whereas Row 2 has (x_4..x_7) = (2,2,2,2). Remaining routes: later frontier-8 rows, non-minimal breach (value ≥ 6 at position 4), or stalled/more complicated erosion.
hypotheses: frontier defined on the prime triangle; the corridor argument is purely local (a 4-row backward propagation on the launchpad prefix).
holds-here: yes — the frontier hypothesis G_r[3] ∈ {0,2} is exactly the run's block-length statement b_k ≥ 3 restricted to the front; the run's depth-1000 minima (13, 24, 96, ...) imply it far more strongly in the computed range. The corridor obstruction is a valid local computation (re-checkable in minutes with the run's oracle).
status: asserted-by-source (working paper, not peer-reviewed; the corridor argument is elementary and self-contained in the full text; the frontier hypothesis and its proof remain open)
bearing: (a) independent confirmation of the {0,2} basin framing (matches the run's closure-0d-double-edge and block lemma); (b) a worked example of the backward-forcing technique at frontier positions 4–7, the same technique the run's regeneration thread applies at the (edge=2, intruder=4) boundary; (c) the exact boundary arithmetic |4−2|=2, |6−4|=2, |6−2|=4, |6−0|=6 is the same table the run's depth-1000 data gives for the intruder values (all intruders ∈ {4,6,8,...} ≡ 0 or 2 mod 4). The honest gap is the same as the run's: prove the frontier / regeneration never fails.
anchor: research/sources/blair-morgan-2026-return-of-the-lemma.full.md; research/summaries/blair-morgan-2026-return-of-the-lemma.md
```

## New holdings this cycle (librarian, this build) — the Ducci-sequence literature

The two proposed approaches `ducci-potential-max-decrease` and
`p-adic-valuation-carry-dynamics` were grounded in their primary literature
this cycle: four peer-reviewed Ducci-sequence papers landed
(`research/sources/{calkin-stevens-thomas,chamberland,glaser-schoffl,avart}*`).
The finding that governs both approaches is the cyclic/non-cyclic boundary
below.

```claim
id: ducci-classical-nilpotence-iff-power-of-2
statement: (Ciamberlini–Marengoni 1937, quoted and reproved in Chamberland 2003 Thm 1.1, Calkin–Stevens–Thomas 2005, Glaser–Schöffl 1995) For the CYCLIC Ducci map D(x1,..,xn) = (|x1−x2|, ..., |xn−x1|) on integer n-tuples, every start iterates to the zero-tuple in finitely many steps iff n is a power of 2. For n ≠ 2^m every start converges to a (nonzero) cycle; the period structure is governed by the minimal polynomial (1+λ)^n + 1 over Z2 (Calkin–Stevens–Thomas Thm 2.1/Cor 2.2, Table 1: cycle lengths for n ≤ 40).
hypotheses: cyclic tuples (wraparound |xn−x1|); integer entries; finite length n.
holds-here: NO — the Gilbreath triangle is the half-infinite NON-cyclic iteration (no wraparound, each row one entry shorter). The mod-2/Pascal local law transfers (see ducci-pascal-mod2-rule90), but the nilpotence/cycle-length conclusions are cyclic-object theorems and must NOT be imported. Eppstein 2011 is the standing proof that the half-infinite object behaves differently (right edge escapes).
status: sourced (four primary peer-reviewed papers, all held)
bearing: kills any argument that "Ducci ⇒ the {0,2} regime converges to zero" in the Gilbreath triangle; the power-of-2 phenomenon is a cyclic fact. The run's Rule-90 interior is the transferred part; the half-infinite regeneration is not covered.
anchor: research/sources/chamberland-unbounded-ducci-sequences.full.md (Thm 1.1); research/sources/calkin-stevens-thomas-ducci-cycles-characterization.full.md (Thm 2.1, Cor 2.2, Table 1)
```

```claim
id: ducci-pascal-mod2-rule90
statement: (Glaser–Schöffl 1995, Thm 1; Avart 2011; Calkin–Stevens–Thomas 2005 §2) The cyclic Ducci map over Z2 is linear, D = (I + shift), D^n(x) = Σ_i C(n,i)·shift^i(x) (Pascal's triangle mod 2 = Rule 90). The n rows of the mod-2 Pascal triangle (padded to n-tuples) are the first n iterates of the basic Ducci sequence from (0,...,0,1). Binomial-parity facts: row 2^r − 1 is all 1s; row 2^r has all-interior 0s; row k has 2^{s2(k)} ones (Glaisher).
hypotheses: cyclic tuples over Z2; |a−b| ≡ a+b (mod 2).
holds-here: YES — this is exactly the run's proved rule90-interior-xor (halved {0,2} entries evolve by XOR = Pascal mod 2), now anchored in four primary Ducci sources rather than Wikipedia/CHT remark alone. The kernel facts (binom(2^r,m) ≡ 0 mod 2; all-1s row at 2^r − 1) are what the rule90-regeneration thread uses to predict all-2 stretches at depths 2^j−1.
status: sourced (peer-reviewed primary); the local transfer to the half-infinite {0,2} interior is the run's own proved statement rule90-interior-xor
bearing: strengthens the Rule-90 microscope; confirms the digit-sum statistic 2^{s2(k)} (Glaisher) that Ross 2026 finds modulating the continuous decay constants.
anchor: research/sources/glaser-schoffl-ducci-sequences-pascal-triangle.full.md (Thm 1, properties (5)-(7)); research/sources/avart-converging-ducci-sequences-z2.full.md (Prop 2.1 identity); research/sources/calkin-stevens-thomas-ducci-cycles-characterization.full.md (§2)
```

```claim
id: ducci-max-factoring-potential-template
statement: (Chamberland 2003, Thm 3.2 proof) The standard Ducci convergence engine is the pair: (i) the maximum of a string at most doubles in two iterations and a power of two can be factored out, after which the factored maximum strictly decreases in every non-borderline case; (ii) the borderline cases where the maximum does not decrease are exactly rigid strings (0,b,d,d), (0,0,c,d), (a,0,c,2a), (a,a,c,c), (a,b,a,b), which then iterate to zero directly. Also (Webb, quoted): in the convergent power-of-2 case there is NO uniform bound on iteration count (Tribonacci construction: 4-strings can take arbitrarily long to reach zero).
hypotheses: cyclic strings; the (−1,2,−1) weighting in the paper's proof, but the max-factoring template is the standard (1,−1) technique.
holds-here: the TEMPLATE transfers to any absolute-difference iteration (it is pointwise: |a−b| ≤ max(a,b) with equality only against 0); the rigidity classification is finite-configuration and could be re-derived for the run's windows; the no-uniform-bound fact is the cyclic analogue of the run's "no uniform regeneration time" stance.
status: sourced (peer-reviewed primary); the template's transfer to half-infinite windows is this run's deduction, not in the paper
bearing: gives the ducci-potential-max-decrease approach its exact precedent (the factored-max + rigidity-equality-case proof shape) and its caution (bounded absorption time is false; only a potential/monotone argument can work).
anchor: research/sources/chamberland-unbounded-ducci-sequences.full.md (Thm 3.2, Lemma 3.1, Webb quote)
```

```claim
id: ducci-avart-nilpotent-concatenation
statement: (Avart 2011, Thm 4.1) Over Z2, a vector is nilpotent under the cyclic Ducci map iff it is the concatenation of several copies of a vector of length a power of 2. Proof: T^{2^ℓ}(x) = x + shift^{2^ℓ}(x), so nilpotence forces 2^ℓ-periodicity, which with gcd(k, 2^ℓ mod k) divising 2^ℓ forces the concatenation form. Necessary condition for integer vectors: nilpotence implies the mod-2 reduction is a concatenation of power-of-2-length copies.
hypotheses: cyclic vectors over Z2.
holds-here: NO (cyclic theorem; half-infinite Gilbreath rows are not cyclic vectors). The mod-2 identity T^n = Σ C(n,i) shift^i is the shared local law with the run's rule90-interior-xor; the concatenation characterization is a cyclic convergence fact.
status: sourced (peer-reviewed primary)
bearing: another precise statement of where the cyclic theory ends and the half-infinite Gilbreath object begins; the mod-2 identity gives an independent check of the run's Rule-90 apex computation for cyclic truncations.
anchor: research/sources/avart-converging-ducci-sequences-z2.full.md (Thm 4.1, Prop 2.1)
```