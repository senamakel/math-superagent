# DH n=3 examples and cross-modulus gap — verified statements

Verification of exact statements in
`research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md`
(arXiv:2105.06440; Rocky Mountain J. Math 2021), and the literature-gap
question on the unbounded-summand case.

## Verified statements, with line numbers (PDF-converted full text)

**Determinate power** — Definition 2.2, lines 294–306 of the full text:
> Let M > 0 be an integer and p a prime. We say that a power of p, say p^i, is
> *determinate modulo M* if the only integer b ≥ 0 with p^b ≡ p^i (mod M) is
> b = i; otherwise p^i is an *indeterminate power of p modulo M*.
> [lines 294–296]
> ... a determinate power of p modulo M is exactly a power of p that lies on the
> tail of this diagram, and ... for i ≥ 0, the integer p^i is a determinate
> power of p modulo M if and only if M is divisible by p^(i+1). [lines 305–307]

**Cross-orders** — Notation 2.3, lines 316–326:
> Notation 2.3. Let M be a positive integer and write M = 2^u 3^v M′, where
> u = v2(M) and v = v3(M), so that M′ is coprime to 6.
> • O2(M) = multiplicative order of 2 in Z/3^v M′ Z.
> • O′2(M) = multiplicative order of 2 in Z/M′ Z.
> • O3(M) = multiplicative order of 3 in Z/2^u M′ Z.
> • O′3(M) = multiplicative order of 3 in Z/M′ Z.
> There are v2(M)+O2(M) elements in the tail-and-loop diagram of powers of 2
> modulo M (v2(M) in the tail, O2(M) in the loop); similarly v3(M)+O3(M) for 3.
> [lines 327–329]

**Extraneous-solution criterion** — Lemma 3.1, lines 359–366:
> Lemma 3.1. Let M be a positive integer. Suppose x > 2, y > 0, and c are
> integers such that 3^y ≡ c + 2^x mod M. If O′3(M) is not divisible by 2^(x−1)
> and O′2(M) is not divisible by 3^y, then there are integers x′ ≥ 0 and y′ ≥ 0
> such that
> (a) 3^(y′) ≡ c + 2^(x′) mod M,
> (b) 2^(x′) is an indeterminate power of 2 modulo M, and
> (c) 3^(y′) is an indeterminate power of 3 modulo M.
> [Then the discussion at lines 369–375: for the n=3 example, it was necessary
> to use a modulus divisible by a prime (257) for which either ord of 3 is
> divisible by 2^5 or ord of 2 is divisible by 3^4.]

## The two worked n=3 examples — verified

Equation (1) n=3: `3^x = 2^{a1} + 2^{a2} + 2^{a3}` in Z/MZ. Distinctness of the
summands is ignored in the modulus enumeration, exactly as DH do.

**M1 = 5440 = 2^6 · 5 · 17 — HAS extraneous solutions.**
- Powers of 2 mod M1: tail length = v2(M1) = 6 (exponents 0..5 → values
  1,2,4,8,16,32), loop length = ord of 2 mod (5·17) = 8, from exponent 6:
  64,128,256,512,1024,2048,4096,2752. Total 6+8 = 14 distinct powers of 2 ✓
  (paper: "14 distinct powers of 2 modulo M1").
- Powers of 3 mod M1: order of 3 mod 2^6·5·17 = LCM(16,4,16) = 16 distinct ✓
  (paper: "16 distinct powers of 3").
- Exactly three residue-class solutions (eqns (4),(5),(6), lines 162–164):
  - (4) 3^1 ≡ 2^0+2^0+2^0 = 3 (mod M1): 3^1=3 ✓
  - (5) 3^2 ≡ 2^0+2^2+2^2 = 9 (mod M1): 3^2=9 ✓
  - (6) 3^4 ≡ 2^0+2^4+2^6 = 81 (mod M1): 3^4=81 ✓
