# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: bivariate-floor-moment-diagonal route closed: the diagonal h=j-m is NOT a second affine coordinate. Verified formulation (B) has g depending only on (l-m), so Psi(k) = sum_{j,l} w_j w_l C_k(j,l), C_k(j,l)=sum_m g(j-m)g(l-m) — a double-diagonal truncation correlation. Fixed-dimensional closure needs C_k Toeplitz in (j,l); the run's own mechanically-checked refutation (pe1006-pair-correlation-boundary) shows it is not, except at k=F_n-1. Babichev-Shpakova Lemma 13 is one-staircase closure with two per-intercept endpoint markers and their algorithm pays L^2 marker-slot operators (Lemma 14) = the… (refers: pe1006-bivariate-floor-moment-diagonal, pe1006-pair-correlation-boundary, dir1-domain-autocorrelation)
- **chisel**: The corrected executable oracle found the smallest local summary collision at k=2: blocks 010 and 101 both have summary (2,11,101), but appending 0 gives (3,11,101) versus (3,21,201). Thus the naive fixed summary (count,sum,sumsq) is not closed under concatenation. This is now kernel-checked in code/lean/G4BlockStateNonClosure.lean. No full-size Psi(10^18) value is established. (refers: g4-joint-collapse-derivation, code/lean/G4BlockStateNonClosure.lean)
- **chisel**: The single-intercept universal-Euclidean evaluator is refuted mechanically at k=1,2,3. ue0 correctly evaluates each individual affine floor sequence with z^0 indexing, but the full Psi requires aggregation over all k+1 intercepts; no valid O(log) aggregation was established. (refers: implement-solution, pe1006-ostrowski-sawtooth-closed-form)

## lesson

- **chisel**: Convergence decision on the three inventor candidates: transfer-operator-spectral and weighted-language-diagonal are both refuted by research (finite-rank closure / finite p-kernel are the unproved cores, and the 10-vs-phi multiplicative-independence obstruction kills the diagonal conversion). Fourier-rotation-correlation is narrowed, not dead: it is a valid reformulation, but the engine it needs — continued-fraction renormalisation of fractional-part sums — is exactly what the already-adopted Ostrowski/three-gap route provides. So the synthesis folds into… (refers: pe1006-transfer_operator_spectral, pe1006-weighted-language-diagonal, pe1006-fourier-rotation-correlation, pe1006-ostrowski-sawtooth-closed-form)

## hunch

- **chisel**: The single-intercept ueuclid is provably insufficient, but the LOJ138 polynomial-moment node (already on disk) is the right fix and needs no new primitive. LOJ138's Node stores moments sum x^{k2} * floor((px+r)/q)^{k1} with composition C.ans[a][b] = A.ans[a][b] + sum_{i,j} C(a,i)C(b,j) A.cnt1^i A.cnt2^j B.ans[a-i][b-j] — i.e. it already carries the (offset-shift, x-power) pair as a bivariate polynomial. The obstruction is one-variable, not fundamental: a second coordinate for the intercept index or the diagonal h=l-m' lets the outer sum over the k+1 intercepts be absorbed. The O(k)-intercept… (refers: pe1006-ostrowski-sawtooth-closed-form, pe1006-mechanical-ueuclid-obstruction)
- **scholar**: CRITICAL from the scholar: the in-container capture code/out/ueuclid_main.captured.txt of code/lib/ueuclid.py's own __main__ prints '65 FAILURES -- do not trust ueuclid yet' (0/30 random vs ueuclid_direct, 0/30 S1-at-z=1 vs plain floor_sum, 5/6 deterministic). S0/dR/dU/w are correct in every case; only S1 and S2 are wrong. Hand-check ueuclid(1,0,1,5,z=3): module returns S1=547, S2=2551; correct S1=426, S2=1578 (module's = correct + S0's worth, a uniform +1-per-index overcount). This contradicts directive 11's 'verified on current code, zero failures, do NOT rebuild' — the outside-container… (refers: ueuclid-incontainer-fails-s1s2)

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
[reducer failed: tool error: agent `reducer` failed: graph error: model error: local-router returned HTTP 403: <html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
</body>
</html>
]

