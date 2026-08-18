# Barina 2021 — convergence verification (method source)

<!-- src: Barina, "Convergence verification of the Collatz problem", J. Supercomput. 77 (2021) 2681–2688, DOI 10.1007/s11227-020-03368-x -->

Full text: `research/sources/barina-2021-convergence-verification.full.md`

## What the source establishes

The algorithmic method behind the current verification records. (The 2025
follow-up "Improved verification limit for the convergence of the Collatz
conjecture" is also in the library as `barina-convergence-2p71`.)

**Core algorithmic contribution:** replacement of huge precomputed tables of
size O(2^N) with small lookup tables of size O(N). The accelerated/Syracuse
form is used, and the O(N)-sized tables let the verification run in
essentially constant space per unit.

**Measured speeds (from the paper):**
- Single-threaded CPU: 4.2×10^9 128-bit numbers/second (Intel Xeon Gold 5218)
- Parallel OpenCL: 2.2×10^11 128-bit numbers/second (NVIDIA RTX 2080)

The program also checks for path records during the convergence test.

The full text is the paywalled Springer landing page with abstract and
references; the method detail (3^k sieves, work units of 2^40) is captured
from the project page (`barina-project-page`) and the 2025 paper
(`barina-convergence-2p71`).

## Claims

```claim
id: barina-2021-method
statement: Barina's 2021 verification method replaces O(2^N) precomputed tables with O(N)-sized lookup tables for the accelerated (Syracuse) form, achieving 4.2e9 (single CPU) and 2.2e11 (OpenCL GPU) 128-bit numbers verified per second.
hypotheses: accelerated/Syracuse Collatz form, 128-bit numbers
holds-here: yes — the method behind the current verification record
status: asserted
bearing: the computational verification flank; the oracle this run builds should reproduce the method's small-table idea
anchor: research/summaries/barina-2021-convergence-verification.md
```
