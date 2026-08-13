# Winning n_t model — on-disk state as of this review

This note records what the workspace's outputs actually establish about the
adopted model (`arc-closure-cs-polynomial`, `n_t(d) = [(c-t)β + (s+t)μ]/π`),
and — critically — what is NOT yet established because the on-disk record is
mutually contradictory. Written by the scholar role from the output files
themselves; my role has no execution tool, so this note is an audit + a
ready-to-run verification script, not a fresh computation.

## What the outputs agree on (consistent across files)

- **Model**: `n_t(d) = [(c−t)·β_t(d) + (s+t)·μ_t(d)]/π`, β = angle of the type-t
  tangency point about the ring centre O, μ = angle about the sun centre S;
  R = c/2π, r = s/2π, a_t = R−t/2π, b_t = r+t/2π,
  d_min = max(|a_p−b_p|,|a_q−b_q|), d_max = min(a_p+b_p, a_q+b_q, R−r−1).
- **Identity** `n_p(d) + n_q(d) = c + s`, verified at mpmath-60 precision at
  arbitrary interior d (incl. `winner_refine.txt` 1e-59/1e-60 residuals; the
  note in `n_integer_count.py` and `structural_test.py` corroborate). This makes
  n_q ∈ ℤ automatic once n_p ∈ ℤ and reduces the four-planet condition to one.
- **Parity condition** is vacuous (G_sequence.txt: s+c+p−q = 2s+2p ≡ 0 mod 2).
- **n_p monotone increasing** on (d_min, d_max) — consistent across scans
  (fast_g.py bisection relies on it; count_formula_test.txt 0 mismatches).
- **g counts integer levels** of n_p strictly between the endpoint values:
  g = #{k ∈ ℤ : n_p(d_min+) < k < n_p(d_max−)} — the closedform/endpoint form.

## What the outputs DISAGREE on (the contradiction to resolve)

| File | g(16,5,5,6) | G(20) | Notes |
| --- | --- | --- | --- |
| `n_integer_model.txt`, `closedform_probe.txt`, `count_formula_test.txt`, `mpmath_table.txt`, `seq_G.txt`, `G_sequence.txt` | 9 | 205 | formula/scan agree; `count_formula_test.txt` reports **0 scan-vs-formula mismatches across 372 tuples (s+p+q≤30)**, G(30)=4538 |
| `count_formula_test2.txt` | **6** (scan) vs 9 (formula) | — | **2369 mismatches** across 2600 tuples (s+p+q≤45); scan uses N=2^17 grid, tol=1e-4, p-only regions |
| `levels.txt` | 0 (rows all-zero) | — | kmin..kmax all `1..0`, nlo=nhi=0.00000 for every tuple — **an artifact** (bad evaluator), not a model result |
| `G20_overcount.md` (claim `g20_overcount_by_eight`, checked) | 9 | **213** (+8) | fast_g.py monotone-crossing at mpmath — the *overcount* claim this run's thread chases |

So g(16,5,5,6) is reported as 9, 6, and 0 by different files that claim to run
the same model. The 9-file family is consistent with the oracle; the 6 and 0
files are grid-resolution artifacts of different scan parameterisations
(count_formula_test2 at 2^17/1e-4 under-resolves the level runs; levels.txt has
a clearly broken evaluator — see its all-zero rows for tuples whose
closedform_probe gives 9–12).

## What is NOT yet on disk (gaps, in priority order)

1. **An executed, uniform, exact verification** of g(16,5,5,6)=9, the 22 G(20)
   per-tuple values (sum 205), and a scan-vs-formula match at several grid
   sizes — needed to retire the 6-vs-9-vs-0 contradiction.
2. **G(500)**: `code/solution.py` prints "G(500) = 1470337306" only as a
   comment (independent_verify.py Route B: "already = 1470337306 in
   code/solution.py") — there is **no output file** with a computed G(500), and
   the run's GOAL requires a verified second route.
3. **A proof** of the identity n_p+n_q = c+s and of monotonicity of n_p over the
   whole interval (currently mpmath-60 numerical, per the approach file's own
   first-step).
4. **Exact endpoint-floor evaluation** (approach first-step 2–3): d_min piecewise
   by sign of c−s−2t, d_max arctan at gap 1; needs exact floor via interval
   arithmetic or the degree-(c+s) unit-circle polynomial (adopted approach).

## Ready-to-run verification

`code/pattern/scholar_verify.py` (written this review): recomputes from the
formula alone — identity at arbitrary d (mpmath-60), g(16,5,5,6), all 22 G(20)
values, G(16)/G(20) sums, and a region-scan diagnostic of (16,5,5,6) across
grid sizes (2^17/1e-4 — the count_formula_test2 params; 2^20/1e-3;
2^20/1e-4; 2^22/1e-4) so the 6-vs-9 contradiction is resolved by data. It is
not yet run (scholar has no execution tool); operator should run it and record
the output beside this note.

```claim
id: n_t_model_oracle_summary
statement: The n_t(d) = [(c-t)*beta + (s+t)*mu]/pi model (identity n_p+n_q = c+s at mpmath-60 precision, parity vacuous, n_p monotone, g = #{k in Z : n_p(d_min+) < k < n_p(d_max-)}) reproduces g(16,5,5,6)=9, G(16)=9 and G(20)=205 in the consistent output files (n_integer_model.txt, closedform_probe.txt, count_formula_test.txt, mpmath_table.txt, seq_G.txt, G_sequence.txt); but count_formula_test2.txt reports 2369 scan-vs-formula mismatches with g(16,5,5,6)_{scan}=6 and levels.txt reports all-zero rows, so the model-level claim still lacks a uniform, executed verification and G(500) has no computed output on disk.
hypotheses: exact tangency (planet centre at circle intersection); per-type residue defined by that three-term angle combination; mod-1 congruence is the meshing condition; n_p monotone.
holds-here: yes for the model as a hypothesis confirmed by the consistent files; unproved parts: identity proof, monotonicity proof, exact endpoint floors, G(500).
status: checked (oracle triple in the consistent files) — but contradicted on disk by count_formula_test2/levels artifacts; G(500) unverified
bearing: pins what the library may legitimately claim (9/9/205 under the n_t model) vs what it may not (G(500)); the next step is running scholar_verify.py and retiring the artifacts
anchor: code/out/scholar_verify.py (to run)
contradicts: g20_overcount_by_eight
answers: the-on-disk-9-9-205-claims (partially: which files establish them, which do not)
```

## Cross-references

- Adopted approach: `research/approaches/arc-closure-cs-polynomial.md`
  (identity + unit-circle polynomial); its verdict
  `arc-closure-cs-polynomial.verdict.md`.
- The W-invariant model (thread `offcentre-mesh-phase-model`, w_invariant_test)
  is a DIFFERENT, dead model: w_invariant_test.md checks A/B/C/D conditions,
  all fail to give 9. The tangency_enum.py residue Q = −ρ(β−γ) + Rβ − rγ is the
  same family that the n_t formula subsumes (angle × tooth-count sums).
- Sources that ground the congruence form: Kurasov 2020 (off-centre GES,
  per-pair signed angle×tooth-count = integer×π), Zhao–Li 2018 (duplex idler,
  internal-mesh sign −), Segade-Robleda 2012 (four-gear pitch difference),
  Guo 2011 (5.21–5.25 coaxial), plus the three least-mesh-angle design guides.