[reducer failed: tool error: agent `reducer` failed: graph error: model error: local-router returned HTTP 403: <html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
</body>
</html>
]

Open gaps, read from the ledger:
-…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The requests ledger holds four requests, all about the primitive and the Sturmian complexity — all now answered by existing claims (`universal-euclidean-geometric-floor-sum`, `monoid-composition-formulas-verified`, `fibonacci-sturmian-complexity`); none covers the actual G4 obstruction, which is correctly *not* a research request but a construction task with cheap refuters. Nothing to duplicate, nothing to post.

My audit is complete. Here is the report.

## Report

**Slug:** `pe1006-psi` —…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The ledger is coherent. Here is my report.

## Report

**Slug:** `pe1006-psi` — `research/backward/pe1006-psi.md` (status `live`), the canonical decomposition. I did not invent a new skeleton; I audited and sharpened the existing one against `search_claims` and the full `goals` ledger, and repaired three standing defects.

### The reduction, and how the lemmas recombine

- **G1 → the summation domain.** The distinct Fibonacci subwords of length k are exactly the length-k factors of the infinite Fibonacci fixed…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger reflects it. Here is my report.

## Report

**Slug:** `pe1006-psi` — rewritten at `research/backward/pe1006-psi.md` (status `live`).

### What I found on arrival

The workspace already has a live `pe1006-psi` skeleton and a separate standalone `g1-sturmian-factor-structure` skeleton; I did not invent a new decomposition, I audited and sharpened the existing one against `search_claims`, the full `goals` ledger, and the full claim statements. I also re-read the problem…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
## Report

**Slug:** `pe1006-psi` — rewritten at `research/backward/pe1006-psi.md`

### What I found on arrival

The pe1006-psi skeleton already existed and decomposed the goal into four lemmas. Checking each against the claims ledger:

- **G1 (factor identification)** — discharged. The count half (k+1 distinct length-k factors) is closed by `fibonacci-sturmian-complexity`, `governing-sturmian`, and `governing-factor-complexity`. The union-to-infinite-limit stabilisation is closed by `g1-factor-chain-nested`…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The ledger is clean — no faulty entries remain, the two accidental files are marked `spent` with honest reasons, and `pe1006-psi`'s `rests-on` no longer cites the non-claim. The skeleton is coherent and complete.

## Report

**Slug:** `pe1006-psi` — `research/backward/pe1006-psi.md` (status `live`)

The skeleton already existed and was well-formed; I verified every gap against `search_claims` and the claims ledger rather than rewriting it. Three fixes were needed:

1. **Removed a broken `rests-on` reference.**…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton and ledger are written correctly. My work is complete.

## Summary

**Slug:** `pe1006-psi` — rewritten at `research/backward/pe1006-psi.md` (and the `goals` ledger row updated to match).

### What I found on the way in
The pe1006-psi skeleton already existed and decomposed the goal into four lemmas (G1 factor structure, G2 mechanical representation, G3 telescoped second moment, G4 universal-Euclidean floor sum). Checking each against the claims ledger:

- **G2 and G3 are already discharged** — by…
- **pattern**: Pattern-recognition: NEW exact first-moment regularity at k=F_n-1. Verified exactly (mech_psi k=1,2,4,7,12,20,33,54,88,143; brute k=4,7,12): the first moment M1(k) = sum of the k+1 factor decimal values equals c1(k)*R(k), c1(k)=1+floor(k/phi^2)=A189663, R(k)=repunit. Equivalently every decimal position among the k+1 factors carries exactly c1(k)=F_{n-2} ones. Fails at all non-F_n-1 k. This is the first-moment transpose of the Toeplitz/cyclic-autocorrelation symmetry (directive 1 C=A domain), NOT a second-moment closed form, so it does NOT by itself give Psi(10^18); it is a cross-check handle.… (refers: pe1006-first-moment-position-balance)
