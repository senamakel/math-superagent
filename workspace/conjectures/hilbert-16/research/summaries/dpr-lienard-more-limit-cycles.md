# DPR (Dumortier–Panazzolo–Roussarie) 2007 — Liénard has more cycles than expected

Full text: [[dpr-lienard-more-limit-cycles.full]]. Proc. AMS 135 (2007).
Note: stored file is the **PAMS record page** (journal metadata, subscription
structure); the abstract and full text are NOT held. Claims below are sourced at
the level already recorded in `research/notes/claims.md` (h16-lienard-ldmp-disproved)
and cross-confirmed by the Llibre–Zhang survey abstract (see llibre-zhang note).

## What it establishes (via the Liénard-conjecture literature, not this record page)

The Lins–de Melo–Pugh conjecture — classical Liénard ẋ=y−F(x), ẏ=−x with deg F = n
has at most ⌊(n−1)/2⌋ limit cycles — is **false for n ≥ 6**: DPR 2007 constructed
a degree-6 Liénard system with 4 limit cycles (relaxation oscillations / canards in
the slow–fast limit). De Maesschalck–Dumortier showed classical Liénard has ≥ n−2
cycles; the Llibre–Zhang survey (2017) records n=5 as still open.

## What it implies here

This is the run's **slow–fast test (test 3) reference**: sharp counting
conjectures die in the singular limit. It does NOT bound H(2) (Liénard degree
∝ cycles means high degree needed). It is a warning about believing sharp
conjectures, exactly as problem.md states. The stored PAMS record itself contains
no mathematics beyond metadata — do not re-open expecting content.

```claim
id: h16-lienard-ldmp-n6
statement: The Lins-de Melo-Pugh conjecture fails for n >= 6: a degree-6
  classical Lienard system has 4 limit cycles (per the held Llibre-Zhang 2017
  full text, the degree-6 base case uses De Maesschalck-Huzak 2015's slow
  divergence integral I1(x)=0.4x^3-1.248x^5+1.17429x^7-0.3x^9 with 3 positive
  zeros -> 4 cycles; DPR 2007's own paper established n >= 7 with one extra
  cycle); >= n-2 cycles exist for general n (De Maesschalck-Huzak 2015);
  n=5 open per Llibre-Zhang 2017 survey.
hypotheses: classical Lienard form y'=-x, x'=y-F(x), deg F = n.
holds-here: yes (received disproof; DPR 2007 full text not held — landing page
  only; the Llibre-Zhang 2017 full survey postprint is held).
status: asserted
bearing: slow-fast test reference; kills any sharp Liénard-type conjecture;
  unrelated to H(2) uniformity.
anchor: research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md
contradicts: none (corrects the earlier degree-6-via-DPR2007 attribution: the
  survey credits DPR 2007 with n>=7 and the degree-6 4-cycle case to the
  De Maesschalck-Huzak induction presented in the survey)
```