# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately. It is not a
catalogue of files (`research/README.md` is that) and not a narration of what
agents did. Token budget `MATH_AGENT_CONTEXT_TOKENS` (10000); the file is
re-sent on every model call, so brevity is a shared bill.

**Reading this run from disk:** this workspace carries a prior
`conjectures_erdos_straus` run. `code/oracle.py` (+ `code/brute.py`,
`code/verify_library_claims.py`) is its oracle and is live; the run's own
findings are in `research/approaches/oracle-findings.md` (read it before
trusting those scripts) and its evidence trail in `code/out/commands.log` and
`code/out/oracle.captured.txt` (`code/out/README.md` explains the split).
`research/summaries/` holds seven source digests with full texts under
`research/sources/`; no claim blocks were ever extracted, so
`research/CLAIMS.md` is empty despite the library reading. Sources are
sourced facts, not checked claims — the ledger must be built from them.

## Established

- **Oracle verified.** `code/oracle.py` `solves()` (exact integer
  cross-multiplication) reproduces all 12 entries of `code/out/witnesses.json`
  (checked, `code/out/commands.log`, also by `solves_fraction` independent
  route). `parallel.py` self-check passes on 26 workers of 28 CPUs (checked).
  Use `oracle.py`s `solves`/`is_identity` as ground truth; do not rebuild.
- **Even case is settled (checked):** `4/(2m)=1/m+1/(2m)+1/(2m)`, verified
  m=1..5000 (`code/out/verify_elementary_reductions.py`).
- **Prime reduction is still `asserted`, not `checked`.** The scaling argument
  `f(nm) ≥ f(n)` (a solution for p lifts to one for every multiple mp by
  `(x,y,z)↦(mx,my,mz)`) has not yet been run through code here; it is the top
  open task in TASKS.md. Do not cite it as checked until the program and
  capture exist. (The prior `oracle.py` demo of it encoded the wrong identity
  and FAILed for that reason — see `research/approaches/oracle-findings.md`.)
- **Six open classes verified by computation** (checked,
  `verify_library_claims.py` Claim 2, which is sound in this part): the five
  Mordell-shape covering conditions (≡2 mod 3, ≡3 mod 4, ≡2/3 mod 5,
  ≡3/5/6 mod 7, ≡5 mod 8) leave exactly residues `{1,121,169,289,361,529}`
  mod 840 among the residues that matter (odd, coprime to 3,5,7) — and all six
  are squares mod 840 and are the *only* squares the five conditions fail to
  cover. Complete list of squares mod 840 in that capture.
