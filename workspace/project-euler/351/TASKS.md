# Tasks

- [x] Restate the problem precisely in GOAL.md with every symbol defined and
      the worked examples (H(5)=30, H(10)=138, H(1000)=1177848) recorded as
      the test oracle.
- [x] Write and run `code/brute.py` (naive enumeration); it reproduces all
      three oracle values.
- [x] Identify the governing theory (coprime iff visible; H(n) = 6(C(n+1,2)
      − Φ(n)); Möbius/Gauss identities) and record it in CONTEXT.md and
      `research/notes/pe351-governing-theory.md`.
- [x] Derive the efficient method (reduce to Φ(10⁸); three independent exact
      routes) in solution.md.
- [x] Implement `code/solution.py`; agree with brute.py at n = 5, 10, 1000
      and reproduce the statement's values before running at full size.
- [x] Compute Φ(10⁸) = 3039635516365908 and H(10⁸) = 11762187201804552.
- [x] Verify by independent routes: Möbius-inversion sieve (`verify_mobius.py`),
      Chai Wah Wu A063985 recursion (`out/patterns.py`), OEIS A064018 check
      values (`out/check_library_values.py`), OEIS A216453 sequence match.
- [x] Scholar pass: audit every source note against its full text, replace
      placeholder digests, mark irrelevant/raw lookups, flag the recalled
      check-anchor contradiction, and store durable findings in Cognee.
