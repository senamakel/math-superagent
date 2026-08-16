# k=25 dyadic extension: no collapse at powers of two (directive 36)

The k=25 dyadic-extension job (the target of directive 35's kill order)
completed without OOM: memory peaked near 2.3 GiB against the 16 GiB cap and
fell back to 1.5 GiB. The job materialised the prime h of length 2^25+2 in
memory (255.3 s) rather than streaming it, but it fit under the cap. The
result is worth recording; it is recorded here as a claim with the exact k
range, the three sequences, the ratio, and the margin. Capture:
`code/out/dyadic_extension_k25.txt`, `code/out/dyadic_extension_k25_capture.txt`.

```claim
id: dyadic-nu2-no-collapse-through-k25
statement: >
  At the 23 dyadic sample indices k = 3..25, n = 2^k, 2^k+1, 2^k-1 (n up to
  2^25 = 33554432), the prime fold does NOT collapse: nu2(2^k)/2^k stays at
  1/2, with nu2(2^25)/2^25 = 16778104/33554432 = 0.50003 (exactly
  1/2 + 888/2^25). The endpoint excess S(2^k) = (2^k-2) - 2*nu2(2^k) stays
  tiny in absolute terms: |S(2^k)| <= 5282 over the whole range (the max is
  attained at k=23), and S(2^25) = -1778; so |S|/n is about 1.6e-4 even for
  the worst |S| = 5282 scaled against n = 2^25, versus the
  0.04n = (1 - 2*0.48)n falsifier threshold for c = 0.48 — three orders of
  magnitude below it. Closed door 4 lives at powers of two; the fold does NOT
  collapse there for the primes.
  The three sequences, k = 3..25:
  nu2(2^k)   = 2 12 13 27 66 136 243 502 1003 2010 4184 8338 16464 32608 65308 131146 261803 524358 1049371 2099362 4191662 8388313 16778104 ;
  S(2^k)     = 2 -10 4 8 -6 -18 24 18 40 74 -178 -294 -162 318 454 -150 680 -142 -1592 -4422 5282 588 -1778 ;
  nu2(2^k+1) = 1 6 18 39 59 128 257 497 994 2097 4068 8055 16537 32703 65569 131418 262106 523369 1048540 2097290 4195033 8388399 16777388 ;
  nu2(2^k-1) = 1 2 12 30 57 127 269 506 1015 2047 4082 8270 16386 32759 65845 130892 262747 525294 1048352 2097047 4194910 8388050 16774858 .
hypotheses: canonical floored fold d in [2,n-1], nu2 = wt(Phi_n h) =
  (n-2-S(n))/2 (claim excess-is-negative-character-sum); prime h built to
  length 2^25+2 and guard-checked (nu2(53)=18, nu2(64)=27, nu2(4000)=1975,
  nu2(40000)=20081). This is 23 sampled dyadic points (k=3..25), not a sweep.
holds-here: yes, scoped to the dyadic sample points n = 2^k, 2^k+1, 2^k-1,
  k = 3..25 only. It does NOT extend the density-1 or dip-sparsity results,
  which remain measured only to N = 40000; powers of two are structurally
  special n, which is what makes the sample interesting and also what stops it
  being density evidence.
status: measured — exact integers over the 23 stated sample indices; not a proof.
bearing: >
  Strengthens the sixth door at the one family where a dyadic collapse would
  show: at n = 2^k the primes sit in the generic-balanced-good class
  (nu2/n -> 1/2), not in the door-4 collapse class (all-ones / Thue-Morse /
  2-regular give nu2 = O(1)). It does NOT extend the density-1/dip-sparsity
  results, whose ceiling stays at N = 40000, and it does not reach the
  surviving open statement (research/CONCLUSION.md section 5), which no finite
  measurement reaches.
anchor: code/out/dyadic_extension_k25.txt ;
  code/out/dyadic_extension_k25_capture.txt
```

## The three sequences (k = 3..25)

```
nu2(2^k):    2 12 13 27 66 136 243 502 1003 2010 4184 8338 16464 32608 65308 131146 261803 524358 1049371 2099362 4191662 8388313 16778104
S(2^k):      2 -10 4 8 -6 -18 24 18 40 74 -178 -294 -162 318 454 -150 680 -142 -1592 -4422 5282 588 -1778
nu2(2^k+1):  1 6 18 39 59 128 257 497 994 2097 4068 8055 16537 32703 65569 131418 262106 523369 1048540 2097290 4195033 8388399 16777388
nu2(2^k-1):  1 2 12 30 57 127 269 506 1015 2047 4082 8270 16386 32759 65845 130892 262747 525294 1048352 2097047 4194910 8388050 16774858
```

`D2(k) = S(2^k+1)+S(2^k-1)-2S(2^k)` (k=3..25):
`4 32 -8 -30 32 34 -80 2 -6 -248 436 702 10 -492 -1596 -36 -2494 106 3700 8774 -13238 354 7924`

## Margin arithmetic (exact)

- `nu2(2^25)/2^25 = 16778104/33554432 = 0.5000265…` (the directive's 0.50003 is
  the 5-decimal rounding).
- `max |S(2^k)|` over k=3..25 = `5282` at k=23; `5282/2^25 = 1.574e-4 ≈ 1.6e-4`.
- `S(2^25) = -1778`; `1778/2^25 = 5.30e-5`.
- Falsifier threshold: `nu2 >= 0.48n` needs `S <= (1-2*0.48)n = 0.04n`, from
  `2*nu2 - (n-2) = -S`. Measured `|S|/n` is three orders of magnitude below it.
