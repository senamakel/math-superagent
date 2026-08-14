# OEIS A064018 — summatory totient at powers of 10

Source: https://oeis.org/A064018 — full text at
`research/sources/oeis-A064018-totient-summatory-powers-of-10.full.md`
[[oeis-A064018-totient-summatory-powers-of-10.full]]
The b-file (terms 0..19) is at `research/summaries/oeis-A064018-bfile.md`.

## What this source establishes

**Definition.** a(n) = Φ(10^n) = Σ_{k ≤ 10^n} φ(k), the summatory totient at
powers of ten (OEIS A002088 evaluated at 10^n).

**The catalogue (b-file, terms 0..19).** a(0..8) =
1, 32, 3044, 304192, 30397486, 3039650754, 303963552392, 30396356427242,
**3039635516365908**. Hence

    Φ(10^8) = 3039635516365908        (index 8)

The b-file's later terms (through Φ(10^19) = 30396355092701331435065976498046398788)
were computed by Lucas A. Brown (arXiv:2506.07386), who ran the computation
twice with matching results.

**Asymptotic.** a(n) ~ (3/π²)·10^{2n}.

## Hypotheses

None beyond the definition. Holds here.

## What it lets this run do

- The independent catalogue check value: `code/out/check_library_values.py`
  computed Φ(10^k) for k=0..8 by a naive sieve and matched every row, and
  `code/solution.py` + `code/verify_mobius.py` independently recompute
  Φ(10⁸)=3039635516365908 by two different sieves.
- The final arithmetic anchor: H(10⁸) = 3·10⁸·(10⁸+1) − 6·Φ(10⁸) =
  11762187201804552.

## What it does not settle

- Nothing about the orchard itself (that is A216453/A063985).

## ⚠️ Indexing caution (learned the hard way)

a(k) = Φ(10^k), **not** Φ(10^{k+1}). A recurring error in this run's notes was
citing Φ(10⁸) = 303963552391 — that is Φ(10⁶) = 303963552392 with a typo, four
orders of magnitude too small. The correct Φ(10⁸) is a(8) = 3039635516365908,
corroborated by two independent sieves in this run. Always check the index
against the magnitude ~0.303964·10^{2k}.

## Claims

```claim
id: totient-sum-verification-values
statement: Φ(10^k) for k=0..8 is 1, 32, 3044, 304192, 30397486, 3039650754,
303963552392, 30396356427242, 3039635516365908 (OEIS A064018 b-file).
hypotheses: none.
holds-here: yes — check_library_values.py reproduces all nine rows with a naive
sieve; solution.py and verify_mobius.py independently recompute Φ(10^8).
status: catalogued (OEIS b-file; terms 0..18 Yamanouchi, term 19 Brown 2025);
checked here by the two sieve routes (solution.py and verify_mobius.py).
bearing: independent verification of the final H(10^8) = 11762187201804552.
anchor: research/summaries/oeis-A064018-totient-summatory-powers-of-10.md
```
