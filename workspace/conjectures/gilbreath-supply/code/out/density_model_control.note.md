# Density-matched model control: the rising prime mean is fold-generic

Ran the previously capture-less code/averaged/density_model_control.py (directive
3b / 8b / 9). Capture: code/out/avg_push_capture.txt.

## The measured prime switch density

ones(h[0..3999]) = 2387, density = 0.5968 (0.5962 over [50,4000)). This is the
operative prime switch density. It corrects TWO stale figures in the workspace:
the '0.597 nu2/w' min at n=105 (unrelated quantity) and the kernel_component
table's wt(h)/n = 0.6250..0.6875 (a different quantity: fold-image weight per
column at small fixed n=8..128, not the switch density of h). The switch density
is ~0.5968 everywhere.

## The result (measured, not proved)

| N | prime M | Bernoulli(p=0.5968) | Bernoulli(0.5) | Thue-Morse |
|---|---|---|---|---|
| 100  | 0.4394 | 0.4503 | 0.4542 | 0.2255 |
| 1000 | 0.4906 | 0.4926 | 0.4929 | 0.1080 |
| 2000 | 0.4952 | 0.4959 | 0.4961 | 0.0836 |
| 4000 | 0.4973 | 0.4977 | 0.4979 | 0.0641 |

(20 trials per model, exact s_sos, oracle fold_nu2 == s_direct checked.)

**Answer to directive 3(b): the rising prime mean M(N) -> ~0.4973 is NOT
prime-specific.** Both Bernoulli models (density-matched p=0.5968 and balanced
0.5) reproduce the prime mean to within Monte-Carlo spread (at N=4000:
prime 0.4973, Ber(p) 0.4977, Ber(0.5) 0.4979). The fold's averaged mean is
generic for balanced random strings at value ~ (n-2)/2n (consistent with
fair-model-exact-binomial, PROVED). What is *not* generic is Thue-Morse's
collapse to 0.0641 (density 1/2 but sublinear fold) and all-ones' 0. So the
signal that is prime-specific is only "the primes do NOT collapse like
Thue-Morse or all-ones" — i.e. their mean lands at the fair value 1/2, and the
difficulty is that the primes are not known to be non-adversarial for the fold.

```claim
id: density-model-rising-mean-is-generic
statement: The rising averaged fold mean M(N) -> ~0.4973 (N=4000) for the prime
  switch string is reproduced by Bernoulli random strings at the measured prime
  switch density p=0.5968 (mean 0.4977) and at balanced density 0.5 (0.4979),
  within 20-trial Monte-Carlo spread (exact s_sos fold, oracle-checked). The
  mean is therefore fold-generic for balanced random inputs, not prime-specific.
  The prime switch density is 0.5968 (ones(h[0..3999])=2387). Negative controls
  discriminate: Thue-Morse (density 1/2) collapses to M=0.0641 and all-ones to 0.
  So the only prime-specific content is that the prime mean sits at the fair
  1/2 value rather than collapsing; the difficulty is that the primes are not
  known to be non-adversarial for the fold.
hypotheses: fold convention d in [2,n-1]; exact s_sos == s_direct; 20 trials per
  random model, length 4001, prefix-consistent; measured.
holds-here: yes, measured to N=4000.
status: measured-not-proved
bearing: confirms GOAL priority-1 difficulty is NOT that the primes have a
  special mean (they don't — it is the fair value) but that they are not known
  to be non-adversarial. Corroborates prefix-variance-fair-model-law
  (variance also fair-model). The switch-density figure in problem.md's '0.597
  nu2/w' row and the kernel_component wt(h)/n figures are other quantities; the
  operative switch density is 0.5968.
anchor: code/out/avg_push_capture.txt; code/averaged/density_model_control.py
```
