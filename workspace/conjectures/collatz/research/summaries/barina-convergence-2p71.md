# Barina 2025 — improved verification limit to 2^71

<!-- src: Barina, "Improved verification limit for the convergence of the Collatz conjecture", J. Supercomput. 81 (2025) 810, DOI 10.1007/s11227-025-07337-0, open access -->

Full text: `research/sources/barina-convergence-2p71.full.md`

## What the source establishes

The current verification record and its consequences. (The 2021 method paper
`barina-2021-convergence-verification` and the project page
`barina-project-page` are the method sources.)

**Verification record (line 253):** all starting values up to 2^71
(= 2048 × 2^60) have been verified to converge to the trivial cycle.

**Cycle-length consequence (line 253):** at this verification limit, the
length of a non-trivial cycle rises to **355,504,839,929** — i.e. any
non-trivial cycle must have length (period) at least that large, conditional
on the Eliahou-type cycle formula and the verification bound.

**Milestones (from project page, `barina-project-page`):** 2^68 (2020-05-07),
2^69 (2021-12-10), 2^70 (2023-07-09), 1.5×2^70 (2023-11-03), 2^71
(2025-01-15). Four new path records found during the convergence test.

**Method:** 3^k sieves with optimized sieving (notably size 3^2), distributed
across thousands of workers on European supercomputers, work unit 2^40
numbers, ~5s per unit on modern GPUs; best GPU implementation ~52× over best
CPU, total cumulative speedup ~1,335× from the initial CPU algorithm.

## Claims

```claim
id: barina-cycle-length-355b
statement: With the verification limit at 2^71 (all n < 2^71 verified to reach 1), the length of a non-trivial Collatz cycle rises to at least 355,504,839,929 (Barina 2025, line 253, citing the Eliahou-type cycle formula).
hypotheses: verification to 2^71 (established), Eliahou cycle-length formula (established)
holds-here: yes
status: asserted
bearing: the current best non-trivial-cycle length lower bound; supersedes the Eliahou 10,439,860,591 period bound
anchor: research/summaries/barina-convergence-2p71.md
```
