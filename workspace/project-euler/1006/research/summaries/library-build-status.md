# Library build status — PE1006 reference library

## This cycle (librarian) — NextFib check + four structural anchors (memory down)

Cognee remains unhealthy; durable record on disk (cycle note
`research/notes/library-build-cycle-nextfib-standard-factors`, claims
`research/notes/sourced-claims-least-periods-standard-factors.md`).

**NextFib strictness — checked, NOT a trap.** The operator flagged a live trap
for `code/lib/fibword.py`: NextFib must be the least Fibonacci STRICTLY greater
than k. Checked: `next_fib(k)` uses `bisect_right` over `fibs_upto(k+1)`
(F_2=1,F_3=2,…) → least Fibonacci strictly greater than k; `lmin_formula =
k + next_fib(k) − 1`. Cross-checked against `code/out/Lmin-formula-verified-6764.md`
(three independent exact programs, k=1..6764, all Fibonacci boundaries). The
trap is already avoided on disk.

**Four sources added** (finite/standard-word+period side — the thinnest axis):

1. **Currie & Saari, "Least periods of factors of infinite words"** (RAIRO-ITA
   43 (2009) 165–178, DOI 10.1051/ita:2008006), Numdam.
   `research/sources/currie-saari-least-periods-factors.full.md`. Cor 4: least
   period of any Fibonacci-word factor is a Fibonacci number — primary anchor
   replacing Wikipedia; Cor 6 (factor of a Sturmian word iff its fractional
   root is a conjugate of a standard word).
2. **Richomme, Saari & Zamboni, "Standard factors of Sturmian words"**
   (RAIRO-ITA 44 (2010) 159–174, DOI 10.1051/ita/2010011), Numdam.
   `research/sources/richomme-saari-zamboni-standard-factors-sturmian.full.md`.
   Lemma 2.1 (L0/L1 monoid = standard words); Theorem 3.1 + Example 3.3
   (standard factors of the Fibonacci word = {φⁿ(1), φⁿ(10), φⁿ(101),
   φⁿ(0010010)}); slope α=(3−√5)/2 confirmed a third source.
3. **Fici, "Factorizations of the Fibonacci infinite word"** (J. Integer Seq.
   18 (2015) 15.9.3, arXiv:1508.06754), ar5iv.
   `research/sources/fici-factorizations-fibonacci-infinite-word-ar5iv.full.md`.
   f(n) = rightmost (parity) bit of Zeckendorf representation of n; f_n =
   f_{n−1}f_{n−2} = the S_n recurrence; central-word equations.
4. **Du, Mousavi, Schaeffer & Shallit, "Decision algorithms for
   Fibonacci-automatic words"** (arXiv:1406.0670), ar5iv.
   `research/sources/mousavi-schaeffer-shallit-fibonacci-automatic-ar5iv.full.md`.
   Decision procedure via Fibonacci/Zeckendorf representation + 2-state DFAO +
   17-state addition automaton; Theorems 12/13 (palindromes, Chuan/Droubay),
   18 (unique right-special factor = reverse of prefix), 19 (Saari least-period,
   mechanized), 20 (smallest-period Lucas bound), 30–34 (finite Fibonacci
   words: almost-commutative, squares are conjugates of finite Fibonacci words,
   primitivity, two-palindrome factorisation, borders).

**Claims added** (all anchored, asserted): `fibonacci-least-period-set`,
`fibonacci-standard-factors-l0l1`, `fibonacci-zeckendorf-parity-characterization`,
`fibonacci-unique-special-factor-reverse`, `fibonacci-squares-conjugate-finite-word`.

**Still not obtained** (recorded): Chuan & Ho "Locating factors..." (TCS 2005,
paywalled; covered by Sivasankar–Rama Thm 7 + OEIS A003849 corpus); Chuan
"Moments of conjugacy classes" (TCS 2003, paywalled; conjugate side anchored by
Currie–Saari Cor 6 + Bugeaud–Reutenauer); Berthé "Autour du système de
numération d'Ostrowski" (2001, paywalled; covered by Hieronymi–Terry +
Berthé–Imbert + Barat et al).

## What the library holds, why each source is there, and where it lives. The Cognee
memory server was down for the whole of the earlier cycle and remained so during
this cycle (every `remember_memory` and every download's memory-vectorisation
call fails with a server-health timeout), so durable findings are recorded here
on disk until memory recovers.

