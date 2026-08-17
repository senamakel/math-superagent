# Library build status — PE1006 reference library

What the library holds, why each source is there, and where it lives. The Cognee
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

## This cycle (librarian) — finite/standard-word side strengthened

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
