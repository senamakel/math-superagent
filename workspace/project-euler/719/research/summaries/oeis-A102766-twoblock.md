# A102766 — the two-block (Kaprekar / "torn number") special case

Source: https://oeis.org/A102766 (downloaded; full text at
`research/summaries/oeis-A102766-twoblock.md`; `index_document` indexed).

A102766 lists numbers k that can be **chopped into exactly two parts** which,
added and squared, give k: k = (a+b)² where a,b are the two left/right pieces
of the decimal string and a+b is the square root.

**Relationship to the S-number problem (A104113 / PE 719).**

- A102766 is the **two-block-only** special case of the general split-and-sum
  rule. OEIS places it *in context* immediately before A104113 (the general
  S-numbers) — A104113 allows "one, two or more" parts, A102766 allows exactly
  two. So:
  - A102766 ⊂ A104113 (every two-block sum-and-square number is an S-number).
  - Every term of A102766 is a perfect square whose two-part split sums to the
    root; these are exactly the "torn numbers" (Dudeney, *Amusements in
    Mathematics*, 1917, problem 113 — the page's own link).
- `a(n) = A248353(n)^2` — the two-block analogue of A104113's
  `a(n) = A038206(n)^2`. A248353 is the two-block roots.

**The two-block solver (Michael S. Branicky, 2024), verbatim from the page:**

```python
def ok(n):
    if n == 1: return True
    r = isqrt(n)
    if r**2 != n: return False
    s = str(n)
    return any(int(s[:i])+int(s[i:])== r for i in range(1, len(s)))
def agen(): yield from (k**2 for k in count(1) if ok(k**2))
```

This confirms the structural point: the general S-rule (arbitrary ≥2 blocks)
is **strictly** more general than the two-block rule, because A102766's roots
are a proper subset of A038206's roots. In particular 81 = 9² = "8+1", while
the general 3+-block examples (e.g. 6724 = 82² = 6+72+4) are S-numbers captured
by A104113/A038206 but not by A102766.

```claim
id: a102766-twoblock-subset
statement: Numbers k that chop into exactly two parts (a+b)² = k are exactly the two-block S-numbers; A102766 (with roots A248353) is a proper subset of the general S-numbers A104113 (roots A038206). The general problem requires the arbitrary-block rule, not the two-block one.
hypotheses: decimal digit strings, contiguous left-to-right blocks; two-block = exactly two nonempty pieces.
holds-here: yes
status: asserted (OEIS cross-reference structure plus identical recursion family)
bearing: rules out using two-block Kaprekar generation to obtain T(10^12); reinforces that A104113/A038206 (arbitrary blocks) are the sequence family that must be summed.
anchor: research/summaries/oeis-A102766-twoblock.md
```

**Does not settle:** the value of T(10¹²) (that is computed from the general
arbitrary-block roots A038206, not from the two-block subcase).