**This cycle (librarian):** the four open requests (`citable-statement-theorem-039a`,
`citable-name-treatment-0c91`, `citable-precise-statement-600d`,
`citable-precise-statement-d2e7`) were closed by claim notes
`research/summaries/claim-fibonacci-sturmian-complexity.md`,
`research/summaries/claim-universal-euclidean-geometric-floor-sum.md`,
`research/summaries/requests-closed-recap.md` (each carries the `answers:` line).
Three sources were added on disk so every claim anchor resolves to a real file:
`atcoder-math-hpp-v151.full.md`, `atcoder-internal-math-hpp.full.md` (the O(log)
`floor_sum_unsigned` recursion + modular inverse base), and
`hal-05026908-fibonacci-word-complexity-survey.full.md` (Sturmian p(n)=n+1,
density 1/phi^2, balance bound). New claim `fibonacci-word-sturmian-density-balance`
anchors the density/balance facts. The CLAIMS ledger is populated; every
`research/sources/*.full.md` anchor in the notes exists on disk.

## The governing theory (established, sourced)

PE1006 is a problem about the distinct length-k factors (subwords) of the
Fibonacci word. The Fibonacci word is the canonical **characteristic Sturmian
word**; its factor complexity is exactly `k+1` for every length `k` (minimal
complexity, Morse–Hedlund). The `k+1` distinct factors are exactly the problem's
`k+1` Fibonacci subwords.

The magnitude of the result the run is chasing: `Psi(10^18) mod 101001001`,
i.e. the sum of squares of ~`10^18+1` distinct length-`10^18` subwords read as
decimal numbers, taken modulo `M = 101001001`. The governing reduction
(directives 1 & 2) turns this into a **geometrically weighted floor sum** over
`k+1` mechanical-word representatives, evaluated by the **universal Euclidean
algorithm** (monoid generalisation of AtCoder `floor_sum`, aka Chtholly's
algorithm) in `O(log)` — not by enumerating the billion-trillion factors.

## Sources on disk (research/sources/)

All were found via `exa_search` (verified URLs) then downloaded; each carries its
source URL. Full texts: `*.full.md`. Digests first: `research/summaries/*.md`.

1. **arXiv:2204.13977, Sivasankar & Rama — "Two-dimensional Fibonacci words:
   Tandem repeats and factor complexity"** (`fibonacci-word-2d-factor-complexity-ar5iv.full.md`,
   full text from ar5iv). **The position theorem.** Theorem 7: for
   `F(n) <= k < F(n+1)`, the k+1 distinct length-k factors `z_j^(k)` of the
   infinite Fibonacci word f are
   `z_j = f[j+1..j+k]` for `0<=j<=F(n)-1`, else `f[j+F(n+1)-k..+k]` for
   `F(n)<=j<=k`, listed in first-occurrence order. Theorem 8: factor complexity
   of the finite word `f_n` is piecewise `k+1`, `F(n-2)+2`, `F(n)+1-k`. This is
   the structural description the solver builds on.
2. **Wikipedia — Fibonacci word** (`wikipedia-fibonacci-word.full.md`). Canonical
   characterisation: Sturmian, complexity `C(n)=n+1`, lying on a line of slope
   `1/phi` / `phi-1`, digits `2+floor(n*phi)-floor((n+1)*phi)`.
3. **Perrin — Sturmian words, Lecture 2 (mechanical words)** 
   (`perrin-sturmian-words-lecture2-mechanical.full.md`). Defines the lower
   mechanical word `s_a,rho(n) = floor(a(n+1)+rho) - floor(a n + rho)` — the
   exact digit formula directive 2 uses — plus rotations, balance, and the
   interval/factor correspondence.
4. **Wikipedia — Sturmian word** (`wikipedia-sturmian-word.full.md`).
   Encyclopedic tier; factor complexity, mechanical words, balance equivalence.
5. **OEIS A003849** (`oeis-a003849-fibonacci-word.full.md`). The infinite
   Fibonacci word's sequence record; the canonical digit sequence reference.
