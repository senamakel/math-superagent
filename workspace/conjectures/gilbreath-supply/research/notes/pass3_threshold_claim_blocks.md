# Third-pass claim blocks — linear-supply threshold (directive 47/48 closure)

This note carries the four claim blocks that `research/CONCLUSION-PASS3.md`
asserts in prose but never filed as fenced blocks, so none reached the claims
ledger. Prior attempts used multi-line folded `statement:` fields with status
`measured-not-proved`; the ledger renderer was found to silently drop
measured-not-proved claims in this configuration. This note uses single-line
`statement:` fields. The two open lemmas render as `asserted`/`open` rows.

The measurement is on disk and independently re-verified by pattern_finder
this run: an independent third route (direct hypergeometric odd-count grouped
by popcount, `code/pattern_finder/verify_wstar_seq.py`) reproduced the exact
threshold weights digit-for-digit, confirmed the sublinear exponent, and
confirmed the two open lemmas are pure-F2/hypergeometric with no primes in
them.

## 1. The positive result — sublinear threshold weight

```claim
id: threshold-weight-sublinear
statement: The exact-mean linear-supply threshold weight w*(n)=min{ w : mean over all weight-w strings in F2^n of nu2/n >= 0.40 } grows sublinearly as w*(n) = n^E * P(log2 n), E ~ 0.555, P a bounded period-1-in-log2(n) log-periodic factor of amplitude ~0.07; phase-1.0 OLS E = 0.55499 +/- 0.00202 (n=256..65536), independent refit E = 0.5522 +/- 0.0022 (n=256..262144); per-doubling slopes settle 0.54-0.57. Hence theta*(n) = w*(n)/n -> 0: linear supply (mean nu2/n >= 0.40) is exact-mean-TYPICAL once the switch count exceeds about n^0.55. Exact w* = 3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239,349,738 at n=8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,65536,262144, theta = 0.375@8 .. 0.0053@2^16 .. 0.00282@2^18, below the pass-2 1/8 plateau, eventually decreasing from n=14.
hypotheses: canonical floored fold d in [2,n-1]; exact mean over the weight-w sphere via Krawtchouk parity formula P_d(w)=(C(n,w)-[z^w](1-z)^k(1+z)^(n-k))/(2 C(n,w)), k=2^popcount(d) (claim threshold-mean-exact-parity-formula), validated against exhaustive s_sos; n in [8,262144].
holds-here: yes -- every w* is an exact integer from the verified formula, reproduced by three independent routes (gen-func, direct hypergeometric, verify_wstar_seq.py); the EXPONENT and the tend-to-zero LIMIT are fitted, not proved.
status: measured-not-proved
bearing: The third pass's affirmative headline: linear supply is typical at a SUBLINEAR switch count (~n^0.55), strictly weaker than a positive mod-4 switch density (Theta(n)); problem.md type 4, never type 1; genericity gap 'typical is not this string' unchanged; needs the two open lemmas G-threshold-asymptotic-zero and G-threshold-concentration for a theorem.
anchor: code/out/threshold_weight_logperiodic_extended.txt; code/out/linear_supply_threshold_pass3.txt; code/out/threshold_limit_exact.txt; code/pattern_finder/verify_wstar_seq.py.
```

## 2. The negative result — rejected or unseparable closed forms

```claim
id: threshold-closed-forms-rejected
statement: The exact phase-1.0 (power-of-2) threshold-weight data over n=256..262144 REJECTS c*sqrt(n) (E=0.5; rejected 27 sigma via OLS E=0.55499+/-0.00202, |E-0.5|/se=27.2; w^2/n rises 0.77->1.74 not flat) and REJECTS c*n^(log2(3)-1) (E=0.58496; rejected 14 sigma, monotone residual drift 0.624->0.531 with spread 0.093 vs bounded-periodic spread 0.024 at 0.555), and CANNOT separate 5/9=0.55556 from the fitted 0.555 (identical residual sd 0.01466 log2-units over n=256..65536; exponent gap ~0.0044 is ~30x smaller than the periodic swing ~0.32). So the established content is sublinear E ~ 0.555 with a log-periodic factor; 1/2 and log2(3)-1 firmly ruled out, 5/9 plausible but not established.
hypotheses: exact phase-1.0 threshold weights n=256..262144; OLS log2 w vs log2 n; residual comparisons at fixed in-cell phase.
holds-here: yes for the fitted constants over the measured range; the rejections are statistical (sigma from OLS), not for all n.
status: measured-not-proved
bearing: Stops a later reader adopting 5/9 (or 1/2, or log2(3)-1) because it is tidy; the honest statement is 'E ~ 0.555 sublinear with a log-periodic factor', not a closed-form constant.
anchor: code/out/threshold_weight_logperiodic_extended.txt (PART E, PART G); code/pattern_finder/directive47_compare.py.
```

## 3. The two open lemmas — pure F2/hypergeometric, no primes

```claim
id: G-threshold-asymptotic-zero
statement: OPEN LEMMA (named gap from measurement to theorem). For every fixed theta in (0,1/2), w = floor(theta*n), the biased-cell sum (1/n)*sum_{d=2}^{n-1} K_w(2^popcount(d); n)/C(n,w) -> 0, K_w(k;n)=sum_{r odd} C(k,r)C(n-k,w-r); so E[nu2/n] -> 1/2 at every fixed theta and theta_mean(n) -> 0. Engine: group by popcount k (N_p=C(floor(log2 n),p) cells), hypergeometric mode bound |E[(-1)^X]| <= max_j P[X=j] = O(1/sqrt(1+Var X)). PURE F2/hypergeometric, no primes.
hypotheses: canonical floored fold; exact parity formula P_d(w) (claim threshold-mean-exact-parity-formula).
holds-here: PLANNED -- turns measured theta->0 (claim threshold-weight-sublinear) into a theorem; NOT proved here (open).
status: open
bearing: If proved, upgrades measured 'theta -> 0' to a theorem for all n, making linear supply exact-mean-typical at any positive switch density.
anchor: research/backward/supply-threshold-limit.md (open rung); research/BLUEPRINT.md.
```

```claim
id: G-threshold-concentration
statement: OPEN LEMMA (named gap between measured fraction-half and a theorem). For every fixed theta in (0,1/2), w = floor(theta*n), Var(nu2(n)) = o(n^2), so nu2/n -> 1/2 in probability and P[nu2/n >= 0.40] -> 1; the measured 'typical' condition (mean >= 0.40 AND frac >= 0.5) then holds in the limit and the sampled threshold theta(n) -> 0. Engine: E[eps_d eps_d'] = (1-2p)^{|M_d symdiff M_d'|} with the meet formula |M_d cap M_d'| = 2^{pc(d^d')} (claim downset-row-intersection-meet-formula). PURE F2/hypergeometric, no primes.
hypotheses: canonical floored fold; second moment over the meet formula.
holds-here: PLANNED -- concentration half; NOT proved here (open).
status: open
bearing: With G-threshold-asymptotic-zero, proves linear supply is TYPICAL at any fixed positive density, turning the measured sublinear-threshold result into a theorem.
anchor: research/backward/supply-threshold-limit.md (open rung); research/BLUEPRINT.md.
```

## Renderer-bug note

The ledger renderer (directive-15 class) was found this run to silently drop
`measured-not-proved` claims whose `statement:` is a multi-line folded block,
while single-line statements render (as `checked` evidence in the table) and
`open`/`asserted` claims render (as `asserted` in the bottom list). Diagnostic
notes (`renderer_test*.md`) were created and deleted; no test claim carries a
standing result. Worked workaround: single-line `statement:` fields.
