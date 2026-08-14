# Scholar assessment of the PE1006 reference library

This note consolidates, per source, what the library establishes, whether the
source's digest is faithful to its full text, and what each source lets this run
do. Status of every claim block is tracked in `research/CLAIMS.md`.

## Load-bearing sources (verified against full text)

### 1. Perrin & Restivo, "A note on Sturmian words" (hal-00828351, TCS 429:265-272) — THE structural source
Verified in full text:
- **Slope** of the Fibonacci word is `α = 2/(3+√5) = (3−√5)/2 = 1/φ²`; continued
  fraction `[0,2,1,1,...]`, convergents 1/2, 1/3, 2/5, 3/8, 5/13,... (Example 2, 5).
- **Proposition 1 (membership):** `w ∈ F(s)` iff **every factor u of w** satisfies
  `|u|_1 − 1 < α|u| < |u|_1 + 1`. This block-wise balance w.r.t. α is the correct
  membership test — the flat `floor/ceil(kα)` count is only necessary.
- **Theorem 2:** two equal-length factors u,v are consecutive in lex order iff
  `u = r·ab·s, v = r·ba·s` or `u = r·a, v = r·b` (r = principal/right-special prefix).
- **Corollary 3 + Next(u):** the factor after u is `rbas` (if u = rabs) or `rb` (if u = ra).
- **Factor-set structure:** for `k = |s_n|` (a Fibonacci/standard word length) the
  length-k factors are the **conjugates of the standard word s_n plus one singular
  factor** (Table 3 k=8: 8 conjugates of abaababa + babaabab; Table 1 k=10).
- **Sturm(n)** generates the k+1 factors in lex order in O(k²) — infeasible at k=10^18,
  so this is the *structure* to build a recurrence on, not the computation itself.
Digest faithful. Claim `PR-consecutive-factors-lex` proved-in-source is accurate.

### 2. Poirier & Steiner, "Factor-balanced S-adic languages" (hal-03869990) — balanced-blocks source
Verified in full text (Section 1, quoting Morse–Hedlund 1940): **each block of length n
in a Sturmian sequence of slope α has ⌊nα⌋ or ⌈nα⌉ occurrences of the α-frequency
letter** (equivalently the difference in letter counts across equal-length blocks is ≤ 1).
This is a NECESSARY condition. The Morse–Hedlund balancedness + Sturmian factor
complexity jointly give that every length-k factor has floor/ceil(kα) ones — but NOT
that all such balanced words are factors (see overreach note). Verified.

### 3. Wojcik, "Formal Intercept of Sturmian words" (hal-01827511) — Morse–Hedlund source
Verified in full text:
- **Theorem 1 (Morse–Hedlund):** x ultimately periodic iff ∃n with p(x,n) ≤ n;
  equivalently aperiodic ⇒ p(x,n) ≥ n+1 for all n.
- **Theorem 2(1):** balanced ⇒ p(x,n) ≤ n+1. **Theorem 2(2):** x Sturmian iff balanced
  and non-ultimately-periodic.
- **Theorem 3(3):** two Sturmian words of same slope have the same factor set (→
  `PE1006-factors-dependent-slop-only`), and Theorem 3(1): balanced is Sturmian iff slope
  irrational.
This is what proves the problem's "exactly k+1" FACT: F is balanced + aperiodic, so
p(k) = k+1. Digest faithful. Claim `MH-kplus1-factors` accurate and implies
`PE1006-kplus1-FACT`.

### 4. Cassaigne–Fici–Sciortino–Zamboni, "Cyclic complexity" (hal-01829144) — Prop 6, 7
Prop 6: x Sturmian iff exactly n+1 length-n factors. Prop 7: two Sturmian words have
same factor set iff same slope. The source of `PE1006-factors-dependent-slop-only`
(which licenses computing from the infinite word). Digest concise and accurate.

## Background / surrounding-theory sources (accurate digests, not load-bearing)

- **Berstel–Lauve–Reutenauer–Saliola, Christoffel Words book (luc.edu PDF):** Christoffel/
  standard/central words, standard-factorization tree, conjugacy of lower/upper
  Christoffel words. Authoritative for the Christoffel apparatus behind the factor
  structure, but no Ψ(k) formula. `christoffel-conjugate-and-forest` claim (proved) is fair.
- **Berthé course notes (irif.fr):** Sturmian=rotation-coded, three-distance theorem.
  Background only; confirms identification.
- **de Luca 2013, Cassaigne 2008:** extremal properties of Fibonacci word — marginal;
  not the factor-value sum. Background.

## Sources that do NOT help (recorded so nobody re-reads them)

- **Lothaire Ch.2 "Sturmian Words" page (CUP):** paywall stub, TOC only, no content.
  Its statements are fully covered by Wojcik + Perrin–Restivo. Do not reopen.
- **Morse & Hedlund 1940 (JSTOR stable/2371487):** paywall cover only, no content.
  Recovered from Wojcik + Poirier–Steiner. Do not re-fetch.
- **Fici, "Factorizations of Fibonacci word" (arXiv:1508.06754):** abstract landing page
  only, pointer; factorization vs. factor-set, no sum formula. Background.
- **Rampersad & Wiebe, "Minimal forbidden factors" (arXiv:2309.07070):** abstract only;
  forbidden-factors route is over-build for a structure we already have via PR Thm 2.
  Not needed.
- **"note-on-sturmian-words-2011.full.md":** MISFILED — arXiv:1202.6175 is an unrelated
  comms-engineering paper (Joda–Lahouti). Contains nothing on Sturmian words. The real
  Perrin–Restivo note is hal-00828351. Do not cite the misfile.

## The one substantive correction this run made

The request `precise-sourced-statement-c1ec` originally framed the k+1 factors as "the
n+1 balanced binary words." That is **falsified**: the count of balanced words with
floor/ceil(kα) ones strictly exceeds k+1. Counterexamples (verified against the Psi
brute factor dump): k=4 factors {0010,0100,0101,1001,1010}, yet 0110 (2 ones) and
0001/1000 (1 one) are balanced of the right count and are NOT factors. Documented in
`research/approaches/balanced-factors-claim-attack.md` and the governing-theory note
(claim `PE1006-factors-one-count-necessary` replaces the retracted
`PE1006-balanced-factors-floornalpha`). Correct enumeration = PR Theorem 2.

## What the collection still does NOT settle

None of these sources yields a closed form for Ψ(k) = Σ (decimal value of the k+1
factors)², nor a poly-log(k) evaluation. Perrin–Restivo gives O(k²) enumeration only.
The run's own computational record (tools: `find_recurrence.py`, `find_small_recurrence.py`)
shows **no constant-order (≤40) linear recurrence in k fits the 150 computed Ψ(k) terms**
(BM order 75 = n/2 is the degenerate ceiling; no order ≤40 consistent across primes).
So Ψ(k) is evidently NOT a fixed-order linear recurrence in k — the "matrix-exponentiate
a fixed recurrence in k" plan in backward/weakened will not work as phrased. The structure
that must be exploited instead is the piecewise-in-log structure: the factor set is
constant in character between Fibonacci/continuant lengths and re-organised only as k
crosses |s_n|; any closed form is therefore indexed by Fibonacci numbers / continuant
blocks, not a plain k-recurrence. This is a derived (non-sourced) conclusion from this
run's own computation and needs an independent route before being relied on.

## Durable memory stored

- PR structural theorem (slope, Prop 1 membership, Thm 2 consecutive factors, conjugates
  + singular factor structure) — source-backed.
- Falsification of the balanced-word bijection, with counterexamples — verified.