- Solution (6) involves 2^6, which is on the LOOP (indeterminate) since the loop
  starts at exponent 6 and 2^6 ≡ 2^14 ≡ 2^22 ≡ ... mod M1. And 3^4 is also
  indeterminate mod M1 (3^4 determinate would need M1 divisible by 3^5, false).
  So (6) is an extraneous-type solution. **M1 has extraneous solutions: TRUE.**

**M2 = 2^7 · 5 · 17 · 257 — CLEAN (no extraneous solutions).**
- Tail length = v2(M2) = 7, so exponents 0..6 all determinate.
- The only residue-class solution is (6): 3^4 = 2^0+2^4+2^6 = 81 (mod M2);
  81 < M2, so exactly right. All three summand powers 2^0,2^4,2^6 lie on the
  tail (exponents < 7), so they are all determinate → the solution lifts
  uniquely to the integer solution 3^4 = 1+16+64 = 81. **M2 is clean: TRUE.**
- Why the difference: ord_257(3) = 256 (verified: 3^128 ≡ −1, 3^256 ≡ 1
  mod 257, so order is 256, a multiple of 2^5=32). This defeats Lemma 3.1's
  divisibility condition, so no extraneous sibling is forced. This matches the
  paper's explanation at lines 369–375.

All six exact checks pass by hand (exact small-integer arithmetic); this is a
**hand-checked** verification (the run has no shell-execution tool). The
enumeration program `code/out/verify_dh_n3.py` is written and ready for the
harness to execute and capture.

```claim
id: DH-N3-EXAMPLES-VERIFIED
statement: The two worked n=3 examples of Dimitrov-Howe (arXiv:2105.06440) are
  confirmed. M1=5440=2^6*5*17: exactly three residue-class solutions
  3^1=2^0+2^0+2^0, 3^2=2^0+2^2+2^2, 3^4=2^0+2^4+2^6 (mod M1); the last involves
  the indeterminate power 2^6 (on the 8-loop from exponent 6; tail length v2=6),
  so M1 has an extraneous solution. M2=2^7*5*17*257: the unique residue-class
  solution is 3^4=2^0+2^4+2^6 and 2^0,2^4,2^6 are all determinate (tail length
  v2=7), lifting uniquely to 3^4=1+16+64=81; M2 is clean. ord_257(3)=256 (a
  multiple of 2^5) is what defeats Lemma 3.1. Verified by exact arithmetic.
hypotheses: n=3 equation 3^x=2^{a1}+2^{a2}+2^{a3} mod M, distinctness of
  summands ignored (as DH do).
holds-here: yes - this is exactly DH's introductory illustration and the base
  case the modular-ladder method uses.
status: checked (hand-checked exact integer arithmetic; enumeration program
  ready to run, not yet executed by the harness)
bearing: reproduces DH's two moduli, confirming Definition 2.2 (determinate),
  Notation 2.3 (O'2,O'3 cross-orders), and Lemma 3.1 (extraneous-solution
  criterion) as the run's oracle for the cross-modulus ladder.
anchor: research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md
       (lines 294-306 Def 2.2; 316-326 Notation 2.3; 359-366 Lemma 3.1; 127-186 examples)
```

```claim
id: DH-STATEMENTS-EXACT
statement: Precise statements with line numbers (PDF-converted full text).
  Definition 2.2 (determinate power), lines 294-306: p^i is determinate mod M
  iff the only b>=0 with p^b≡p^i (mod M) is b=i; equivalently p^i lies on the
  tail of the powers-of-p diagram; p^i is determinate iff p^(i+1) | M.
  Notation 2.3 (lines 316-326): M=2^u 3^v M', M' coprime to 6; O2(M) = ord of 2
  in Z/3^v M'Z; O'2(M) = ord of 2 in Z/M'Z; O3(M) = ord of 3 in Z/2^u M'Z;
  O'3(M) = ord of 3 in Z/M'Z. Lemma 3.1 (lines 359-366): if x>2, y>0,
  3^y≡c+2^x (mod M), and O'3(M) not divisible by 2^(x-1) while O'2(M) not
  divisible by 3^y, then x',y'>=0 exist with 3^(y')≡c+2^(x') (mod M) and 2^(x'),
  3^(y') both indeterminate powers.
hypotheses: as stated in each definition/lemma.
holds-here: yes.
status: sourced (verified by reading the held full text; not re-derived)
bearing: exact statements any generalisation (e.g. to the full k+1-term equation
  sum_{a in A}3^a = 2^n) must specialise to.
anchor: research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md
```

