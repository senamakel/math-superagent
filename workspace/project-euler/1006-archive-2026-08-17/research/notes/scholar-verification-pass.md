# Scholar verification pass (this run)

Read and verified the load-bearing structural claims directly against the full texts
of the downloaded sources, and cross-checked them against the run's brute oracle on
disk (`code/out/factors_k12.txt`, `psi_brute_k1_30.txt`). What was verified, and how:

## Directly verified in source full texts

1. **MSS Theorem 18** (`PE1006-rightspecial-reverse-prefix`):
   "The unique special factor of length n is f[0..n-1]^R" — the right-special length-n
   factor of the Fibonacci word is the reverse of the length-n prefix.
   Source: mousavi-schaeffer-shallit-fibonacci-automatic-I.full (cs.uwaterloo.ca/~shallit/Papers/part1.pdf).
   Bearing: fixes R(k) in the run's verified extension formula
   Psi(k+1) = 100(Psi(k) + v_R(k)^2) + 20 P1(k) + N1(k).

2. **Perrin–Restivo Theorem 2** (`PR-consecutive-factors-lex`) and Prop 1 membership,
   plus Table 1 (length-10) / Table 3 (length-8) factor lists.
   Source: sturmian-words-hal-note.full (hal-00828351).
   Bearing: structural enumeration rule; the length-8/10 lists cross-check the oracle.

3. **Poirier–Steiner** Introduction (`PE1006-factors-one-count-necessary`):
   "each block of length n in a Sturmian sequence of slope alpha has floor(n*alpha) or
   ceil(n*alpha) occurrences of the letter of frequency alpha" (quoting Morse-Hedlund 1940).
   Source: morse-hedlund-balanced-blocks-floor-alpha.full (hal-03869990v2).

4. **Cassaigne–Fici–Sciortino–Zamboni Prop 7** (`PE1006-factors-dependent-slop-only`):
   "Fact(x)=Fact(y) iff x,y are Sturmian of the same slope."
   Source: character-of-sturmian-words.full (hal-01829144).

## Two-way verification (source vs run's oracle)

- Cassaigne array A_{5,3} (Fig 1) lists the 8 length-8 factors of F with Parikh (5,3) =
  {00100101,00101001,01001001,01001010,01010010,10010010,10010100,10100100} and states "the
  other factor of length 8 of F is 10100101". This EXACTLY matches the on-disk oracle
  (factors_k12.txt, length-8: 9 factors). Independently confirms
  `PerrinRestivo-len8-len10-lists` (conjugates + singular structure).

## Correction found and recorded

**Chuan** (`Chuan-cyclic-shift-indexed-enumeration`): the paper's F_n n-th Fibonacci words
are the F_n cyclic shifts of the canonical word q_n — but they are exactly the CONJUGATES
of the standard length-F_n word, a STRICT subset of the length-F_n factor set, which has
F_n+1 members (Morse-Hedlund k+1). The unique singular factor is separate. Verified at
F_4=3: shifts with a->1 are {100,010,001}; the factor set {001,010,100,101} adds singular
'101'. Stored in Cognee; claim block updated in chuan-fibonacci-words-fq.md; thread
references fixed (previously pointed at non-existent ids
`PE1006-conjugate-singular-iff-fibonacci`, `chuan-cyclic-shift-index`).

## Sources that do not help (recorded, do not re-read)

- Lothaire Ch.2 (CUP paywall stub): covered by Wojcik + Perrin–Restivo.
- Morse & Hedlund 1940 (JSTOR paywall): recovered via Wojcik + Poirier–Steiner.
- Fici arXiv:1508.06754 (abstract only), Rampersad–Wiebe (background), de Luca 2013 /
  Cassaigne 2008 (extremal palindromic properties, not the factor-value sum).
- The misfiled "note-on-sturmian-words-2011.full.md" (arXiv:1202.6175 is an unrelated
  comms-engineering paper, not Perrin–Restivo) — do not cite.

## What the library still lacks

No source yields a closed form / poly-log recurrence for Psi(k); PR enumeration is O(k^2),
infeasible at 10^18. Chuan covers only Fibonacci lengths, and even there gives only the
conjugates (singular must be added). Reaching k=10^18 still needs the gap bridged from the
verified extension recurrence / Chuan rotation-sum. The run's modular facts (M prime,
ord_10(M)=50500500, Pisano=101001000, no small period, no low-order linear recurrence) are
checked and stand; the final Psi(10^18) mod M value remains open.