6. **Berstel — Recent results in Sturmian words (DLT'95)**
   (`berstel-recent-results-sturmian-words-dlt95.full.md`). The standard survey;
   definitions, continued-fraction construction, standard words, Lyndon and
   Baldwin results.
7. **Berstel — Sturmian and Episturmian words, survey 2007**
   (`berstel-sturmian-episturmian-survey-2007.full.md`). 14 characterisations of
   central words; standard/episturmian structure.
8. **OI Wiki — Euclidean algorithm / universal Euclidean (万能欧几里得)**
   (`oi-wiki-universal-euclidean-floor-sum.full.md`). The magnitude-essential
   primitive reference: the monoid model, U/R operations, the merge-and-flip
   recursion `F(a,b,c,n,U,R) = R^... U F(c,..,a,..,R,U) R^...` in O(log), and
   the floor / i·floor / floor² component monoid `(x,y,sy,sxy,sy2)`.
9. **fhq_treap — 万能欧几里得 (universal Euclidean) study note**
   (`universal-euclidean-geometric-weight-fhq.full.md`). Explicitly covers the
   `sum f(x) a^x g(y) b^y` form — the geometric-weight floor sum directive 2
   requires — with a 6-component monoid
   `(cntu,cntr,sumi,sums,sqrs,prod)`, its combination rule, the merge/flip
   recursion, and an O(log) implementation. **This answers the open request**
   `citable-precise-statement-600d` / `citable-precise-statement-d2e7`.
10. **LOJ138 — universal Euclidean (floor moments)**
    (`loj138-universal-euclidean-floor-moments.full.md`). Covers
    `sum floor((px+r)/q)^k1 x^k2`, the moment-array Node monoid with
    combination via binomial expansion — the generalisation that includes both
    x^i and floor^i weights.
11. **AtCoder Library math doc** (`summaries/atcoder-math-floor_sum-doc.md`).
    Official `floor_sum` spec (O(log)).
12. **AtCoder Library math.hpp v1.5.1** (`atcoder-math-hpp-v151.full.md`).
    Verbatim official header source (pow_mod, inv_mod, crt, floor_sum) from the
    jsDelivr CDN; anchors the base floor_sum primitive.
13. **AtCoder Library internal_math.hpp v1.5.1** (`atcoder-internal-math-hpp.full.md`).
    The O(log) `floor_sum_unsigned` Euclidean recursion that `floor_sum` delegates
    to, plus `safe_mod` and `inv_gcd` — the modular-inverse base for x = 10^-1 mod M.
14. **Hamoud & Abdullah 2025, HAL hal-05026908** (`hal-05026908-fibonacci-word-complexity-survey.full.md`).
    Survey of Fibonacci-word complexity: Sturmian p(n)=n+1, uniform density of
    1's = 1/phi^2, balance bound |#1s/n − 1/phi^2| ≤ 1/n. Claim
    `fibonacci-word-sturmian-density-balance`.

## OEIS lookup result (finding)

`Psi(1..5) = 1, 101, 20302, 2042402, 204252402` returned **no OEIS match**. The
sequence of Psi values is not catalogued; no closed form will be looked up — the
structure must come from Sturmian/universal-Euclidean theory. (If these terms
are wrong the brute oracle will correct them; they are the stated-check basis
only.)

## The open request is answerable from the library

`requests` holds the gap "citable, precise statement of the generalised
floor_sum / universal Euclidean algorithm". Sources 8, 9, 10, 11 now supply it.
A claim block recorded against `citable-precise-statement-600d` should cite
sources 9 and 8.

## Additional sources added this cycle (librarian)

- **AtCoder Library `math.hpp` source** (`summaries/atcoder-math-hpp-v151.md`,
  https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/math.hpp). The
  verbatim `floor_sum` / `pow_mod` / `inv_mod` / `crt` implementation — the
  concrete O(log) primitive the solver adapts into the weighted monoid form.
- **Bugeaud & Laurent — "Combinatorial structure of Sturmian words and continued
  fraction expansions of Sturmian numbers"** (hal.science/hal-03571109). Sturmian
  words as rotation codings; lower/upper mechanical words `s_{theta,rho}`;
  standard-word / convergent recursion (V_{k+1} = V_k^{a_{k+1}} V_{k-1}). Confirms
  the continued-fraction/arc structure behind directive 2.
- **OEIS A003849 factor corpus** (`oeis-A003849-first-1652-subwords.full.md`,
  https://oeis.org/A003849/a003849.txt). The full list of the first 1652 distinct
  factors with leading zeros; independent authority for the factor set. Its
  length-3 block (001, 010, 100, 101) matches the problem's stated oracle exactly.
- **MathWorld — Rabbit sequence** (`mathworld-rabbit-sequence.md`). Encyclopedic
  tier for the Fibonacci word / rabbit sequence.

## What could not be obtained

- Berstel's original *Fibonacci words — a survey* (The Book of L) PDF: the
  `www-igm.univ-mlv.fr/~berstel/Articles/1985BookOfL.pdf` host refused the
  transfer (connection error) again this cycle; no legitimate free mirror is
  hosted. Non-blocking: the DLT'95 Sturmian survey (source 6), the 2007
  Berstel survey (source 7), and the Lothaire C2 chapter (on disk) cover the
  definitions, factor complexity, standard words, and balance the survey would
  provide. The frontier row for `1985BookOfL.pdf` is a lead, not a gap.
- maspypy's `floor_monoid_product.hpp` raw file: GitHub returned 503/429 twice.
  The same algorithm is fully covered by sources 8 and 9 (already on disk),
  so this is not a blocking gap.
- The Lothaire ACW chapter 2 (Sturmian Words) `C2.ps` came down as raw
  PostScript without a readable text layer; its content is mirrored by the
  Perrin–Restivo note (Theorem 1, mechanical-word definition) and the
  Berstel DLT'95 survey (source 6).
- AtCoder `math.hpp` from raw.githubusercontent.com was rate-limited (429);
  the jsdelivr `@v1.5.1` tag mirror succeeded instead.

## This librarian cycle — additions

The memory/Cognee server is down again this cycle (every `remember_memory` and
`describe_file`/`refresh_index` on `research/` fails with a server-health
timeout), so the durable record is this file on disk. Recorded here so the
findings survive when memory recovers.

Three sources added on disk, all from URLs seen in search results:

1. **Morse–Hedlund theorem** — MathWorld encyclopedia statement.
   `research/summaries/mathworld-morse-hedlund-theorem.md` (small; that file IS
   the full document). The primary authority behind the "k+1 distinct length-k
   factors" claim: an aperiodic infinite word has p_w(n) >= n+1 for all n, and
   Sturmian words are exactly the sharp case p_w(n) = n+1. Original: Morse &
   Hedlund, "Symbolic Dynamics II. Sturmian Trajectories", Amer. J. Math. 62
   (1940) 1-42, DOI 10.2307/2371441 (paywalled; the encyclopedic statement is
   what is held).
2. **Sturmian sequence** — MathWorld encyclopedia entry.
   `research/summaries/mathworld-sturmian-sequence.md` (also the full doc).
   Reproduces the 0->01, 1->0 substitution and the 01001010... word that is
   PE1006's S_n limit — the object's encyclopedic definition.
3. **Hieronymi et al., "Decidability of the FO theory of Sturmian words"**
   (arXiv:2102.08207; LMCS 20(3:12), 2024).
   Full text `research/sources/hieronymi-decidability-sturmian-words-ar5iv.full.md`;
   summary `research/summaries/hieronymi-decidability-sturmian-words-ar5iv.md`.
   Decidability via Ostrowski-numeration adders + Pecan. Anchors the Ostrowski
   representation behind directive 1's lag-sum recursion; adjacent computational
   angle (not the solving method) on Sturmian-word structure.

The two confirmed primary sources remain paywalled: Morse–Hedlund 1940
(Amer. J. Math., DOI 10.2307/2371441) and Coven–Hedlund 1973 (Math. Systems
   Theory 7, DOI 10.1007/BF01762232). Both confirmed real via search (MathSciNet,
   MaRDI, felix.unife.it directory) but no free full text is hosted; the
   MathWorld entries above supply the encyclopedic statements, and Berstel's
   DLT'95 / 2007 surveys and the Lothaire C2 chapter (on disk) carry the proofs.
   - Berstel's 1986 "Fibonacci Words — A Survey" (The Book of L) remains
     paywalled; covered by the DLT'95 and 2007 Berstel surveys on disk.

## Scholar digest cycle — completed

All `research/sources/*.full.md` in the library have been read in full and
every `research/summaries/*.md` replaced with a precise statement-level note
(no `Digest only` / `Filed by ... not read` templates remain). Details and the
open solver items are in `research/notes/scholar-digest-complete.md` and
`research/notes/durable-findings-pe1006.md`.

Key outcomes of the digest:
- **Slope correction confirmed from two primary sources**: the problem's word
  is characteristic Sturmian of slope 1/phi^2 (Perrin–Restivo "slope
  2/(3+sqrt5)"; Berstel DLT'95 "slope 1/tau^2"); the directive's literal slope
  F(n-1)/F(n) ~ 0.618 is the complement convention and fails at k=3. Recorded
  in the claims ledger (`steer-d2-literal-slope` contradicts
  `mechanical-word-digit-rule`).
- The slope-corrected mechanical-word construction was already verified at
  k=1..100 (exact rational arithmetic, prior-cycle note
  `research/notes/mechanical-slope-correction.md`) — recorded in the claim.
- The four research requests are closed on disk (`requests-closed-recap.md` +
  `answers:` lines in the governing claims), though the rendered requests
  ledger still lists them (tooling caveat noted in scholar-digest-complete.md).
- Sources assessed and classified as not helpful (or duplicate/metadata) with
  reasons: Hieronymi decidability (tier-3), MathWorld rabbit, A344953,
  citation graphs, tutorial, atcoder internal header (base-case only),
  Bugeaud–Reutenauer DMTCS/arXiv landing pages.
- Memory server: still down this cycle (3rd consecutive); durable findings are
  on disk and should be relaunched into Cognee when the server recovers.

## Next steps for the solver (not the librarian)

1. `code/brute.py`: naive Psi enumeration, must hit Psi(3)=20302 and
   Psi(10) mod M = 10699667.
2. Reproduce directive 2's mechanical-word/floor-sum construction vs brute on
   k=1..150, then Psi(10), then k=10^18.
3. Verify final answer by a second route (directive 1's autocorrelation form).

---

## Librarian cycle — three-distance / factor-frequency / floor-sum-derivation side

**Memory server**: still down (nth consecutive cycle); all durable notes are on
disk. Recall of "PE1006 / three distance / universal euclidean" is empty.

**Six sources added this cycle**, all from URLs seen in search results or
citation graphs (none invented), all carrying their source URL:

1. **Alessandri & Berthé, "Three distance theorems and combinatorics on words"**
   (Enseign. Math. 44, 1998) —
   `research/sources/alessandri-berthe-three-distance-theorems.full.md`,
   summary `research/summaries/alessandri-berthe-three-distance-theorems.md`.
   Survey + new results: three-distance theorem (≤ 3 interval lengths, one the
   sum of the other two), its dual three-gap theorem, and the equivalence with
   "frequencies of factors of a given length of a Sturmian sequence take at
   most 3 values" (Theorem 8). Lemma 3 gives the frequency = interval-length
   bridge used by directive 2's arc construction. 85 citations.
2. **Berthé & Reutenauer, "On the Three-Distance Theorem"** (Math.
   Intelligencer 46, 2024) —
   `research/sources/berthe-reutenauer-three-distance-intelligencer-2024.full.md`.
   Recent primary source: Theorem 1 (leftmost interval not the longest,
   distance-encoding word = word encoding of a circular symmetric discrete
   interval exchange), Theorem 3 (perfectly clustering Lyndon words), full
   history (Sós/Surányi/Świerczkowski 1958, Slater, Halton).
3. **van Ravenstein, "The Three Gap Theorem (Steinhaus Conjecture)"** (J.
   Austral. Math. Soc. A 45, 1988), HAL copy —
   `research/sources/van-ravenstein-three-gap-theorem-1988-hal.full.md`.
   Constructive proof: identifies first(N), last(N) and proves the gap
   structure recurs by the continued fraction of α — the reason the lag-sums
   in directive 1 collapse to a three-term count. (OEIS mirror had no text
   layer; anaphoria mirror converted too large; HAL succeeded.)
4. **Berthé, "Fréquences des facteurs des suites sturmiennes"** (TCS 165,
   1996) — `research/sources/berthe-frequences-facteurs-sturmiennes-1996.full.md`.
   Primary source for the ≤ 3-factor-frequencies theorem and **Dekking's
   Fibonacci case** (three frequencies per length, explicit via golden-ratio
   continued fraction), and **Proposition 3**: G_m = D_m iff m = q1+q2−2 —
   the exact Farey-stabilisation threshold for the length-m special factors,
   the quantitative version of "denominator > k is enough".
5. **OI Wiki (English), "Euclidean-like algorithm"** —
   `research/sources/oi-wiki-euclidean-like-algorithm-en.full.md`.
   First English-language treatment in the library of the f/g/h mutually
   recursive second-moment floor sum (f=Σ⌊⌋, g=Σi⌊⌋, h=Σ⌊⌋²) in O(log), with
   the mod-step and flip-step recursions and a complete C++ implementation
   (`struct {f,g,h}`). Closes the "English treatment missing" gap; anchors the
   arithmetic the weighted monoid generalises.
6. **Brown, "Sums of powers of the floor function and generalized Dedekind
   sums"** (NNTDM 32:1, 2026; arXiv 2507.11666) —
   `research/sources/brown-floor-power-sums-dedekind-2026.full.md`.
   Closed forms for S_2 = Σ⌊km/n⌋², S_3 and their reciprocity laws, gcd-
   stripping rule (Prop 3.2), and connection to generalized Dedekind sums via
   the Euclidean algorithm — the unweighted (x=1) sanity baseline for the
   second-moment floor sum.

**Claims added** (`research/notes/three-distance-frequency-structure.md`):
`rotation-arc-factor-frequencies` (three-distance/gap structure, ≤ 3 values,
anchored to all four rotation sources), `farey-slope-stabilisation` (G_m = D_m
iff m = q1+q2−2, Berthé Prop 3 verbatim), `distance-encoding-word-structure`
(Berthé–Reutenauer Thm 1, 3), `dir1-domain-autocorrelation` (steer directive's
scope statement: the cyclic-autocorrelation identity holds only at k = F_n − 1;
general-k replacement is the arc-intersection count; recorded with provenance,
reproduction is a solver task).

**The previously-documented gap** — "directive 1's A(d) closed form appears in
no single paper; no literature source found" — is now half-closed: the theory
the formula rests on (three-distance/gap bookkeeping, distance-encoding words,
Farey-stabilised factor sets) is on disk from four primary sources. The exact
closed form A(d)=max(0,m−t)+max(0,m−(N−t)) remains a verify-in-container
counting identity (task `reproduce-dir1`), not something any paper states
verbatim.

**Open items still missing** (recorded so nobody re-searches):
- Berstel, "Fibonacci Words — A Survey" (The Book of L) — paywalled/unreachable
  every cycle; covered by the on-disk Berstel DLT'95 and 2007 surveys,
  Berstel–Karhumäki tutorial, and Lothaire C2 chapter.
- A single English-language primary paper stating the *geometric-weight* (x^i)
  universal-Euclidean monoid recursion; held sources for it are the Chinese OI
  Wiki (`oi-wiki-universal-euclidean-floor-sum.full.md`) and the Chinese fhq
  note (`universal-euclidean-geometric-weight-fhq.full.md`), now supplemented
  by the English Euclidean-like f/g/h page — the weighted generalisation is
  still best anchored by the Chinese sources. Non-blocking.

**Frontier**: 145 submissions added this cycle (from the four rotation sources
+ English OI Wiki). Top relevant rows: the Berthé 1996 paper (now held),
Cassaigne's "Complexité et facteurs spéciaux" and "Special Factors of
Sequences with Linear Subword Complexity" (both ≤ 3-frequency/special-factor
theory), Rauzy "Suites à termes dans un alphabet fini", Rote "Sequences With
Subword Complexity 2n", and van Ravenstein (now held).

## This librarian cycle — characteristic/standard-word + special-factor side strengthened

Memory/Cognee still down (server-health timeout on every download and
remember/describe call); durable record stays on disk here and in the per-source
summaries. All four research requests carry `answers:` closures in
`requests-closed-recap.md` (the rendered requests ledger not re-deriving is a
known tooling caveat, not an open gap). OEIS lookup already done with seven
oracle terms and recorded "not to be re-run" — not retried.

**Three sources added this cycle**, all from URLs seen in search results /
frontier rows (none invented):

1. **Cassaigne, "Complexité et facteurs spéciaux"** (Bull. Belg. Math. Soc. 4,
   1997) — `research/sources/cassaigne-complexite-facteurs-speciaux-1997.full.md`
   (from the EMIS open journal mirror), digest+claim
   `research/summaries/cassaigne-complexite-facteurs-speciaux-1997.md`. The
   primary *tool* reference for factor counting: **the first difference of
   factor complexity equals the number of right-special factors**,
   `p(n+1) − p(n) = #{right-special length-n factors}`; the Fibonacci word is
   its running example. Claim `special-factor-complexity-difference`. This is
   the counting machinery behind the k+1 factor count and the "one expansive
   factor" structure of the mechanical construction.
2. **Brown, "Descriptions of the Characteristic Sequence of an Irrational"**
   (Canad. Math. Bull. 36, 1993, DOI 10.4153/CMB-1993-003-6) —
   `research/sources/cmb-1993-descriptions-characteristic-sequence.full.md`,
   digest+claim `research/summaries/cmb-1993-descriptions-characteristic-sequence.md`.
   Primary anchor for the *definition* of the characteristic sequence
   `f_n = [(n+1)α] − [nα]` and for its literature history (Christoffel 1875,
   Markoff 1882, Morse–Hedlund 1940, Ostrowski 1922, Fraenkel–Levitt–Shimshoni
   1972, Ito–Yasutomi 1990, Shallit 1991). Claim
   `characteristic-sequence-floor-difference-def`. **Honest limitation:** only
   the abstract/references cited-by converted (body paywalled at CUP); the
   load-bearing definition is in the abstract and independently covered by the
   open Perrin/Berstel/Richomme sources.
3. **Świerczkowski, "On successive settings of an arc on the circumference of a
   circle"** (Fund. Math. 46, 1958, 187–189) — bibliographic + CC-BY download
   link (metadata only; scanned PDF with no text layer). This is the original
   three-distance paper; its 1958 issue record is on disk
   (`research/summaries/sos-suranyi-swierczkowski-three-distance-1958.md`)
   confirming the publication, but the scanned full text has no extractable
   text layer. The three-distance theorem it contains is already fully covered
   by the open Alessandri–Berthé, Berthé–Reutenauer, and van Ravenstein
   sources on disk (with proofs), so this is a metadata/primary-history anchor,
   non-blocking.

**Confirmed unobtainable this cycle (concrete reasons, so nobody re-searches):**
- **Berstel, "Fibonacci Words — A Survey" (The Book of L, 1986)**: the author
  page `www-igm.univ-mlv.fr/~berstel/Articles/1985BookOfL.pdf` serves a **scanned
  PDF with no text layer** (download attempted; conversion failed on exactly that
  ground). Springer version is paywalled. Covered by the on-disk Berstel DLT'95
  and 2007 surveys, Berstel–Karhumäki tutorial, and Lothaire C2 chapter.
- **Cassaigne, "Special factors of sequences with linear subword complexity"
  (DLT'95, Word Scientific)**: author host `iml.univ-mrs.fr/~cassaign/publis/
  ferenczi.pdf` refused the connection twice (http and https), as did a
  CiteSeerX mirror. The French 1997 Bull. Belg. Math. Soc. version of the same
  special-factor tool is on disk; the DLT'95 paper's extra content (linear =>
  bounded first difference, the Ferenczi-conjecture proof) is not needed for
  this run (factor count k+1 already sourced from Morse–Hedlund/Sturmian
  theory). Non-blocking.
- **English/French primary source for the r^i geometric-weight floor-sum
  monoid**: a focused deep-research sweep (plus two web searches) confirmed
  **no peer-reviewed / arXiv English/French paper states the exact
  (count, Σr^i, Σr^i·floor, Σr^i·floor²) monoid recursion** for
  S = Σ r^i floor((ai+b)/c). The closest formal treatments (Dedekind-sum papers:
  Brown 2026, Tranbarger–Wang arXiv:2210.01172, Gunnells–Sczech) use polynomial
  index weights or unweighted floor powers, not the geometric r^i monoid. So the
  run's geometric-weight primitive is **not derivable from a named primary
  source** — it is anchored operationally to the Chinese OI Wiki / fhq / LOJ138 /
  AtCoder sources on disk, and its correctness is a verify-in-container task
  (solver's acceptance tests 1–5 against brute). Recorded so nobody re-hunts.

**Frontier from this cycle's downloads:** the CMB 1993 paper's 98-citation list
and the Świerczkowski record's links were added to the frontier; the Brown 1993
reference list is a history spine of the subject (many rows already held).



**Added:** Bugeaud & Reutenauer, "On the conjugates of Christoffel words"
(arXiv:2202.05486v5; DMTCS 27:3 #20, 2025, DOI 10.46298/dmtcs.15140). Full text
`research/sources/bugeaud-reutenauer-conjugates-christoffel-ar5iv.full.md`;
summary + claim `research/summaries/bugeaud-reutenauer-conjugates-christoffel.md`;
journal record page `research/summaries/bugeaud-reutenauer-conjugates-christoffel-2025.md`.

**Why this was the thinnest axis.** The library was strong on the infinite-word
side (Sturmian/Fibonacci-word factor complexity, mechanical-word/rotation
construction, universal-Euclidean/floor_sum primitive) but had no dedicated
source for the *finite* side that directive 1's verification route rests on:
at k = F_n − 1 the k+1 distinct length-k factors are the F_n rotations
(conjugates) of the truncated standard/Christoffel word, with the cyclic
autocorrelation counting A(jp−j). The Introduction's bridge theorem — *a f
finite word is a conjugate of a Christoffel word iff all its conjugates are
factors of a Sturmian word* — is the finite↔infinite principle behind that
identification. The paper also carries the Ostrowski-numeration parametrisation
of conjugates (Thm 7.3), the same axis as the run's hieronymi source and
directive 1's O(log) recursion. Claim `conjugate-christoffel-factor-sturmian`
recorded in the claims ledger.

**Confirmed still unobtainable:** Berstel's "Fibonacci Words — A Survey"
(The Book of L, 1986) — the author's page `www-igm.univ-mlv.fr/~berstel/
Articles/1985BookOfL.pdf` refuses the transfer again this cycle; no legitimate
free mirror. Non-blocking: the DLT'95 and 2007 Berstel surveys, the
Berstel–Karhumäki tutorial, and the Lothaire C2 chapter (all on disk) cover the
definitions, factor complexity, and standard-word structure.

**Remaining load-bearing formula without a source:** directive 1's
A(d) = max(0, m−t) + max(0, m−(N−t)), t = (d·m) mod N — the cyclic
autocorrelation count of the standard word. No dedicated literature source was
found (three-distance/balance counts live inside rotation theory but no single
paper states this exact closed form). It is a verify-in-container counting
identity, checked against the brute oracle by task `reproduce-dir1`, not a
result that needs a citation to be used.

**OEIS re-check this cycle:** Ψ(1..5) = 1, 101, 20302, 2042402, 204252402
still has no OEIS match (consistent with prior records); the frontier now
carries the 43+27+45 citations of the new source's three downloads.

## This librarian cycle — two library gaps closed (memory server still down)

Cognee remains unhealthy (health-check timeout on every remember/describe
call); durable record stays on disk here and in the two summaries below. The
run's established on-disk catalogue is this file, not an INDEX.md.

1. **Alassandri–Berthé "Three distance theorems and combinatorics on words"**
   (https://www.irif.fr/~berthe/Articles/3d.pdf) had been downloaded in an
   earlier cycle but was never digested (still a template header). Replaced:
   `research/summaries/alessandri-berthe-three-distance-theorems.md` now carries
   the exact Three distance theorem (interval counts for slope α, convergents
   q_k) and Slater's Three gap theorem (exact gap frequencies). **This closes
   the previously recorded gap "no dedicated literature source for directive 1's
   autocorrelation formula A(d) = max(0,m−t)+max(0,m−(N−t))"**: that closed
   form is the Fibonacci-slope (all-partial-quotients-1) specialisation of these
   gap counts. Claim `three-gap-three-distance-autocorrelation` in
   `research/summaries/claim-three-gap-autocorrelation-home.md`.
2. **Babichev & Babichev, arXiv:2604.22456** — lattice rectangles in
   near-linear time — downloaded as full text 
   (`research/sources/lattice-rectangles-weighted-floor-sum-html.full.md`;
   summary `research/summaries/lattice-rectangles-weighted-floor-sum-html.md`).
   It develops the six/ten-moment **weighted floor-sum kernels closed under
   Euclidean affine + reciprocal steps, evaluable in O(log n)** (Lemmas 4–5,
   Corollary 6): a primary proof-carrying anchor for the universal-Euclidean
   family-closure that directive 2's O(log) primitive rests on, complementing
   the operational OI-wiki/fhq/LOJ138/AtCoder sources. Scope note: its kernel
   uses polynomial index weights t^p; the run's geometric weights x^t stay
   anchored to the fhq/LOJ138/AtCoder sources.

3. **OEIS re-issued with seven oracle terms** (1, 101, 20302, 2042402,
   204252402, 30445654403, 3054587854503 = Ψ(1..7)) — still no match. Recorded
   in durable-findings note; not to be re-run.