- **The brief's `n ≡ 3 (mod 4)` lead is wrong.** `4/n = 1/n + 1/((n+1)/2) +
  1/(n(n+1)/2)` simplifies to `3/n` (checked symbolically, diff = 1/(4k+3);
  verified several times in `commands.log`). The corrected families, both
  verified as exact identities with integral positive denominators:
  - family A (in `oracle-findings.md`, k=0..1999): `n=4k+3`,
    `x=(n+1)/4`, `y=n(n+1)/4+1`, `z=y(y-1)`; diff == 0 (symbolic).
  - family B (in `commands.log`, k=0..299 confirmed integral/positive/solve):
    `x=(n+1)/4`, `y=(n(n+1)+4)/4`, `z=n(n+1)(n(n+1)+4)/16`; diff == 0
    (symbolic), i.e. `x=k+1`, `y=(k+1)(4k+3)+1`,
    `z=(k+1)(4k+3)((k+1)(4k+3)+1)`. Both are identities in k, hence settle the
    whole class `n ≡ 3 (mod 4)`.
- **Sourced background** (from `research/summaries/erdos-problems-242.md`,
  erdosproblems.com/242, and the other summaries — asserted-by-source, not yet
  claim-blocked): conjecture open since 1948, first in Obláth 1950 (submitted
  1948); it suffices to prove for prime n; **verified for all n ≤ 10¹⁸**
  [MiDu25] — *not* yet reproduced here; Mordell [Mo69] settled all but the six
  840-classes; Terzi [Te71] reduced to 198 bad congruences mod 120120; Vaughan
  [Va70] exceptions ≤ x·exp(−c(log x)^(2/3)); Elsholtz–Tao [ElTa13]
  Σ_{p≤N}f(p)=N(log N)^(2+o(1)), f(p) ≤ p^(3/5+o(1)); no Brauer–Manin
  obstruction [BrLo20]; equivalence to two congruence conditions [BlEl22,
  Theorem 1]; Elsholtz–Planitzer [ElPl20] lower bounds; Schinzel/Sierpiński
  5/n generalisation; related OEIS A073101, A075245–8, A287116. The salez
  papers give the modular-equation sieve method and its "complete set of
  seven" modular equations (used to check to 10¹⁷, 2014).

## Ruled out

- **`oracle.py`'s mod-4 rows FAIL — do not re-verify them as gaps.** Three of
  its checks encode the brief's wrong identity (`x=n, y=(n+1)/2,
  z=n(n+1)/2`), which solves 3/n; the FAILs are the script's bug, not the
  equation's. `oracle-findings.md` calls this out. Same for its naive-solve
  sweep "unsolved" lists.
- **`verify_library_claims.py` Claim 3 output is meaningless.** Its `type_of`
  counts denominators divisible by n, and the tiny-n search bound (x ≤ 4n)
  manufactures such hits for every triple, so its "I/II among them = all"
  at odd squares 9,25,49,81,121 proves nothing about Elsholtz–Tao
  Proposition 1.6. Rework with the true Mordell type definition before any
  use. (`oracle-findings.md`.)
- **"Unsolved for n=127,149,157,167,179,193,197,199" is a cap artifact.**
  naivy_solve cap=4000 < minimal z (n=127 needs z=134112; witness found at
  cap 2·10⁵). Not gaps in the conjecture.
- **A claim "no type-I/type-II solution for prime n ≡ r (mod 840)" must be
  checked against prime witnesses.** `witnesses.json` contains *prime* solved
  n: 1009 (class 169), 1129 (class 289), 1201 (class 361), all verified.
  Any impossibility lemma that contradicts them is false as stated.

## Numbers

- 12 witnesses in `code/out/witnesses.json`, every one verified OK
  (`commands.log`): n = 121, 169, 289, 361, 529, 841, 961, 1009, 1129, 1201,
  1369, 1681 covering all six open classes (two each, one square and one
  other). E.g. n=121: 4/121 = 1/31 + 1/1254 + 1/427614 (checked).
- **Observed (not proved) pattern in all 12:** `x = (n+t)/4` with
  t ∈ {3,15,19,23,31,47}, so the residual terms satisfy
  `1/y + 1/z = 4t / (n(n+t))`. Worth mining for the structure of a new shape.
- n ≡ 3 (mod 4) families A and B: symbolic diff exactly 0 (checked).
- `parallel.py` self-check: 2000 values across 26 workers, PASS (checked).

## Recalled

Durable memory holds only the pointer card for
`research/summaries/erdos-problems-242.md` from the prior project: topic
"Erdős problem #242" (recalled; the summary itself is on disk and is the
source of the sourced background above). No Cognee findings exist from this
run beyond the two micro-results I stored this cycle (corrected n≡3 mod 4
identity; witness-set observation above). Treat everything else recalled from
memory as unverified pointers.

## Contradictions

- The brief's `n ≡ 3 (mod 4)` identity **disagrees with computation**: it
  equals 3/n, and all three places `oracle.py` encodes it FAIL, while the two
  corrected families above pass. (Computed, multiple captures.)
- `verify_library_claims.py`'s docstring asserts "Elsholtz–Tao Prop 1.6: an
  odd perfect square n has NO Type-I and NO Type-II solution" while its own
  output prints type I/II hits at every odd square — its detector is broken,
  so **the proposition's exact statement is unverified here**, and the n=841
  witness (z = 841·22149, exactly one denominator divisible by n) shows the
  naive divisibility reading cannot be what Prop 1.6 says. The real statement
  must come from the full text.
- Verification bound differs by source vintage: 10¹⁷ (Salez 2014) vs 10¹⁸
  [MiDu25] (erdosproblems page, edited 2026). The 10¹⁸ claim is
  asserted-by-source, not reproduced.

## Gaps

- **Exact statement of Elsholtz–Tao Proposition 1.6** (Vanishing) from
  `research/sources/pomerance-erdos-straus.full.md`, with the Mordell type
  definition (exactly one / exactly two of x,y,z divisible by n?) and its
  hypotheses (n prime? n an odd square?). This is the hypothesized
  square-obstruction at the heart of the brief; every ansatz search must know
  exactly what identity shapes (type I / type II) cannot reach the six open
  classes, so the run does not rediscover what Mordell already ruled out.
- **Wikipedia's "Nonexistence of identities" and "Modular identities"
  sections** in `research/sources/wikipedia-erdos-straus.full.md`: exact
  claims about which identity shapes have been shown not to exist. (The run
  knew of the section but never extracted its claim.)
- **Prime witnesses for the remaining open classes** (1,121,529,169?): the
  run has prime witnesses only for classes 169, 289, 361. It is unknown
  whether classes 1, 121, 529 have prime n in some range with known
  solutions. A small bounded search for prime witnesses in classes 1, 121,
  529 would harden the falsification oracle (uses `naive_solve`, cheap).
- **Reproduce the 10¹⁸ verification bound** — the literature claims it; the
  run has reproduced nothing past n=121. An independent check of even a small
  slice (or of the Salez seven-equation sieve on a subset) would make the
  sourced bound a checked one.