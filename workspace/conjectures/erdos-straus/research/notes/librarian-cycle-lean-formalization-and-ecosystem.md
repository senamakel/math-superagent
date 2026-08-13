# Librarian cycle: Lean formalisation ecosystem and the active research frontier (2026)

Date: this cycle. Sources added: `research/sources/erdos-242-forum-thread.full.md`,
`research/sources/tao-whatsnew-erdos-straus-counting.full.md`,
`research/summaries/formal-conjectures-242.lean.md`.

## What the new sources establish

### 1. Erdős Problem #242 discussion thread (erdosproblems.com/forum/discuss/242)

An 18-comment thread by active workers in the field (Thomas Bloom [site owner,
analyst], Terence Tao himself posting a quality gate for preprint "proofs",
several formalisation workers). Load-bearing contents:

- **Expert quality gate for new preprints on this conjecture** (Terence Tao,
  13 Feb 2026): do not take seriously any new preprint unless (a) accepted in a
  reputable journal, (b) the author has a track record in the area, (c) only
  realistic partial results claimed, (d) an expert vouches, or (e) it is
  formally verified. Applies to Bradford's arXiv:2602.11774 "solution" claim
  and Mballa's arXiv:2502.20935/2508.07367 "almost complete proof" — all
  publicly dissected as mistaken (StijnC, Bloom).
- **Bloom's specific debunking of an attempted full coverage of
  `n ≡ 529 (mod 840)`** (thread 29 Jan 2026, and the `R529.lean` file in the
  leonelchlon repo): the "proof" verified a collection of small n and appealed
  to "periodicity" to extend to the infinite congruence class. That does not
  work — the statement is not periodic — so it is not a covering identity. This
  is a live warning for this run's own deliverable: a family verified for many
  small n is not a covering family unless it is a polynomial identity in the
  progression parameter.
- **A concrete single-construction reduction** (leonelchlon, 27 Jan 2026,
  asserted in thread, NOT independently verified here): the full conjecture
  reduces to: given `q ≡ 3 (mod 4)` and `s² + p = qk`, find `δ, b, c` with
  `(4b−1)(4c−1) = 4pδ + 1` and `δ | bc`; setting `b = (q+1)/4` works for small
  `q`, the general case is open. Claimed Lean formalisation: ES for
  `n = 420k + r` with `k odd`, `r ∈ {121,169,289,361}`; all `n ≡ 529 mod 840`
  "via CRT" (since debunked, see above); 348/420 coverage; 20 conditional
  certificates for `n ≡ 1 (mod 840)` reducing to divisor conditions; a formal
  refutation of one proposed ED2 covering scheme.
- **The repo is now 404** (`https://github.com/leochlon/erdstrau`, both root
  and raw file fetches failed this cycle). The claims above are therefore
  attributed to the thread (user leonelchlon), not to a current readable source.
- Terzi (1971) narrowing: 198 bad congruence classes mod 120120 (confirms the
  claim already on disk in ROOT.md).
- Verification-history additions: Ko–Sun–Chang 1964 (400000), Rosati 1954
  (171649), Jollensten (1.1×10^7) — minor confirmations of Elsholtz–Tao Table 1.

### 2. Tao's "What's new" post on the Elsholtz–Tao counting paper (July 2011)

