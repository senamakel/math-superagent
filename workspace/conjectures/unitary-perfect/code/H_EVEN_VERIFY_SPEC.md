# H_even verification — implementation spec

Goal: an independent, exact verification of Theorem 8 of arXiv:2605.20475 (full
text at research/sources/maciejewski-bounded-box-subbarao-warren.full.md), plus
identity checks. All arithmetic exact integers, no floats.

## Definitions (from the paper, sections 1.1, 3, 5)

- sigma*(n) = prod over p^a || n of (p^a + 1).  n is unitary perfect iff sigma*(n) == 2*n.
- 3-Higgs prime: p is 3-Higgs iff p-1 divides the cube of the product of all
  smaller 3-Higgs primes. Equivalent working form: every prime factor q of p-1
  is 3-Higgs AND v_q(p-1) <= 3 for every q | p-1. Base: 2 is 3-Higgs.
  First non-Higgs prime: 17, since 17-1 = 2^4 has v2 = 4 > 3.  (Check both
  forms agree computationally on primes up to ~1000 as a sanity test.)
- H_even = { even m : every prime factor of 2^m + 1 is 3-Higgs }.
- Theorem 8 (the target):  H_even ∩ [2,1200] = {2, 6, 10, 18, 26, 30, 46, 62, 82, 122}.
  The ten numbers above are the ONLY hard-coded expectation; the comparison is
  the reproducibility check and a mismatch must be reported loudly.

## Phase A — worked examples (must run and pass before Phase B)

A1. sigma_star oracle: verify 6, 60, 90, 87360, 146361946186458562560000 each
    satisfy sigma*(n) == 2*n, and that 12 does not.  Print the 2-adic budget
    table for each: a, omega(odd part), sum_i v2(p_i^e_i + 1), a+1 — the
    identity sum = a+1 must hold exactly for all five.

A2. 3-Higgs predicate, recursive and memoized: factor p-1 completely (trial
    division by primes <= sqrt, sympy.factorint for any cofactor; verify the
    product of returned factors equals p-1 and each factor is prime via
    sympy.isprime).  Print Higgs status of every prime <= 31 and record 17 as
    non-Higgs, 31 as Higgs (31-1 = 2·3·5).

A3. Cyclotomic / Aurifeuillean identities, all exact:
    - 2**(2p) + 1 == 5 * Phi_{4p}(2) for the first 30 odd primes p
      (sympy.cyclotomic_poly(4*p).eval at x=2, or compute the cyclotomic value
      by the exact product formula).
    - For odd primes p <= 100: 2**(2p)+1 == (2**p - 2**((p+1)//2) + 1)
      * (2**p + 2**((p+1)//2) + 1).
    - Paper's worked example (section 5.2), m = 2426, p = 1213:
      x = 2**303; L = 2*x**4 - 2*x**2 + 1; M = 2*x**4 + 2*x**2 + 1;
      assert L*M == 2**2426 + 1 and L % 25893760589 == 0.
    - Filter-N example (sections 3.2, 6): assert pow(2, 1509, 20127043)
      == 20127042 (i.e. 20127043 | 2^1509 + 1); assert factorisation of
      20127042 == 2·3^4·13·19·503 and v3 = 4 > 3, so 20127043 is non-3-Higgs.

## Phase B — H_even ∩ [2,1200], exact classification

B1. Cross-check only (never used to kill): an m = 2k in H_even forces every
    prime factor of k to be 3-Higgs with exponent <= 3 (k Higgs-cubefree).
    Count how many odd k in [1,600] pass; paper says 246.

B2. Witness sieve.  Enumerate odd primes r with gmpy2.next_prime, threaded
    across all cores (28 on this box; disjoint ranges per worker).
    - First pass to 10^8; second pass to 10^9.  The second pass settles:
      which even m <= 1200 have a non-3-Higgs prime divisor r with
      10^8 < r <= 10^9.  Report both passes' statistics.
    - For each prime r: if pow(2, 2400, r) != 1, skip (then ord_r(2) cannot
      divide 2400 = 2*max_m, so r divides no 2^m + 1 with even m <= 1200).
    - Else compute ord_r(2): factor r-1 (trial division; r-1 <= 10^9), start
      d = r-1, and while a prime ell | d has pow(2, d//ell, r) == 1, d //= ell.
    - If ord is even and ord <= 2400: for every even m <= 1200 with
      m ≡ ord//2 (mod ord): double-check pow(2, m, r) == r-1, then archive
      (r, m, ord) to code/out/witnesses_1200.tsv, certify r prime by trial
      division to sqrt(r), and if r is non-3-Higgs (exact recursive check)
      mark m killed with witness r.
    - Write (r, ord) pairs to code/out/ord_sieve_table.tsv incrementally so a
      timeout loses no progress.
    - Print: primes enumerated, primes passing the pow filter, witnessed m
      count, killed m count.

B3. Survivor classification.  For every even m <= 1200 not killed by the
    sieve: fully factor 2**m + 1 with sympy.factorint (for m <= 122 this is at
    most 37 digits and must succeed; if factorint returns before a complete
    factorisation, treat m as undecided and say why).  For each prime factor q
    verify 3-Higgs recursively (factor q-1, chain terminates because factors
    strictly decrease).  If every factor is 3-Higgs -> m in H_even, record the
    full factorization.  Else m killed by the found non-Higgs factor.

B4. Output: the computed H_even ∩ [2,1200] list; equality with the ten numbers
    (or a loud discrepancy); killed counts (killed-by-sieve, killed-by-full-
    factor, in-H_even, undecided); every undecided m with its obstruction;
    B1 count for cross-check.  Also spot-check by full hand-verifiable
    factorisations: 2^6+1 = 5·13, 2^18+1 = 5·13·37·109 (37: 36 = 2^2·3^2;
    109: 108 = 2^2·3^3, both Higgs).

## Constraints

- Never enumerate n testing sigma*(n) == 2n; never search for a sixth UPN;
  never backtrack over the product form.  Only the checks specified above.
- Every "killed" m must carry a printed witness: a prime r dividing 2^m + 1
  (verified by pow(2, m, r) == r-1) that is non-3-Higgs (verified exactly).
- No floats anywhere in arithmetic.
- Bound every run: `timeout 540 python3 <prog> 2>&1 | tee
  code/out/<name>.captured.txt; echo EXIT_CODE=$?` from /workspace/code.
  State in the capture what range was covered and what was left undecided.
- Split into two scripts: code/heven_sieve.py (B2, writes the two tables) and
  code/heven_classify.py (reads tables, does B1/B3/B4 and the Phase A checks or
  imports them).  Library: code/lib/higgs.py — sigma_star, is_3_higgs (memoized,
  records a Pratt-style tree), factor_small, factorize (exact, sympy fallback),
  each with a docstring saying what established it.  describe_file every new
  file.  Refresh code/INDEX.md / lib index as needed.

## Report back (as the captured key lines)

Worked examples A1-A3 pass/fail; final H_even set; counts killed/survivor/
undecided; sieve statistics for both passes; EXIT_CODEs; any deviation from
this spec or from the paper's Theorem 8 statement.