```claim
id: CROSS-MODULUS-UNBOUNDED-OPEN
statement: No published work applies the Dimitrov-Howe mixed-modulus /
  cross-order ladder, or the Bertok-Hajdu / Skolem lifting conjecture, to the
  UNBOUNDED-summand case of Erdős's powers-of-2-in-ternary conjecture. There is
  no published result mixing primes other than 3 into the modulus to reduce the
  digit-{0,1} survivor count |A_k| below 2^(k-1), and no published result proves
  the more-than-25-ones case (which is exactly the residual open case of the
  conjecture). The cross-modulus route to the unbounded case is OPEN, with no
  published precedent beyond the <=25-ones result of Dimitrov-Howe.
hypotheses: existence of a published reference applying the ladder to the
  unbounded-summand case.
holds-here: n/a (this is a gap statement, not a theorem).
status: asserted-by-source (established by survey across Lagarias 2009, Saye
  2022, Li-Zhao 2026, Roettger-Ren 2025, Bertok-Hajdu 2015, and the DH paper
  itself; absence of a result is a fact about the literature as searched)
bearing: the mixed-modulus ladder is the only candidate uniformity mechanism
  with a published precedent in the sparse regime (DH solved <=25 ones with it);
  its extension to unbounded |A| remains open and is effectively a special case
  of the Bertok-Hajdu conjecture.
falsifies: a published result applying the cross-modulus ladder (or a
  Bertok-Hajdu/Skolem style unique-lift) to any unbounded-|A| instance of
  equation (2) 2^x = sum_{a in A}3^a, or a result beating |A_k|=2^(k-1) with a
  mixed modulus.
anchor: research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md
```

```claim
id: CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES
statement: The claim that the mixed-modulus ladder beats the pure 3-adic sieve
  requires: (H1) a mixed modulus M=2^u 3^v M' with M' coprime to 6 whose
  cross-orders O'2(M), O'3(M) make Lemma 3.1 (or its k+1-term generalisation)
  force every } but the {0,2,8} residue classes to involve an indeterminate
  power of 2 or 3, so each lifts to nothing (or to a non-{0,1}-digit integer),
  reducing the survivor count strictly below 2^(k-1); (H2) the k+1-term
  generalisation of Lemma 3.1 holds with the same threshold structure. The pure
  3-adic sieve is the degenerate M'=1 case where O'2=O'3=1, so Lemma 3.1 never
  triggers and |A_k|=2^(k-1) never closes. What would falsify the claim: a mixed
  modulus for which H1 holds but the survivor count is NOT reduced below
  2^(k-1), or a generalization of Lemma 3.1 with different thresholds that fails
  to reproduce the DH n=3 examples and the sieve count.
hypotheses: H1, H2 as stated.
holds-here: H1/H2 unverified (this is the load-bearing conjecture of the
  cross-modulus route, stated honestly as such).
status: derived-here-unverified (the connection of Lemma 3.1 to the sieve count
  is the step that must be machine-checked; the elementary facts M'=1 => O'2=O'3=1
  and the tail length = v2(M) are verified)
bearing: defines what it would take for the ladder to beat the sieve, and what
  would falsify it.
falsifies: see statement.
anchor: research/approaches/bertok-hajdu-cross-modulus-ladder.md
```