`research/sources/tao-whatsnew-erdos-straus-counting.full.md` (58 KB). Content:
announcement of the paper (J. Austral. Math. Soc. 94 (2013) 50–105; supersedes
Tao's 2011 "On the number of solutions to 4/p = 1/n_1+..." paper), the
`f(nm) ≥ f(n)` prime reduction, Type I / Type II definitions, and the counting
results. Supplements the two Elsholtz–Tao full texts already in the library
with the author's own exposition; no new mathematics beyond the paper. Useful
as the citation anchor for [ElTa13] at the "detailed blog discussion" level.

### 3. Formal Conjectures: Lean statement of Erdős Problem #242

`research/summaries/formal-conjectures-242.lean.md` (google-deepmind/
formal-conjectures repo, file `FormalConjectures/ErdosProblems/242.lean`,
Apache-2.0). The theorem is stated with the **strict inequality variant**
(`distinct integers 1 ≤ x < y < z`), as an `∃ x y z` with all hypotheses, body
`sorry` (unproved), plus the Schinzel generalisation variant. Two points worth
recording:

- The run's `problem.md` states the conjecture without distinctness; the
  formalised version demands distinct denominators. These are **equivalent**
  only up to cases where a solution has equal denominators — a solution
  `(x,y,z)` with two equal can be perturbed, but the equivalence is not
  automatic. Any claim this run makes should state which variant it proves.
- The Lean statement is the natural target if the lean_prover role formalises
  ESC's statement early, as instructed; the file is the exact reference text.

## Claims

```claim
id: esc-formal-lean-statement-distinct
statement: The google-deepmind formal-conjectures repo states Erdős Problem #242 in Lean as: for every n > 2 there exist 1 ≤ x < y < z (strictly increasing, hence distinct) with 4/n = 1/x + 1/y + 1/z; the theorem body is `sorry` (open), and a Schinzel-generalisation variant (a/n for fixed a, n sufficiently large) is also stated with `sorry`.
hypotheses: n : ℕ, 2 < n; statement is the distinct-denominator variant of ESC.
holds-here: yes — the run's problem.md states ESC without demanding distinctness; the formalised statement is the distinct variant, so results should be labelled by which variant they prove.
status: sourced (github.com/google-deepmind/formal-conjectures, FormalConjectures/ErdosProblems/242.lean); not independently verified this run (no Lean build).
bearing: fixes the exact formal target; lean_prover role can start from this statement and its imports.
anchor: research/summaries/formal-conjectures-242.lean.md
```

```claim
id: esc-529-crt-periodicity-refuted
statement: A claimed Lean "Full CRT coverage for n ≡ 529 (mod 840)" (repo erdstrau, R529.lean) is not a covering proof: per Thomas Bloom (erdosproblems.com forum, 29 Jan 2026) it verified finitely many small n and appealed to periodicity, which is invalid because solvability of 4/n is not periodic in n. The repo has since gone 404.
hypotheses: claims made in a forum thread about a Lean repo; Bloom's analysis is expert commentary, not a formal refutation.
holds-here: yes — same trap as this run's own deliverable: a family checked on finitely many n is not a covering family unless it is a provable identity in the progression parameter.
status: asserted-by-source (Thomas Bloom, erdosproblems.com forum thread on #242); repo unavailable for independent check.
bearing: warning for any ansatz work: coverage must be established as an identity in k (is_identity), never by a finite check plus "periodicity".
anchor: research/sources/erdos-242-forum-thread.full.md
```

```claim
id: esc-single-construction-reduction-leonelchlon
statement: Forum user leonelchlon (27 Jan 2026, asserted, not independently verified) claims ESC reduces to one construction: given q ≡ 3 (mod 4) and s² + p = qk, find δ, b, c with (4b−1)(4c−1) = 4pδ + 1 and δ | bc; setting b = (q+1)/4 works for small q, general case open. Same thread claims Lean formalisations: ES for n = 420k + r, k odd, r ∈ {121,169,289,361}; 348/420 residue coverage; 20 conditional certificates for n ≡ 1 (mod 840) reducing to divisor conditions.
hypotheses: forum-user claims; repo erdstrau now 404, claims unverifiable from a current readable source.
holds-here: possible — the claimed reduction (if correct) would be a bridge between the Type-II parametrisation (p = qr − 4s₁s₂, Chamberland) and a covering construction; worth a verification attempt, but unproven here.
status: asserted-by-source (forum thread); NOT checked.
bearing: a candidate structural route: the single-construction form and the "conditional certificates for n ≡ 1 mod 840" are the closest thing to a working ansatz idea found in the ecosystem this cycle.
anchor: research/sources/erdos-242-forum-thread.full.md
```

```claim
id: esc-expert-quality-gate
statement: Terence Tao (erdosproblems.com forum, 13 Feb 2026): new ESC preprints should not be given attention unless published in a reputable venue, or by an author with a track record in the area, or claiming only realistic partial results, or vouched for by an expert, or formally verified. Bradford (arXiv:2602.11774) and Mballa's "almost proof" (arXiv:2508.07367) were publicly dissected as mistaken by StijnC and Bloom.
hypotheses: expert commentary on preprint quality, not a mathematical theorem.
holds-here: yes — this run's own deliverable must clear the same bar: a verified symbolic identity family with stated coverage, never a claimed proof on unverified structure.
status: asserted-by-source (forum thread).
bearing: quality gate for any future source the library adds; explains why the library holds no claimed full proofs.
anchor: research/sources/erdos-242-forum-thread.full.md
```

## Status of the open REQUEST

`research/REQUESTS.md` row `exact-statement-from-b7df` (why the six square
classes resist the standard type I/II families) is **answered**: the exact
statement is in `research/notes/es-structure.md` section (d), with primary
citations (Elsholtz–Tao Prop. 1.6 and §4 proof; Salez Prop. 2 = Schinzel's
non-residue theorem; Elsholtz–Tao §10 "unless r is a perfect square"), and the
claim block `mordell-six-open-classes-840` in that note carries
`answers: exact-statement-from-b7df`. The REQUESTS.md row will close on the
next regeneration; do not post it again.